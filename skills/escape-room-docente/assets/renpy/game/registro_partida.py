"""Registro cronológico por partida, conservado fuera del estado reversible."""
import csv
import io
import os
import time
import uuid
from datetime import datetime

CAMPOS = [
    "version", "partida_id", "evento", "fecha_hora", "inicio_partida",
    "fin_partida", "tiempo_total_s", "reto", "tiempo_reto_s",
    "decision", "opcion", "correcta", "intento", "errores_acumulados",
    "acierto_primera", "estado_partida",
]


class Registro:
    def __init__(self, carpeta, prefijo="partida"):
        self.carpeta = carpeta
        self.identificador = uuid.uuid4().hex
        self.inicio = datetime.now().astimezone().isoformat(timespec="seconds")
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
            version=1, partida_id=self.identificador, evento=evento,
            fecha_hora=datetime.now().astimezone().isoformat(timespec="seconds"),
            inicio_partida=self.inicio, fin_partida=self.fin,
            tiempo_total_s=round(time.monotonic() - self.reloj, 3) if self.total == "" else self.total,
            reto=self.reto, estado_partida=self.estado,
        )
        if self.reloj_reto is not None:
            fila["tiempo_reto_s"] = round(time.monotonic() - self.reloj_reto, 3)
        fila.update(datos)
        self.filas.append(fila)
        self.guardar()

    def empezar_reto(self, numero):
        if self.reto == numero:
            return
        if self.reto:
            self.anotar("fin_reto")
        self.reto = numero
        self.reloj_reto = time.monotonic()
        self.anotar("inicio_reto")

    def respuesta(self, decision, opcion, correcta=None):
        clave = (self.reto, decision)
        self.intentos[clave] = self.intentos.get(clave, 0) + 1
        self.errores[clave] = self.errores.get(clave, 0) + int(correcta is False)
        self.anotar(
            "respuesta", decision=decision, opcion=str(opcion),
            correcta="" if correcta is None else int(correcta),
            intento=self.intentos[clave], errores_acumulados=self.errores[clave],
            acierto_primera="" if correcta is None else int(correcta and self.intentos[clave] == 1),
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
        self.fin = datetime.now().astimezone().isoformat(timespec="seconds")
        self.total = round(time.monotonic() - self.reloj, 3)
        self.estado = estado
        self.anotar("fin_partida")
        # Fechas finales y estado en todas las filas facilitan reunir varios CSV.
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
