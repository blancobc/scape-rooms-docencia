define estudiante = Character("Estudiante", color="#ffcd9a")
image encargada vaso = Transform("images/encargada-vaso.png", xysize=(660, 610), fit="contain")
image estudiante contento = Transform("images/estudiante-contento.png", xysize=(570, 590), fit="contain")
image estudiante desconcertado = Transform("images/estudiante-vaso.png", xysize=(570, 590), fit="contain")
image maquina devolviendo_espresso = Transform("images/maquina-devuelve-espresso.png", xysize=(1280, 720), fit="cover")
image maquina espresso = Transform("images/maquina-espresso.png", xysize=(1280, 720), fit="cover")

# Cada par indica si la rama acepta o rechaza la medida exacta del límite.
define reparaciones_altura = (
    (True, False),
    (False, True),
    (False, False),
)

init python:
    def ramas_altura(altura, guardas):
        acepta_limite, rechaza_limite = guardas
        return (
            altura > 80 or (altura == 80 and acepta_limite),
            altura < 80 or (altura == 80 and rechaza_limite),
        )

    def etiqueta_altura(altura):
        return "{},{} cm".format(altura // 10, altura % 10)

transform centro_cafeteria:
    xalign 0.44
    yalign 1.0

label reto_altura:
    $ iniciar_reto(2)
    scene cafeteria
    show encargada vaso at junto_mostrador
    with fade
    "La cafetería abre. Durante el desayuno, la máquina devuelve un euro por cada vaso. A media mañana, la encargada vuelve a llamarte."
    encargada "Lo del euro ya funciona. Ahora tenemos un problema de altura."

    encargada "La máquina dice que este vaso es demasiado pequeño. Prueba con él. Como siga así, vamos a tener que servir el café con alzas."

    "La encargada te deja el vaso de prueba y vuelve al mostrador."
    hide encargada
    show estudiante desconcertado at centro_cafeteria
    with dissolve
    "El estudiante que acaba de intentar devolver su vaso se acerca a la máquina."
    estudiante "Es el del café solo. Me lo habéis dado aquí hace cinco minutos."

    scene maquina vacia with dissolve
    show screen pantalla_maquina("Modo de prueba", "Mínimo: 8 cm")
    call screen accion("Probar el vaso de café solo")

    show maquina espresso
    show screen pantalla_maquina("Altura detectada", "8,0 cm")
    with cambio_vaso
    "Colocas el vaso pequeño en la compuerta. El sensor lee {b}8,0 cm{/b}, justo la altura mínima admitida."

    show maquina devolviendo_espresso
    show screen pantalla_maquina("Vaso demasiado pequeño", "Devuelto")
    with cambio_vaso
    "La máquina te devuelve el vaso. La pantalla insiste: {b}«Vaso demasiado pequeño»{/b}."
    show maquina vacia with cambio_vaso

    call screen accion("Ver recorrido de la altura")
    hide screen pantalla_maquina
    call screen recorrido_altura

label reparar_altura:
    call screen elegir_guardas_altura
    $ guardas_propuestas = _return
    $ registrar_respuesta("guardas", guardas_propuestas, guardas_propuestas == reparaciones_altura[0])
    call screen verificar_guardas_altura(guardas_propuestas)

    if _return == "revisar":
        jump reparar_altura

    show screen pantalla_maquina("Inserta el vaso")
    call screen accion("Repetir la devolución")

    show maquina espresso
    show screen pantalla_maquina("Vaso aceptado", "8,0 cm")
    with cambio_vaso
    "El sensor vuelve a leer 8,0 cm. Esta vez la máquina acepta el vaso."

    show maquina vacia
    show screen pantalla_maquina("Abono recibido", "1 €")
    with cambio_vaso
    "El vaso cae al depósito y la máquina abona un euro."

    hide screen pantalla_maquina
    scene cafeteria
    show estudiante contento at centro_cafeteria
    with dissolve
    "El estudiante mira el móvil y sonríe al ver el abono."
    estudiante "Perfecto. Ya puedo permitirme devolver el siguiente."
    call screen tarjeta("Reto 2 resuelto", "Un vaso al que le falta un milímetro", "Las guardas son mutuamente excluyentes y el vaso de 8 cm entra por la ruta de aceptación.", "Seguir")
    jump reto_tiempo

screen recorrido_altura():
    modal True

    add Solid("#071e22b8")
    frame:
        align (0.5, 0.5)
        xsize 1100
        padding (34, 30)
        background Solid("#10292e")
        vbox:
            spacing 17
            text "Recorrido de la validación" size 34
            add Transform("images/diagrama-validacion.png", xysize=(1032, 210), fit="contain") xalign 0.5
            textbutton "Proponer nuevas guardas" action Return() style "boton"
    key "game_menu" action Show("pausa")

screen elegir_guardas_altura():
    modal True
    add Solid("#071e22b8")
    frame:
        align (0.5, 0.5)
        xsize 1100
        padding (36, 32)
        background Solid("#10292e")
        vbox:
            spacing 16
            text "Elige las guardas de validación" size 34
            add Transform("images/diagrama-validacion.png", xysize=(1028, 205), fit="contain") xalign 0.5
            text "Los vasos de 8 cm o más se aceptan. Los más pequeños se devuelven. Cada medida debe habilitar una sola salida." size 24
            textbutton "Aceptar ≥ 8 cm · Rechazar < 8 cm" action Return(reparaciones_altura[0]) style "boton"
            textbutton "Aceptar > 8 cm · Rechazar ≤ 8 cm" action Return(reparaciones_altura[1]) style "boton"
            textbutton "Aceptar > 8 cm · Rechazar < 8 cm" action Return(reparaciones_altura[2]) style "boton"
    key "game_menu" action Show("pausa")

screen verificar_guardas_altura(guardas):
    modal True
    $ medidas = (79, 80, 81)
    $ resultados = ("Devuelto", "Aceptado", "Aceptado")
    $ correcta = guardas == reparaciones_altura[0]
    add Solid("#071e22b8")
    frame:
        align (0.5, 0.5)
        xsize 1020
        padding (34, 30)
        background Solid("#10292e")
        vbox:
            spacing 16
            text "Banco de pruebas del sensor" size 25
            if correcta:
                text "Solución correcta" size 34 color "#a6ead5"
            else:
                text "Solución incorrecta" size 34 color "#ffb1a7"
            for indice, medida in enumerate(medidas):
                $ lectura = etiqueta_altura(medida)
                $ acepta, rechaza = ramas_altura(medida, guardas)
                $ resultado = "Aceptado" if acepta else "Devuelto" if rechaza else "Ninguna salida"
                $ esperado = resultados[indice]
                text "[lectura] · [resultado]   (esperado: [esperado])" size 24
            if correcta:
                text "Cada altura habilita una sola ruta y el vaso de 8 cm se acepta." size 24 color "#a6ead5"
                textbutton "Aplicar la reparación" action Return("aplicar") style "boton"
            else:
                if guardas[1]:
                    text "Las guardas son excluyentes, pero el vaso de 8 cm aún se rechaza." size 24 color "#ffb1a7"
                else:
                    text "Con 8 cm ninguna guarda se cumple. La máquina se queda esperando." size 24 color "#ffb1a7"
                textbutton "Revisar las guardas" action Return("revisar") style "boton"
    key "game_menu" action Show("pausa")
