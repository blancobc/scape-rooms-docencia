"""Registro cronológico de una partida en CSV, fuera del estado reversible de Ren'Py.

Adaptado del módulo de registro de la skill escape-room-docente (esquema v1) para
novela-visual-evaluable (esquema v2: añade alias, concepto y texto_opcion).

- Un fichero por partida: <prefijo>_<partida_id>.csv, UTF-8 con BOM y ';'.
- Se guarda de forma atómica tras cada evento (un cierre forzado conserva lo anotado).
- 'reto' es el identificador del concepto (c01, c02...) o 'ods'.
- Tiempos: fechas ISO con zona horaria + segundos monotónicos desde el inicio.
"""
import csv
import io
import os
import time
import uuid
from datetime import datetime

VERSION_ESQUEMA = 2

CAMPOS = [
    "version", "partida_id", "alias", "modo", "evento", "fecha_hora",
    "inicio_partida", "fin_partida", "tiempo_total_s", "reto", "tiempo_reto_s",
    "decision", "opcion", "texto_opcion", "correcta", "intento",
    "errores_acumulados", "acierto_primera", "estado_partida",
]

## Registro en curso. Vive en este módulo (no en el store de Ren'Py) para que
## no se guarde en las partidas ni se deshaga con rollback.
actual = None


class Registro:
    def __init__(self, carpeta, prefijo="partida", modo="", alias=""):
        self.carpeta = carpeta
        self.identificador = uuid.uuid4().hex
        self.alias = alias
        self.modo = modo
        self.inicio = _ahora()
        self.reloj = time.monotonic()
        self.fin = ""
        self.total = ""
        self.reto = ""
        self.reloj_reto = None
        self.intentos = {}
        self.errores = {}
        self.filas = []
        self.estado = "en_curso"
        self.error = ""
        self.ruta = os.path.join(carpeta, prefijo + "_" + self.identificador + ".csv")
        self.anotar("inicio_partida")

    def anotar(self, evento, **datos):
        fila = dict.fromkeys(CAMPOS, "")
        fila.update(
            version=VERSION_ESQUEMA, partida_id=self.identificador, alias=self.alias,
            modo=self.modo, evento=evento, fecha_hora=_ahora(),
            inicio_partida=self.inicio, fin_partida=self.fin,
            tiempo_total_s=round(time.monotonic() - self.reloj, 3) if self.total == "" else self.total,
            reto=self.reto, estado_partida=self.estado,
        )
        if self.reloj_reto is not None:
            fila["tiempo_reto_s"] = round(time.monotonic() - self.reloj_reto, 3)
        fila.update(datos)
        self.filas.append(fila)
        self.guardar()

    def poner_alias(self, alias):
        self.alias = alias
        for fila in self.filas:
            fila["alias"] = alias
        self.anotar("alias", opcion=alias)

    def empezar_reto(self, reto):
        if self.reto == reto:
            return
        if self.reto:
            self.anotar("fin_reto")
        self.reto = reto
        self.reloj_reto = time.monotonic()
        self.anotar("inicio_reto")

    def respuesta(self, decision, opcion, correcta=None, texto_opcion=""):
        clave = (self.reto, decision)
        self.intentos[clave] = self.intentos.get(clave, 0) + 1
        self.errores[clave] = self.errores.get(clave, 0) + int(correcta is False)
        self.anotar(
            "respuesta", decision=decision, opcion=str(opcion), texto_opcion=texto_opcion,
            correcta="" if correcta is None else int(correcta),
            intento=self.intentos[clave], errores_acumulados=self.errores[clave],
            acierto_primera="" if correcta is None else int(bool(correcta) and self.intentos[clave] == 1),
        )

    def cerrar_reto(self):
        if self.reto:
            self.anotar("fin_reto")
            self.reto = ""
            self.reloj_reto = None

    def terminar(self, estado="completada"):
        if self.estado != "en_curso":
            return
        self.cerrar_reto()
        self.fin = _ahora()
        self.total = round(time.monotonic() - self.reloj, 3)
        self.estado = estado
        self.anotar("fin_partida")
        # Fecha final y estado en todas las filas: facilita reunir muchos CSV.
        for fila in self.filas:
            fila["fin_partida"] = self.fin
            fila["estado_partida"] = self.estado
        self.guardar()

    def contenido(self):
        salida = io.StringIO(newline="")
        escritor = csv.DictWriter(salida, fieldnames=CAMPOS, delimiter=";")
        escritor.writeheader()
        escritor.writerows(self.filas)
        return salida.getvalue()

    def guardar(self):
        try:
            os.makedirs(self.carpeta, exist_ok=True)
            temporal = self.ruta + ".tmp"
            with open(temporal, "w", encoding="utf-8-sig", newline="") as fichero:
                fichero.write(self.contenido())
                fichero.flush()
                os.fsync(fichero.fileno())
            os.replace(temporal, self.ruta)
            self.error = ""
        except OSError as exc:
            self.error = str(exc)


def _ahora():
    return datetime.now().astimezone().isoformat(timespec="seconds")
