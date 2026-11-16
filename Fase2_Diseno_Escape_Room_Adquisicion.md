# Fase 2. Diseño del escape room de adquisición

**Descripción.** Diseño de una actividad sobre máquinas de estados UML para Ingeniería del Software I. El tema pertenece al bloque de diseño de la asignatura, que sigue a los de requisitos y arquitectura.

**Participantes.** Carlos, como responsable principal, con el apoyo del resto del equipo.  
**Temporización prevista en la memoria.** Octubre de 2026.  
**Estado.** Borrador para revisión por escenas. Se propone una máquina de devolución de vasos reutilizables.

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

### Misión y secuencia provisional de retos

Esta semana la facultad ha instalado una máquina para recuperar y reutilizar los vasos de la cafetería. Al pedir una bebida, se paga un euro de depósito por el vaso. Al devolverlo a la máquina, se recupera ese euro y el vaso se recoge para lavarlo y volver a usarlo. En **Operación Vaso Doble**, el jugador debe reparar la máquina antes de que abra la facultad por la mañana. Cada reto arranca con un fallo visible. El jugador reproduce el incidente, abre el panel con la clase y el fragmento de diagrama pertinente, elige una reparación y repite la prueba para ver sus efectos.

| Reto | Lo que ve el jugador | Qué investiga y corrige |
| --- | --- | --- |
| **1. Un vaso, dos euros** | Entra un vaso con un euro de depósito. El móvil vibra dos veces y el historial muestra dos abonos. La pantalla dice «Gracias por volver». | Rastrear las llamadas y las acciones del modelo. El abono se ejecuta al validar el vaso y al cerrar la devolución. Situarlo en la transición que confirma la recogida y comprobar que se ejecuta una sola vez. |
| **2. Admitido y expulsado** | El vaso de 8 cm, justo en el límite admitido, recibe el mensaje «Vaso aceptado» o acaba devuelto según qué ruta habilitada tome el controlador. | Revisar las dos salidas del mismo estado ante `validarVaso(altura)`. Probar las guardas con medidas por debajo, justo en el límite y por encima. |
| **3. Cinco segundos de paciencia** | La compuerta se cierra en cuanto el jugador pulsa «Devolver». La pantalla le aconseja que la próxima vez se dé más prisa. | Colocar `after(5 s)` en la salida del estado «Esperando vaso». Comparar una devolución a tiempo con una sesión en la que nadie introduce el vaso. |
| **4. Mantenimiento en plena hora punta** | La encargada programa el autodiagnóstico para las ocho. La máquina se pone a hacerlo en ese mismo momento, delante de toda la cola. | Usar `at(horaProgramada)` desde el estado de espera. Verificar que programar la hora deja pendiente el diagnóstico hasta que llegue ese momento. |
| **5. El vaso que ya no cabe** | El último vaso llena el módulo de recogida. La máquina saluda al siguiente cliente con «Todavía hay sitio» y admite otro vaso. | Añadir `when(depositoLleno)` mientras está activo el estado que supervisa la capacidad. Comprobar que el sensor pasa de falso a verdadero y que, una vez lleno, `iniciarDevolucion()` deja de abrir la compuerta. |

Los tiempos son orientativos. Se reservan **3 minutos para el arranque, 5 por reto y 2 para el cierre**. El primer reto introduce la clase y el panel de diagnóstico. En el cuarto se puede revisar el fragmento del ciclo de autodiagnóstico para trabajar la salida sin disparador del nodo inicial y el estado final sin salidas.

## 2. Adaptación del marco metodológico al contexto concreto

La partida será individual y durará unos 30 minutos. Se combinarán retos de elección múltiple con decisiones que modifican la escena, pistas y retroalimentación inmediata. El alumnado podrá completar la misión por cualquier ruta y recibirá un resumen final con los errores que conviene revisar.

Detectar fallos practica el **pensamiento crítico**. Completar el modelo y recorrerlo con eventos concretos practica la **resolución de problemas**. Elegir entre diseños válidos y anticipar sus consecuencias practica la **toma de decisiones**.

El **ODS 12, Producción y consumo responsables**, se integra mediante el circuito de devolución y reutilización de vasos. Tras el último fallo, el jugador puede pedir un recambio y seguir atendiendo con el módulo de reserva o pausar la máquina para sustituir el lleno. El cierre muestra cómo afecta la decisión a las devoluciones completadas y a la espera en la cola. La Fase 4 definirá el registro de la primera partida y la encuesta.
