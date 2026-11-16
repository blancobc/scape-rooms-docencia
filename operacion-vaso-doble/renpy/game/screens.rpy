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
    tag menu
    add "cafeteria"
    add Solid("#071e22b0") xsize 620
    vbox:
        xpos 72
        yalign 0.52
        spacing 24
        text "Operación\nVaso Doble" size 76 color "#fff6e5"
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
    textbutton etiqueta action Return() style "boton" xalign 0.5 yalign 0.88
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
            textbutton boton action Return() style "boton"
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

screen recorrido_devolucion():
    modal True

    add Solid("#071e22b8")
    frame:
        align (0.5, 0.5)
        xsize 1120
        padding (34, 30)
        background Solid("#10292e")
        vbox:
            spacing 18
            text "Recorrido de la devolución" size 35
            add Transform("images/diagrama-devolucion.png", xysize=(1052, 220), fit="contain") xalign 0.5
            textbutton "Proponer reparación" action Return() style "boton"

    key "game_menu" action Show("pausa")

screen elegir_abono():
    modal True
    add Solid("#071e22b8")
    frame:
        align (0.5, 0.5)
        xsize 1120
        padding (36, 32)
        background Solid("#10292e")
        vbox:
            spacing 18
            text "¿En qué transición dejarías el abono?" size 33
            add Transform("images/diagrama-devolucion.png", xysize=(1048, 185), fit="contain") xalign 0.5
            text "Deja un solo abono. Comprueba qué pasaría si el vaso cae al depósito o si se retira antes." size 24
            textbutton "Al abrir la compuerta · iniciarDevolucion()" action Return("inicio") style "boton"
            textbutton "Al reconocer el vaso · validarVaso()" action Return("validacion") style "boton"
            textbutton "Al recoger el vaso · confirmarRecogida()" action Return("caida") style "boton"
    key "game_menu" action Show("pausa")

screen pantalla_maquina(mensaje, detalle=None):
    vbox:
        xpos 648
        ypos 135
        xanchor 0.5
        yanchor 0.5
        xsize 200
        spacing 3
        text mensaje xalign 0.5 textalign 0.5 color "#b5fff0" size 19
        if detalle:
            text detalle xalign 0.5 textalign 0.5 color "#f5fffc" size 29
