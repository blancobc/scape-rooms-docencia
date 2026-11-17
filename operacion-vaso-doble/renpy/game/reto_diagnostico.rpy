define cliente = Character("Desde la cola", color="#ffcd9a")
image cafeteria cola_bloqueada = Transform("images/cafeteria-cola-bloqueada.png", xysize=(1280, 720), fit="cover")
image cafeteria mediodia = Transform("images/cafeteria-mediodia.png", xysize=(1280, 720), fit="cover")
image encargada cola = Transform("images/encargada-cola.png", xysize=(660, 610), fit="contain")

label reto_diagnostico:
    scene cafeteria cola_bloqueada with fade
    "Son casi las dos. Vas a la cafetería a comer y, antes de llegar al mostrador, ves una cola delante de la máquina de devolución. Todo el mundo lleva un vaso en la mano."

    show encargada cola at junto_mostrador with dissolve
    "La encargada te ve y te hace señas."
    encargada "Menos mal. He programado la revisión para mañana a las ocho, antes de abrir. En cuanto he pulsado Guardar, ha cerrado la compuerta."

    scene maquina cerrada
    show screen pantalla_maquina("Autodiagnóstico", "En curso")
    with dissolve
    "La pantalla dice «Autodiagnóstico en curso»."
    cliente "¿Va para largo?"
    encargada "Según lo que yo he programado, hasta mañana."

    call screen accion("Reproducir el fallo")
    hide screen pantalla_maquina
    show maquina vacia
    call screen tarjeta(
        "Panel técnico · Modo de prueba",
        "Programar autodiagnóstico",
        "Hora del registro: hoy, 13:55.\nHora programada: mañana, 08:00.",
        "Guardar en modo de prueba"
    )
    show maquina cerrada
    show screen pantalla_maquina("Autodiagnóstico", "Hoy · 13:55")
    with cambio_vaso
    "Al guardar, el diagnóstico arranca a las 13:55. La máquina acaba de bloquear las devoluciones en plena hora de comer."

    call screen accion("Ver recorrido del autodiagnóstico")
    hide screen pantalla_maquina
    call screen recorrido_diagnostico

label reparar_diagnostico:
    call screen elegir_diagnostico
    $ diagnostico_hora_fija = _return
    call screen resultado_diagnostico(diagnostico_hora_fija)

    if not diagnostico_hora_fija:
        jump reparar_diagnostico

    "Termina el diagnóstico que estaba en curso. La máquina vuelve a admitir vasos."
    call screen accion("Guardar la programación")
    show screen pantalla_maquina("Programado", "Mañana · 08:00")
    "La encargada guarda de nuevo la programación. Esta vez la máquina sigue disponible."

    show maquina con_vaso
    show screen pantalla_maquina("Vaso aceptado")
    with cambio_vaso
    "La primera de la cola devuelve su vaso."

    show maquina cerrada
    show screen pantalla_maquina("Abono recibido", "1 €")
    with cambio_vaso
    "El vaso cae al depósito y la máquina abona un euro."

    hide screen pantalla_maquina
    scene cafeteria mediodia with dissolve
    encargada "¿Y ahora?"
    "Ahora sí puedes ir a comer."
    call screen tarjeta("Reto 4 resuelto", "Mantenimiento en plena hora punta", "La revisión arranca en la fecha y hora programadas.", "Seguir")
    jump reto_capacidad

screen recorrido_diagnostico():
    modal True
    add Solid("#071e22b8")
    frame:
        align (0.5, 0.5)
        xsize 1120
        padding (34, 30)
        background Solid("#10292e")
        vbox:
            spacing 18
            text "Recorrido del autodiagnóstico" size 34
            add Transform("images/diagrama-diagnostico.png", xysize=(1052, 220), fit="contain") xalign 0.5
            textbutton "Proponer reparación" action Return() style "boton"
    key "game_menu" action Show("pausa")

screen elegir_diagnostico():
    modal True
    add Solid("#071e22b8")
    frame:
        align (0.5, 0.5)
        xsize 1120
        padding (34, 30)
        background Solid("#10292e")
        vbox:
            spacing 18
            text "¿Qué evento debe iniciar el autodiagnóstico?" size 34
            add Transform("images/diagrama-diagnostico.png", xysize=(1052, 205), fit="contain") xalign 0.5
            text "Al guardar, el equipo queda programado y sigue admitiendo vasos. La revisión debe empezar mañana a las 08:00." size 24
            textbutton "Al llegar la fecha y hora · at(fechaHoraProgramada)" action Return(True) style "boton"
            textbutton "Ocho horas después de guardar · after(8 h)" action Return(False) style "boton"
    key "game_menu" action Show("pausa")

screen resultado_diagnostico(correcta):
    modal True
    add Solid("#071e22b8")
    frame:
        align (0.5, 0.5)
        xsize 1060
        padding (34, 30)
        background Solid("#10292e")
        vbox:
            spacing 16
            text "Banco de pruebas del autodiagnóstico" size 25
            if correcta:
                text "Solución correcta" size 34 color "#a6ead5"
                text "Guardas hoy a las 13:55 · Empieza mañana a las 08:00." size 24
                text "Guardas hoy a las 16:00 · Empieza mañana a las 08:00." size 24
                text "at(fechaHoraProgramada) responde a una fecha y hora concretas." size 23
                textbutton "Aplicar la reparación" action Return() style "boton"
            else:
                text "Solución incorrecta" size 34 color "#ffb1a7"
                text "Guardas hoy a las 13:55 · Empieza hoy a las 21:55." size 24
                text "Guardas hoy a las 16:00 · Empieza mañana a las 00:00." size 24
                text "after(8 h) mide un plazo desde que se guarda la programación. La hora de inicio cambia según cuándo pulses Guardar." size 23
                textbutton "Probar otra opción" action Return() style "boton"
    key "game_menu" action Show("pausa")
