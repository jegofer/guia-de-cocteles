# Tareas pendientes

## CRÍTICAS
*(No hay tareas críticas pendientes. La publicación y el PDF se encuentran íntegramente compilados y validados).*

## ALTAS
- [ ] **Validación final del PDF con el usuario:**
  - **Por qué:** Confirmar que la selección de nuevas imágenes (San Francisco, Sol y sombra, Paloma, Sangría, etc.) cumple plenamente sus expectativas estéticas y editoriales.
  - **Dependencias:** Apertura y visualización del archivo por parte del usuario.
  - **Archivos afectados:** `50_cocteles_explicados_paso_a_paso.pdf`.
  - **Resultado esperado:** Aprobación definitiva del documento para su uso final.

## MEDIAS
- [ ] **Limpieza de archivos temporales de prueba:**
  - **Por qué:** Retirar la carpeta `test_images/` y scripts efímeros de validación si ya no son requeridos, manteniendo el directorio limpio.
  - **Dependencias:** Confirmación de que no se requerirán más pruebas fotográficas.
  - **Archivos afectados:** Carpeta `test_images/`, `review_gallery.html`, `contact_sheet.jpg`.
  - **Resultado esperado:** Directorio de trabajo con solo los archivos nucleares del proyecto.

## BAJAS
- [ ] **Ajuste de perfiles de color CMYK para imprenta:**
  - **Por qué:** Si el usuario decide imprimir el libro en imprenta tradicional física en papel cuché, los perfiles RGB de pantalla pueden experimentar ligeras variaciones de saturación.
  - **Dependencias:** Petición expresa de tirada física profesional.
  - **Archivos afectados:** `generate_book.py`, `images/*.jpg`.
  - **Resultado esperado:** Archivo PDF/X-1a o PDF/X-4 preparado para preimpresión.

## IDEAS / MEJORAS FUTURAS
- [ ] **Exportación en formato interactivo EPUB / eBook:**
  - **Por qué:** Permitir la lectura fluida en tabletas, iPads y lectores de libros electrónicos tipo Kindle con índice navegable.
  - **Dependencias:** Reestructuración en HTML adaptativo para e-readers.
  - **Archivos afectados:** Nuevo script de exportación EPUB.
  - **Resultado esperado:** Archivo `.epub` validado.
- [ ] **Versión con maridaje gastronómico (tapas y aperitivos):**
  - **Por qué:** Añadir en cada página una pequeña sugerencia de bocado o tapa española acorde con el perfil de sabor de cada cóctel.
  - **Dependencias:** Ampliación del esquema de datos en `cocktails_data.py`.
  - **Archivos afectados:** `cocktails_data.py`, `generate_book.py`.
  - **Resultado esperado:** Campo de maridaje integrado en la ficha técnica.
