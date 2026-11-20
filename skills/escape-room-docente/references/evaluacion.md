# Encuestas y CSV

Presenta la confianza en una matriz única con todas las tareas visibles y un botón Siguiente, tanto antes como después. Presenta en otra matriz las cinco valoraciones finales de experiencia. Preselecciona 3 en cada fila, permite cambiar cada respuesta y guarda el conjunto al confirmar. Las columnas deben mantener anchura fija y alinearse; verifica que todos los textos y botones caben. Si aumenta el número de conceptos, adapta el diseño al espacio disponible.

Repite tareas concretas de confianza con idénticas palabras y escala antes y después. La plantilla usa de 1 Ninguna a 5 Mucha. Adapta tareas e identificadores a los conceptos del nuevo juego.

Después se pregunta por comprensión, explicaciones, historia, motivación y adecuación del juego, con escala de acuerdo 1–5. El ítem sobre explicaciones conserva su escala incluso si todo se acertó; el registro permite cruzarlo con errores. La dificultad usa Muy baja, Baja, Adecuada, Alta, Muy alta. La última pantalla reúne dificultad y un comentario opcional sobre mejoras, hasta 500 caracteres. La pregunta abierta sobre dudas se retiró del diseño acordado.

El CSV usa UTF-8 con BOM y punto y coma. Guarda atómicamente tras cada evento. Contiene identificador aleatorio, fechas ISO con zona horaria, tiempos monotónicos, reto, decisión, opción, corrección, intento, errores acumulados y acierto inicial. Las decisiones ODS pueden tener corrección vacía. Las encuestas usan evento encuesta, decisión pre.clave o post.clave y opción numérica 1–5 o texto. Conserva vacíos opcionales.

Registra inicio_juego y fin_juego y principio/fin de cada encuesta. Cierra el último reto antes de la encuesta final. El total incluye encuestas; la diferencia entre los eventos de juego permite excluirlas. El primer reto puede incluir el prólogo y el último la decisión ODS.

El estado del registro queda fuera del rollback y la plantilla lo desactiva. Si añades carga de partidas, implementa recuperación de sesión y relojes antes de habilitarla. Una salida normal marca interrumpida y un cierre forzado puede conservar solo el último evento guardado. Cada juego necesita prefijo y directorio propios. Conserva un mapa de códigos y versiona cambios de esquema.

Para analizar, prioriza acierto inicial por concepto, distractores, intentos, tiempo y cambio de confianza emparejado. La confianza es autopercepción y el acierto final depende de reintentos. Los tiempos incluyen lectura y pausas. Las pruebas al azar no calibran dificultad ni duración de clase. Evita atribuir impacto causal a muestras pequeñas.

Los valores 3 preseleccionados también se exportan aunque no se modifiquen. No permiten distinguir una selección deliberada de una respuesta dejada por defecto. Tenlo en cuenta al interpretar la confianza y la valoración.
