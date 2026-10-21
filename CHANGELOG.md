# Registro de Cambios (CHANGELOG)

Todas las modificaciones notables realizadas en este proyecto serán documentadas en este archivo.
El formato se basa en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/) y este proyecto se adhiere a versionado semántico.

---

## [1.3.0] - 2026-10-21

### Añadido
- **Sistema de Cócteles Favoritos**:
  - Marcado directo con botón de estrella ⭐ tanto desde las tarjetas del catálogo como desde la cabecera de la ficha detallada.
  - Persistencia bidireccional en el navegador mediante `localStorage` y cookies (`cocteles_favoritos`) sin necesidad de registro ni cuenta de usuario.
  - Filtro rápido prioritario `⭐ Favoritos (N)` en la barra de categorías con pantalla explicativa para estado vacío.
- **Nuevo Cóctel Tradicional**:
  - Incorporación del cóctel **#51 Calimocho (Kalimotxo)** en `cocktails_data.py` con historia en Algorta, fórmula 50/50 y vaso de sidra.
  - Fotografía de estudio dedicada `images/51_calimocho.jpg`.

### Cambiado
- **Renovación fotográfica de estudio**:
  - Sustitución de imágenes por tomas de estudio profesional con iluminación cálida y natural para: Margarita (`09_margarita.jpg`), Mint Julep (`45_mint_julep.jpg`), Café irlandés (`48_irish_coffee.jpg`), Negroni (`08_negroni.jpg`), Mojito (`02_mojito.jpg`), Agua de Valencia (`06_agua_de_valencia.jpg`), Rebujito (`07_rebujito.jpg`).
- **Corrección de interfaz y diseño responsive móvil**:
  - Eliminación del dato de tiempo de elaboración de las fichas y tarjetas.
  - Rediseño de la cuadrícula de especificaciones (*Copa, Método y Hielo*) en 3 columnas adaptativas con auto-ajuste de texto para evitar desbordamientos en pantallas móviles estrechas.
  - Corrección de la cabecera del modal: el número y la etiqueta de categoría ahora fluyen de manera natural e independiente por encima del título, impidiendo cualquier solapamiento u ocultación del nombre del cóctel.

## [1.2.0] - 2026-10-20

### Añadido
- **Aplicación Web Móvil Interactiva (SPA)** para GitHub Pages:
  - `index.html`: Web responsiva táctil ultraligera (101 KB) con buscador instantáneo, filtros por categoría y tipo de alcohol, fichas con checklist interactivo de ingredientes y visor de pasos.
  - `generate_web.py`: Script en Python para compilar `index.html` a partir de `cocktails_data.py`.
  - `README.md`: Documentación completa del proyecto con enlace a la web pública de GitHub Pages (`https://jegofer.github.io/guia-de-cocteles/`) y botón de descarga del PDF.
  - `.gitignore`: Configuración de exclusiones de archivos temporales para el repositorio.

## [1.1.0] - 2026-10-20

### Añadido
- **Archivos de memoria técnica y contexto persistente** bajo la especificación `gestion-contexto-memoria`:
  - `DME.md`: Documento Maestro de Especificaciones (20 secciones completas).
  - `ESTADO_PROYECTO.md`: Estado actual, módulos y métricas de avance.
  - `DECISIONES.md`: Registro de decisiones de arquitectura y diseño (DEC-001 a DEC-006).
  - `INCIDENCIAS.md`: Registro de incidencias resueltas, causas raíz y mitigaciones (INC-001 a INC-004).
  - `TODO.md`: Lista de tareas pendientes categorizadas por criticidad.
  - `ARCHIVOS.md`: Inventario de archivos verificados del proyecto.
  - `CONTEXTO_SESION.md`: Archivo de contexto ultraligero para arranque rápido de sesiones futuras sin consumo excesivo de tokens.
  - `CHANGELOG.md`: Historial cronológico de cambios.
- **Archivo de preservación de requisitos iniciales**:
  - `PROMPT_ORIGINAL.md`: Contiene el prompt inicial de la conversación y las instrucciones complementarias de diseño editorial.

### Cambiado
- **Auditoría visual y reemplazo de 15 fotografías de cócteles** en `/images/` por imágenes de alta resolución, fotogénicas y fidedignas procedentes de Wikimedia Commons (*Wiki Loves Cocktails*) y Pxhere:
  - `24_san_francisco.jpg`: Sustituido falso cóctel azul por el clásico San Francisco español en copa tulipa con escarchado rosa de azúcar, degradado cálido de naranja/granadina, rodajas de naranja/limón, cereza y menta.
  - `46_sol_y_sombra.jpg`: Sustituida fotografía errónea de globo aerostático (trampa de homonimia *ballon*) por copa balón de cristal tallado con brandy y anís sobre fondo oscuro de estudio.
  - `19_paloma.jpg`: Sustituido tarro de mermelada de baja resolución por vaso alto tallado con tequila, refresco de pomelo rosado, hielo translúcido y rodaja de pomelo y lima.
  - `03_sangria.jpg`: Sustituida postal/menú de papel por copa y jarra de cristal con sangría española tradicional de vino tinto y frutas frescas.
  - `09_margarita.jpg`: Sustituido icono vectorial por fotografía oficial de estudio de Margarita en copa coupette con escarchado de sal y lima.
  - `11_marianito.jpg`: Sustituido Dry Martini transparente por vermut rojo servido en vaso con hielo, rodaja de naranja y aceituna sobre barra de bar.
  - `25_bloody_mary.jpg`: Sustituida botella comercial por vaso alto con Bloody Mary, escarchado de sal de apio, limón y garnitura vegetal.
  - `37_french_75.jpg`: Sustituida copa metálica vacía por copa flauta de champán espumoso con ginebra y espiral de limón sobre barra de caoba.
  - `44_kir_royale.jpg`: Sustituida fachada de restaurante por copa flauta de champán con licor de cassis profundo.
  - `50_laguna_azul.jpg`: Sustituida botella RTD por copa huracán con curaçao azul eléctrico, hielo picado y garnituras frescas.
  - `04_tinto_de_verano.jpg`: Sustituida foto casera de teléfono por copa de tinto de verano ruby brillante servida en terraza de bar.
  - `21_manhattan.jpg`: Sustituido plano cerrado distorsionado por copa clásica de tallo con Manhattan carmesí y cereza marrasquino.
  - `29_bellini.jpg`: Sustituida copa oscura turbia por Bellini original en Harry's Bar (Venecia).
  - `06_agua_de_valencia.jpg`: Sustituido recorte blanco aislado por copa de Agua de Valencia servida junto a jarra y cítricos.
  - `07_rebujito.jpg`: Sustituida foto de dos vasos lejanos por rebujito andaluz en mesa de mármol con plato de aceitunas.
- **Recompilación del libro**:
  - `libro_cocteles.html`: Recompilado con las nuevas imágenes en Base64.
  - `50_cocteles_explicados_paso_a_paso.pdf`: Re-exportado mediante Google Chrome headless. Verificado estrictamente en 55 páginas A4 sin desbordamientos de texto.

---

## [1.0.0] - 2026-10-19

### Añadido
- Creación de la base de datos de cócteles (`cocktails_data.py`) con 50 recetas exhaustivas categorizadas (Ibéricos/Españoles, Internacionales contemporáneos, Clásicos legendarios, Sin alcohol/Mocktails, Festivos y sofisticados).
- Generador HTML editorial para impresión (`generate_book.py`) con maquetación estricta A4 (1 cóctel = 1 página), paleta oscura editorial, fichas técnicas, historia, notas de cata y maridaje.
- Descarga inicial automatizada de imágenes desde Wikimedia Commons y Pxhere (`download_images.py`).
- Exportación del libro a PDF de alta resolución (`50_cocteles_explicados_paso_a_paso.pdf`, 55 páginas) con portada, índice de dos páginas, prólogo, 50 fichas y contraportada.
