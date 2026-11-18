# Scape Rooms Docencia

Proyecto de innovación docente de la Universidad de Cantabria sobre el uso de escape rooms digitales narrativos para el aprendizaje activo y la evaluación formativa. El alumnado resuelve retos de la asignatura y toma decisiones que cambian su recorrido y el desenlace de la historia. Los retos permiten practicar el pensamiento crítico, la resolución de problemas y la toma de decisiones, e incorporan los Objetivos de Desarrollo Sostenible (ODS).

El proyecto aplica el mismo modelo en tres momentos del aprendizaje:

- **Diagnóstico** de conocimientos previos en Desarrollo de Sistemas de Información.
- **Adquisición** de contenidos en Ingeniería del Software I.
- **Consolidación** mediante repaso antes del examen en Prehistoria II.

## Documentación disponible

- [Memoria de la propuesta](Memoria_propuesta_publica.md)
- [Fase 1. Enfoque metodológico general](Fase1_Resumen_Marco_Metodologico.md)
- [Fase 2. Diseño del escape room de adquisición](Fase2_Diseno_Escape_Room_Adquisicion.md)

## Operación Vaso Doble

Eres becario de la facultad y la máquina de devolución de vasos de la cafetería empieza a abonar dos euros por cada euro de depósito. A lo largo de la jornada aparecen cinco averías que tendrás que investigar y reparar mediante diagramas de estados UML.

El juego trabaja acciones en transiciones, guardas y valores límite, eventos temporales con `after(...)` y `at(...)`, y eventos de cambio con `when(...)`. El último reto incorpora una decisión sobre el aviso preventivo de capacidad, vinculada al **ODS 12, Producción y consumo responsables**.

- [Proyecto Ren’Py](operacion-vaso-doble/renpy), con el código y las ilustraciones.
- [Paquete web para itch.io](operacion-vaso-doble/operacion-vaso-doble-web.zip), para jugar desde el navegador una vez alojado.

La actividad incluye encuestas antes y después del juego. Al finalizar permite obtener un CSV con sus respuestas, los tiempos de partida y de cada reto, las opciones elegidas y los reintentos. El alumnado puede entregar ese archivo en una tarea de Moodle.

Para ejecutar el proyecto localmente, selecciona la carpeta que contiene `renpy` como directorio de proyectos en el lanzador de Ren’Py y ejecuta el juego. Para alojarlo en itch.io, sube el paquete web como proyecto HTML y marca que se juega en el navegador.

## Materiales para reutilizar

Los materiales están orientados a que otros equipos docentes adapten el modelo a sus asignaturas y titulaciones. Además del juego de ejemplo y los documentos metodológicos, se incluye la [skill escape-room-docente](skills/escape-room-docente/SKILL.md) para trabajar con Codex.

La skill recoge el proceso de selección de contenidos y ODS, diseño narrativo y revisión por escenas, implementación de retos, evaluación y publicación web. Incluye una [plantilla Ren’Py](skills/escape-room-docente/assets/renpy) con un reto de ejemplo, encuestas y registro CSV, y un [generador de proyectos](skills/escape-room-docente/scripts/crear_proyecto.py).

Las ilustraciones de Operación Vaso Doble se han generado con inteligencia artificial y se han seleccionado y adaptado para la actividad.
