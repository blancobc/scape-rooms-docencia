# Publicación web

Construye desde Web en el lanzador Ren’Py o con web_build del launcher. Comprueba la sintaxis en la versión instalada y consulta documentación oficial cuando cambie.

El ZIP debe tener index.html en raíz, recursos completos y módulo de registro. Excluye CSV y partidas de prueba. Verifica integridad, límites del alojamiento y descarga del CSV en navegador. Una compilación satisfactoria no prueba el flujo dentro del iframe.

El caso de referencia precarga imágenes mediante progressive_download.txt. Es configurable según tamaño y conexión. Conserva el código de descarga por Blob en web y apertura de carpeta en escritorio.

En itch.io el ZIP es HTML y se marca para jugar en navegador. El diseño preferido es Click to launch in fullscreen y Edit theme, Layout, Screenshots, Sidebar. Confirma los nombres con la interfaz vigente. La portada usada mide 630 × 500. Usa capturas reales y declara las imágenes generadas con IA en el campo correspondiente.

Flujo de aula: enlace desde Moodle, juego, encuesta final, descarga CSV y entrega manual en una tarea que acepte .csv. La subida automática requiere integración adicional.

Fuentes oficiales:
- https://www.renpy.org/doc/html/web.html
- https://itch.io/docs/creators/html5
- https://itch.io/docs/creators/design
