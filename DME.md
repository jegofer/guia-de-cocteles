# Documento maestro de especificaciones (DME)

## 1. Identificación del proyecto
- **Título de la obra:** 50 cócteles explicados paso a paso: Guía visual y práctica para principiantes
- **Tipo de proyecto:** Publicación editorial gastronómica digital maquetada en PDF de alta fidelidad y HTML autocontenido.
- **Directorio de trabajo:** `/home/jesus/Documentos/GIT/Libro de cocteles`
- **Fecha de creación inicial:** 2026-10-19
- **Fecha de última actualización:** 2026-10-20
- **Versión actual:** v1.1.0

## 2. Objetivo principal
Diseñar, maquetar y compilar un libro editorial completo de coctelería en formato PDF y HTML, accesible para principiantes pero con rigor técnico profesional, compuesto por 50 recetas destacadas y consumidas en España, estructurado a razón de una página exacta por cóctel con fotografía en alta resolución, ficha técnica, ingredientes en ml, pasos numerados y consejo del bartender.

## 3. Alcance
- **Contenido global (55 páginas A4):**
  - Página 1: Portada editorial (Dark luxury, tonos pizarra, ámbar y cobre).
  - Página 2: Prólogo y fundamentos (equilibrio dulce/ácido/amargo, importancia del hielo, dilución y técnicas).
  - Página 3: Guía visual de cristalería y herramientas caseras de barra.
  - Página 4: Tabla de contenidos estructurada por 5 familias sensoriales (Cítricos y refrescantes, Aromáticos y secos, Dulces y cremosos, Tradición española e ibérica, Tropicales y exóticos).
  - Páginas 5 a 54: Las 50 fichas de cócteles individuales a página completa.
  - Página 55: Índice alfabético A-Z y tabla de conversión de medidas de barra (ml, oz, golpes, cucharillas, jiggers).
- **Formatos generados:** PDF vectorial compilado mediante Chromium headless (`50_cocteles_explicados_paso_a_paso.pdf`) y documento HTML compilable con fuentes web e imágenes incrustadas en Base64 (`libro_cocteles.html`).

## 4. Fuentes de información
- Recetario estándar oficial de la International Bartenders Association (IBA).
- Manuales y recetarios clásicos de la coctelería tradicional española (Museo Chicote, coctelería madrileña, valenciana y andaluza).
- Banco de imágenes de alta resolución bajo licencias abiertas (Wikimedia Commons / Wiki Loves Cocktails / Pxhere CC0).

## 5. Datos de partida
- Archivo estructurado de datos `cocktails_data.py` con las 50 recetas completas (nombre, clave, base alcohólica, método, cristalería, tiempo, perfil, hielo, ingredientes, preparación paso a paso, consejo de bartender e indicador de `sin_alcohol`).
- Banco local de 50 imágenes procesadas en `images/{num:02d}_{key}.jpg`.

## 6. Sistema de referencia / formatos / estándares
- **Estándar dimensional:** A4 portrait (210 mm × 297 mm) con márgenes nulos a nivel de página y padding interno de 16-20 mm en retícula.
- **Tipografías:**
  - Títulos principales y cabeceras: `Playfair Display` (serif editorial clásico) y `Cinzel` (versalitas elegantes para cubiertas).
  - Textos de lectura, ingredientes y fichas: `Plus Jakarta Sans` (sans-serif moderno de gran legibilidad).
  - Datos numéricos y métricas: `JetBrains Mono`.
- **Paleta cromática:** Pizarra oscuro (`#0f172a`, `#1e293b`), blanco puro (`#ffffff`), gris suave (`#f8fafc`, `#f1f5f9`), acentos ámbar/cobre (`#d97706`, `#b45309`), verde esmeralda para sin alcohol (`#059669`, `#10b981`).
- **Unidades de medida:** Sistema Métrico Decimal (mililitros `ml`) como unidad primaria, con tabla de conversión a onzas líquidas (`fl oz`), golpes y cucharillas.

## 7. Requisitos técnicos
- Estricto cumplimiento del principio de **1 cóctel = 1 página**, sin saltos de línea desbordantes ni páginas fantasma.
- Imágenes en proporción horizontal panorámica (3:1 a 2.5:1, `height: 250px-280px`, `object-fit: cover`) con esquinas redondeadas (`border-radius: 12px`).
- Fichas técnicas en píldoras CSS estructuradas mediante grid responsivo.
- Indicador explícito `0,0% SIN ALCOHOL` destacado en verde para elaboraciones vírgenes.

## 8. Criterios y decisiones adoptadas
- Ver catálogo completo de decisiones en `DECISIONES.md` (DEC-001 a DEC-006).
- Sustitución de imágenes desalineadas o poco fotogénicas por tomas reales en cristalería adecuada.
- Autocontención total del documento HTML mediante codificación Base64 de las 50 imágenes para garantizar portabilidad sin dependencias relativas externas.

## 9. Metodología de trabajo
1. Definición de la estructura de datos en Python (`cocktails_data.py`).
2. Adquisición y validación visual de fotografías (`images/`).
3. Generación programática del HTML editorial (`generate_book.py`).
4. Renderizado y compilación a PDF mediante motor Chromium headless (`--headless=new --print-to-pdf`).
5. Control de calidad visual mediante extracción y verificación de páginas con `pdftoppm`.

## 10. Productos y resultados esperados
- `50_cocteles_explicados_paso_a_paso.pdf`: PDF final de 55 páginas listo para visualización o imprenta.
- `libro_cocteles.html`: Archivo HTML autónomo de maquetación editorial.
- `cocktails_data.py`: Diccionario estructurado de las 50 recetas.
- `generate_book.py`: Script generador y plantilla Jinja/HTML en Python.
- Memoria técnica y contexto en archivos Markdown (`DME.md`, `ESTADO_PROYECTO.md`, etc.).

## 11. Estructura de archivos
```text
/home/jesus/Documentos/GIT/Libro de cocteles/
├── 50_cocteles_explicados_paso_a_paso.pdf
├── libro_cocteles.html
├── cocktails_data.py
├── generate_book.py
├── download_images.py
├── PROMPT_ORIGINAL.md
├── DME.md
├── ESTADO_PROYECTO.md
├── DECISIONES.md
├── INCIDENCIAS.md
├── TODO.md
├── ARCHIVOS.md
├── CONTEXTO_SESION.md
├── CHANGELOG.md
└── images/
    ├── 01_gin_tonic.jpg ... 50_laguna_azul.jpg
```

## 12. Estado actual del proyecto
- **Fase:** Fase de pulido editorial, auditoría visual y documentación persistente completada con éxito.
- **Compilación PDF:** Verificada (55 páginas exactas, peso ~37.9 MB).
- **Imágenes corregidas:** 15 fotografías actualizadas a tomas profesionales reales.

## 13. Tareas completadas
- [x] Selección, confirmación y redacción de las 50 recetas de coctelería.
- [x] Maquetación editorial CSS de portada, prólogo, guía de cristalería, tabla de contenidos, fichas e índice A-Z.
- [x] Generación del libro en HTML con Base64 y compilación a PDF de 55 páginas.
- [x] Auditoría visual integral de las 50 imágenes mediante hoja de contactos.
- [x] Sustitución de imágenes erróneas (*San Francisco*, *Sol y sombra*, *Paloma*, *Margarita*, *Sangría*, *Bloody Mary*, *French 75*, *Kir Royale*, *Laguna Azul*, *Marianito*, *Tinto de verano*, *Manhattan*, *Bellini*, *Agua de Valencia*, *Rebujito*).
- [x] Recompilación limpia y validación de páginas del PDF final.
- [x] Creación de `PROMPT_ORIGINAL.md`.
- [x] Implementación del sistema de contexto y memoria técnica persistente del proyecto.

## 14. Tareas pendientes
- [ ] Opcional: Revisar exportación en CMYK / alta resolución (300 DPI) si se destina a imprenta comercial física offset.
- [ ] Opcional: Generar versión interactiva en EPUB para lectores de libros electrónicos.

## 15. Incidencias y problemas conocidos
- Consulta detallada en `INCIDENCIAS.md` (INC-001 a INC-004).
- Errores de búsqueda por homonimia resueltos (ej. "copa de balón/brandy" devolvía globos aerostáticos; "Sol y sombra" descargó un globo al atardecer).

## 16. Soluciones adoptadas
- Filtrado exhaustivo y verificación visual directa de cada archivo gráfico mediante herramientas multimodales y generación de hojas de contactos.
- Búsqueda en categorías especializadas (`Category:Wiki Loves Cocktails`, categorías específicas de la IBA y fotógrafos gastronómicos reputados como Evan Swigart y Ralf Roletschek).

## 17. Restricciones y aspectos que NO deben modificarse
- La regla estricta de **1 cóctel = 1 página** A4 (altura fija de página de 297 mm).
- El total de 50 recetas estructuradas en `cocktails_data.py`.
- La presencia del distintivo verde `0,0% SIN ALCOHOL` en combinados sin alcohol.
- Las medidas en mililitros exactos en todos los ingredientes.

## 18. Información pendiente de verificar
- Ninguna técnica crítica pendiente. Todo el flujo de compilación y datos de recetas está contrastado en disco y validado.

## 19. Criterios de control de calidad
- Validación visual de renderizado en cada página (ausencia de desbordamientos y solapamientos de texto).
- Coherencia entre la cristalería descrita en la ficha y la mostrada en la fotografía.
- Comprobación de que la paleta cromática del combinado y la guarnición coincidan con los ingredientes indicados.

## 20. Historial de cambios del DME
- **v1.0.0 (2026-10-19):** Creación del proyecto inicial de 20 cócteles y posterior ampliación a 50 recetas, maquetación HTML y exportación a PDF de 55 páginas.
- **v1.1.0 (2026-10-20):** Auditoría visual y reemplazo de 15 fotografías desalineadas o de baja calidad (incluyendo San Francisco, Sol y sombra y Paloma). Recompilación del PDF editorial y creación del sistema de contexto técnico persistente.
