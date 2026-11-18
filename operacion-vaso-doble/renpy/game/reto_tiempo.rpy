image encargada reloj = Transform("images/encargada-reloj.png", xysize=(660, 610), fit="contain")
image encargada cartel = Transform("images/encargada-cartel.png", xysize=(660, 610), fit="contain")
image maquina cerrada = Transform("images/maquina-cerrada.png", xysize=(1280, 720), fit="cover")

label reto_tiempo:
    $ iniciar_reto(3)
    scene cafeteria
    show encargada reloj at junto_mostrador
    with fade
    "Poco antes del descanso, la encargada vuelve a llamarte. Está delante de la máquina con un vaso en una mano y el móvil en la otra."
    encargada "Ahora acepta el vaso pequeño. Si consigues meterlo."

    scene maquina cerrada with dissolve
    show screen pantalla_maquina("Lista para devolver")
    call screen accion("Devolver")

    show maquina vacia
    show screen pantalla_maquina("Inserta el vaso")
    with cambio_vaso
    pause 0.25

    show maquina cerrada
    show screen pantalla_maquina("Tiempo agotado", "Gracias por tu paciencia", tam_detalle=16)
    with cambio_vaso
    "La compuerta se abre y se cierra antes de que puedas levantar el vaso."
    encargada "La mía también se está agotando."

    call screen accion("Ver recorrido del temporizador")
    hide screen pantalla_maquina
    call screen recorrido_tiempo

label reparar_tiempo:
    call screen elegir_tiempo
    $ temporizador_en_espera = _return
    $ registrar_respuesta("temporizador", temporizador_en_espera, temporizador_en_espera)
    call screen resultado_tiempo(temporizador_en_espera)

    if not temporizador_en_espera:
        jump reparar_tiempo

    show screen pantalla_maquina("Lista para devolver")
    call screen accion("Repetir la devolución")
    show maquina vacia
    show screen pantalla_maquina("Inserta el vaso")
    with cambio_vaso
    "La encargada espera un segundo a propósito."

    show maquina espresso
    show screen pantalla_maquina("Vaso aceptado")
    with cambio_vaso
    "Mete el vaso. Esta vez todavía está a tiempo."

    show maquina cerrada
    show screen pantalla_maquina("Abono recibido", "1 €")
    with cambio_vaso
    "El vaso cae al depósito y el móvil confirma el abono de un euro."

    hide screen pantalla_maquina
    scene cafeteria
    show encargada cartel at junto_mostrador
    with dissolve
    encargada "Un segundo."
    "Saca del bolsillo un papel doblado. Pone «ACERQUE EL VASO ANTES DE PULSAR». Debajo, en letra más pequeña: «Y SEA RÁPIDO»."
    "Lo arruga y lo tira al cubo."
    encargada "Ya me veía plastificándolo."
    call screen tarjeta("Reto 3 resuelto", "Cinco segundos de paciencia", "El plazo empieza al entrar en «Esperando vaso».", "Seguir")
    jump reto_diagnostico

screen recorrido_tiempo():
    modal True
    add Solid("#071e22b8")
    frame:
        align (0.5, 0.5)
        xsize 1120
        padding (34, 30)
        background Solid("#10292e")
        vbox:
            spacing 18
            text "Recorrido del temporizador" size 34
            add Transform("images/diagrama-temporizador.png", xysize=(1052, 220), fit="contain") xalign 0.5
            textbutton "Proponer reparación" action Return() style "boton"
    key "game_menu" action Show("pausa")

screen elegir_tiempo():
    modal True
    add Solid("#071e22b8")
    frame:
        align (0.5, 0.5)
        xsize 1120
        padding (34, 30)
        background Solid("#10292e")
        vbox:
            spacing 18
            text "¿Desde qué estado cuentas los cinco segundos?" size 34
            add Transform("images/diagrama-temporizador.png", xysize=(1052, 205), fit="contain") xalign 0.5
            text "La compuerta debe esperar hasta cinco segundos desde que se abre. Si detecta un vaso a tiempo, pasa a validarlo." size 24
            textbutton "Desde «Disponible» · after(5 s)" action Return(False) style "boton"
            textbutton "Desde «Esperando vaso» · after(5 s)" action Return(True) style "boton"
    key "game_menu" action Show("pausa")

screen resultado_tiempo(correcta):
    modal True
    add Solid("#071e22b8")
    frame:
        align (0.5, 0.5)
        xsize 1060
        padding (34, 30)
        background Solid("#10292e")
        vbox:
            spacing 16
            text "Banco de pruebas del temporizador" size 25
            if correcta:
                text "Solución correcta" size 34 color "#a6ead5"
            else:
                text "Solución incorrecta" size 34 color "#ffb1a7"
            text "En ambos casos dejas la máquina seis segundos en reposo antes de pulsar Devolver." size 23
            text "Vaso a los 3 s de abrir · Pasa a validación." size 24
            if correcta:
                text "Sin vaso · Se cierra a los 5 s de abrir." size 24
                text "El evento temporal se programa al entrar en «Esperando vaso»." size 23
                textbutton "Aplicar la reparación" action Return() style "boton"
            else:
                text "Sin vaso · Sigue abierta después de 5 s." size 24 color "#ffb1a7"
                text "El temporizador vence durante el reposo. Cuando la compuerta se abre, el plazo ya ha transcurrido." size 23
                textbutton "Probar otra opción" action Return() style "boton"
    key "game_menu" action Show("pausa")
