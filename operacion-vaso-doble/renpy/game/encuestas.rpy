define preguntas_confianza = (
    ("interpretacion", "Interpretar un diagrama de estados UML y seguir qué ocurre al producirse una secuencia de eventos."),
    ("acciones", "Elegir en qué transición debe ejecutarse una acción para obtener el comportamiento esperado."),
    ("guardas", "Definir guardas mutuamente excluyentes que funcionen también en los valores límite."),
    ("after", "Usar after(...) y elegir el estado desde el que debe comenzar a contarse un plazo."),
    ("at", "Usar at(...) para provocar una transición en una fecha y hora programadas."),
    ("when", "Usar when(...) para reaccionar a un cambio de condición y distinguirlo de una guarda."),
)
define escala_confianza = ("Ninguna", "Poca", "Moderada", "Bastante", "Mucha")
define escala_acuerdo = ("Totalmente en desacuerdo", "En desacuerdo", "Ni de acuerdo ni en desacuerdo", "De acuerdo", "Totalmente de acuerdo")
define preguntas_experiencia = (
    ("comprension", "El juego me ha ayudado a comprender mejor las máquinas de estados UML."),
    ("explicaciones", "Las explicaciones de las respuestas me han ayudado a entender mis errores."),
    ("historia", "La historia ha mantenido mi interés durante la actividad."),
    ("motivacion", "La actividad ha aumentado mi motivación para practicar con diagramas de estados."),
    ("adecuacion", "Considero adecuado utilizar juegos de este tipo para aprender contenidos de la asignatura."),
)
define preguntas_abiertas = (
    ("mejoras", "¿Qué cambiarías para mejorar la actividad?"),
)

init python:
    def guardar_encuesta(fase, pregunta, valor):
        registro_actual.anotar("encuesta", decision=fase + "." + pregunta, opcion=str(valor))

label encuesta_confianza(fase):
    $ registro_actual.anotar("inicio_encuesta", decision=fase)
    call screen matriz_confianza(fase)
    $ respuestas_confianza = _return
    $ indice_encuesta = 0
    while indice_encuesta < len(preguntas_confianza):
        $ guardar_encuesta(fase, preguntas_confianza[indice_encuesta][0], respuestas_confianza[indice_encuesta])
        $ indice_encuesta += 1
    if fase == "pre":
        $ registro_actual.anotar("fin_encuesta", decision=fase)
    return

label encuesta_posterior:
    call encuesta_confianza("post")
    call screen matriz_experiencia
    $ respuestas_experiencia = _return
    $ indice_encuesta = 0
    while indice_encuesta < len(preguntas_experiencia):
        $ guardar_encuesta("post", preguntas_experiencia[indice_encuesta][0], respuestas_experiencia[indice_encuesta])
        $ indice_encuesta += 1
    call screen pregunta_abierta(preguntas_abiertas[0][1], 13)
    $ dificultad_final, comentario_final = _return
    $ guardar_encuesta("post", "dificultad", dificultad_final)
    $ guardar_encuesta("post", "mejoras", comentario_final)
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
    default dificultad = 3
    add Solid("#10292ef5")
    frame:
        align (0.5, 0.5)
        xsize 1080
        padding (34, 30)
        background Solid("#10292e")
        vbox:
            spacing 20
            text "Después del juego · Comentario final" size 24 color "#a6ead5"
            text "¿Cómo valorarías la dificultad del juego?" size 24 color "#a6ead5"
            hbox:
                spacing 12
                for valor, etiqueta in enumerate(("Muy baja", "Baja", "Adecuada", "Alta", "Muy alta"), 1):
                    textbutton etiqueta:
                        selected dificultad == valor
                        action SetScreenVariable("dificultad", valor)
                        style "boton"
                        selected_background Solid("#a6ead5")
                        text_selected_color "#10292e"
                        text_size 22
            text pregunta size 30
            text "Respuesta breve opcional · Hasta 500 caracteres" size 22
            frame:
                xfill True
                ysize 180
                padding (18, 15)
                background Solid("#173b41")
                input value ScreenVariableInputValue("respuesta_abierta") length 500 multiline True size 24
            textbutton "Continuar" action Return((dificultad, respuesta_abierta.strip())) style "boton"
    key "game_menu" action Show("pausa")


screen matriz_confianza(fase):
    modal True
    default respuestas = [3] * len(preguntas_confianza)
    add Solid("#10292ef5")
    frame:
        align (0.5, 0.5)
        xsize 1220
        padding (26, 24)
        background Solid("#10292e")
        vbox:
            spacing 14
            text ("Antes del juego" if fase == "pre" else "Después del juego") size 26 color "#a6ead5"
            text "¿Qué seguridad tienes de poder realizar estas tareas?" size 29
            text "1 Ninguna · 2 Poca · 3 Moderada · 4 Bastante · 5 Mucha" size 22
            hbox:
                fixed:
                    xsize 790
                    ysize 26
                    text "Tarea" size 21 color "#a6ead5"
                for valor in range(1, 6):
                    fixed:
                        xsize 68
                        ysize 26
                        text str(valor) xalign 0.5 size 22 color "#a6ead5"
            for indice, pregunta in enumerate(preguntas_confianza):
                hbox:
                    ysize 65
                    fixed:
                        xsize 790
                        ysize 65
                        text pregunta[1] xmaximum 775 size 21 yalign 0.5
                    for valor in range(1, 6):
                        textbutton str(valor):
                            xsize 62
                            ysize 48
                            yalign 0.5
                            selected respuestas[indice] == valor
                            action SetScreenVariable("respuestas", respuestas[:indice] + [valor] + respuestas[indice + 1:])
                            background Solid("#173b41")
                            hover_background Solid("#316760")
                            selected_background Solid("#a6ead5")
                            text_color "#fff6e5"
                            text_selected_color "#10292e"
                            text_size 23
                            text_xalign 0.5
                            text_yalign 0.5
                        null width 6
            textbutton "Siguiente" action Return(list(respuestas)) style "boton" xalign 1.0
    key "game_menu" action Show("pausa")


screen matriz_experiencia():
    modal True
    default respuestas = [3] * len(preguntas_experiencia)
    add Solid("#10292ef5")
    frame:
        align (0.5, 0.5)
        xsize 1220
        padding (26, 24)
        background Solid("#10292e")
        vbox:
            spacing 12
            text "Después del juego · Valora la experiencia" size 28 color "#a6ead5"
            text "1 Totalmente en desacuerdo · 2 En desacuerdo · 3 Ni de acuerdo ni en desacuerdo" size 20
            text "4 De acuerdo · 5 Totalmente de acuerdo" size 20
            for indice, pregunta in enumerate(preguntas_experiencia):
                hbox:
                    ysize 62
                    fixed:
                        xsize 790
                        ysize 62
                        text pregunta[1] xmaximum 775 size 21 yalign 0.5
                    for valor in range(1, 6):
                        textbutton str(valor):
                            xsize 62
                            ysize 48
                            yalign 0.5
                            selected respuestas[indice] == valor
                            action SetScreenVariable("respuestas", respuestas[:indice] + [valor] + respuestas[indice + 1:])
                            background Solid("#173b41")
                            hover_background Solid("#316760")
                            selected_background Solid("#a6ead5")
                            text_color "#fff6e5"
                            text_selected_color "#10292e"
                            text_size 23
                            text_xalign 0.5
                            text_yalign 0.5
                        null width 6
            textbutton "Siguiente" action Return(list(respuestas)) style "boton" xalign 1.0
    key "game_menu" action Show("pausa")
