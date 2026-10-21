# CONTEXTO DE SESIÓN

## PROYECTO
50 cócteles explicados paso a paso: Guía visual y práctica para principiantes

## OBJETIVO
Libro editorial gastronómico de 55 páginas en formato PDF y HTML con 50 recetas clásicas y españolas, maquetación profesional a página individual y fotografías de alta calidad.

## SITUACIÓN ACTUAL
Proyecto ampliado a 51 cócteles con la incorporación del Calimocho, sistema de favoritos interactivo en la web móvil con persistencia dual (localStorage y cookie), rediseño visual responsive de especificaciones sin desbordes y actualización fotográfica de estudio para 8 cócteles.

## ÚLTIMO TRABAJO REALIZADO
Actualización de la SPA móvil (`index.html` y `generate_web.py`):
1. Sistema de favoritos con botón de estrella ⭐ en tarjetas y modal, persistencia sin registro mediante cookie y localStorage, y filtro prioritario ⭐ Favoritos.
2. Eliminación del tiempo de elaboración.
3. Corrección de la fila de especificaciones (Copa, Método y Hielo) para evitar desbordes móviles.
4. Corrección de cabecera en la ficha detallada (el número y la categoría ya no solapan ni tapan el nombre del cóctel).
5. Incorporación de la receta y fotografía de Calimocho (#51).
6. Renovación fotográfica con estética de estudio e iluminación cálida natural para Margarita, Mint Julep, Café irlandés, Negroni, Mojito, Agua de Valencia, Rebujito y Calimocho.

## PRÓXIMA ACCIÓN
Revisión por parte del usuario de las novedades en la aplicación web móvil y despliegue a GitHub Pages.

## DECISIONES IMPORTANTES
- Formato fijo de 1 cóctel = 1 página exacta A4, sin desbordamientos de texto.
- Codificación de imágenes en Base64 dentro de `libro_cocteles.html` para garantizar autocontención e independencia de rutas relativas.
- Distintivo verde `0,0% SIN ALCOHOL` destacado en cócteles vírgenes.
- Todas las medidas expresadas en mililitros exactos (ml).

## RESTRICCIONES IMPORTANTES
- No alterar la altura ni la retícula de las páginas A4 para evitar que se desborden a páginas adicionales.
- Mantener la correspondencia estricta entre la cristalería indicada en la ficha técnica y la imagen visible.
- No modificar el repertorio de 50 cócteles sin instrucción expresa del usuario.

## PROBLEMAS ABIERTOS
- Ninguno. Todas las incidencias detectadas (INC-001 a INC-004) han quedado resueltas.

## ARCHIVOS CLAVE
- `/home/jesus/Documentos/GIT/Libro de cocteles/50_cocteles_explicados_paso_a_paso.pdf`: PDF final de 55 páginas.
- `/home/jesus/Documentos/GIT/Libro de cocteles/libro_cocteles.html`: Maquetación editorial completa en HTML.
- `/home/jesus/Documentos/GIT/Libro de cocteles/cocktails_data.py`: Base de datos de las 50 recetas.
- `/home/jesus/Documentos/GIT/Libro de cocteles/generate_book.py`: Script de generación editorial.
- `/home/jesus/Documentos/GIT/Libro de cocteles/images/`: Banco de 50 fotografías de alta resolución.
- `/home/jesus/Documentos/GIT/Libro de cocteles/PROMPT_ORIGINAL.md`: Prompt inicial y directrices del proyecto.

## DOCUMENTOS DE REFERENCIA
- DME.md
- ESTADO_PROYECTO.md
- DECISIONES.md
- INCIDENCIAS.md
- TODO.md
- ARCHIVOS.md
