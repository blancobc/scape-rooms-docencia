# Fase 2. Diseño del escape room de adquisición

**Descripción.** Diseño de una actividad sobre máquinas de estados UML para Ingeniería del Software I. El tema pertenece al bloque de diseño de la asignatura, que sigue a los de requisitos y arquitectura.

**Participantes.** Carlos, como responsable principal, con el apoyo del resto del equipo.  
**Temporización prevista en la memoria.** Octubre de 2026.  
**Estado.** Borrador de contenidos y retos. La narrativa y el dispositivo quedan por elegir.

## 1. Diseño del escape room de adquisición

### Conceptos que se trabajarán

| Concepto | Qué deberá hacer el alumnado |
| --- | --- |
| **Comportamiento de una clase** | Identificar los estados relevantes de una instancia y predecir cómo responde al mismo evento según su estado. Comprobar que los atributos y las operaciones utilizados están definidos en la clase. |
| **Inicio y fin** | Identificar el primer estado y corregir la única transición que sale del nodo inicial, que debe ir sin disparador. Usar un estado final cuando termina el comportamiento modelado y comprobar que carece de transiciones salientes. |
| **Disparadores y acciones** | Leer y completar etiquetas con la forma `evento [guarda] / acción`. Usar llamadas a operaciones de la clase como disparadores y distinguirlas de las acciones ejecutadas al recorrer la transición. En los diagramas de la actividad, toda transición ordinaria requiere un disparador explícito. |
| **Eventos temporales** | Distinguir una hora programada, `at(...)`, de un plazo contado desde la entrada en el estado, `after(...)`. |
| **Eventos de cambio** | Usar `when(...)` para reaccionar cuando una condición pasa de falsa a verdadera. Una guarda se comprueba al producirse su evento disparador. |
| **Guardas** | Si dos transiciones salen del mismo estado con el mismo evento, comprobar que sus guardas sean mutuamente excluyentes. Probar el valor límite y comprobar qué casos debe cubrir el modelo según el enunciado. |

Las transparencias también incluyen señales y acciones de estado (`entry`, `do` y `exit`). Pueden aparecer en un reto adicional si encajan en el dispositivo elegido. El ejercicio resuelto de la clase `Inmueble` aporta otro criterio de diseño: se puede representar una capacidad con estados distintos o con una guarda, siempre que se conserve el comportamiento pedido.

### Secuencia de retos

La misión consiste en poner en servicio un dispositivo que se comporta de forma inesperada. Cada reto empieza con una escena que muestra el fallo. Después se abre el panel de diagnóstico con la secuencia de eventos, la clase y el fragmento de diagrama implicado. El alumnado selecciona una reparación y vuelve a ejecutar el caso para ver qué ocurre. Los tres incidentes se ilustran con una expendedora y se pueden adaptar a otros dispositivos.

| Bloque | Lo que se ve en el juego | Qué se repara o diseña |
| --- | --- | --- |
| **1. La compra sale gratis** | La máquina entrega un refresco y devuelve todo el dinero introducido. | Seguir la compra por el diagrama y corregir la acción que calcula el cambio. |
| **2. La máquina cancela antes de tiempo** | El cliente está eligiendo un refresco y la máquina le devuelve las monedas nada más empezar la compra. | Revisar el evento temporal. La compra debe caducar a los 30 segundos de entrar en el estado de selección con `after(30 s)`. Este reto puede incluir un segundo caso breve, como programar el inicio del autodiagnóstico a una hora fija con `at(...)`. |
| **3. La máquina sigue aceptando monedas sin existencias** | Se retira la última lata durante una revisión y, al quedar vacía, la máquina todavía acepta monedas. | Diseñar el paso a «Sin existencias» desde «Disponible» con `when(existenciasTotales == 0)`. La prueba debe provocar el cambio de una unidad a cero mientras «Disponible» está activo y comprobar que se deshabilita el cobro. |

### Ejemplo de escena jugable

El jugador introduce **2 €**, elige un refresco de **1,50 €** y ve caer la lata seguida de **2 €** en la bandeja. En el panel de diagnóstico, el rastro de la compra muestra que se ejecutó `devolverCambio(saldo)`. El jugador elige cómo corregir el modelo y repite la compra. Con `devolverCambio(saldo - precio)`, ve caer una sola lata y **0,50 €**. Una segunda compra con importe exacto permite comprobar que el cambio es cero.

Un incidente breve del mismo bloque puede trabajar las **guardas** con un fallo que solo aparece al pagar el importe exacto. El panel muestra que, ante la misma selección, quedan habilitadas a la vez las rutas de dispensar y de rechazar por saldo insuficiente. El jugador ajusta las guardas y comprueba los tres casos de saldo inferior, igual y superior al precio.

## 2. Adaptación del marco metodológico al contexto concreto

La partida será individual y durará unos 30 minutos. Se combinarán retos de elección múltiple con decisiones que modifican la escena, pistas y retroalimentación inmediata. El alumnado podrá completar la misión por cualquier ruta y recibirá un resumen final con los errores que conviene revisar.

Detectar fallos practica el **pensamiento crítico**. Completar el modelo y recorrerlo con eventos concretos practica la **resolución de problemas**. Elegir entre diseños válidos y anticipar sus consecuencias practica la **toma de decisiones**.

Como opción para integrar el **ODS 12, Producción y consumo responsables**, una máquina de refrescos podría plantear una decisión sobre cuándo activar el modo de bajo consumo, considerando el ahorro energético y el tiempo de respuesta. Esta propuesta depende del dispositivo elegido. El diseño final concretará la narrativa, los diagramas, las opciones y las consecuencias de cada decisión. La Fase 4 definirá el registro de la primera partida y la encuesta.
