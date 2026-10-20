# Registro de incidencias técnicas del proyecto

## INC-001 — Descarga de imagen errónea para el cóctel "Sol y sombra"

- **Problema:** La imagen asignada al cóctel nº 46 (*Sol y sombra*) mostraba un globo aerostático volando frente al sol al atardecer en lugar de una copa con licor.
- **Contexto:** Script automatizado de búsqueda y descarga `download_images.py`.
- **Causa conocida:** La búsqueda con los términos *"Sol y sombra"* y *"Brandy glass"* / *"Copa de balón"* coincidió en Wikimedia Commons con la acepción francesa/española de globos aerostáticos (*ballon / copa de balón / sol y sombra como efecto de luz en el cielo*).
- **Causa probable:** N/A (Causa confirmada de forma fehaciente).
- **Solución aplicada:** Búsqueda precisa de cristalería de destilados y descarga de la fotografía de estudio en copa snifter de cristal con destilado caoba y reflejo dorado (`test_images/brandy_evan_crop.jpg`).
- **Resultado:** Fotografía impecable, acorde con la cristalería y receta tradicional del combinado.
- **Estado:** RESUELTA
- **Acciones pendientes:** Ninguna.

---

## INC-002 — Discrepancia cromática y de receta en el cóctel "San Francisco"

- **Problema:** La fotografía original del cóctel nº 24 (*San Francisco*) mostraba un cóctel azul en degradado con curaçao y pajita de caña de azúcar, mientras que el San Francisco es un cóctel de zumos de frutas amarillo/anaranjado con granadina roja.
- **Contexto:** Búsqueda genérica de *"Tropical mocktail cocktail"*.
- **Causa conocida:** La consulta genérica de mocktail seleccionó un cóctel sin alcohol tropical azul que no respetaba la fórmula histórica del San Francisco español.
- **Causa probable:** N/A (Causa confirmada).
- **Solución aplicada:** Descarga de fotografía auténtica de cóctel San Francisco (`File:Gran Canaria Yumbo Centre San Francisco Cocktail.jpg`) que presenta escarchado de azúcar rosa con granadina, degradado de zumos de naranja y melocotón, rodajas de naranja/limón, menta y guinda.
- **Resultado:** Coherencia absoluta entre la imagen, el badge sin alcohol y la receta explicada.
- **Estado:** RESUELTA
- **Acciones pendientes:** Ninguna.

---

## INC-003 — Presentación inadecuada del cóctel "Paloma"

- **Problema:** La imagen original del cóctel nº 19 (*Paloma*) mostraba un tarro rústico de conservas con cubos de hielo y hojas de albahaca, en lugar de un vaso alto con borde salino y pomelo rosado.
- **Contexto:** Selección automática de `download_images.py`.
- **Causa conocida:** Consulta laxa que enlazó a un servicio experimental de bar con tarro de mermelada y albahaca.
- **Causa probable:** N/A (Causa confirmada).
- **Solución aplicada:** Sustitución por fotografía de alta resolución de estudio (`Paloma Cocktail2.jpg`), mostrando un vaso alto de cristal tallado con refresco de pomelo rosado, gajo de lima, piel de pomelo/naranja y hielo cristalino.
- **Resultado:** Imagen fotogénica, elegante y perfectamente ajustada a la cristalería y proporciones de la receta.
- **Estado:** RESUELTA
- **Acciones pendientes:** Ninguna.

---

## INC-004 — Archivos no fotográficos o con elementos ajenos a la copa

- **Problema:** Varios cócteles incorporaban imágenes inadecuadas: un menú de restaurante en papel para la *Sangría*, una copa vacía para la *Margarita*, un Dry Martini blanco para el *Marianito* (que es vermut rojo), una botella de mixer para el *Bloody Mary*, una copa vacía para el *French 75*, la fachada de un restaurante para el *Kir Royale* y un refresco comercial embotellado para la *Laguna Azul*.
- **Contexto:** Recolección inicial rápida de imágenes sin filtrado manual minucioso.
- **Causa conocida:** El scraper inicial priorizó el primer resultado coincidente sin validar el contenido del encuadre ni verificar si se trataba de una botella, un cartel o un vaso vacío.
- **Causa probable:** N/A (Causa confirmada).
- **Solución aplicada:** Auditoría completa mediante generación de una hoja de contactos (`contact_sheet.jpg`) e inspección visual multimodal; reemplazo de las 15 imágenes defectuosas por tomas profesionales en barra o estudio de *Wiki Loves Cocktails*.
- **Resultado:** 100% de las 50 imágenes del libro muestran cócteles reales, bien iluminados, fotogénicos y fieles a sus respectivas recetas.
- **Estado:** RESUELTA
- **Acciones pendientes:** Ninguna.
