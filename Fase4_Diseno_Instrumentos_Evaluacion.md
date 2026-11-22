# Fase 4. Diseño de los instrumentos de evaluación

**Descripción.** Diseño e integración de encuestas antes y después del juego y de un registro de la actividad para valorar la experiencia e identificar contenidos que requieren refuerzo.  
**Ámbito actual.** Operación Vaso Doble, en Ingeniería del Software I. Instrumentos adaptables a los demás juegos del proyecto.  
**Temporización.** Preparación previa a la aplicación en el aula; fecha pendiente de concretar.  
**Estado.** Instrumentos implementados en Ren’Py y exportación conjunta en CSV. Pendiente de pilotaje con alumnado.

## 1. Encuestas inicial y final

### Confianza para aplicar los contenidos

Antes y después del juego se plantea la misma pregunta: **«¿Qué seguridad tienes de poder realizar estas tareas?»**. Las seis tareas se muestran juntas en una matriz, con escala **1 Ninguna · 2 Poca · 3 Moderada · 4 Bastante · 5 Mucha**.

| Contenido | Tarea que se valora |
| --- | --- |
| Interpretación | Interpretar un diagrama de estados UML y seguir qué ocurre al producirse una secuencia de eventos. |
| Acciones | Elegir en qué transición debe ejecutarse una acción para obtener el comportamiento esperado. |
| Guardas | Definir guardas mutuamente excluyentes que funcionen también en los valores límite. |
| Tiempo relativo | Usar `after(...)` y elegir el estado desde el que debe comenzar a contarse un plazo. |
| Fecha y hora | Usar `at(...)` para provocar una transición en una fecha y hora programadas. |
| Cambio de condición | Usar `when(...)` para reaccionar a un cambio de condición y distinguirlo de una guarda. |

Las respuestas se inicializan en 3 y se guardan al pulsar «Siguiente». La encuesta mide confianza percibida; su cambio no demuestra por sí solo una mejora del aprendizaje. Un 3 guardado tampoco permite distinguir una elección deliberada de una opción dejada por defecto.

### Valoración de la experiencia

Solo al finalizar se muestra otra matriz con estas afirmaciones y escala **1 Totalmente en desacuerdo · 2 En desacuerdo · 3 Ni de acuerdo ni en desacuerdo · 4 De acuerdo · 5 Totalmente de acuerdo**:

- El juego me ha ayudado a comprender mejor las máquinas de estados UML.
- Las explicaciones de las respuestas me han ayudado a entender mis errores.
- La historia ha mantenido mi interés durante la actividad.
- La actividad ha aumentado mi motivación para practicar con diagramas de estados.
- Considero adecuado utilizar juegos de este tipo para aprender contenidos de la asignatura.

También se inicializan en 3. Todo el alumnado responde a la afirmación sobre las explicaciones; el registro permitirá distinguir después a quienes acertaron a la primera.

La última pantalla reúne **«¿Cómo valorarías la dificultad del juego?»**, con opciones Muy baja, Baja, Adecuada, Alta y Muy alta, y **«¿Qué cambiarías para mejorar la actividad?»**, como respuesta opcional de hasta 500 caracteres. La dificultad tiene «Adecuada» preseleccionada. No se incluye una pregunta abierta adicional sobre dudas de UML.

## 2. Registro de la actividad y entrega de datos

Cada partida genera un identificador aleatorio y un único CSV que reúne los siguientes datos:

| Datos | Finalidad |
| --- | --- |
| Inicio, fin y estado de la partida | Distinguir sesiones completadas e interrumpidas. |
| Tiempo total, comienzo y final del juego y de cada reto | Separar la duración global, que incluye encuestas, del recorrido narrativo y los retos. |
| Decisión, opción elegida, corrección, número de intento y errores acumulados | Identificar fallos frecuentes y aciertos a la primera en cada decisión evaluada. |
| Respuestas iniciales y finales | Comparar la confianza por contenido y recoger la valoración de la experiencia. |

El tiempo es transcurrido e incluye lectura y posibles pausas; no mide exclusivamente resolución. Las decisiones del aviso preventivo se analizan por su elección y consecuencias, sin convertirlas automáticamente en errores conceptuales.

El archivo utiliza separador de punto y coma y codificación UTF-8. En la versión web se descarga al finalizar; en escritorio se guarda en la carpeta de registros del juego. El alumnado entrega el CSV mediante una tarea de Moodle. El juego no solicita nombre ni correo; la entrega en Moodle permite al docente asociarlo con quien lo presenta. El identificador distingue partidas, pero por sí solo no identifica repeticiones de una misma persona.

## 3. Criterios de análisis y revisión

Se revisarán los tiempos por reto, el porcentaje de aciertos en el primer intento y las alternativas incorrectas más elegidas. Esto permitirá localizar, por ejemplo, dificultades con valores límite, con el origen del plazo de `after(...)` o con la diferencia entre `when(...)` y una guarda. Se compararán las respuestas iniciales y finales por contenido dentro de cada partida y se resumirán las valoraciones y propuestas de mejora.

Las partidas de prueba del equipo se separarán de las del alumnado. Se distinguirán sesiones completas e incompletas y, cuando puedan identificarse por la entrega, repeticiones. Los tiempos extremos se revisarán antes de interpretarlos. La confianza, las decisiones y los comentarios se analizarán conjuntamente, sin atribuir al juego mejoras académicas todavía no contrastadas. La comparación con resultados de otros cursos prevista en la memoria requiere datos adicionales.

Antes del pilotaje se comprobará que las matrices se leen bien, que las selecciones se conservan y que el CSV contiene las 19 respuestas previstas —6 iniciales y 13 finales, incluido el comentario vacío si se omite— y los registros de los cinco retos. También se verificará la descarga desde itch.io y la entrega en Moodle.

[Actividad y materiales de Operación Vaso Doble](operacion-vaso-doble/README.md) · [Diseño del escape room, fase 2](Fase2_Diseno_Escape_Room_Adquisicion.md)
