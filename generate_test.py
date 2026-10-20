import base64
import os
from cocktails_data import COCKTAILS

def get_base64_img(path):
    if os.path.exists(path):
        with open(path, 'rb') as f:
            data = f.read()
            return f"data:image/jpeg;base64,{base64.b64encode(data).decode('utf-8')}"
    return ""

test_cocktail = COCKTAILS[0]
img_path = f"images/{test_cocktail['num']:02d}_{test_cocktail['key']}.jpg"
img_b64 = get_base64_img(img_path)

html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,600;0,700;1,400&family=Cinzel:wght@600;700;800&display=swap');

  @page {{
    size: A4 portrait;
    margin: 0;
  }}
  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }}
  body {{
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #1e293b;
    background: #e2e8f0;
  }}
  .page {{
    width: 210mm;
    height: 297mm;
    max-height: 297mm;
    background: #ffffff;
    margin: 0 auto;
    position: relative;
    overflow: hidden;
    page-break-after: always;
    padding: 14mm 16mm 12mm 16mm;
    display: flex;
    flex-direction: column;
  }}
  
  /* Header */
  .header {{
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    border-bottom: 2px solid #0f172a;
    padding-bottom: 8px;
    margin-bottom: 12px;
  }}
  .title-group {{
    display: flex;
    flex-direction: column;
  }}
  .meta-tag {{
    font-size: 8pt;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.8px;
    color: #b45309;
    margin-bottom: 2px;
  }}
  .cocktail-title {{
    font-family: 'Playfair Display', serif;
    font-size: 27pt;
    font-weight: 700;
    color: #0f172a;
    line-height: 1.1;
    letter-spacing: -0.5px;
  }}
  .cocktail-num-box {{
    display: flex;
    flex-direction: column;
    align-items: flex-end;
  }}
  .cocktail-num-label {{
    font-size: 6.5pt;
    font-weight: 700;
    letter-spacing: 1.5px;
    color: #94a3b8;
    text-transform: uppercase;
  }}
  .cocktail-num {{
    font-family: 'Cinzel', serif;
    font-size: 26pt;
    font-weight: 800;
    color: #0f172a;
    line-height: 0.9;
  }}

  /* Hero image */
  .hero-container {{
    width: 100%;
    height: 265px;
    border-radius: 8px;
    overflow: hidden;
    position: relative;
    box-shadow: 0 4px 16px rgba(15,23,42,0.14);
    margin-bottom: 12px;
  }}
  .hero-img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
  }}
  .badge-alcohol {{
    position: absolute;
    top: 12px;
    right: 12px;
    background: rgba(15, 23, 42, 0.88);
    color: #f8fafc;
    font-size: 8pt;
    font-weight: 700;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    padding: 6px 14px;
    border-radius: 20px;
    backdrop-filter: blur(4px);
    box-shadow: 0 2px 6px rgba(0,0,0,0.3);
  }}
  .badge-sin-alcohol {{
    background: #059669 !important;
    color: #ffffff !important;
    border: 1px solid #34d399;
  }}

  /* Ficha técnica */
  .specs-bar {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 8px;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 10px 14px;
    margin-bottom: 14px;
  }}
  .spec-item {{
    display: flex;
    flex-direction: column;
  }}
  .spec-label {{
    font-size: 6.8pt;
    font-weight: 700;
    color: #64748b;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin-bottom: 3px;
  }}
  .spec-val {{
    font-size: 8.8pt;
    font-weight: 600;
    color: #0f172a;
    line-height: 1.25;
  }}

  /* Main content layout (2 cols) */
  .content-grid {{
    display: grid;
    grid-template-columns: 39% 59%;
    gap: 16px;
    margin-bottom: 14px;
    flex-grow: 1;
  }}
  .section-h {{
    font-size: 8.5pt;
    font-weight: 700;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    color: #0f172a;
    border-bottom: 1.5px solid #cbd5e1;
    padding-bottom: 5px;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 6px;
  }}
  
  /* Ingredients */
  .ingredients-list {{
    list-style: none;
  }}
  .ingredients-list li {{
    font-size: 8.6pt;
    line-height: 1.5;
    color: #334155;
    margin-bottom: 8px;
    padding-left: 16px;
    position: relative;
  }}
  .ingredients-list li::before {{
    content: "•";
    color: #d97706;
    font-weight: bold;
    font-size: 13pt;
    position: absolute;
    left: 0;
    top: -3px;
  }}

  /* Preparation */
  .steps-list {{
    list-style: none;
    counter-reset: step-counter;
  }}
  .steps-list li {{
    counter-increment: step-counter;
    position: relative;
    padding-left: 28px;
    font-size: 8.6pt;
    line-height: 1.5;
    color: #334155;
    margin-bottom: 8px;
  }}
  .steps-list li::before {{
    content: counter(step-counter);
    position: absolute;
    left: 0;
    top: 1px;
    width: 19px;
    height: 19px;
    background: #0f172a;
    color: #ffffff;
    font-size: 7.5pt;
    font-weight: 700;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    line-height: 19px;
  }}

  /* Bartender note */
  .bartender-box {{
    background: #fffbeb;
    border: 1px solid #fde68a;
    border-left: 4px solid #d97706;
    border-radius: 6px;
    padding: 11px 14px;
    margin-bottom: 12px;
  }}
  .bartender-title {{
    font-size: 8pt;
    font-weight: 700;
    color: #92400e;
    text-transform: uppercase;
    letter-spacing: 0.9px;
    margin-bottom: 4px;
    display: flex;
    align-items: center;
    gap: 6px;
  }}
  .bartender-text {{
    font-size: 8.3pt;
    line-height: 1.45;
    color: #78350f;
    font-style: italic;
  }}

  /* Footer */
  .footer {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid #e2e8f0;
    padding-top: 8px;
    font-size: 7.2pt;
    color: #94a3b8;
    text-transform: uppercase;
    letter-spacing: 0.8px;
  }}
</style>
</head>
<body>
  <div class="page">
    <div class="header">
      <div class="title-group">
        <span class="meta-tag">{test_cocktail['metodo']}</span>
        <h1 class="cocktail-title">{test_cocktail['nombre']}</h1>
      </div>
      <div class="cocktail-num-box">
        <span class="cocktail-num-label">Receta</span>
        <div class="cocktail-num">{test_cocktail['num']:02d}</div>
      </div>
    </div>

    <div class="hero-container">
      <img class="hero-img" src="{img_b64}" alt="{test_cocktail['nombre']}">
      <div class="badge-alcohol {'badge-sin-alcohol' if test_cocktail['sin_alcohol'] else ''}">
        {'🌿 0,0% SIN ALCOHOL' if test_cocktail['sin_alcohol'] else 'BASE: ' + test_cocktail['base_alcohol'].upper()}
      </div>
    </div>

    <div class="specs-bar">
      <div class="spec-item">
        <span class="spec-label">Tiempo</span>
        <span class="spec-val">⏱ {test_cocktail['tiempo_min']} min</span>
      </div>
      <div class="spec-item">
        <span class="spec-label">Cristalería</span>
        <span class="spec-val">🍸 {test_cocktail['cristaleria']}</span>
      </div>
      <div class="spec-item">
        <span class="spec-label">Perfil de sabor</span>
        <span class="spec-val">🍋 {test_cocktail['perfil_sabor']}</span>
      </div>
      <div class="spec-item">
        <span class="spec-label">Hielo sugerido</span>
        <span class="spec-val">🧊 {test_cocktail['hielo']}</span>
      </div>
    </div>

    <div class="content-grid">
      <div class="col-ingredients">
        <div class="section-h">Ingredientes exactos</div>
        <ul class="ingredients-list">
          {''.join(f'<li>{i}</li>' for i in test_cocktail['ingredientes'])}
        </ul>
      </div>

      <div class="col-preparation">
        <div class="section-h">Preparación paso a paso</div>
        <ol class="steps-list">
          {''.join(f'<li>{s}</li>' for s in test_cocktail['preparacion'])}
        </ol>
      </div>
    </div>

    <div class="bartender-box">
      <div class="bartender-title">💡 Consejo del bartender</div>
      <div class="bartender-text">"{test_cocktail['consejo_bartender']}"</div>
    </div>

    <div class="footer">
      <span>50 cócteles explicados paso a paso · Guía de iniciación</span>
      <span>Página {test_cocktail['num']}</span>
    </div>
  </div>
</body>
</html>
"""

with open('test_page.html', 'w', encoding='utf-8') as f:
    f.write(html)
