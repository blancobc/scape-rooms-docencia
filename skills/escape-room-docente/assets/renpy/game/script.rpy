define config.name = "Juego docente"
define config.window_title = "Juego docente"
define config.save_directory = "juego-docente-ejemplo"
define config.rollback_enabled = False
define prefijo_csv = "juego_docente"

init python:
    gui.init(1280, 720)

label start:
    $ iniciar_registro()
    call encuesta_confianza("pre")
    $ registro_actual.anotar("inicio_juego")
    $ iniciar_reto(1)
    scene expression Solid("#173b41")
    "En este ejemplo, un equipo emite dos confirmaciones por una sola entrega."
    "El registro muestra una confirmación al validar la petición y otra al completar la entrega."

label reparar_ejemplo:
    call screen elegir_reparacion_ejemplo
    $ opcion_ejemplo = _return
    $ registrar_respuesta("confirmacion", opcion_ejemplo, opcion_ejemplo == "entrega")
    if opcion_ejemplo != "entrega":
        call screen tarjeta("Comprobación", "Solución incorrecta", "Una petición validada todavía puede cancelarse antes de completarse.", "Probar otra opción", acento="#ffb1a7")
        jump reparar_ejemplo
    call screen tarjeta("Comprobación", "Solución correcta", "La confirmación corresponde a la entrega completada.", "Continuar", acento="#a6ead5")
    $ registro_actual.cerrar_reto()
    $ registro_actual.anotar("fin_juego")
    call encuesta_posterior
    $ registro_actual.terminar()
    call screen exportar_registro
    return

screen elegir_reparacion_ejemplo():
    modal True
    add Solid("#10292e")
    vbox:
        align (0.5, 0.5)
        xmaximum 1000
        spacing 20
        text "¿Cuándo debe confirmarse la entrega?" size 34
        text "Petición → Validación → Entrega completada" color "#a6ead5"
        textbutton "Al validar la petición" action Return("validacion") style "boton"
        textbutton "Al completar la entrega" action Return("entrega") style "boton"
