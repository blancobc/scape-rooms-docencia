style default:
    color "#fff6e5"
    size 26

style boton is button:
    background Solid("#103c3b")
    hover_background Solid("#21645e")
    padding (24, 14)

style boton_text is button_text:
    color "#fff6e5"
    hover_color "#ffffff"
    size 24

screen main_menu():
    on "show" action Function(cerrar_registro)
    tag menu
    add Solid("#173b41")
    add Solid("#071e22b0") xsize 620
    vbox:
        xpos 72
        yalign 0.52
        spacing 24
        text "[config.name]" size 76 color "#fff6e5"
        textbutton "Empezar" action Start() style "boton"
        textbutton "Salir" action Quit(confirm=False) style "boton"

screen say(who, what):
    window:
        id "window"
        xalign 0.5
        yalign 0.97
        xsize 1104
        yminimum 153
        padding (32, 18)
        background Solid("#10292ef5")
        vbox:
            spacing 9
            if who is not None:
                text who id "who" size 22 color "#a6ead5"
            text what id "what" size 27
    key "game_menu" action Show("pausa")

screen accion(etiqueta):
    modal True
    textbutton etiqueta action [Function(registrar_boton, etiqueta), Return()] style "boton" xalign 0.5 yalign 0.88
    key "game_menu" action Show("pausa")

screen tarjeta(seccion, titulo, detalle, boton, acento="#fff6e5"):
    modal True
    add Solid("#071e227c")
    frame:
        xalign 0.5
        yalign 0.5
        xmaximum 680
        padding (38, 32)
        background Solid("#10292e")
        vbox:
            spacing 19
            text seccion color "#a6ead5" size 22
            text titulo size 36 color acento
            text detalle size 25
            textbutton boton action [Function(registrar_boton, boton), Return()] style "boton"
    key "game_menu" action Show("pausa")

screen pausa():
    modal True
    zorder 100
    add Solid("#071e22a0")
    vbox:
        align (0.5, 0.5)
        spacing 15
        textbutton "Continuar" action Hide("pausa") style "boton"
        textbutton "Volver al menú" action MainMenu(confirm=False) style "boton"
    key "game_menu" action Hide("pausa")

