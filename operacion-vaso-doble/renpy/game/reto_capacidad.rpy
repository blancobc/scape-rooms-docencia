image cafeteria sobremesa = Transform("images/cafeteria-sobremesa.png", xysize=(1280, 720), fit="cover")
image encargada pensando = Transform("images/encargada-pensando.png", xysize=(660, 610), fit="contain")
image maquina llena = Transform("images/maquina-llena.png", xysize=(1280, 720), fit="cover")
image encargada aviso = Transform("images/encargada-aviso.png", xysize=(660, 610), fit="contain")

define opciones_capacidad = (
    "when(depositoLleno) / bloquearDevoluciones()",
    "iniciarDevolucion() [depositoLleno] / bloquearDevoluciones()",
    "after(5 s) / bloquearDevoluciones()",
    "when(not depositoLleno) / bloquearDevoluciones()",
)
define errores_capacidad = (
    "",
    "Una guarda se comprueba cuando llega su evento. La máquina seguirá ofreciendo el servicio hasta que alguien pulse Devolver.",
    "El plazo vence aunque quede espacio. El tiempo transcurrido no indica si el depósito está lleno.",
    "La condición se activa cuando vuelve a haber espacio. Bloquearías la máquina al vaciar el depósito.",
)

label reto_capacidad:
    scene cafeteria sobremesa with fade
    "Estás terminando de comer cuando oyes a la encargada desde la máquina."
    encargada "No metas ese. Espera."

    scene maquina llena
    show screen pantalla_maquina("Adelante")
    with dissolve
    "Un estudiante acerca su vaso. El depósito está lleno hasta arriba, pero la compuerta sigue abierta."
    encargada "El sensor marca lleno. La máquina se ha tomado el dato como una sugerencia."
    cliente "Si lo pongo de lado…"
    encargada "Tú tampoco."

    call screen accion("Probar el sensor")
    show screen pantalla_maquina("Señal simulada", "Lleno: no", tam_detalle=22)
    with cambio_vaso
    "El panel permite simular la señal del sensor para comprobar el programa. El depósito sigue lleno. Durante la prueba, la encargada impide que se introduzcan más vasos."
    "Fijas la señal de prueba en «Lleno: no». Ahora vas a cambiarla a «Lleno: sí» para reproducir la transición de falso a verdadero."
    call screen accion("Activar el sensor de lleno")
    show screen pantalla_maquina("Señal simulada", "Lleno: sí", tam_detalle=22)
    with cambio_vaso
    "La señal simulada cambia a verdadero. El registro sigue indicando «Disponible»: el controlador no reacciona al cambio."
    call screen accion("Ver recorrido de la capacidad")
    hide screen pantalla_maquina
    call screen recorrido_capacidad

label reparar_capacidad:
    call screen elegir_capacidad
    $ reparacion_capacidad = _return
    call screen resultado_capacidad(reparacion_capacidad)
    if reparacion_capacidad != 0:
        jump reparar_capacidad

    show maquina cerrada
    show screen pantalla_maquina("Depósito lleno", "Espera al personal", tam_detalle=18)
    with cambio_vaso
    "Repites el cambio de la señal simulada. Ahora el controlador pasa a «Depósito lleno» y cierra la compuerta. Terminas la prueba y reconectas la lectura real del sensor, que también indica lleno."
    "La encargada abre el compartimento de servicio, retira el depósito lleno y coloca uno vacío. El sensor real vuelve a marcar espacio disponible y el servicio se reanuda."
    show maquina vacia
    show screen pantalla_maquina("Adelante")
    with cambio_vaso
    cliente "¿Ahora?"
    encargada "Ahora recto, por favor."
    hide screen pantalla_maquina

    scene cafeteria sobremesa
    show encargada pensando at junto_mostrador
    with dissolve
    encargada "Vale, ya sabe cuándo está lleno. ¿Podemos conseguir que me avise antes de que haya seis personas esperando?"
    call screen configurar_aviso

label decidir_aviso:
    call screen elegir_aviso
    $ umbral_aviso = _return
    call screen consecuencia_aviso(umbral_aviso)
    if _return == "revisar":
        jump decidir_aviso

    "Más tarde, durante el siguiente periodo de devoluciones, llega el momento de comprobar el aviso."
    scene cafeteria sobremesa
    show encargada aviso at junto_mostrador
    with dissolve
    if umbral_aviso == 80:
        "Cuando el depósito alcanza el 80 por ciento de su capacidad, suena el móvil de la encargada. Quedan unos diez minutos de margen al ritmo previsto."
        encargada "Qué detalle. Esta vez me llama antes de montar la cola."
    elif umbral_aviso == 50:
        "Con el depósito a la mitad llega el aviso. La encargada organiza una revisión con margen."
        encargada "Todavía cabe media cafetería. Bueno, voy organizándome."
    elif umbral_aviso == 95:
        "El aviso llega casi al llenarse. La máquina se bloquea antes de que el personal pueda acudir."
        encargada "Me ha avisado. La cola también."
    else:
        "El aviso llega con el depósito lleno. Durante los cinco minutos de espera, las devoluciones quedan interrumpidas."
        encargada "El móvil y la cola me lo han dicho a la vez."

    call screen tarjeta("Reto 5 completado", "Operación Vaso Doble", "Reparaste el evento de cambio y configuraste el aviso de capacidad. El circuito de devolución permite lavar los vasos y volver a usarlos.", "Volver al menú")
    return

screen recorrido_capacidad():
    modal True
    add Solid("#071e22b8")
    frame:
        align (0.5, 0.5)
        xsize 1120
        padding (34, 30)
        background Solid("#10292e")
        vbox:
            spacing 18
            text "Recorrido de la capacidad" size 34
            add Transform("images/diagrama-capacidad.png", xysize=(1052, 210), fit="contain") xalign 0.5
            textbutton "Proponer reparación" action Return() style "boton"
    key "game_menu" action Show("pausa")

screen elegir_capacidad():
    modal True
    add Solid("#071e22b8")
    frame:
        align (0.5, 0.5)
        xsize 1120
        padding (30, 24)
        background Solid("#10292e")
        vbox:
            spacing 12
            text "¿Qué evento debe bloquear las devoluciones?" size 32
            add Transform("images/diagrama-capacidad.png", xysize=(1060, 155), fit="contain") xalign 0.5
            text "El sensor debe provocar el cambio de estado sin esperar a una nueva petición del usuario." size 23
            for indice, opcion in enumerate(opciones_capacidad):
                textbutton opcion substitute False action Return(indice) style "boton" text_size 22
    key "game_menu" action Show("pausa")

screen resultado_capacidad(opcion):
    modal True
    add Solid("#071e22b8")
    frame:
        align (0.5, 0.5)
        xsize 1060
        padding (34, 30)
        background Solid("#10292e")
        vbox:
            spacing 16
            text "Banco de pruebas de capacidad" size 25
            if opcion == 0:
                text "Solución correcta" size 34 color "#a6ead5"
                text "El sensor pasa a lleno, sin pulsar nada · Se bloquean las devoluciones." size 23
                text "Sigue habiendo espacio · Se mantiene disponible." size 23
                text "when(depositoLleno) reacciona al cambio de falso a verdadero." size 23
                textbutton "Aplicar la reparación" action Return() style "boton"
            else:
                text "Solución incorrecta" size 34 color "#ffb1a7"
                if opcion == 1:
                    text "Se llena sin pulsar nada · Sigue disponible." size 23
                    text "Hay espacio y pulsas Devolver · Funciona la devolución." size 23
                elif opcion == 2:
                    text "Se llena antes de 5 s · Sigue disponible hasta que vence el plazo." size 23
                    text "Hay espacio al cumplirse 5 s · Se bloquea igualmente." size 23
                else:
                    text "El sensor pasa a lleno · No se produce el bloqueo." size 23
                    text "Se vacía el depósito · Se bloquea al pasar a tener espacio." size 23
                $ motivo = errores_capacidad[opcion]
                text motivo size 23
                textbutton "Probar otra opción" action Return() style "boton"
    key "game_menu" action Show("pausa")

screen configurar_aviso():
    modal True
    add Solid("#071e22b8")
    frame:
        align (0.5, 0.5)
        xsize 950
        padding (34, 30)
        background Solid("#10292e")
        vbox:
            spacing 18
            text "Un aviso antes de llegar al límite" size 34
            text "Capacidad: 100 vasos.\nLlegadas durante el descanso: unos 2 vasos/minuto.\nEl personal tarda 5 minutos en acudir." size 25
            text "ODS 12 · Producción y consumo responsables" size 24 color "#a6ead5"
            text "Elige cuándo avisar para mantener el circuito de reutilización y organizar el trabajo del personal. El bloqueo al llenarse sigue activo." size 23
            textbutton "Configurar el aviso" action Return() style "boton"
    key "game_menu" action Show("pausa")

screen elegir_aviso():
    modal True
    add Solid("#071e22b8")
    frame:
        align (0.5, 0.5)
        xsize 1000
        padding (34, 30)
        background Solid("#10292e")
        vbox:
            spacing 16
            text "¿Cuándo debe avisar al personal?" size 34
            text "100 vasos · 2 vasos/minuto · 5 minutos para acudir" size 24
            for umbral in (50, 80, 95, 100):
                $ opcion_aviso = "Solo al llenarse" if umbral == 100 else "Al " + str(umbral) + " %"
                textbutton opcion_aviso action Return(umbral) style "boton"
    key "game_menu" action Show("pausa")

screen consecuencia_aviso(umbral):
    modal True
    add Solid("#071e22b8")
    frame:
        align (0.5, 0.5)
        xsize 1040
        padding (34, 30)
        background Solid("#10292e")
        vbox:
            spacing 16
            text "Consecuencias de la configuración" size 32
            if umbral == 80:
                text "Margen adecuado para este caso" size 29 color "#a6ead5"
                text "Quedan 20 plazas, unos 10 minutos. El personal llega en 5 minutos, antes del bloqueo." size 24
            elif umbral == 50:
                text "Aviso muy anticipado" size 29 color "#ffcd9a"
                text "Quedan 50 plazas, unos 25 minutos. Hay margen de sobra, pero habrá que revisar y organizar el recambio antes y con más frecuencia si se sustituye a media capacidad." size 24
            elif umbral == 95:
                text "El aviso llega tarde" size 29 color "#ffb1a7"
                text "Quedan 5 plazas, unos 2,5 minutos. El personal tarda 5 minutos: el servicio puede interrumpirse unos 2,5 minutos." size 24
            else:
                text "El aviso coincide con el bloqueo" size 29 color "#ffb1a7"
                text "La máquina ya está llena. Las devoluciones se interrumpen durante los 5 minutos que tarda el personal." size 24
            text "Los tiempos suponen una llegada constante. Si cambia la afluencia o el tiempo de respuesta, hay que revisar el umbral." size 22
            text "Evitar interrupciones facilita que los vasos vuelvan a recogerse, lavarse y reutilizarse." size 23
            hbox:
                spacing 16
                textbutton "Cambiar configuración" action Return("revisar") style "boton"
                textbutton "Mantener configuración" action Return("mantener") style "boton"
    key "game_menu" action Show("pausa")
