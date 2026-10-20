# Registro de decisiones del proyecto

## DEC-001 — Adopción de arquitectura HTML/CSS + Chromium headless para maquetación

- **Fecha:** 2026-10-19
- **Decisión:** Utilizar HTML5 y CSS Paged Media con flexbox/grid y exportar a PDF mediante Google Chrome/Chromium en modo headless (`--headless=new --print-to-pdf`), en lugar de LaTeX o Typst.
- **Motivo:** Permite un control tipográfico y visual contemporáneo extremadamente refinado, soporte directo para Google Fonts, fácil incrustación de imágenes en Base64 y retícula pixel-perfect a escala milimétrica.
- **Alternativas consideradas:**
  - *LaTeX:* Tipografía clásica pero muy rígida y compleja para maquetación editorial publicitaria/gastronómica con fotografías a sangre y fondos oscuros.
  - *Weasyprint:* No disponible en el entorno del sistema.
  - *Typst:* No instalado en el sistema.
- **Consecuencias:** Se obtiene un PDF de 55 páginas idéntico al renderizado web, sin dependencias externas complejas.
- **Estado:** APROBADA

---

## DEC-002 — Ampliación del catálogo de 20 a 50 cócteles

- **Fecha:** 2026-10-19
- **Decisión:** Incrementar el repertorio de 20 a 50 combinados a petición del usuario, retirando el *Calimocho* y abarcando clásicos internacionales y recetas de fuerte arraigo en la hostelería española.
- **Motivo:** Dotar a la publicación de un valor editorial exhaustivo como guía de referencia completa para principiantes.
- **Alternativas consideradas:** Mantener una selección breve de 20 o 40 tragos.
- **Consecuencias:** Se estructuró un libro de 55 páginas con tabla de contenidos clasificada en 5 familias sensoriales e índice alfabético con tabla de conversiones.
- **Estado:** VIGENTE

---

## DEC-003 — Estricta regla de maquetación: 1 cóctel = 1 página exacta

- **Fecha:** 2026-10-19
- **Decisión:** Cada receta debe quedar contenida de forma fija e inmutable en exactamente una página A4 (`210mm x 297mm`), con `page-break-after: always`.
- **Motivo:** Claridad visual y usabilidad en la cocina/barra, permitiendo consultar la receta completa de un vistazo sin pasar página.
- **Alternativas consideradas:** Recetas a dos páginas o texto continuo fluido.
- **Consecuencias:** Exige calibrar rigurosamente el espaciado, tamaño de fuentes e interlineados para que las recetas más largas no provoquen desbordamiento de página.
- **Estado:** VIGENTE

---

## DEC-004 — Distintivo específico para cócteles sin alcohol

- **Fecha:** 2026-10-19
- **Decisión:** Incluir un badge destacado en verde esmeralda `🌿 0,0% SIN ALCOHOL` en la cabecera de la ficha técnica y en la esquina de la fotografía en combinados sin alcohol (como el *San Francisco*).
- **Motivo:** Petición expresa del usuario para identificar rápidamente opciones para personas que no consumen alcohol o conductores.
- **Alternativas consideradas:** Texto simple en la lista de ingredientes o ficha técnica.
- **Consecuencias:** Mayor claridad visual y valor inclusivo en el recetario.
- **Estado:** VIGENTE

---

## DEC-005 — Auditoría visual y reemplazo de fotografías disonantes

- **Fecha:** 2026-10-20
- **Decisión:** Auditar las 50 fotografías y sustituir 15 imágenes que no coincidían con la receta o presentaban estética amateur/inadecuada (especialmente San Francisco, Sol y sombra y Paloma).
- **Motivo:** El usuario observó que algunas imágenes no correspondían a la bebida descrita (ej. Sol y sombra mostraba un globo aerostático al atardecer por homonimia de búsqueda, San Francisco era una bebida azul y Paloma estaba en un tarro de mermelada con albahaca).
- **Alternativas consideradas:** Mantener las imágenes existentes o usar ilustraciones vectoriales.
- **Consecuencias:** Sustitución por fotografías de calidad de estudio de Wiki Loves Cocktails y Wikimedia Commons, verificadas mediante hojas de contacto y previsualizaciones PNG.
- **Estado:** VIGENTE

---

## DEC-006 — Empaquetado autocontenido de imágenes en Base64

- **Fecha:** 2026-10-19
- **Decisión:** Incrustar todas las fotografías en el archivo `libro_cocteles.html` como `data:image/jpeg;base64,...`.
- **Motivo:** Evitar problemas de rutas relativas o permisos de acceso local al compilar con Chromium headless y permitir compartir el archivo HTML como un artefacto único y autónomo.
- **Alternativas consideradas:** Referencias por ruta de archivo local `file://`.
- **Consecuencias:** Aumenta el tamaño de `libro_cocteles.html` (~12.7 MB), pero garantiza una portabilidad y estabilidad de compilación absolutas.
- **Estado:** VIGENTE
