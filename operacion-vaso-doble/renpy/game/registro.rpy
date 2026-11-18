init python:
    import registro_partida
    import os
    import json
    from pathlib import Path

    registro_actual = None

    def iniciar_registro():
        global registro_actual
        if registro_actual is not None:
            registro_actual.terminar("interrumpida")
        registro_actual = registro_partida.Registro(os.path.join(config.savedir, "registros"))

    def iniciar_reto(numero):
        registro_actual.empezar_reto(numero)

    def registrar_respuesta(decision, opcion, correcta=None):
        registro_actual.respuesta(decision, opcion, correcta)

    def registrar_boton(etiqueta):
        if registro_actual is not None and registro_actual.estado == "en_curso":
            registro_actual.anotar("boton", opcion=etiqueta)

    def cerrar_registro():
        if registro_actual is not None:
            registro_actual.terminar("interrumpida")

    def descargar_csv():
        nombre = os.path.basename(registro_actual.ruta)
        contenido = "\ufeff" + registro_actual.contenido()
        if renpy.emscripten:
            renpy.emscripten.run_script(
                "var blob = new Blob([" + json.dumps(contenido) + "], {type: 'text/csv;charset=utf-8'});"
                "var enlace = document.createElement('a');"
                "var url = URL.createObjectURL(blob); enlace.href = url;"
                "enlace.download = " + json.dumps(nombre) + ";"
                "document.body.appendChild(enlace); enlace.click(); enlace.remove();"
                "setTimeout(function(){ URL.revokeObjectURL(url); }, 1000);"
            )
        else:
            abrir_registros()

    def abrir_registros():
        registro_actual.guardar()
        if not registro_actual.error:
            renpy.run(OpenURL(Path(registro_actual.carpeta).as_uri()))

    config.quit_callbacks.append(cerrar_registro)

screen exportar_registro():
    modal True
    add Solid("#071e22b8")
    frame:
        align (0.5, 0.5)
        xsize 1040
        padding (34, 30)
        background Solid("#10292e")
        vbox:
            spacing 17
            text "Registro de tu partida" size 34
            if renpy.emscripten:
                text "Descarga tu CSV y entrégalo donde indique el profesorado." size 24
                textbutton "Descargar CSV" action Function(descargar_csv) style "boton"
            elif registro_actual.error:
                text "No se pudo guardar el CSV. Comprueba el espacio y los permisos e inténtalo otra vez." size 24 color "#ffb1a7"
                textbutton "Reintentar guardado" action Function(registro_actual.guardar) style "boton"
            else:
                text "Tu CSV está guardado. Entrega este archivo donde indique el profesorado." size 24
                text os.path.basename(registro_actual.ruta) size 20 substitute False
                text "Incluye tiempos, respuestas y reintentos. El identificador de partida permite distinguir los archivos." size 23
                textbutton "Abrir carpeta del CSV" action Function(abrir_registros) style "boton"
            textbutton "Volver al menú" action Return() style "boton"
    key "game_menu" action Show("pausa")
