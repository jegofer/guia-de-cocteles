# -*- coding: utf-8 -*-
"""
Generador de la aplicación Web Móvil Interactiva (Single Page Application):
'50 CÓCTELES EXPLICADOS PASO A PASO'
Optimizada para GitHub Pages, dispositivos móviles y pantallas táctiles.
"""

import json
import os
from cocktails_data import COCKTAILS

# Mapeo de categorías por número de cóctel según la estructura del libro
SECTION_MAP = {
    # I. Aperitivos, Vermuts & Spritz
    1: "Aperitivos & Spritz", 3: "Aperitivos & Spritz", 4: "Aperitivos & Spritz",
    5: "Aperitivos & Spritz", 7: "Aperitivos & Spritz", 8: "Aperitivos & Spritz",
    11: "Aperitivos & Spritz", 27: "Aperitivos & Spritz",
    
    # II. Agitados Cítricos & Sours
    9: "Cítricos & Sours", 10: "Cítricos & Sours", 22: "Cítricos & Sours",
    23: "Cítricos & Sours", 28: "Cítricos & Sours", 34: "Cítricos & Sours",
    40: "Cítricos & Sours", 47: "Cítricos & Sours",
    
    # III. Efervescentes, Cava & Brunch
    6: "Cava & Brunch", 17: "Cava & Brunch", 29: "Cava & Brunch",
    30: "Cava & Brunch", 37: "Cava & Brunch", 44: "Cava & Brunch",
    
    # IV. Tragos Largos & Tropicales
    2: "Tragos Largos & Tropicales", 12: "Tragos Largos & Tropicales", 14: "Tragos Largos & Tropicales",
    15: "Tragos Largos & Tropicales", 16: "Tragos Largos & Tropicales", 19: "Tragos Largos & Tropicales",
    24: "Tragos Largos & Tropicales", 25: "Tragos Largos & Tropicales", 31: "Tragos Largos & Tropicales",
    32: "Tragos Largos & Tropicales", 38: "Tragos Largos & Tropicales", 39: "Tragos Largos & Tropicales",
    41: "Tragos Largos & Tropicales", 42: "Tragos Largos & Tropicales", 43: "Tragos Largos & Tropicales",
    45: "Tragos Largos & Tropicales", 50: "Tragos Largos & Tropicales",
    
    # V. Grandes Clásicos & Sobremesas
    13: "Clásicos & Sobremesa", 18: "Clásicos & Sobremesa", 20: "Clásicos & Sobremesa",
    21: "Clásicos & Sobremesa", 26: "Clásicos & Sobremesa", 33: "Clásicos & Sobremesa",
    35: "Clásicos & Sobremesa", 36: "Clásicos & Sobremesa", 46: "Clásicos & Sobremesa",
    48: "Clásicos & Sobremesa", 49: "Clásicos & Sobremesa"
}

# Iconos representativos de la tradición ibérica
SPANISH_COCKTAILS = {1, 3, 4, 6, 7, 11, 24, 26, 33, 46}

def get_liquor_group(c):
    if c.get("sin_alcohol"):
        return "sin-alcohol"
    base = c.get("base_alcohol", "").lower()
    if "ginebra" in base or "gin" in base:
        return "ginebra"
    if "ron" in base or "cachaça" in base:
        return "ron"
    if "vodka" in base:
        return "vodka"
    if "tequila" in base or "mezcal" in base:
        return "tequila"
    if "whisky" in base or "bourbon" in base:
        return "whisky"
    if "vermut" in base or "vino" in base or "cava" in base or "anís" in base or "brandy" in base:
        return "vermut-vinos"
    return "otros"

def build_web_app():
    # Enriquecer los datos para el frontend interactivo
    data_for_json = []
    for c in COCKTAILS:
        num = c["num"]
        key = c["key"]
        c_copy = dict(c)
        c_copy["section"] = SECTION_MAP.get(num, "Coctelería")
        c_copy["is_spanish"] = num in SPANISH_COCKTAILS
        c_copy["liquor_group"] = get_liquor_group(c)
        c_copy["image_url"] = f"images/{num:02d}_{key}.jpg"
        data_for_json.append(c_copy)

    cocktails_json_str = json.dumps(data_for_json, ensure_ascii=False)

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, viewport-fit=cover">
  <meta name="theme-color" content="#090d16">
  <meta name="description" content="Guía interactiva para móvil de 50 cócteles explicados paso a paso con medidas exactas, fotos de alta resolución y trucos de bartender.">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <title>50 Cócteles explicados paso a paso | Guía Web Móvil</title>
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">

  <style>
    :root {{
      --bg-dark: #090d16;
      --bg-surface: #111827;
      --bg-surface-elevated: #1f293d;
      --bg-surface-hover: #26334d;
      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-gold: rgba(245, 158, 11, 0.35);
      --gold-primary: #f59e0b;
      --gold-light: #fbbf24;
      --gold-glow: rgba(245, 158, 11, 0.2);
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-soft: #cbd5e1;
      --accent-green: #10b981;
      --radius-sm: 8px;
      --radius-md: 14px;
      --radius-lg: 20px;
      --radius-full: 9999px;
      --shadow-card: 0 10px 25px -5px rgba(0, 0, 0, 0.4), 0 8px 10px -6px rgba(0, 0, 0, 0.3);
      --shadow-modal: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }}

    body {{
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--bg-dark);
      color: var(--text-main);
      min-height: 100vh;
      line-height: 1.5;
      padding-bottom: 60px;
    }}

    /* HEADER & HERO */
    header.hero {{
      background: linear-gradient(180deg, #131b2e 0%, #090d16 100%);
      border-bottom: 1px solid var(--border-subtle);
      padding: 2.2rem 1.25rem 1.8rem;
      text-align: center;
      position: relative;
    }}

    .hero-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(245, 158, 11, 0.12);
      border: 1px solid var(--border-gold);
      color: var(--gold-light);
      font-size: 0.75rem;
      font-weight: 700;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      padding: 6px 14px;
      border-radius: var(--radius-full);
      margin-bottom: 1rem;
    }}

    .hero-title {{
      font-family: 'Cinzel', serif;
      font-size: clamp(1.8rem, 5vw, 2.8rem);
      font-weight: 800;
      letter-spacing: 1px;
      line-height: 1.15;
      margin-bottom: 0.75rem;
      background: linear-gradient(135deg, #ffffff 40%, #fbbf24 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    .hero-subtitle {{
      color: var(--text-soft);
      font-size: 0.95rem;
      max-width: 600px;
      margin: 0 auto 1.5rem;
      line-height: 1.5;
    }}

    /* HERO ACTIONS */
    .hero-actions {{
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 10px;
      margin-bottom: 1rem;
    }}

    .btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      padding: 10px 18px;
      border-radius: var(--radius-full);
      font-size: 0.88rem;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.2s ease;
      cursor: pointer;
      border: none;
    }}

    .btn-gold {{
      background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
      color: #090d16;
      box-shadow: 0 4px 15px var(--gold-glow);
    }}
    .btn-gold:hover, .btn-gold:active {{
      background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%);
      transform: translateY(-1px);
    }}

    .btn-glass {{
      background: rgba(255, 255, 255, 0.08);
      color: var(--text-main);
      border: 1px solid var(--border-subtle);
      backdrop-filter: blur(10px);
    }}
    .btn-glass:hover, .btn-glass:active {{
      background: rgba(255, 255, 255, 0.14);
      border-color: rgba(255, 255, 255, 0.2);
    }}

    /* SEARCH & FILTER CONTROLS (STICKY) */
    .sticky-controls {{
      position: sticky;
      top: 0;
      z-index: 40;
      background: rgba(9, 13, 22, 0.92);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border-subtle);
      padding: 0.75rem 1rem;
    }}

    .controls-inner {{
      max-width: 1200px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }}

    /* SEARCH INPUT */
    .search-box {{
      position: relative;
      width: 100%;
    }}

    .search-icon {{
      position: absolute;
      left: 14px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-muted);
      pointer-events: none;
      width: 18px;
      height: 18px;
    }}

    .search-input {{
      width: 100%;
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-full);
      padding: 11px 40px 11px 42px;
      color: var(--text-main);
      font-size: 0.95rem;
      outline: none;
      transition: all 0.2s ease;
    }}
    .search-input:focus {{
      border-color: var(--gold-primary);
      box-shadow: 0 0 0 3px var(--gold-glow);
      background: var(--bg-surface-elevated);
    }}
    .search-input::placeholder {{
      color: var(--text-muted);
    }}

    .search-clear {{
      position: absolute;
      right: 12px;
      top: 50%;
      transform: translateY(-50%);
      background: none;
      border: none;
      color: var(--text-muted);
      font-size: 1.1rem;
      cursor: pointer;
      display: none;
      padding: 4px 8px;
    }}

    /* PILLS / CHIPS SCROLLER */
    .chips-scroller {{
      display: flex;
      gap: 6px;
      overflow-x: auto;
      scrollbar-width: none;
      -webkit-overflow-scrolling: touch;
      padding-bottom: 2px;
    }}
    .chips-scroller::-webkit-scrollbar {{
      display: none;
    }}

    .chip {{
      white-space: nowrap;
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      color: var(--text-soft);
      padding: 6px 14px;
      border-radius: var(--radius-full);
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.15s ease;
      display: inline-flex;
      align-items: center;
      gap: 5px;
    }}
    .chip:hover {{
      background: var(--bg-surface-elevated);
      color: #ffffff;
    }}
    .chip.active {{
      background: var(--gold-primary);
      color: #090d16;
      border-color: var(--gold-light);
      box-shadow: 0 2px 10px var(--gold-glow);
    }}

    /* METRICS / STATS BAR */
    .stats-bar {{
      max-width: 1200px;
      margin: 1rem auto 0.5rem;
      padding: 0 1rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.82rem;
      color: var(--text-muted);
    }}

    /* GRID DE RECETAS */
    .cocktails-container {{
      max-width: 1200px;
      margin: 0.75rem auto 2rem;
      padding: 0 1rem;
    }}

    .cocktails-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(290px, 1fr));
      gap: 1.25rem;
    }}

    /* TARJETA DE CÓCTEL */
    .card {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      overflow: hidden;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
      box-shadow: var(--shadow-card);
      position: relative;
    }}
    .card:hover {{
      transform: translateY(-3px);
      box-shadow: 0 16px 30px -10px rgba(0,0,0,0.6);
      border-color: rgba(245, 158, 11, 0.4);
    }}
    .card:active {{
      transform: scale(0.98);
    }}

    /* IMAGEN DE TARJETA */
    .card-img-wrap {{
      position: relative;
      width: 100%;
      height: 200px;
      background: #0f172a;
      overflow: hidden;
    }}

    .card-img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center 45%;
      transition: transform 0.35s ease;
    }}
    .card:hover .card-img {{
      transform: scale(1.05);
    }}

    .card-num {{
      position: absolute;
      top: 10px;
      left: 10px;
      background: rgba(9, 13, 22, 0.85);
      border: 1px solid rgba(255, 255, 255, 0.15);
      backdrop-filter: blur(6px);
      color: var(--gold-light);
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.75rem;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: var(--radius-sm);
    }}

    .card-badge {{
      position: absolute;
      top: 10px;
      right: 10px;
      background: rgba(9, 13, 22, 0.85);
      backdrop-filter: blur(6px);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #ffffff;
      font-size: 0.7rem;
      font-weight: 700;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      padding: 4px 9px;
      border-radius: var(--radius-full);
    }}
    .card-badge.badge-mocktail {{
      background: #047857;
      border-color: #34d399;
    }}
    .card-badge.badge-spanish {{
      background: #b45309;
      border-color: #fbbf24;
    }}

    /* CONTENIDO DE TARJETA */
    .card-body {{
      padding: 1.1rem;
      display: flex;
      flex-direction: column;
      flex-grow: 1;
    }}

    .card-header {{
      margin-bottom: 0.6rem;
    }}

    .card-category {{
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: var(--gold-primary);
      margin-bottom: 2px;
    }}

    .card-title {{
      font-family: 'Cinzel', serif;
      font-size: 1.25rem;
      font-weight: 700;
      color: #ffffff;
      line-height: 1.2;
    }}

    .card-taste {{
      font-size: 0.82rem;
      color: var(--text-muted);
      margin-bottom: 0.8rem;
      font-style: italic;
    }}

    .card-specs {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 6px;
      background: var(--bg-surface-elevated);
      border-radius: var(--radius-sm);
      padding: 8px 10px;
      font-size: 0.75rem;
      margin-bottom: 0.9rem;
    }}
    .card-spec-item {{
      display: flex;
      flex-direction: column;
    }}
    .card-spec-label {{
      color: var(--text-muted);
      font-size: 0.65rem;
      text-transform: uppercase;
      font-weight: 600;
    }}
    .card-spec-val {{
      color: var(--text-main);
      font-weight: 600;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    .card-footer {{
      margin-top: auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 0.6rem;
      border-top: 1px solid var(--border-subtle);
      font-size: 0.78rem;
      color: var(--gold-light);
      font-weight: 600;
    }}

    /* NO RESULTS */
    .no-results {{
      text-align: center;
      padding: 4rem 1rem;
      color: var(--text-muted);
      display: none;
    }}
    .no-results h3 {{
      font-size: 1.3rem;
      color: #ffffff;
      margin-bottom: 0.5rem;
    }}

    /* MODAL / BOTTOM SHEET DE RECETA */
    .modal-backdrop {{
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(0, 0, 0, 0.8);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      z-index: 100;
      display: none;
      align-items: flex-end;
      justify-content: center;
      opacity: 0;
      transition: opacity 0.25s ease;
    }}
    .modal-backdrop.open {{
      opacity: 1;
    }}

    .modal-sheet {{
      background: var(--bg-surface);
      width: 100%;
      max-width: 680px;
      max-height: 92vh;
      border-radius: var(--radius-lg) var(--radius-lg) 0 0;
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-bottom: none;
      overflow-y: auto;
      -webkit-overflow-scrolling: touch;
      display: flex;
      flex-direction: column;
      box-shadow: var(--shadow-modal);
      transform: translateY(100%);
      transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    @media (min-width: 680px) {{
      .modal-backdrop {{
        align-items: center;
        padding: 1.5rem;
      }}
      .modal-sheet {{
        border-radius: var(--radius-lg);
        border-bottom: 1px solid rgba(255, 255, 255, 0.12);
        max-height: 88vh;
        transform: scale(0.95) translateY(20px);
      }}
      .modal-backdrop.open .modal-sheet {{
        transform: scale(1) translateY(0);
      }}
    }}
    .modal-backdrop.open .modal-sheet {{
      transform: translateY(0);
    }}

    /* MODAL HERO */
    .modal-hero {{
      position: relative;
      height: 240px;
      width: 100%;
      background: #0f172a;
    }}
    .modal-hero-img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center 45%;
    }}
    .modal-hero-gradient {{
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, rgba(9, 13, 22, 0.3) 0%, rgba(17, 24, 39, 0.95) 100%);
    }}

    .modal-close-btn {{
      position: absolute;
      top: 14px;
      right: 14px;
      width: 36px;
      height: 36px;
      border-radius: var(--radius-full);
      background: rgba(9, 13, 22, 0.8);
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 1.2rem;
      z-index: 10;
      transition: all 0.15s ease;
    }}
    .modal-close-btn:hover, .modal-close-btn:active {{
      background: rgba(255, 255, 255, 0.25);
    }}

    .modal-header-content {{
      position: absolute;
      bottom: 14px;
      left: 18px;
      right: 18px;
    }}
    .modal-badge-row {{
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 6px;
    }}
    .modal-title {{
      font-family: 'Cinzel', serif;
      font-size: 1.6rem;
      font-weight: 800;
      color: #ffffff;
      line-height: 1.15;
    }}
    .modal-subtitle {{
      color: var(--gold-light);
      font-size: 0.85rem;
      font-style: italic;
    }}

    /* MODAL BODY */
    .modal-content-area {{
      padding: 1.25rem 1.25rem 2.5rem;
    }}

    /* SPECS GRID */
    .modal-specs-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 8px;
      background: var(--bg-surface-elevated);
      border-radius: var(--radius-sm);
      padding: 10px;
      margin-bottom: 1.5rem;
      border: 1px solid var(--border-subtle);
    }}
    .modal-spec-cell {{
      text-align: center;
    }}
    .modal-spec-cell .lbl {{
      font-size: 0.65rem;
      text-transform: uppercase;
      font-weight: 700;
      color: var(--text-muted);
      margin-bottom: 2px;
    }}
    .modal-spec-cell .val {{
      font-size: 0.8rem;
      font-weight: 600;
      color: #ffffff;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    /* INGREDIENTES CHECKLIST */
    .modal-section-title {{
      font-size: 0.85rem;
      font-weight: 700;
      letter-spacing: 1.2px;
      text-transform: uppercase;
      color: var(--gold-light);
      margin-bottom: 0.75rem;
      display: flex;
      align-items: center;
      gap: 6px;
      border-bottom: 1px solid var(--border-subtle);
      padding-bottom: 4px;
    }}

    .checklist {{
      list-style: none;
      margin-bottom: 1.5rem;
    }}
    .checklist-item {{
      display: flex;
      align-items: flex-start;
      gap: 10px;
      padding: 7px 0;
      border-bottom: 1px solid rgba(255, 255, 255, 0.04);
      cursor: pointer;
      user-select: none;
    }}
    .checklist-item:last-child {{
      border-bottom: none;
    }}
    .checklist-item input[type="checkbox"] {{
      appearance: none;
      -webkit-appearance: none;
      width: 18px;
      height: 18px;
      border: 1.5px solid var(--border-gold);
      border-radius: 4px;
      outline: none;
      background: transparent;
      cursor: pointer;
      margin-top: 2px;
      flex-shrink: 0;
      display: grid;
      place-content: center;
      transition: all 0.15s ease;
    }}
    .checklist-item input[type="checkbox"]:checked {{
      background: var(--gold-primary);
      border-color: var(--gold-light);
    }}
    .checklist-item input[type="checkbox"]:checked::before {{
      content: "✓";
      color: #090d16;
      font-size: 12px;
      font-weight: 900;
    }}
    .checklist-item.checked span {{
      text-decoration: line-through;
      color: var(--text-muted);
    }}
    .checklist-text {{
      font-size: 0.92rem;
      color: var(--text-soft);
      line-height: 1.4;
    }}

    /* PASOS PASO A PASO */
    .steps-list {{
      list-style: none;
      counter-reset: step-counter;
      margin-bottom: 1.5rem;
    }}
    .step-item {{
      counter-increment: step-counter;
      display: flex;
      gap: 12px;
      margin-bottom: 12px;
    }}
    .step-num {{
      width: 26px;
      height: 26px;
      background: rgba(245, 158, 11, 0.15);
      border: 1px solid var(--border-gold);
      color: var(--gold-light);
      border-radius: var(--radius-full);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.8rem;
      font-weight: 700;
      flex-shrink: 0;
      margin-top: 2px;
    }}
    .step-desc {{
      font-size: 0.92rem;
      color: var(--text-soft);
      line-height: 1.45;
    }}

    /* CONSEJO DEL BARTENDER */
    .bartender-box {{
      background: linear-gradient(135deg, rgba(245, 158, 11, 0.1) 0%, rgba(217, 119, 6, 0.05) 100%);
      border: 1px solid var(--border-gold);
      border-radius: var(--radius-sm);
      padding: 12px 14px;
      margin-bottom: 1.5rem;
    }}
    .bartender-title {{
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: var(--gold-light);
      margin-bottom: 4px;
      display: flex;
      align-items: center;
      gap: 5px;
    }}
    .bartender-text {{
      font-size: 0.85rem;
      color: #fde68a;
      font-style: italic;
      line-height: 1.4;
    }}

    /* MODAL SHARE / ACTION */
    .modal-footer-actions {{
      display: flex;
      gap: 10px;
      padding-top: 0.5rem;
    }}

    /* INFO MODAL (GUÍA BÁSICA) */
    .guide-modal-body {{
      padding: 1.5rem;
    }}
    .guide-box {{
      background: var(--bg-surface-elevated);
      border-radius: var(--radius-sm);
      padding: 12px;
      margin-bottom: 12px;
      border: 1px solid var(--border-subtle);
    }}
    .guide-box strong {{
      color: var(--gold-light);
      display: block;
      margin-bottom: 4px;
      font-size: 0.9rem;
    }}
    .guide-box p {{
      font-size: 0.85rem;
      color: var(--text-soft);
      line-height: 1.4;
    }}

    /* FLOATING ACTION / SCROLL TO TOP */
    .btn-top {{
      position: fixed;
      bottom: 20px;
      right: 20px;
      width: 44px;
      height: 44px;
      border-radius: var(--radius-full);
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-gold);
      color: var(--gold-light);
      display: none;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      box-shadow: 0 4px 15px rgba(0,0,0,0.5);
      z-index: 30;
      transition: all 0.2s ease;
    }}
    .btn-top:active {{
      transform: scale(0.9);
    }}
  </style>
</head>
<body>

  <!-- HERO SECTION -->
  <header class="hero">
    <div class="hero-badge">Colección de Barra & Coctelería</div>
    <h1 class="hero-title">50 Cócteles Explicados Paso a Paso</h1>
    <p class="hero-subtitle">
      Guía visual interactiva de bolsillo: clásicos legendarios, iconos de la barra española y combinados contemporáneos con medidas exactas y trucos profesionales.
    </p>

    <div class="hero-actions">
      <a href="50_cocteles_explicados_paso_a_paso.pdf" class="btn btn-gold" download>
        <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 15V3m0 12l-4-4m4 4l4-4M2 17l.621 2.485A2 2 0 0 0 4.561 21h14.878a2 2 0 0 0 1.94-1.515L22 17"></path></svg>
        Descargar Libro PDF (55 Páginas)
      </a>
      <button class="btn btn-glass" onclick="openGuideModal()">
        <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><path d="M12 16v-4m0-4h.01"></path></svg>
        Técnicas y Cristal
      </button>
    </div>
  </header>

  <!-- CONTROLES ADHERENTES (STICKY SEARCH & FILTERS) -->
  <div class="sticky-controls">
    <div class="controls-inner">
      <!-- BUSCADOR -->
      <div class="search-box">
        <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
        <input type="text" id="searchInput" class="search-input" placeholder="Buscar por nombre, ingrediente (tequila, ron, limón...)" autocomplete="off">
        <button id="searchClear" class="search-clear" onclick="clearSearch()">&times;</button>
      </div>

      <!-- FILTROS POR CATEGORÍA -->
      <div class="chips-scroller" id="categoryChips">
        <button class="chip active" data-filter="all">Todos (50)</button>
        <button class="chip" data-filter="spanish">🇪🇸 Españoles (10)</button>
        <button class="chip" data-filter="sin-alcohol">🌿 Sin alcohol</button>
        <button class="chip" data-filter="Aperitivos & Spritz">Aperitivos</button>
        <button class="chip" data-filter="Cítricos & Sours">Sours</button>
        <button class="chip" data-filter="Cava & Brunch">Cava & Brunch</button>
        <button class="chip" data-filter="Tragos Largos & Tropicales">Tropicales</button>
        <button class="chip" data-filter="Clásicos & Sobremesa">Clásicos</button>
      </div>

      <!-- FILTROS POR DESTILADO BASE -->
      <div class="chips-scroller" id="spiritChips">
        <button class="chip active" data-spirit="all">Cualquier base</button>
        <button class="chip" data-spirit="ginebra">Ginebra</button>
        <button class="chip" data-spirit="ron">Ron</button>
        <button class="chip" data-spirit="vodka">Vodka</button>
        <button class="chip" data-spirit="tequila">Tequila</button>
        <button class="chip" data-spirit="whisky">Whisky</button>
        <button class="chip" data-spirit="vermut-vinos">Vermut & Vino</button>
      </div>
    </div>
  </div>

  <!-- BARRA DE RESULTADOS -->
  <div class="stats-bar">
    <span id="resultsCount">Mostrando 50 recetas</span>
    <span>Toca cualquier cóctel para ver la receta</span>
  </div>

  <!-- CONTENEDOR DE CÓCTELES -->
  <main class="cocktails-container">
    <div class="cocktails-grid" id="cocktailsGrid">
      <!-- Se inyecta dinámicamente con JavaScript -->
    </div>

    <!-- MENSAJE SIN RESULTADOS -->
    <div class="no-results" id="noResults">
      <h3>No se encontraron cócteles</h3>
      <p>Prueba con otro ingrediente, nombre o limpia los filtros.</p>
      <button class="btn btn-gold" style="margin-top:1rem;" onclick="resetAllFilters()">Mostrar todos los cócteles</button>
    </div>
  </main>

  <!-- BOTÓN VOLVER ARRIBA -->
  <button class="btn-top" id="btnTop" onclick="window.scrollTo({{top:0, behavior:'smooth'}})">
    <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M5 15l7-7 7 7"></path></svg>
  </button>

  <!-- MODAL / BOTTOM SHEET DE RECETA DETALLADA -->
  <div class="modal-backdrop" id="recipeModal" onclick="closeRecipeModal(event)">
    <div class="modal-sheet" id="modalSheet" onclick="event.stopPropagation()">
      <div class="modal-hero">
        <img id="mImg" class="modal-hero-img" src="" alt="">
        <div class="modal-hero-gradient"></div>
        <button class="modal-close-btn" onclick="closeRecipeModal()">&times;</button>
        
        <div class="modal-header-content">
          <div class="modal-badge-row">
            <span id="mNum" class="card-num">#00</span>
            <span id="mBadge" class="card-badge">CLÁSICO</span>
          </div>
          <h2 id="mTitle" class="modal-title">Nombre del Cóctel</h2>
          <div id="mSubtitle" class="modal-subtitle">Perfil de sabor</div>
        </div>
      </div>

      <div class="modal-content-area">
        <!-- SPECS BAR -->
        <div class="modal-specs-grid">
          <div class="modal-spec-cell">
            <div class="lbl">Copa</div>
            <div class="val" id="mGlass">-</div>
          </div>
          <div class="modal-spec-cell">
            <div class="lbl">Método</div>
            <div class="val" id="mMethod">-</div>
          </div>
          <div class="modal-spec-cell">
            <div class="lbl">Hielo</div>
            <div class="val" id="mIce">-</div>
          </div>
          <div class="modal-spec-cell">
            <div class="lbl">Tiempo</div>
            <div class="val" id="mTime">-</div>
          </div>
        </div>

        <!-- INGREDIENTES CON CHECKBOXES -->
        <div class="modal-section-title">
          <span>Ingredientes exactos</span>
          <span style="font-size:0.7rem; font-weight:normal; color:var(--text-muted); text-transform:none;">(marca según añadas)</span>
        </div>
        <ul class="checklist" id="mIngredients">
          <!-- Dinámico -->
        </ul>

        <!-- PASOS NUMERADOS -->
        <div class="modal-section-title">Preparación paso a paso</div>
        <ol class="steps-list" id="mSteps">
          <!-- Dinámico -->
        </ol>

        <!-- CONSEJO DEL BARTENDER -->
        <div class="bartender-box">
          <div class="bartender-title">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg>
            Consejo del bartender
          </div>
          <div class="bartender-text" id="mTip">-</div>
        </div>

        <!-- ACCIONES COMPARTIR / CERRAR -->
        <div class="modal-footer-actions">
          <button class="btn btn-gold" style="flex:1;" onclick="shareCocktail()">
            <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8m-4-6l-4-4-4 4m4-4v13"></path></svg>
            Compartir receta
          </button>
          <button class="btn btn-glass" onclick="closeRecipeModal()">Cerrar</button>
        </div>
      </div>
    </div>
  </div>

  <!-- MODAL DE GUÍA Y TÉCNICAS BÁSICAS -->
  <div class="modal-backdrop" id="guideModal" onclick="closeGuideModal(event)">
    <div class="modal-sheet" style="max-width: 600px;" onclick="event.stopPropagation()">
      <div style="padding: 1.5rem 1.5rem 0.5rem; display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--border-subtle);">
        <h3 style="font-family:'Cinzel',serif; font-size:1.3rem; color:#ffffff;">Guía Básica del Bartender</h3>
        <button class="modal-close-btn" style="position:static;" onclick="closeGuideModal()">&times;</button>
      </div>
      <div class="guide-modal-body">
        <div class="guide-box">
          <strong>1. El Hielo no es un adorno</strong>
          <p>Usa siempre hielo abundante, limpio y macizo. Cuanto más hielo tenga la copa, menor será la dilución indeseada y más frío y equilibrado se mantendrá el trago.</p>
        </div>
        <div class="guide-box">
          <strong>2. Agitado en coctelera (Shake)</strong>
          <p>Imprescindible para cócteles con zumos cítricos, siropes o cremas (Margarita, Daiquiri, Pisco sour). Emulsiona los ingredientes y aporta microburbujas sedosas.</p>
        </div>
        <div class="guide-box">
          <strong>3. Refrescado en vaso mezclador (Stir)</strong>
          <p>Para bebidas de alcoholes puros y vermuts (Negroni, Manhattan, Dry Martini). Remueve con cuchara imperial durante 25-30 segundos para enfriar sin enturbiar el líquido.</p>
        </div>
        <div class="guide-box">
          <strong>4. Construido directo en copa (Build)</strong>
          <p>Para tragos efervescentes y combinados (Gin-tonic, Aperol spritz, Mojito). Preserva la fuerza del carbónico con removidos muy suaves.</p>
        </div>
      </div>
    </div>
  </div>

  <!-- DATA & SCRIPTS -->
  <script>
    const COCKTAILS_DATA = {cocktails_json_str};

    let activeFilter = 'all';
    let activeSpirit = 'all';
    let searchQuery = '';
    let currentCocktail = null;

    const grid = document.getElementById('cocktailsGrid');
    const resultsCount = document.getElementById('resultsCount');
    const noResults = document.getElementById('noResults');
    const searchInput = document.getElementById('searchInput');
    const searchClear = document.getElementById('searchClear');
    const btnTop = document.getElementById('btnTop');
    const recipeModal = document.getElementById('recipeModal');
    const guideModal = document.getElementById('guideModal');

    // INICIALIZACIÓN
    function init() {{
      renderCards();
      setupEventListeners();
      checkUrlHash();
    }}

    // RENDERIZADO DE TARJETAS
    function renderCards() {{
      const filtered = COCKTAILS_DATA.filter(c => {{
        // Filtro por categoría / sección
        if (activeFilter === 'spanish' && !c.is_spanish) return false;
        if (activeFilter === 'sin-alcohol' && !c.sin_alcohol) return false;
        if (activeFilter !== 'all' && activeFilter !== 'spanish' && activeFilter !== 'sin-alcohol' && c.section !== activeFilter) return false;

        // Filtro por destilado
        if (activeSpirit !== 'all' && c.liquor_group !== activeSpirit) return false;

        // Búsqueda por texto
        if (searchQuery.trim() !== '') {{
          const q = searchQuery.toLowerCase().trim();
          const matchName = c.nombre.toLowerCase().includes(q);
          const matchBase = c.base_alcohol.toLowerCase().includes(q);
          const matchTaste = (c.perfil_sabor || '').toLowerCase().includes(q);
          const matchGlass = (c.cristaleria || '').toLowerCase().includes(q);
          const matchIng = c.ingredientes.some(i => i.toLowerCase().includes(q));
          if (!matchName && !matchBase && !matchTaste && !matchGlass && !matchIng) return false;
        }}

        return true;
      }});

      grid.innerHTML = '';

      if (filtered.length === 0) {{
        noResults.style.display = 'block';
        resultsCount.textContent = '0 recetas encontradas';
        return;
      }}

      noResults.style.display = 'none';
      resultsCount.textContent = `Mostrando ${{filtered.length}} de 50 recetas`;

      filtered.forEach(c => {{
        const card = document.createElement('div');
        card.className = 'card';
        card.onclick = () => openCocktail(c.num);

        let badgeClass = 'card-badge';
        let badgeText = c.section;
        if (c.sin_alcohol) {{
          badgeClass += ' badge-mocktail';
          badgeText = '🌿 Sin alcohol';
        }} else if (c.is_spanish) {{
          badgeClass += ' badge-spanish';
          badgeText = '🇪🇸 Ibérico';
        }}

        card.innerHTML = `
          <div class="card-img-wrap">
            <span class="card-num">#${{String(c.num).padStart(2, '0')}}</span>
            <span class="${{badgeClass}}">${{badgeText}}</span>
            <img class="card-img" src="${{c.image_url}}" alt="${{c.nombre}}" loading="lazy">
          </div>
          <div class="card-body">
            <div class="card-header">
              <div class="card-category">${{c.base_alcohol}}</div>
              <h3 class="card-title">${{c.nombre}}</h3>
            </div>
            <div class="card-taste">${{c.perfil_sabor || ''}}</div>
            <div class="card-specs">
              <div class="card-spec-item">
                <span class="card-spec-label">Copa</span>
                <span class="card-spec-val">${{c.cristaleria}}</span>
              </div>
              <div class="card-spec-item">
                <span class="card-spec-label">Método</span>
                <span class="card-spec-val">${{c.metodo}}</span>
              </div>
            </div>
            <div class="card-footer">
              <span>${{c.ingredientes.length}} ingredientes</span>
              <span>Ver receta &rarr;</span>
            </div>
          </div>
        `;
        grid.appendChild(card);
      }});
    }}

    // MODAL DE CÓCTEL
    function openCocktail(num) {{
      const c = COCKTAILS_DATA.find(item => item.num === num);
      if (!c) return;
      currentCocktail = c;

      // Actualizar hash en la barra de navegación para compartir enlaces
      history.replaceState(null, null, `#${{c.key}}`);

      document.getElementById('mImg').src = c.image_url;
      document.getElementById('mNum').textContent = `#${{String(c.num).padStart(2, '0')}}`;
      
      const badge = document.getElementById('mBadge');
      badge.textContent = c.sin_alcohol ? '🌿 Sin alcohol' : (c.is_spanish ? '🇪🇸 Ibérico' : c.section);
      badge.className = 'card-badge' + (c.sin_alcohol ? ' badge-mocktail' : (c.is_spanish ? ' badge-spanish' : ''));

      document.getElementById('mTitle').textContent = c.nombre;
      document.getElementById('mSubtitle').textContent = `${{c.base_alcohol}} · ${{c.perfil_sabor || ''}}`;
      document.getElementById('mGlass').textContent = c.cristaleria;
      document.getElementById('mMethod').textContent = c.metodo;
      document.getElementById('mIce').textContent = c.hielo;
      document.getElementById('mTime').textContent = c.tiempo_min;

      // Ingredientes
      const ingList = document.getElementById('mIngredients');
      ingList.innerHTML = '';
      c.ingredientes.forEach((ing, idx) => {{
        const li = document.createElement('li');
        li.className = 'checklist-item';
        li.innerHTML = `
          <input type="checkbox" id="ing_${{idx}}">
          <span class="checklist-text">${{ing}}</span>
        `;
        li.onclick = (e) => {{
          if (e.target.tagName !== 'INPUT') {{
            const chk = li.querySelector('input');
            chk.checked = !chk.checked;
          }}
          li.classList.toggle('checked', li.querySelector('input').checked);
        }};
        ingList.appendChild(li);
      }});

      // Pasos
      const stepsList = document.getElementById('mSteps');
      stepsList.innerHTML = '';
      c.preparacion.forEach((step, idx) => {{
        const li = document.createElement('li');
        li.className = 'step-item';
        li.innerHTML = `
          <div class="step-num">${{idx + 1}}</div>
          <div class="step-desc">${{step}}</div>
        `;
        stepsList.appendChild(li);
      }});

      // Consejo
      document.getElementById('mTip').textContent = c.consejo_bartender || 'Medir con precisión en mililitros garantiza el equilibrio.';

      recipeModal.style.display = 'flex';
      setTimeout(() => recipeModal.classList.add('open'), 10);
      document.body.style.overflow = 'hidden';
    }}

    function closeRecipeModal(e) {{
      if (e && e.target !== recipeModal && !e.target.classList.contains('modal-close-btn') && !e.target.classList.contains('btn-glass')) return;
      recipeModal.classList.remove('open');
      setTimeout(() => {{
        recipeModal.style.display = 'none';
        document.body.style.overflow = '';
      }}, 250);
      history.replaceState(null, null, ' ');
    }}

    // MODAL DE GUÍA
    function openGuideModal() {{
      guideModal.style.display = 'flex';
      setTimeout(() => guideModal.classList.add('open'), 10);
      document.body.style.overflow = 'hidden';
    }}
    function closeGuideModal(e) {{
      guideModal.classList.remove('open');
      setTimeout(() => {{
        guideModal.style.display = 'none';
        document.body.style.overflow = '';
      }}, 250);
    }}

    // COMPARTIR
    function shareCocktail() {{
      if (!currentCocktail) return;
      const shareData = {{
        title: `${{currentCocktail.nombre}} | 50 Cócteles`,
        text: `Aprende a preparar ${{currentCocktail.nombre}} paso a paso: ${{currentCocktail.ingredientes.join(', ')}}`,
        url: window.location.href
      }};
      if (navigator.share) {{
        navigator.share(shareData).catch(() => {{}});
      }} else {{
        navigator.clipboard.writeText(window.location.href);
        alert('¡Enlace de la receta copiado al portapapeles!');
      }}
    }}

    // LISTENERS & EVENTOS
    function setupEventListeners() {{
      // Búsqueda
      searchInput.addEventListener('input', (e) => {{
        searchQuery = e.target.value;
        searchClear.style.display = searchQuery ? 'block' : 'none';
        renderCards();
      }});

      // Filtros de categoría
      document.querySelectorAll('#categoryChips .chip').forEach(btn => {{
        btn.addEventListener('click', () => {{
          document.querySelectorAll('#categoryChips .chip').forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          activeFilter = btn.dataset.filter;
          renderCards();
        }});
      }});

      // Filtros de destilado
      document.querySelectorAll('#spiritChips .chip').forEach(btn => {{
        btn.addEventListener('click', () => {{
          document.querySelectorAll('#spiritChips .chip').forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          activeSpirit = btn.dataset.spirit;
          renderCards();
        }});
      }});

      // Scroll top button
      window.addEventListener('scroll', () => {{
        if (window.scrollY > 300) {{
          btnTop.style.display = 'flex';
        }} else {{
          btnTop.style.display = 'none';
        }}
      }});

      // Tecla Escape para cerrar modales
      window.addEventListener('keydown', (e) => {{
        if (e.key === 'Escape') {{
          closeRecipeModal();
          closeGuideModal();
        }}
      }});
    }}

    function clearSearch() {{
      searchInput.value = '';
      searchQuery = '';
      searchClear.style.display = 'none';
      renderCards();
    }}

    function resetAllFilters() {{
      clearSearch();
      activeFilter = 'all';
      activeSpirit = 'all';
      document.querySelectorAll('#categoryChips .chip').forEach(b => b.classList.toggle('active', b.dataset.filter === 'all'));
      document.querySelectorAll('#spiritChips .chip').forEach(b => b.classList.toggle('active', b.dataset.spirit === 'all'));
      renderCards();
    }}

    function checkUrlHash() {{
      const hash = window.location.hash.replace('#', '').trim();
      if (!hash) return;
      const found = COCKTAILS_DATA.find(c => c.key === hash || String(c.num) === hash);
      if (found) {{
        openCocktail(found.num);
      }}
    }}

    // INICIAR
    init();
  </script>
</body>
</html>
"""
    return html

def main():
    print("Generando index.html para la aplicación Web Móvil...")
    html_content = build_web_app()
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"¡index.html generado exitosamente! ({len(html_content):,} bytes)")

if __name__ == "__main__":
    main()
