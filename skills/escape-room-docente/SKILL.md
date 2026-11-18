---
name: escape-room-docente
description: Diseñar y desarrollar juegos docentes narrativos en Ren’Py a partir de materiales de clase, con retos conceptuales, integración de ODS, encuestas previa y posterior y exportación CSV. Usar para crear o continuar estas actividades y preparar su publicación web.
---

# Escape room docente

Acompaña al docente desde los contenidos hasta un juego evaluable. Operación Vaso Doble es el caso de referencia de este repositorio.

## Colaboración y diseño

Lee los materiales de clase antes de definir objetivos observables, convenciones docentes y errores que se trabajarán. Distingue las decisiones del docente de tus propuestas. Selecciona la narrativa y el ODS según el contexto.

Avanza por escenas con el feedback del docente. Si pide una propuesta, desarrolla la siguiente escena para revisarla. Cuando autorice implementar, termina esa parte y compruébala. Conserva los acuerdos entre turnos. Los documentos de fase serán breves, orientativamente una o dos páginas, organizados por los resultados esperados del proyecto.

Lee [Diseño y estilo](references/diseno.md) al redactar narrativa y retos. La secuencia habitual es fallo visible, reproducción, diagnóstico con modelo, elección con el modelo a la vista, retroalimentación y comprobación narrativa. La duración y el número de retos se adaptan al contexto.

## Implementación

Lee [Ren’Py y verificación](references/renpy.md). Crea un proyecto desde assets/renpy mediante scripts/crear_proyecto.py, que exige destino vacío. La plantilla ejecutable incluye un reto ilustrativo, encuestas y CSV. Adapta el contenido y genera recursos propios.

Las imágenes de los modelos deben poder reemplazarse independientemente. Usa diagramación determinista para modelos técnicos e imágenes generadas o aportadas para personajes y fondos. Conserva continuidad visual de personas, objetos y estados de la máquina.

## Evaluación

Lee [Evaluación y CSV](references/evaluacion.md) antes de cambiar preguntas o instrumentación y al analizar resultados. Repite las mismas preguntas de confianza y escalas en pre y post. Conserva identificador de partida, respuestas cronológicas y tiempos diferenciables de juego y encuestas.

## Publicación

Lee [Publicación web](references/publicacion.md) al generar el paquete. Distingue compilación de validación en navegador. Publica en servicios externos cuando el usuario lo solicite.

En una copia completa del repositorio, consulta operacion-vaso-doble/renpy y los documentos Fase1_Resumen_Marco_Metodologico.md y Fase2_Diseno_Escape_Room_Adquisicion.md como ejemplos del caso. La plantilla funciona también sin ellos.
