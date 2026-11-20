# Ren’Py y verificación

Ejecuta python3 scripts/crear_proyecto.py DESTINO --nombre "Título" --id identificador-unico. El destino debe ser inexistente o vacío. Adapta el ejemplo de reto y las preguntas de confianza al contenido validado con el docente.

La plantilla proporciona script.rpy, encuestas.rpy, registro.rpy, registro_partida.py y screens.rpy. El script muestra cómo empezar sesión, encuestas, retos, respuestas y exportación. Cada recurso referenciado debe estar en el proyecto y los módulos Python deben viajar también en la versión web.

Ejecuta lint con un SDK compatible. Recorre elecciones erróneas, reintentos, respuestas correctas y enlaces entre retos. Inspecciona capturas con textos largos y modelos. Comprueba comentarios con acentos y separadores, respuestas vacías, cronología, fin único por reto y fin de partida posterior a la encuesta. En las matrices prueba con clics valores de varias filas y verifica el CSV: conservar el valor 3 por defecto y guardar cambios como 1, 2, 4 y 5 son comportamientos distintos que hay que comprobar. Abre el CSV real generado.

Usa temporales para pruebas y excluye sus datos de la distribución. Copia de vuelta solo los cambios autorizados, preservando ediciones del usuario.

En diálogos, «80 % suena» puede interpretarse como formato porcentual e insertar una representación interna. Usa «80 por ciento» o un escape comprobado. Para mostrar guardas con corchetes literalmente, usa substitute False. Las pantallas se evalúan repetidamente: las escrituras deben ocurrir en acciones del usuario o instrucciones del guion.

Una instalación puede tener nombre antiguo y componentes actualizados parcialmente. Confirma versión y compatibilidad del soporte web; utiliza una copia temporal completa compatible si es necesario.
