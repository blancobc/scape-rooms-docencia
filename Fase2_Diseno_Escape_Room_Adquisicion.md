# Fase 2. Diseño del escape room de adquisición

**Descripción.** Diseño de una actividad sobre máquinas de estados UML para Ingeniería del Software I, dentro del bloque de diseño, posterior a requisitos y arquitectura.

**Participantes.** Carlos, como responsable principal, con el apoyo del resto del equipo.  
**Temporización prevista en la memoria.** Octubre de 2026.  
**Estado.** Prototipo funcional en Ren’Py con cinco retos, encuestas integradas y exportación de registros. Paquete web preparado para itch.io. Pendiente de pilotaje en el aula.

[Proyecto e instrucciones de Operación Vaso Doble](operacion-vaso-doble/README.md)

## 1. Diseño del escape room de adquisición

### Historia y objetivos de aprendizaje

En **Operación Vaso Doble**, el jugador es becario de la facultad y ayuda a reparar una máquina de devolución de vasos reutilizables instalada esa semana. Al pedir una bebida se paga un euro de depósito, que se recupera al devolver el vaso para su lavado y reutilización.

La historia empieza treinta minutos antes de abrir la facultad. Circula un vídeo titulado «Cómo financiar el café de todo el cuatrimestre» porque la máquina abona dos euros por cada vaso. Tras reparar ese fallo, aparecen nuevas incidencias durante el desayuno, antes del descanso, a la hora de comer y durante la sobremesa. La encargada y los estudiantes introducen los problemas mediante escenas breves de humor cotidiano.

El alumnado deberá interpretar transiciones con la forma `evento [guarda] / acción`, distinguir operaciones disparadoras de acciones, corregir guardas en casos límite y elegir eventos temporales y de cambio adecuados. Se aplican las convenciones de los ejercicios de clase, que requieren un disparador explícito en las transiciones ordinarias.

### Los cinco retos

| Reto | Fallo presentado | Reparación y comprobación |
| --- | --- | --- |
| **1. Un vaso, dos euros** | Un único vaso produce dos abonos. | Dejar el abono en `confirmarRecogida()`. Las otras opciones lo sitúan al abrir la compuerta o al validar el vaso. La explicación contrasta devolverlo con retirarlo antes de que caiga al depósito. |
| **2. Un vaso al que le falta un milímetro** | Se rechaza el vaso de café solo, de 8 cm, aunque cumple el mínimo. | Corregir las guardas solapadas `>= 8` y `<= 8`. Se prueban juntas las alturas 7,9, 8,0 y 8,1 cm. La solución acepta con `>= 8` y rechaza con `< 8`. |
| **3. Cinco segundos de paciencia** | La compuerta se cierra inmediatamente y agradece la paciencia del usuario. | Sustituir `after(0 s)` por `after(5 s)` desde «Esperando vaso». Se compara con contar desde «Disponible». Las pruebas incluyen un vaso introducido a los tres segundos y una espera sin vaso, tras seis segundos previos de reposo. |
| **4. Mantenimiento en plena hora punta** | A las 13:55, la encargada programa la revisión para mañana a las 08:00 y el diagnóstico arranca inmediatamente, formando una cola. | Mantener el servicio tras guardar e iniciar con `at(fechaHoraProgramada)`. Se contrasta con `after(8 h)` para programaciones guardadas a las 13:55 y a las 16:00. |
| **5. Todavía cabe uno más** | El depósito está lleno y la máquina sigue ofreciendo devoluciones. | Usar `when(depositoLleno)` para bloquearlas. Las alternativas esperan una operación con guarda, un plazo de cinco segundos o el cambio de la condición inversa. Después se configura el aviso preventivo. |

Los eventos temporales se trabajan en dos retos distintos, uno para el plazo relativo con `after(...)` y otro para la fecha y hora con `at(...)`. El evento de cambio `when(...)` ocupa el quinto reto y se diferencia de la comprobación de una guarda.

En la prueba del sensor, el depósito permanece lleno mientras el panel simula la señal pasando de falso a verdadero. Solo se muestra vacío después de que la encargada lo sustituya.

## 2. Adaptación del marco metodológico al contexto concreto

### Dinámica y retroalimentación

La actividad se plantea como una partida individual de unos 30 minutos, duración pendiente de comprobar con alumnado, incluyendo las encuestas inicial y final. Cada reto presenta el fallo, permite reproducirlo y muestra un fragmento del diagrama con un botón para proponer la reparación. El diagrama permanece visible junto a las opciones.

La elección produce una explicación inmediata con **«Solución correcta» en verde** o **«Solución incorrecta» en rojo**. Los casos del banco de pruebas aparecen juntos. Una reparación incorrecta permite volver a elegir y la correcta conduce a la comprobación narrativa y al siguiente incidente. Las ilustraciones de personajes, máquina y pantalla cambian según la acción.

Detectar errores practica el **pensamiento crítico**. Aplicar las reglas a los casos de prueba practica la **resolución de problemas**. La configuración final permite ejercitar la **toma de decisiones**.

### Integración del ODS 12

El **ODS 12, Producción y consumo responsables**, se hace explícito al configurar el aviso preventivo para mantener el circuito de reutilización. El caso establece una capacidad de 100 vasos, llegadas de unos dos vasos por minuto y cinco minutos de respuesta del personal.

Se puede avisar al 50 %, al 80 %, al 95 % o al llenarse. Cada alternativa muestra el margen disponible, el riesgo de interrupción y sus implicaciones para el trabajo del personal. El 80 % ofrece diez minutos de capacidad al ritmo previsto. El jugador puede cambiar o mantener su configuración y recibe un cierre acorde con ella. Estos tiempos son estimaciones del escenario con afluencia constante.


## 3. Evaluación y materiales disponibles

Antes del prólogo se presenta una matriz de confianza sobre seis tareas relacionadas con los contenidos. Tras los cinco retos se repite esa matriz y se recoge la valoración de la experiencia. Una última pantalla reúne la dificultad percibida y un comentario opcional de mejora. Las opciones están inicialmente en 3 y pueden modificarse antes de continuar.

Cada partida registra las fechas de inicio y fin, los tiempos, las opciones seleccionadas en las decisiones registradas, los errores y los reintentos, junto con las respuestas a las encuestas. Al finalizar, el alumnado puede obtener un único CSV y entregarlo en Moodle. El diseño de los instrumentos y los criterios de análisis se recogen en la [fase 4](Fase4_Diseno_Instrumentos_Evaluacion.md).

Se dispone del proyecto Ren’Py con código e ilustraciones y de un paquete web para jugar sin instalación desde itch.io. El pilotaje deberá comprobar la duración, la claridad de las instrucciones y la descarga y entrega del CSV en los equipos del aula.
