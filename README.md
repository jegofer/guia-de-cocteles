# 🍸 50 Cócteles Explicados Paso a Paso

Guía interactiva visual y editorial de coctelería contemporánea, iconos de la barra española y clásicos legendarios internacionales. Formulada con medidas exactas en mililitros, fotografías en alta definición y trucos profesionales de bartender.

---

## 📱 Acceso Web Móvil y Descarga

* **🌐 Aplicación Web:** [https://jegofer.github.io/guia-de-cocteles/](https://jegofer.github.io/guia-de-cocteles/) *(en GitHub Pages)*
* **📖 Descargar Libro Completo en PDF:** [`50_cocteles_explicados_paso_a_paso.pdf`](50_cocteles_explicados_paso_a_paso.pdf) *(55 páginas A4)*

---

## ✨ Características de la Web Móvil

- **Diseño Mobile-First:** Diseñada para consultar cómodamente desde teléfonos móviles y barras de cocina.
- **Búsqueda Instantánea:** Filtrado en tiempo real por nombre de cóctel, destilado base (*ginebra, ron, vodka, tequila, whisky, vermut*) o ingredientes (*limón, pomelo, café, menta*).
- **Filtros por Categoría:** Aperitivos & Spritz, Cítricos & Sours, Cava & Brunch, Tragos Largos & Tropicales, Grandes Clásicos, Iconos Ibéricos y Cócteles Sin Alcohol.
- **Fichas Interactivas con Checklist:** Permite ir marcando los ingredientes según los agregas a la copa o coctelera.
- **Consejos del Bartender:** Trucos de equilibrio, dilución de hielo y cristalería recomendada.

---

## 📂 Estructura del Repositorio

* `index.html`: Aplicación web interactiva SPA (Single Page Application) ligera (102 KB).
* `50_cocteles_explicados_paso_a_paso.pdf`: Libro editorial completo en PDF de 55 páginas.
* `images/`: Banco de 50 fotografías en alta resolución auditadas.
* `cocktails_data.py`: Base de datos estructurada en Python con las 50 recetas completas.
* `generate_web.py`: Script para regenerar `index.html` a partir de los datos.
* `generate_book.py`: Script para generar el libro editorial HTML para impresión a PDF.
* `DME.md`: Documento Maestro de Especificaciones técnicas del proyecto.

---

## 🛠️ Generación Local

Si modificas alguna receta en `cocktails_data.py`:

```bash
# Regenerar la web móvil:
python3 generate_web.py

# Regenerar el libro de imprenta:
python3 generate_book.py
```
