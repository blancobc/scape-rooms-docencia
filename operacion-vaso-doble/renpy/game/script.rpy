define config.rollback_enabled = False
define config.name = "Operación Vaso Doble"
define config.save_directory = "operacion-vaso-doble"
define config.window_title = "Operación Vaso Doble"
define encargada = Character("Encargada", color="#a6ead5")

init python:
    gui.init(1280, 720)

image cafeteria = Transform("images/cafeteria.png", xysize=(1280, 720), fit="cover")
image maquina con_vaso = Transform("images/maquina.png", xysize=(1280, 720), fit="cover")
image maquina vacia = Transform("images/maquina-vacia.png", xysize=(1280, 720), fit="cover")

define cambio_vaso = Dissolve(0.2)
image encargada hablando = Transform("images/encargada-hablando.png", xysize=(660, 610), fit="contain")
image encargada llave = Transform("images/encargada-preocupada.png", xysize=(660, 610), fit="contain")

transform junto_mostrador:
    xalign 0.16
    yalign 1.0

label start:
    $ iniciar_registro()
    call encuesta_confianza("pre")
    $ registro_actual.anotar("inicio_juego")
    $ iniciar_reto(1)
    scene cafeteria with dissolve
    "Es una mañana cualquiera y faltan treinta minutos para que abra la facultad. Esta semana han instalado una máquina para recuperar los vasos reutilizables de la cafetería. Cuando pides un café, pagas un euro de depósito por el vaso. Al devolverlo a la máquina, recuperas el euro y el vaso se recoge para lavarlo y volver a usarlo."

    "Anoche, alguien descubrió que la máquina devolvía dos euros por un solo vaso. En el grupo de clase ya circula un vídeo titulado «Cómo financiar el café de todo el cuatrimestre». El primer comentario es de hace tres minutos: «¿A qué hora abren?»."

    show encargada hablando at junto_mostrador with dissolve
    "Eres becario de la facultad y hoy te toca echar una mano con el sistema de devolución. Nada más llegar, la encargada de la cafetería te llama desde el mostrador."
    encargada "¿Puedes echarle un vistazo a la máquina antes de que abramos? Como se corra más la voz, hoy nos van a salir caros los cafés."
    show encargada llave at junto_mostrador with dissolve
    "Te entrega la llave del panel técnico y deja un vaso de prueba junto a la máquina."
    encargada "Toma. Es el mismo del vídeo. A este paso, lo ponemos en nómina."

    call screen accion("Abrir el panel técnico")
    scene maquina vacia with dissolve
    show screen pantalla_maquina("Inserta el vaso")
    "Giras la llave y se enciende el panel. La compuerta se abre. Acercas el vaso a la boca de la máquina."

    show maquina con_vaso
    show screen pantalla_maquina("Abono recibido", "1 €")
    with cambio_vaso
    "Dejas el vaso en la compuerta. La máquina lo reconoce y suena un bip. {b}«Abono recibido: 1 €»{/b}."

    show maquina vacia
    show screen pantalla_maquina("Segundo abono", "1 €")
    with cambio_vaso
    "El vaso cae al depósito y desaparece de la compuerta. Suena otro bip. {b}«Abono recibido: 1 €»{/b}."

    show screen pantalla_maquina("Gracias por volver", "Total: 2 €")
    "La máquina muestra {b}«Gracias por volver»{/b}."

    call screen accion("Ver recorrido")
    hide screen pantalla_maquina
    call screen recorrido_devolucion
    jump reparar_abono

label reparar_abono:
    call screen elegir_abono
    $ momento_abono = _return
    $ registrar_respuesta("abono", momento_abono, momento_abono == "caida")

    if momento_abono == "caida":
        call screen tarjeta(
            "Comprobación del abono",
            "Solución correcta",
            "Si el vaso cae al depósito, se abona 1 €. Si lo retiras tras validarlo, se abonan 0 €. confirmarRecogida() solo se dispara cuando la máquina ha recogido el vaso.",
            "Confirmar reparación",
            acento="#a6ead5"
        )
        encargada "Un vaso, un euro. Ya podemos dejar de buscarle despacho."
        call screen tarjeta("Reto 1 resuelto", "Un vaso, dos euros", "Vinculaste el abono a la transición que confirma la recogida.", "Seguir")
        jump reto_altura

    if momento_abono == "inicio":
        $ motivo_abono = "La máquina abona 1 € al abrir la compuerta, aunque no hayas presentado ningún vaso."
    else:
        $ motivo_abono = "La máquina abona 1 € al reconocer el vaso. Si lo retiras antes de que caiga, cobras el euro y te quedas con el vaso."

    call screen tarjeta(
        "Comprobación del abono",
        "Solución incorrecta",
        motivo_abono,
        "Probar otra opción",
        acento="#ffb1a7"
    )
    jump reparar_abono
