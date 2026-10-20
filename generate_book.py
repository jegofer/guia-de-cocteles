# -*- coding: utf-8 -*-
"""
Generador del libro editorial completo en PDF:
'50 CÓCTELES EXPLICADOS PASO A PASO'
"""

import os
import base64
from cocktails_data import COCKTAILS

def get_base64_image(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            data = f.read()
            # check extension
            ext = "jpeg" if file_path.lower().endswith((".jpg", ".jpeg")) else "png"
            return f"data:image/{ext};base64,{base64.b64encode(data).decode('utf-8')}"
    return ""

def build_html():
    # Pre-encode all cocktail images
    encoded_images = {}
    for c in COCKTAILS:
        img_path = f"images/{c['num']:02d}_{c['key']}.jpg"
        encoded_images[c['num']] = get_base64_image(img_path)

    # Let's check cover image: we can use a magnificent bar image or gin_tonic / negroni as hero cover
    cover_bg = encoded_images.get(8) or encoded_images.get(1) # Negroni or Gin tonic

    # HTML Header & CSS
    html = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>50 Cócteles explicados paso a paso - Libro Editorial</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Playfair+Display:ital,wght@0,600;0,700;0,800;1,400;1,600&family=Cinzel:wght@600;700;800;900&family=JetBrains+Mono:wght@400;600&display=swap');

  @page {
    size: A4 portrait;
    margin: 0;
  }
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }
  body {
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #1e293b;
    background: #0f172a;
    -webkit-font-smoothing: antialiased;
  }
  .page {
    width: 210mm;
    height: 297mm;
    max-height: 297mm;
    background: #ffffff;
    margin: 0 auto;
    position: relative;
    overflow: hidden;
    page-break-after: always;
    page-break-inside: avoid;
    display: flex;
    flex-direction: column;
  }

  /* ===================================================
     PORTADA EDITORIAL (COVER)
     =================================================== */
  .page-cover {
    background: linear-gradient(145deg, #090d16 0%, #151c2c 55%, #0d121c 100%);
    color: #ffffff;
    padding: 24mm 20mm;
    justify-content: space-between;
    align-items: center;
    text-align: center;
    border: 1px solid #1e293b;
  }
  .cover-frame {
    width: 100%;
    height: 100%;
    border: 1px solid rgba(217, 119, 6, 0.4);
    border-radius: 4px;
    padding: 16mm 14mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    position: relative;
    box-shadow: inset 0 0 40px rgba(0,0,0,0.5);
  }
  .cover-frame::before {
    content: "";
    position: absolute;
    top: 6px; left: 6px; right: 6px; bottom: 6px;
    border: 1px solid rgba(217, 119, 6, 0.15);
    pointer-events: none;
  }
  .cover-label {
    font-size: 8pt;
    font-weight: 700;
    letter-spacing: 4px;
    text-transform: uppercase;
    color: #f59e0b;
  }
  .cover-title-group {
    margin: 20px 0;
  }
  .cover-num {
    font-family: 'Cinzel', serif;
    font-size: 72pt;
    font-weight: 900;
    color: #fbbf24;
    line-height: 0.9;
    letter-spacing: 2px;
    text-shadow: 0 4px 20px rgba(245, 158, 11, 0.3);
  }
  .cover-main-title {
    font-family: 'Cinzel', serif;
    font-size: 28pt;
    font-weight: 800;
    letter-spacing: 3px;
    color: #ffffff;
    line-height: 1.15;
    margin-top: 10px;
    text-transform: uppercase;
  }
  .cover-subtitle-pill {
    display: inline-block;
    background: rgba(245, 158, 11, 0.15);
    border: 1px solid rgba(245, 158, 11, 0.4);
    color: #fbbf24;
    font-size: 10.5pt;
    font-weight: 600;
    letter-spacing: 1.5px;
    padding: 6px 20px;
    border-radius: 30px;
    margin-top: 14px;
    text-transform: uppercase;
  }
  .cover-desc {
    max-width: 480px;
    font-size: 10.5pt;
    line-height: 1.6;
    color: #cbd5e1;
    font-style: italic;
    margin: 0 auto;
  }
  .cover-features {
    display: flex;
    justify-content: center;
    gap: 24px;
    border-top: 1px solid rgba(217, 119, 6, 0.3);
    border-bottom: 1px solid rgba(217, 119, 6, 0.3);
    padding: 12px 0;
    width: 90%;
  }
  .cover-feature-item {
    font-size: 7.5pt;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #f8fafc;
  }
  .cover-footer {
    font-size: 8pt;
    letter-spacing: 2px;
    color: #94a3b8;
    text-transform: uppercase;
  }

  /* ===================================================
     PÁGINAS EDITORIALES / GUÍA DE INICIACIÓN
     =================================================== */
  .page-editorial {
    padding: 18mm 18mm 14mm 18mm;
    background: #ffffff;
  }
  .editorial-header {
    border-bottom: 2px solid #0f172a;
    padding-bottom: 8px;
    margin-bottom: 18px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
  }
  .editorial-tag {
    font-size: 8pt;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #b45309;
  }
  .editorial-title {
    font-family: 'Playfair Display', serif;
    font-size: 24pt;
    font-weight: 700;
    color: #0f172a;
  }
  .editorial-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    line-height: 1.6;
    font-size: 9pt;
    color: #334155;
  }
  .editorial-col h3 {
    font-family: 'Playfair Display', serif;
    font-size: 13pt;
    font-weight: 700;
    color: #0f172a;
    margin: 14px 0 6px 0;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 4px;
  }
  .editorial-col p {
    margin-bottom: 10px;
    text-align: justify;
  }
  .tool-box {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 10px 12px;
    margin-bottom: 10px;
  }
  .tool-box strong {
    color: #0f172a;
    display: block;
    font-size: 9pt;
    margin-bottom: 2px;
  }

  /* ===================================================
     ÍNDICE DE CONTENIDOS (TABLE OF CONTENTS)
     =================================================== */
  .toc-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    font-size: 8pt;
  }
  .toc-section {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 10px 12px;
  }
  .toc-section-title {
    font-size: 8pt;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: #b45309;
    border-bottom: 1.5px solid #cbd5e1;
    padding-bottom: 4px;
    margin-bottom: 8px;
  }
  .toc-list {
    list-style: none;
  }
  .toc-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 2.5px 0;
    border-bottom: 1px dotted #e2e8f0;
  }
  .toc-item:last-child {
    border-bottom: none;
  }
  .toc-name {
    font-weight: 600;
    color: #1e293b;
  }
  .toc-num {
    font-family: 'JetBrains Mono', monospace;
    font-weight: 600;
    color: #64748b;
    font-size: 7.5pt;
  }
  .toc-page {
    font-family: 'JetBrains Mono', monospace;
    font-weight: 700;
    color: #b45309;
  }

  /* ===================================================
     PÁGINA DE CÓCTEL (RECIPE PAGE)
     =================================================== */
  .page-cocktail {
    padding: 13mm 16mm 11mm 16mm;
    background: #ffffff;
    justify-content: space-between;
  }

  /* Header */
  .recipe-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    border-bottom: 2px solid #0f172a;
    padding-bottom: 7px;
    margin-bottom: 10px;
  }
  .recipe-title-group {
    display: flex;
    flex-direction: column;
  }
  .recipe-method-tag {
    font-size: 7.5pt;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.8px;
    color: #b45309;
    margin-bottom: 2px;
  }
  .recipe-title {
    font-family: 'Playfair Display', serif;
    font-size: 26pt;
    font-weight: 700;
    color: #0f172a;
    line-height: 1.1;
    letter-spacing: -0.5px;
  }
  .recipe-num-box {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
  }
  .recipe-num-label {
    font-size: 6.5pt;
    font-weight: 700;
    letter-spacing: 1.5px;
    color: #94a3b8;
    text-transform: uppercase;
  }
  .recipe-num {
    font-family: 'Cinzel', serif;
    font-size: 26pt;
    font-weight: 800;
    color: #0f172a;
    line-height: 0.9;
  }

  /* Hero Image */
  .recipe-hero-container {
    width: 100%;
    height: 260px;
    border-radius: 8px;
    overflow: hidden;
    position: relative;
    box-shadow: 0 4px 16px rgba(15,23,42,0.12);
    margin-bottom: 11px;
    background: #0f172a;
  }
  .recipe-hero-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center 45%;
    display: block;
  }
  .badge-tag {
    position: absolute;
    top: 12px;
    right: 12px;
    background: rgba(15, 23, 42, 0.90);
    color: #f8fafc;
    font-size: 7.8pt;
    font-weight: 700;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    padding: 6px 14px;
    border-radius: 20px;
    backdrop-filter: blur(4px);
    box-shadow: 0 2px 8px rgba(0,0,0,0.3);
    border: 1px solid rgba(255,255,255,0.15);
  }
  .badge-mocktail {
    background: #047857 !important;
    color: #ffffff !important;
    border: 1px solid #34d399 !important;
    box-shadow: 0 2px 10px rgba(4, 120, 87, 0.4) !important;
  }

  /* Specs Bar */
  .recipe-specs-bar {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 8px;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 9px 12px;
    margin-bottom: 12px;
  }
  .recipe-spec-item {
    display: flex;
    flex-direction: column;
  }
  .recipe-spec-label {
    font-size: 6.8pt;
    font-weight: 700;
    color: #64748b;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin-bottom: 2px;
  }
  .recipe-spec-val {
    font-size: 8.5pt;
    font-weight: 600;
    color: #0f172a;
    line-height: 1.25;
  }

  /* Main Body Grid */
  .recipe-body-grid {
    display: grid;
    grid-template-columns: 39% 59%;
    gap: 16px;
    margin-bottom: 10px;
    flex-grow: 1;
  }
  .recipe-section-title {
    font-size: 8.2pt;
    font-weight: 700;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    color: #0f172a;
    border-bottom: 1.5px solid #cbd5e1;
    padding-bottom: 4px;
    margin-bottom: 8px;
    display: flex;
    align-items: center;
    gap: 6px;
  }

  /* Ingredients */
  .recipe-ingredients-list {
    list-style: none;
  }
  .recipe-ingredients-list li {
    font-size: 8.4pt;
    line-height: 1.45;
    color: #334155;
    margin-bottom: 6.5px;
    padding-left: 14px;
    position: relative;
  }
  .recipe-ingredients-list li::before {
    content: "•";
    color: #d97706;
    font-weight: bold;
    font-size: 13pt;
    position: absolute;
    left: 0;
    top: -4px;
  }

  /* Preparation Steps */
  .recipe-steps-list {
    list-style: none;
    counter-reset: recipe-step;
  }
  .recipe-steps-list li {
    counter-increment: recipe-step;
    position: relative;
    padding-left: 27px;
    font-size: 8.4pt;
    line-height: 1.45;
    color: #334155;
    margin-bottom: 6.5px;
  }
  .recipe-steps-list li::before {
    content: counter(recipe-step);
    position: absolute;
    left: 0;
    top: 1px;
    width: 18px;
    height: 18px;
    background: #0f172a;
    color: #ffffff;
    font-size: 7.2pt;
    font-weight: 700;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    line-height: 18px;
  }

  /* Bartender Tip Box */
  .recipe-bartender-box {
    background: #fffbeb;
    border: 1px solid #fde68a;
    border-left: 4px solid #d97706;
    border-radius: 6px;
    padding: 10px 14px;
    margin-bottom: 10px;
  }
  .recipe-bartender-title {
    font-size: 7.8pt;
    font-weight: 700;
    color: #92400e;
    text-transform: uppercase;
    letter-spacing: 0.9px;
    margin-bottom: 3px;
    display: flex;
    align-items: center;
    gap: 6px;
  }
  .recipe-bartender-text {
    font-size: 8.2pt;
    line-height: 1.42;
    color: #78350f;
    font-style: italic;
  }

  /* Footer */
  .recipe-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid #e2e8f0;
    padding-top: 7px;
    font-size: 7pt;
    color: #94a3b8;
    text-transform: uppercase;
    letter-spacing: 0.8px;
  }

  /* ===================================================
     PÁGINA FINAL: ÍNDICE ALFABÉTICO Y EQUIVALENCIAS
     =================================================== */
  .alphabetical-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 14px;
    font-size: 8pt;
    margin-bottom: 16px;
  }
  .alpha-group-title {
    font-family: 'Cinzel', serif;
    font-size: 11pt;
    font-weight: 700;
    color: #b45309;
    border-bottom: 1.5px solid #b45309;
    padding-bottom: 2px;
    margin-bottom: 6px;
  }
  .alpha-item {
    display: flex;
    justify-content: space-between;
    padding: 2px 0;
    color: #334155;
    border-bottom: 1px dotted #e2e8f0;
  }
  .alpha-page {
    font-family: 'JetBrains Mono', monospace;
    font-weight: 700;
    color: #0f172a;
  }
  .conversion-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 8pt;
    margin-top: 10px;
  }
  .conversion-table th {
    background: #0f172a;
    color: #ffffff;
    font-weight: 700;
    text-transform: uppercase;
    padding: 6px 10px;
    text-align: left;
    letter-spacing: 0.8px;
  }
  .conversion-table td {
    padding: 6px 10px;
    border-bottom: 1px solid #e2e8f0;
    color: #334155;
  }
  .conversion-table tr:nth-child(even) td {
    background: #f8fafc;
  }
</style>
</head>
<body>
"""

    # ----------------------------------------------------
    # 1. PORTADA EDITORIAL (PÁGINA 1)
    # ----------------------------------------------------
    html += f"""
  <!-- PORTADA -->
  <div class="page page-cover">
    <div class="cover-frame">
      <div class="cover-label">Colección de Coctelería de Autor & Gastronomía</div>
      
      <div class="cover-title-group">
        <div class="cover-num">50</div>
        <h1 class="cover-main-title">Cócteles explicados<br>paso a paso</h1>
        <div class="cover-subtitle-pill">Guía visual y práctica para principiantes</div>
      </div>

      <div class="cover-desc">
        Clásicos internacionales legendarios, iconos imprescindibles de la barra española y combinados de referencia formulados con rigor técnico, medidas exactas y trucos profesionales para preparar en casa sin complicaciones.
      </div>

      <div class="cover-features">
        <div class="cover-feature-item">50 Recetas exclusivas</div>
        <div class="cover-feature-item">Medidas en mililitros</div>
        <div class="cover-feature-item">Consejos del bartender</div>
        <div class="cover-feature-item">Fotografía de alta definición</div>
      </div>

      <div class="cover-footer">
        Edición Española de Coctelería Contemporánea
      </div>
    </div>
  </div>
"""

    # ----------------------------------------------------
    # 2. PRÓLOGO EDITORIAL Y TÉCNICAS FUNDAMENTALES (PÁGINA 2)
    # ----------------------------------------------------
    html += """
  <!-- PRÓLOGO Y TÉCNICAS -->
  <div class="page page-editorial">
    <div class="editorial-header">
      <div>
        <span class="editorial-tag">Fundamentos de Barra</span>
        <h2 class="editorial-title">El arte del cóctel en casa</h2>
      </div>
      <span style="font-family:'Cinzel',serif; font-size:14pt; color:#cbd5e1; font-weight:700;">I</span>
    </div>

    <div class="editorial-grid">
      <div class="editorial-col">
        <h3>La santísima trinidad del equilibrio</h3>
        <p>
          Hacer un buen cóctel no consiste en sumar botellas al azar, sino en dominar la relación armónica entre tres pilares fundamentales: <strong>el espíritu o base alcohólica</strong> (que aporta carácter, cuerpo y notas botánicas o añejadas), <strong>el dulce</strong> (azúcares, almíbares o licores que redondean las aristas del alcohol) y <strong>la acidez o amargor</strong> (zumos cítricos frescos o bitters que tensan el trago y despiertan el paladar).
        </p>
        <p>
          Cuando estos tres elementos conviven en proporciones precisas, la bebida fluye en boca sin que ningún ingrediente opaque a los demás. La regla básica para quien se inicia es medir siempre con exactitud: el mejor bartender no improvisa las dosis, las calibra.
        </p>

        <h3>El hielo: el ingrediente invisible</h3>
        <p>
          Uno de los errores más extendidos en la coctelería casera es considerar el hielo como un mero refrigerante. En realidad, el agua resultante de la dilución controlada es el ingrediente que integra químicamente los sabores y doma la graduación alcohólica.
        </p>
        <p>
          El hielo debe ser siempre abundante, limpio y macizo. Cuanto más hielo tenga un vaso, más lenta será la dilución no deseada, ya que la masa fría mantiene el cóctel a temperatura polar sin aguarlo prematuramente.
        </p>
      </div>

      <div class="editorial-col">
        <h3>Las tres técnicas maestras</h3>
        
        <div class="tool-box">
          <strong>1. Construido directo en copa (Build)</strong>
          Para tragos largos, espumosos y combinados (como el Gin-tonic, Aperol spritz o Rebujito). Se ensamblan directamente sobre hielo en el vaso de servicio, respetando el carbónico con removidos mínimos.
        </div>

        <div class="tool-box">
          <strong>2. Agitado en coctelera (Shake)</strong>
          Imprescindible cuando intervienen ingredientes de distintas densidades que requieren emulsión: zumos cítricos, claras de huevo, purés o siropes (como en el Margarita, Daiquiri o Whisky sour). Aporta frío extremo, aireación y microburbujas sedosas.
        </div>

        <div class="tool-box">
          <strong>3. Refrescado con cuchara (Stir)</strong>
          Reservado a cócteles de alcoholes nobles puros y vermuts (como el Negroni, Manhattan o Dry martini). Se remueve en vaso mezclador con hielo durante 25-30 segundos para enfriar a temperaturas bajo cero conservando una transparencia cristalina impecable.
        </div>

        <h3>El valor del producto fresco</h3>
        <p>
          Ningún destilado de gama prémium puede compensar un zumo de cítrico envasado o una menta marchita. Exprimir limones y limas en el momento de preparar el trago garantiza los aceites aromáticos vivos que marcan la diferencia entre una copa doméstica ordinaria y una experiencia de alta coctelería.
        </p>
      </div>
    </div>

    <div class="recipe-footer" style="margin-top:auto;">
      <span>50 CÓCTELES EXPLICADOS PASO A PASO</span>
      <span>Página 2</span>
    </div>
  </div>
"""

    # ----------------------------------------------------
    # 3. CRISTALERÍA Y EQUIPO ESENCIAL (PÁGINA 3)
    # ----------------------------------------------------
    html += """
  <!-- CRISTALERÍA Y EQUIPO -->
  <div class="page page-editorial">
    <div class="editorial-header">
      <div>
        <span class="editorial-tag">Guía del Bartender</span>
        <h2 class="editorial-title">Herramientas y cristalería básica</h2>
      </div>
      <span style="font-family:'Cinzel',serif; font-size:14pt; color:#cbd5e1; font-weight:700;">II</span>
    </div>

    <div class="editorial-grid">
      <div class="editorial-col">
        <h3>El equipamiento imprescindible</h3>
        
        <div class="tool-box">
          <strong>Jigger o medidor de barra</strong>
          Pequeña copa doble de acero (habitualmente de 25/50 ml o 30/60 ml). Es la herramienta más crucial para garantizar la reproducibilidad y el balance exacto de cada receta.
        </div>

        <div class="tool-box">
          <strong>Coctelera (Shaker)</strong>
          Ya sea la clásica de tres piezas (*Cobbler*) con colador integrado, o la de dos cuerpos (*Boston* / *Parisian*). Debe cerrar herméticamente para agitar con firmeza sin salpicaduras.
        </div>

        <div class="tool-box">
          <strong>Cuchara imperial de bar (Barspoon)</strong>
          Cuchara de mango espiralado extralargo. Permite deslizar bebidas carbónicas sin romper la burbuja y refrescar hielo en vaso mezclador con suavidad y rapidez.
        </div>

        <div class="tool-box">
          <strong>Colador gusanillo (Hawthorne strainer)</strong>
          Disco de acero con espiral de alambre perimetral. Retiene los cubos de hielo tras agitar o remover, permitiendo verter un líquido limpio en la copa de servicio.
        </div>

        <div class="tool-box">
          <strong>Mortero de coctelería (Muddler)</strong>
          De madera o teflón estriado. Diseñado para presionar hierbas aromáticas o cítricos extrayendo sus aceites y jugos sin triturar la corteza amarga.
        </div>
      </div>

      <div class="editorial-col">
        <h3>La cristalería adecuada</h3>
        
        <div class="tool-box">
          <strong>Copa balón (Gin tonic / Spritz)</strong>
          De gran volumen y cáliz amplio. Permite albergar abundante hielo macizo y concentrar los aromas botánicos sin que la mano caliente el líquido al sostenerla por el tallo.
        </div>

        <div class="tool-box">
          <strong>Vaso bajo (Old fashioned / Rocks)</strong>
          Vaso cilíndrico de base gruesa y pesada. El estándar universal para destilados con hielo en roca y tragos cortos y concentrados (como el Negroni, Old fashioned o Caipiriña).
        </div>

        <div class="tool-box">
          <strong>Copa cóctel (Coupette / Martini)</strong>
          Copa de cáliz ancho y tallo esbelto, diseñada para servir tragos colados sin hielo (*straight up*). Impide que la temperatura corporal altere la copa helada.
        </div>

        <div class="tool-box">
          <strong>Vaso alto (Collins / Highball)</strong>
          Vaso alargado para cócteles efervescentes y tragos largos refrescantes con hielo abundante (Mojito, Tom Collins, Cuba libre, Moscow mule).
        </div>

        <div class="tool-box">
          <strong>Copa flauta de champán</strong>
          De silueta esbelta para minimizar la superficie de evaporación y preservar la finísima columna de burbujas en cócteles con cava (Mimosa, Bellini, French 75).
        </div>
      </div>
    </div>

    <div class="recipe-footer" style="margin-top:auto;">
      <span>50 CÓCTELES EXPLICADOS PASO A PASO</span>
      <span>Página 3</span>
    </div>
  </div>
"""

    # ----------------------------------------------------
    # 4. ÍNDICE GENERAL / TABLA DE CONTENIDOS (PÁGINA 4)
    # ----------------------------------------------------
    html += """
  <!-- ÍNDICE GENERAL -->
  <div class="page page-editorial">
    <div class="editorial-header">
      <div>
        <span class="editorial-tag">Estructura del Libro</span>
        <h2 class="editorial-title">Tabla de contenidos</h2>
      </div>
      <span style="font-family:'Cinzel',serif; font-size:14pt; color:#cbd5e1; font-weight:700;">III</span>
    </div>

    <div class="toc-grid">
      <!-- Columna 1 -->
      <div>
        <div class="toc-section" style="margin-bottom:12px;">
          <div class="toc-section-title">I. Aperitivos, Vermuts & Spritz</div>
          <ul class="toc-list">
            <li class="toc-item"><span class="toc-name"><span class="toc-num">01.</span> Gin-tonic</span><span class="toc-page">Pág. 5</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">03.</span> Sangría tradicional</span><span class="toc-page">Pág. 7</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">04.</span> Tinto de verano</span><span class="toc-page">Pág. 8</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">05.</span> Aperol spritz</span><span class="toc-page">Pág. 9</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">07.</span> Rebujito</span><span class="toc-page">Pág. 11</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">08.</span> Negroni</span><span class="toc-page">Pág. 12</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">11.</span> Marianito (vermut preparado)</span><span class="toc-page">Pág. 15</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">27.</span> Americano</span><span class="toc-page">Pág. 31</span></li>
          </ul>
        </div>

        <div class="toc-section" style="margin-bottom:12px;">
          <div class="toc-section-title">II. Agitados Cítricos & Coctelería Sour</div>
          <ul class="toc-list">
            <li class="toc-item"><span class="toc-name"><span class="toc-num">09.</span> Margarita</span><span class="toc-page">Pág. 13</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">10.</span> Daiquiri clásico</span><span class="toc-page">Pág. 14</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">22.</span> Whisky sour</span><span class="toc-page">Pág. 26</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">23.</span> Cosmopolitan</span><span class="toc-page">Pág. 27</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">28.</span> Pisco sour</span><span class="toc-page">Pág. 32</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">34.</span> Gimlet</span><span class="toc-page">Pág. 38</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">40.</span> Amaretto sour</span><span class="toc-page">Pág. 44</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">47.</span> Sidecar</span><span class="toc-page">Pág. 51</span></li>
          </ul>
        </div>

        <div class="toc-section">
          <div class="toc-section-title">III. Efervescentes, Cava & Brunch</div>
          <ul class="toc-list">
            <li class="toc-item"><span class="toc-name"><span class="toc-num">06.</span> Agua de Valencia</span><span class="toc-page">Pág. 10</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">17.</span> Tom Collins</span><span class="toc-page">Pág. 21</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">29.</span> Bellini</span><span class="toc-page">Pág. 33</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">30.</span> Mimosa</span><span class="toc-page">Pág. 34</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">37.</span> French 75</span><span class="toc-page">Pág. 41</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">44.</span> Kir Royale</span><span class="toc-page">Pág. 48</span></li>
          </ul>
        </div>
      </div>

      <!-- Columna 2 -->
      <div>
        <div class="toc-section" style="margin-bottom:12px;">
          <div class="toc-section-title">IV. Tragos Largos, Tropicales & Macerados</div>
          <ul class="toc-list">
            <li class="toc-item"><span class="toc-name"><span class="toc-num">02.</span> Mojito</span><span class="toc-page">Pág. 6</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">12.</span> Piña colada</span><span class="toc-page">Pág. 16</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">14.</span> Moscow mule</span><span class="toc-page">Pág. 18</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">15.</span> Caipiriña</span><span class="toc-page">Pág. 19</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">16.</span> Cuba libre</span><span class="toc-page">Pág. 20</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">19.</span> Paloma</span><span class="toc-page">Pág. 23</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">24.</span> San Francisco <strong>(🌿 Sin alcohol)</strong></span><span class="toc-page">Pág. 28</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">25.</span> Bloody Mary</span><span class="toc-page">Pág. 29</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">31.</span> Tequila sunrise</span><span class="toc-page">Pág. 35</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">32.</span> Sex on the beach</span><span class="toc-page">Pág. 36</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">38.</span> Dark and stormy</span><span class="toc-page">Pág. 42</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">39.</span> Caipiroska</span><span class="toc-page">Pág. 43</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">41.</span> Bramble</span><span class="toc-page">Pág. 45</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">42.</span> Mai Tai</span><span class="toc-page">Pág. 46</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">43.</span> Sea breeze</span><span class="toc-page">Pág. 47</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">45.</span> Mint julep</span><span class="toc-page">Pág. 49</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">50.</span> Laguna azul (Blue lagoon)</span><span class="toc-page">Pág. 54</span></li>
          </ul>
        </div>

        <div class="toc-section">
          <div class="toc-section-title">V. Grandes Clásicos & Sobremesas</div>
          <ul class="toc-list">
            <li class="toc-item"><span class="toc-name"><span class="toc-num">13.</span> Espresso martini</span><span class="toc-page">Pág. 17</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">18.</span> Dry martini</span><span class="toc-page">Pág. 22</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">20.</span> Old fashioned</span><span class="toc-page">Pág. 24</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">21.</span> Manhattan</span><span class="toc-page">Pág. 25</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">26.</span> Carajillo quemado (cremaet)</span><span class="toc-page">Pág. 30</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">33.</span> Lumumba</span><span class="toc-page">Pág. 37</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">35.</span> Black Russian</span><span class="toc-page">Pág. 39</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">36.</span> White Russian</span><span class="toc-page">Pág. 40</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">46.</span> Sol y sombra</span><span class="toc-page">Pág. 50</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">48.</span> Café irlandés (Irish coffee)</span><span class="toc-page">Pág. 52</span></li>
            <li class="toc-item"><span class="toc-name"><span class="toc-num">49.</span> Padrino (Godfather)</span><span class="toc-page">Pág. 53</span></li>
          </ul>
        </div>
      </div>
    </div>

    <div class="recipe-footer" style="margin-top:auto;">
      <span>50 CÓCTELES EXPLICADOS PASO A PASO</span>
      <span>Página 4</span>
    </div>
  </div>
"""

    # ----------------------------------------------------
    # 5. PÁGINAS DE CÓCTEL INDIVIDUALES (PÁGINAS 5 A 54)
    # ----------------------------------------------------
    page_offset = 4 # pages 1 to 4 are preliminaries

    for c in COCKTAILS:
        current_page = c['num'] + page_offset
        img_src = encoded_images.get(c['num'], '')

        # Sin alcohol badge styling
        if c['sin_alcohol']:
            badge_html = '<div class="badge-tag badge-mocktail">🌿 0,0% SIN ALCOHOL</div>'
        else:
            badge_html = f'<div class="badge-tag">BASE: {c["base_alcohol"].upper()}</div>'

        # Ingredients HTML
        ing_items = "".join(f"<li>{item}</li>" for item in c['ingredientes'])

        # Steps HTML
        step_items = "".join(f"<li>{step}</li>" for step in c['preparacion'])

        html += f"""
  <!-- CÓCTEL #{c['num']:02d}: {c['nombre']} -->
  <div class="page page-cocktail">
    <!-- Header -->
    <div class="recipe-header">
      <div class="recipe-title-group">
        <span class="recipe-method-tag">{c['metodo']}</span>
        <h2 class="recipe-title">{c['nombre']}</h2>
      </div>
      <div class="recipe-num-box">
        <span class="recipe-num-label">Receta</span>
        <div class="recipe-num">{c['num']:02d}</div>
      </div>
    </div>

    <!-- Fotografía Destacada -->
    <div class="recipe-hero-container">
      <img class="recipe-hero-img" src="{img_src}" alt="{c['nombre']}">
      {badge_html}
    </div>

    <!-- Ficha Técnica -->
    <div class="recipe-specs-bar">
      <div class="recipe-spec-item">
        <span class="recipe-spec-label">Tiempo</span>
        <span class="recipe-spec-val">⏱ {c['tiempo_min']} min</span>
      </div>
      <div class="recipe-spec-item">
        <span class="recipe-spec-label">Cristalería</span>
        <span class="recipe-spec-val">🍸 {c['cristaleria']}</span>
      </div>
      <div class="recipe-spec-item">
        <span class="recipe-spec-label">Perfil de sabor</span>
        <span class="recipe-spec-val">🍋 {c['perfil_sabor']}</span>
      </div>
      <div class="recipe-spec-item">
        <span class="recipe-spec-label">Hielo sugerido</span>
        <span class="recipe-spec-val">🧊 {c['hielo']}</span>
      </div>
    </div>

    <!-- Contenido en 2 columnas: Ingredientes y Preparación -->
    <div class="recipe-body-grid">
      <div>
        <div class="recipe-section-title">Ingredientes exactos</div>
        <ul class="recipe-ingredients-list">
          {ing_items}
        </ul>
      </div>

      <div>
        <div class="recipe-section-title">Preparación paso a paso</div>
        <ol class="recipe-steps-list">
          {step_items}
        </ol>
      </div>
    </div>

    <!-- Consejo del Bartender -->
    <div class="recipe-bartender-box">
      <div class="recipe-bartender-title">💡 Consejo del bartender</div>
      <div class="recipe-bartender-text">"{c['consejo_bartender']}"</div>
    </div>

    <!-- Pie de página -->
    <div class="recipe-footer">
      <span>50 cócteles explicados paso a paso · Guía de iniciación</span>
      <span>Página {current_page}</span>
    </div>
  </div>
"""

    # ----------------------------------------------------
    # 6. PÁGINA FINAL: ÍNDICE ALFABÉTICO Y EQUIVALENCIAS (PÁGINA 55)
    # ----------------------------------------------------
    # Sort cocktails alphabetically
    sorted_cocktails = sorted(COCKTAILS, key=lambda x: x['nombre'])
    
    # Divide into 3 columns
    col1 = sorted_cocktails[:17]
    col2 = sorted_cocktails[17:34]
    col3 = sorted_cocktails[34:]

    def render_alpha_col(items):
        res = "<div>"
        for item in items:
            page = item['num'] + page_offset
            extra = " 🌿" if item['sin_alcohol'] else ""
            res += f'<div class="alpha-item"><span>{item["nombre"]}{extra}</span><span class="alpha-page">{page}</span></div>'
        res += "</div>"
        return res

    html += f"""
  <!-- ÍNDICE ALFABÉTICO Y EQUIVALENCIAS -->
  <div class="page page-editorial">
    <div class="editorial-header">
      <div>
        <span class="editorial-tag">Directorio de Referencia</span>
        <h2 class="editorial-title">Índice alfabético & tablas</h2>
      </div>
      <span style="font-family:'Cinzel',serif; font-size:14pt; color:#cbd5e1; font-weight:700;">IV</span>
    </div>

    <div class="alphabetical-grid">
      {render_alpha_col(col1)}
      {render_alpha_col(col2)}
      {render_alpha_col(col3)}
    </div>

    <div style="margin-top: 14px;">
      <h3 style="font-family:'Playfair Display',serif; font-size:12pt; font-weight:700; color:#0f172a; margin-bottom:6px;">
        Tabla de equivalencias rápidas de coctelería
      </h3>
      <table class="conversion-table">
        <thead>
          <tr>
            <th>Medida tradicional</th>
            <th>Equivalencia en ml</th>
            <th>Uso común en barra</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>1 Golpe (Dash)</strong></td>
            <td>Aprox. 0,8 - 1 ml</td>
            <td>Amargos aromáticos (Angostura, Peychaud's, tabasco).</td>
          </tr>
          <tr>
            <td><strong>1 Cucharilla imperial (Barspoon)</strong></td>
            <td>5 ml</td>
            <td>Jarabes concentrados, licores potentes, azúcar.</td>
          </tr>
          <tr>
            <td><strong>1 Parte estándar (Shot / Chupito)</strong></td>
            <td>30 ml</td>
            <td>Medida base simple de licor o zumo.</td>
          </tr>
          <tr>
            <td><strong>1 Onza líquida estadounidense (1 fl oz)</strong></td>
            <td>29,57 ml (aprox. 30 ml)</td>
            <td>Referencia estándar de recetarios anglosajones.</td>
          </tr>
          <tr>
            <td><strong>Dosis estándar de destilado (Jigger completo)</strong></td>
            <td>50 ml</td>
            <td>Base alcohólica principal de un cóctel largo o agitado.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="recipe-bartender-box" style="margin-top:14px;">
      <div class="recipe-bartender-title">🍸 Nota final del bartender</div>
      <div class="recipe-bartender-text">
        "El mayor secreto de la coctelería no radica en tener un botellero inmenso, sino en el afecto y la precisión con que recibes a tus invitados. Disfruta del proceso, atrévete a experimentar y brinda con responsabilidad."
      </div>
    </div>

    <div class="recipe-footer" style="margin-top:auto;">
      <span>50 CÓCTELES EXPLICADOS PASO A PASO · EDICIÓN COMPLETA</span>
      <span>Página 55</span>
    </div>
  </div>

</body>
</html>
"""

    with open("libro_cocteles.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("libro_cocteles.html generado con éxito!")

if __name__ == "__main__":
    build_html()
