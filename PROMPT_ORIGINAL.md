# Prompt original del proyecto

A continuación se registra de forma íntegra el prompt original con el que se inició la conversación de este proyecto el 19 de octubre de 2026, así como las directrices inmediatas de refinamiento acordadas con el usuario.

---

## 1. Prompt inicial (Fase de arranque)

```text
Actúa como un experto coctelero internacional y diseñador editorial profesional especializado en publicaciones gastronómicas.

Tu tarea es maquetar y generar un libro de recetas de cócteles en formato PDF, dirigido a personas que se inician en la coctelería, combinando rigor técnico con una estética visual atractiva, limpia y moderna.

### 1. Parámetros de selección de cócteles
- Incluye exactamente 20 cócteles famosos, muy consumidos y reconocibles en España (tanto clásicos internacionales populares como elaboraciones y combinados de gran tradición local).
- Las recetas deben ser accesibles para principiantes: pocos ingredientes, técnicas directas (construido en vaso, agitado simple o refrescado) y sin preparaciones caseras complejas (siropes complejos o clarificaciones).

### 2. Estructura y maquetación de cada página
Cada cóctel ocupará exactamente una página individual (diseño a página completa) con la siguiente distribución y elementos:
- Título del cóctel: tipografía clara y destacada (con mayúscula inicial solo en la primera palabra o nombres propios, evitando la capitalización en cascada en español).
- Fotografía destacada: imagen cenital o en ángulo de 45°, formato grande y alta resolución.
  - Estilo visual homogéneo: iluminación natural y cálida de estudio fotográfico sobre barra de madera oscura o mármol mate, fondo ligeramente desenfocado (bokeh sutil), cristalería impecable con condensación suave y guarnición fresca y nítida.
- Ficha técnica:
  - Tiempo de preparación (minutos).
  - Perfil de sabor (por ejemplo: cítrico y refrescante, dulce y frutal, amargo y herbal).
  - Tipo de vaso / cristalería adecuada (vaso de tubo, copa balón, vaso bajo tipo old fashioned, copa cóctel, jarra de barro, etc.).
- Ingredientes: lista con medidas exactas en mililitros (ml) o partes.
- Preparación: método paso a paso numerado, conciso y redactado con lenguaje accesible.
- Consejo del bartender: un breve truco técnico para mejorar el resultado casero.

### 3. Flujo de trabajo obligatorio en dos fases
- Fase 1 (Confirmación previa): Antes de generar el documento maquetado en PDF, presenta una tabla resumen con los 20 cócteles seleccionados que incluya: número, nombre del cóctel, base alcohólica principal, método de elaboración y tipo de vaso. Solicita confirmación.
- Fase 2 (Generación editorial): Tras recibir la confirmación de la lista, genera el libro de cócteles completo en PDF aplicando un estilo editorial contemporáneo, márgenes limpios, jerarquía visual equilibrada y coherencia cromática y tipográfica en todas las páginas.
```

---

## 2. Peticiones de ampliación y ajuste durante la conversación

Durante el desarrollo de la sesión inicial, el usuario aportó las siguientes instrucciones clave de refinamiento:

1. **Ampliación de repertorio y sustituciones:**
   - Retirar el *Calimocho* de la selección.
   - Añadir 20 recetas adicionales y posteriormente otros 10 cócteles más hasta alcanzar exactamente **50 cócteles**.
2. **Distintivos técnicos:**
   - Incorporar un distintivo explícito y destacado para combinados sin alcohol (ej. `0,0% SIN ALCOHOL` en el cóctel *San Francisco*).
3. **Título editorial definitivo:**
   - Titular la obra: ***«50 cócteles explicados paso a paso: Guía visual y práctica para principiantes»***.
4. **Revisión fotográfica y de contexto (sesión 2026-10-20):**
   - Sustituir imágenes no acordes o erróneas (como *San Francisco*, *Sol y sombra* o *Paloma*), seleccionando fotografías de alta resolución en Wikimedia Commons o Pxhere.
   - Incorporar los archivos de contexto y memoria persistente del proyecto.
   - Preservar este prompt en `PROMPT_ORIGINAL.md`.
