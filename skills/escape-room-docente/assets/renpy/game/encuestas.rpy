define preguntas_confianza = (
    ("interpretar", "Interpretar el modelo utilizado en la actividad."),
    ("localizar", "Localizar un error a partir del comportamiento observado."),
    ("reparar", "Elegir una reparación que cumpla las reglas del caso."),
)
define escala_confianza = ("Ninguna", "Poca", "Moderada", "Bastante", "Mucha")
define escala_acuerdo = ("Totalmente en desacuerdo", "En desacuerdo", "Ni de acuerdo ni en desacuerdo", "De acuerdo", "Totalmente de acuerdo")
define preguntas_experiencia = (
    ("comprension", "El juego me ha ayudado a comprender mejor los contenidos de la actividad."),
    ("explicaciones", "Las explicaciones de las respuestas me han ayudado a entender mis errores."),
    ("historia", "La historia ha mantenido mi interés durante la actividad."),
    ("motivacion", "La actividad ha aumentado mi motivación para practicar con contenidos de la actividad."),
    ("adecuacion", "Considero adecuado utilizar juegos de este tipo para aprender contenidos de la asignatura."),
)
define preguntas_abiertas = (
    ("dudas", "¿Qué aspecto de los contenidos de la actividad te sigue generando más dudas?"),
    ("mejoras", "¿Qué cambiarías para mejorar la actividad?"),
)

init python:
    def guardar_encuesta(fase, pregunta, valor):
        registro_actual.anotar("encuesta", decision=fase + "." + pregunta, opcion=str(valor))

label encuesta_confianza(fase):
    $ registro_actual.anotar("inicio_encuesta", decision=fase)
    $ indice_encuesta = 0
    while indice_encuesta < len(preguntas_confianza):
        $ clave_encuesta, texto_encuesta = preguntas_confianza[indice_encuesta]
        call screen pregunta_escala(
            "Antes del juego" if fase == "pre" else "Después del juego",
            "¿Qué seguridad tienes de poder realizar esta tarea?" if fase == "pre" else "¿Qué seguridad tienes ahora de poder realizar esta tarea?",
            texto_encuesta, escala_confianza, indice_encuesta + 1, len(preguntas_confianza) if fase == "pre" else len(preguntas_confianza) + len(preguntas_experiencia) + 3
        )
        $ guardar_encuesta(fase, clave_encuesta, _return)
        $ indice_encuesta += 1
    if fase == "pre":
        $ registro_actual.anotar("fin_encuesta", decision=fase)
    return

label encuesta_posterior:
    call encuesta_confianza("post")
    $ indice_encuesta = 0
    while indice_encuesta < len(preguntas_experiencia):
        $ clave_encuesta, texto_encuesta = preguntas_experiencia[indice_encuesta]
        call screen pregunta_escala("Después del juego", "Indica tu grado de acuerdo.", texto_encuesta, escala_acuerdo, indice_encuesta + len(preguntas_confianza) + 1, len(preguntas_confianza) + len(preguntas_experiencia) + 3)
        $ guardar_encuesta("post", clave_encuesta, _return)
        $ indice_encuesta += 1
    call screen pregunta_escala("Después del juego", "", "¿Cómo valorarías la dificultad del juego?", ("Muy baja", "Baja", "Adecuada", "Alta", "Muy alta"), len(preguntas_confianza) + len(preguntas_experiencia) + 1, len(preguntas_confianza) + len(preguntas_experiencia) + 3)
    $ guardar_encuesta("post", "dificultad", _return)
    $ indice_encuesta = 0
    while indice_encuesta < len(preguntas_abiertas):
        $ clave_encuesta, texto_encuesta = preguntas_abiertas[indice_encuesta]
        call screen pregunta_abierta(texto_encuesta, indice_encuesta + len(preguntas_confianza) + len(preguntas_experiencia) + 2)
        $ guardar_encuesta("post", clave_encuesta, _return)
        $ indice_encuesta += 1
    $ registro_actual.anotar("fin_encuesta", decision="post")
    return

screen pregunta_escala(fase, instruccion, pregunta, opciones, numero, total):
    modal True
    add Solid("#10292ef5")
    frame:
        align (0.5, 0.5)
        xsize 1110
        padding (34, 28)
        background Solid("#10292e")
        vbox:
            spacing 15
            text "[fase] · Pregunta [numero] de [total]" size 24 color "#a6ead5"
            if instruccion:
                text instruccion size 25
            text pregunta size 29
            for valor, etiqueta in enumerate(opciones, 1):
                textbutton "[valor] · [etiqueta]" action Return(valor) style "boton" text_size 22
    key "game_menu" action Show("pausa")

screen pregunta_abierta(pregunta, numero):
    modal True
    default respuesta_abierta = ""
    add Solid("#10292ef5")
    frame:
        align (0.5, 0.5)
        xsize 1080
        padding (34, 30)
        background Solid("#10292e")
        vbox:
            spacing 20
            text "Después del juego · Pregunta [numero] de [len(preguntas_confianza) + len(preguntas_experiencia) + 3]" size 24 color "#a6ead5"
            text pregunta size 30
            text "Respuesta breve opcional · Hasta 500 caracteres" size 22
            frame:
                xfill True
                ysize 180
                padding (18, 15)
                background Solid("#173b41")
                input value ScreenVariableInputValue("respuesta_abierta") length 500 multiline True size 24
            textbutton "Continuar" action Return(respuesta_abierta.strip()) style "boton"
    key "game_menu" action Show("pausa")
