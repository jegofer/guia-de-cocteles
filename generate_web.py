# -*- coding: utf-8 -*-
"""
Generador de la aplicación Web Móvil Interactiva (Single Page Application):
'51 CÓCTELES EXPLICADOS PASO A PASO'
Optimizada para GitHub Pages, dispositivos móviles y pantallas táctiles.
Incluye sistema de favoritos con persistencia en localStorage/cookies.
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
    45: "Tragos Largos & Tropicales", 50: "Tragos Largos & Tropicales", 51: "Tragos Largos & Tropicales",
    
    # V. Grandes Clásicos & Sobremesas
    13: "Clásicos & Sobremesa", 18: "Clásicos & Sobremesa", 20: "Clásicos & Sobremesa",
    21: "Clásicos & Sobremesa", 26: "Clásicos & Sobremesa", 33: "Clásicos & Sobremesa",
    35: "Clásicos & Sobremesa", 36: "Clásicos & Sobremesa", 46: "Clásicos & Sobremesa",
    48: "Clásicos & Sobremesa", 49: "Clásicos & Sobremesa"
}

# Iconos representativos de la tradición ibérica
SPANISH_COCKTAILS = {1, 3, 4, 6, 7, 11, 24, 26, 33, 46, 51}

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
    total_cocktails = len(data_for_json)
    spanish_count = sum(1 for c in data_for_json if c["is_spanish"])

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, viewport-fit=cover">
  <meta name="theme-color" content="#090d16">
  <meta name="description" content="Guía interactiva para móvil de {total_cocktails} cócteles explicados paso a paso con medidas exactas, fotos de alta resolución, trucos de bartender y favoritos.">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <title>{total_cocktails} Cócteles explicados paso a paso | Guía Web Móvil</title>
  
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
      user-select: none;
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

    .chip-fav {{
      background: rgba(245, 158, 11, 0.08);
      border-color: rgba(245, 158, 11, 0.3);
      color: var(--gold-light);
    }}
    .chip-fav:hover {{
      background: rgba(245, 158, 11, 0.18);
      color: #ffffff;
    }}
    .chip-fav.active {{
      background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
      color: #090d16;
      border-color: #fbbf24;
      font-weight: 700;
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
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 1.25rem;
    }}

    @media (max-width: 640px) {{
      .cocktails-grid {{
        grid-template-columns: 1fr;
        gap: 1rem;
      }}
    }}

    /* TARJETA DE CÓCTEL */
    .card {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      overflow: hidden;
      box-shadow: var(--shadow-card);
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      cursor: pointer;
      display: flex;
      flex-direction: column;
      position: relative;
    }}

    .card:hover {{
      transform: translateY(-4px);
      border-color: var(--border-gold);
      box-shadow: 0 12px 30px -5px rgba(0, 0, 0, 0.6), 0 0 20px var(--gold-glow);
    }}

    .card-img-wrap {{
      position: relative;
      width: 100%;
      height: 190px;
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
      -webkit-backdrop-filter: blur(6px);
      color: var(--gold-light);
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.75rem;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: var(--radius-sm);
      z-index: 2;
    }}

    .card-fav-btn {{
      position: absolute;
      top: 10px;
      right: 10px;
      width: 34px;
      height: 34px;
      border-radius: var(--radius-full);
      background: rgba(9, 13, 22, 0.85);
      backdrop-filter: blur(6px);
      -webkit-backdrop-filter: blur(6px);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #94a3b8;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      z-index: 5;
      transition: all 0.2s ease;
      padding: 0;
    }}
    .card-fav-btn:hover {{
      transform: scale(1.15);
      border-color: var(--gold-light);
      color: var(--gold-light);
    }}
    .card-fav-btn.active {{
      background: rgba(245, 158, 11, 0.25);
      border-color: var(--gold-primary);
      color: var(--gold-light);
      box-shadow: 0 0 10px var(--gold-glow);
    }}

    .card-badge {{
      position: absolute;
      bottom: 10px;
      left: 10px;
      background: rgba(9, 13, 22, 0.88);
      backdrop-filter: blur(6px);
      -webkit-backdrop-filter: blur(6px);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #ffffff;
      font-size: 0.7rem;
      font-weight: 700;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      padding: 3px 8px;
      border-radius: var(--radius-full);
      z-index: 2;
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
      margin-bottom: 0.5rem;
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
      min-width: 0;
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
      background: rgba(0, 0, 0, 0.82);
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
      transform: translateY(100%);
      transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .modal-backdrop.open .modal-sheet {{
      transform: translateY(0);
    }}

    /* MODAL HERO (SOLO IMAGEN Y BOTONES FLOTANTES DE ACCIÓN) */
    .modal-hero {{
      position: relative;
      height: 220px;
      width: 100%;
      background: #0f172a;
      flex-shrink: 0;
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
      background: linear-gradient(180deg, rgba(9, 13, 22, 0.4) 0%, rgba(9, 13, 22, 0.05) 50%, rgba(17, 24, 39, 1) 100%);
    }}

    .modal-hero-bar {{
      position: absolute;
      top: 14px;
      left: 14px;
      right: 14px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      z-index: 10;
    }}

    .modal-icon-btn {{
      width: 38px;
      height: 38px;
      border-radius: var(--radius-full);
      background: rgba(9, 13, 22, 0.85);
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 1.2rem;
      transition: all 0.18s ease;
      padding: 0;
    }}
    .modal-icon-btn:hover, .modal-icon-btn:active {{
      background: rgba(255, 255, 255, 0.25);
    }}
    .modal-icon-btn.active {{
      background: rgba(245, 158, 11, 0.25);
      border-color: var(--gold-primary);
      color: var(--gold-light);
      box-shadow: 0 0 12px var(--gold-glow);
    }}

    /* CABECERA DE LA FICHA EN FLUJO NATURAL (SIN SOLAPAMIENTO) */
    .modal-header-section {{
      padding: 1.1rem 1.25rem 0.4rem;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}
    .modal-badge-row {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }}
    .modal-pill-num {{
      background: rgba(245, 158, 11, 0.15);
      border: 1px solid var(--border-gold);
      color: var(--gold-light);
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.78rem;
      font-weight: 700;
      padding: 3px 9px;
      border-radius: var(--radius-sm);
    }}
    .modal-pill-badge {{
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: var(--text-soft);
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      padding: 3px 10px;
      border-radius: var(--radius-full);
    }}
    .modal-pill-badge.badge-mocktail {{
      background: rgba(16, 185, 129, 0.2);
      border-color: #34d399;
      color: #6ee7b7;
    }}
    .modal-pill-badge.badge-spanish {{
      background: rgba(245, 158, 11, 0.2);
      border-color: var(--gold-light);
      color: var(--gold-light);
    }}

    .modal-title {{
      font-family: 'Cinzel', serif;
      font-size: clamp(1.4rem, 5vw, 1.85rem);
      font-weight: 800;
      color: #ffffff;
      line-height: 1.2;
      margin-top: 2px;
      word-break: break-word;
    }}
    .modal-subtitle {{
      color: var(--gold-light);
      font-size: 0.88rem;
      font-style: italic;
    }}

    /* CUERPO DEL MODAL */
    .modal-content-area {{
      padding: 0.75rem 1.25rem 2.5rem;
    }}

    /* SPECS GRID (COPA, MÉTODO Y HIELO - ADAPTADO A MÓVILES) */
    .modal-specs-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
      background: var(--bg-surface-elevated);
      border-radius: var(--radius-md);
      padding: 12px 10px;
      margin-bottom: 1.5rem;
      border: 1px solid var(--border-subtle);
    }}
    .modal-spec-cell {{
      text-align: center;
      padding: 0 4px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-width: 0;
    }}
    .modal-spec-cell:not(:last-child) {{
      border-right: 1px solid rgba(255, 255, 255, 0.08);
    }}
    .modal-spec-cell .lbl {{
      font-size: 0.68rem;
      text-transform: uppercase;
      font-weight: 700;
      letter-spacing: 0.8px;
      color: var(--text-muted);
      margin-bottom: 4px;
      display: flex;
      align-items: center;
      gap: 3px;
    }}
    .modal-spec-cell .val {{
      font-size: 0.82rem;
      font-weight: 600;
      color: #ffffff;
      line-height: 1.3;
      word-break: normal;
      white-space: normal;
      overflow-wrap: break-word;
      max-width: 100%;
    }}

    @media (max-width: 360px) {{
      .modal-specs-grid {{
        padding: 10px 6px;
        gap: 4px;
      }}
      .modal-spec-cell .val {{
        font-size: 0.76rem;
      }}
      .modal-spec-cell .lbl {{
        font-size: 0.62rem;
      }}
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

    /* PASOS DE PREPARACIÓN */
    .steps-list {{
      list-style: none;
      counter-reset: step-counter;
      margin-bottom: 1.5rem;
    }}
    .step-item {{
      display: flex;
      gap: 12px;
      margin-bottom: 0.9rem;
      align-items: flex-start;
    }}
    .step-num {{
      width: 24px;
      height: 24px;
      border-radius: var(--radius-full);
      background: rgba(245, 158, 11, 0.15);
      border: 1px solid var(--border-gold);
      color: var(--gold-light);
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.75rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      margin-top: 2px;
    }}
    .step-desc {{
      font-size: 0.92rem;
      color: var(--text-main);
      line-height: 1.45;
    }}

    /* TIP BARTENDER */
    .tip-box {{
      background: rgba(245, 158, 11, 0.08);
      border-left: 3px solid var(--gold-primary);
      border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
      padding: 12px 14px;
      margin-bottom: 1.5rem;
    }}
    .tip-title {{
      font-size: 0.75rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: var(--gold-light);
      margin-bottom: 4px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .tip-content {{
      font-size: 0.88rem;
      color: var(--text-soft);
      line-height: 1.4;
      font-style: italic;
    }}

    /* MODAL FOOTER */
    .modal-footer {{
      display: flex;
      gap: 10px;
      margin-top: 1rem;
    }}

    /* BOTÓN VOLVER ARRIBA */
    .btn-top {{
      position: fixed;
      bottom: 20px;
      right: 20px;
      width: 46px;
      height: 46px;
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
    .btn-top:hover, .btn-top:active {{
      background: var(--gold-primary);
      color: #090d16;
      transform: translateY(-2px);
    }}
  </style>
</head>
<body>

  <!-- CABECERA PRINCIPAL -->
  <header class="hero">
    <div class="hero-badge">
      <span>🍸</span> {total_cocktails} RECETAS DE COCTELERÍA ILUSTRADAS PASO A PASO
    </div>
    <h1 class="hero-title">{total_cocktails} CÓCTELES</h1>
    <p class="hero-subtitle">
      La guía visual definitiva para dominar la coctelería casera y profesional. Medidas exactas en mililitros, fotos en alta resolución, trucos de bartender y tus recetas favoritas guardadas en tu navegador.
    </p>

    <div class="hero-actions">
      <a href="50_cocteles_explicados_paso_a_paso.pdf" class="btn btn-gold" download>
        <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
        Descargar Libro PDF
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

      <!-- FILTROS POR CATEGORÍA & FAVORITOS -->
      <div class="chips-scroller" id="categoryChips">
        <button class="chip chip-fav" data-filter="favorites" id="favFilterChip">
          ⭐ Favoritos (<span id="favFilterCount">0</span>)
        </button>
        <button class="chip active" data-filter="all">Todos ({total_cocktails})</button>
        <button class="chip" data-filter="spanish">🇪🇸 Españoles ({spanish_count})</button>
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
    <span id="resultsCount">Mostrando {total_cocktails} recetas</span>
    <span>Toca la ⭐ para guardar en favoritos</span>
  </div>

  <!-- CONTENEDOR DE CÓCTELES -->
  <main class="cocktails-container">
    <div class="cocktails-grid" id="cocktailsGrid">
      <!-- Se inyecta dinámicamente con JavaScript -->
    </div>

    <!-- MENSAJE SIN RESULTADOS -->
    <div class="no-results" id="noResults">
      <h3 id="noResultsTitle">No se encontraron cócteles</h3>
      <p id="noResultsText">Prueba con otro ingrediente, nombre o limpia los filtros.</p>
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
        <div class="modal-hero-bar">
          <button class="modal-icon-btn" id="mHeroFavBtn" onclick="toggleCurrentFavorite(event)" title="Favorito" aria-label="Marcar como favorito">
            <svg class="star-icon" viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
          </button>
          <button class="modal-icon-btn modal-close-btn" onclick="closeRecipeModal()">&times;</button>
        </div>
      </div>

      <!-- CABECERA EN FLUJO LIMPIO (NUNCA TAPA EL TÍTULO) -->
      <div class="modal-header-section">
        <div class="modal-badge-row">
          <span id="mNum" class="modal-pill-num">#00</span>
          <span id="mBadge" class="modal-pill-badge">CLÁSICO</span>
        </div>
        <h2 id="mTitle" class="modal-title">Nombre del Cóctel</h2>
        <div id="mSubtitle" class="modal-subtitle">Perfil de sabor</div>
      </div>

      <div class="modal-content-area">
        <!-- SPECS BAR: COPA, MÉTODO Y HIELO (SIN TIEMPO) -->
        <div class="modal-specs-grid">
          <div class="modal-spec-cell">
            <div class="lbl">
              <svg width="13" height="13" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M8 21h8m-4-7v7m-7-18l7 9 7-9H5z"/></svg>
              Copa
            </div>
            <div class="val" id="mGlass">-</div>
          </div>
          <div class="modal-spec-cell">
            <div class="lbl">
              <svg width="13" height="13" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg>
              Método
            </div>
            <div class="val" id="mMethod">-</div>
          </div>
          <div class="modal-spec-cell">
            <div class="lbl">
              <svg width="13" height="13" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"/></svg>
              Hielo
            </div>
            <div class="val" id="mIce">-</div>
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
        <div class="tip-box">
          <div class="tip-title">
            <svg width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
            Consejo del Bartender
          </div>
          <div class="tip-content" id="mTip">Consejo profesional</div>
        </div>

        <!-- BOTONES DE ACCIÓN DEL MODAL -->
        <div class="modal-footer">
          <button class="btn btn-gold" style="flex:1;" onclick="shareCocktail()">
            <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.368 2.684 3 3 0 00-5.368-2.684z"></path></svg>
            Compartir receta
          </button>
          <button class="btn btn-glass" onclick="closeRecipeModal()">
            Cerrar
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- MODAL DE GUÍA TÉCNICA Y CRISTALERÍA -->
  <div class="modal-backdrop" id="guideModal" onclick="closeGuideModal(event)">
    <div class="modal-sheet" onclick="event.stopPropagation()">
      <div style="padding:1.5rem 1.25rem; border-bottom:1px solid var(--border-subtle); display:flex; justify-content:space-between; align-items:center;">
        <h2 style="font-family:'Cinzel', serif; font-size:1.3rem; color:#ffffff;">Guía Rápida de Barra</h2>
        <button class="modal-icon-btn modal-close-btn" onclick="closeGuideModal()">&times;</button>
      </div>
      <div style="padding:1.25rem 1.25rem 2.5rem; font-size:0.9rem; color:var(--text-soft); line-height:1.6;">
        <h3 style="color:var(--gold-light); margin-bottom:0.4rem; font-size:1rem;">1. La Regla de Oro del Hielo</h3>
        <p style="margin-bottom:1rem;">Usa siempre hielo abundante, limpio y macizo. Cuanto más hielo tenga la copa, menor será la dilución indeseada y más frío y equilibrado se mantendrá el trago.</p>

        <h3 style="color:var(--gold-light); margin-bottom:0.4rem; font-size:1rem;">2. Cristalería Esencial</h3>
        <ul style="list-style:disc; margin-left:1.2rem; margin-bottom:1rem;">
          <li><strong>Copa Coupette / Cocktail:</strong> Para tragos colados sin hielo (Margarita, Daiquiri, Cosmopolitan).</li>
          <li><strong>Vaso Bajo (Old Fashioned):</strong> Para destilados con hielo en roca o agitados cortos (Negroni, Whisky Sour).</li>
          <li><strong>Vaso Alto (Highball / Collins):</strong> Para combinados con carbónico y refresco (Mojito, Gin-tonic, Cuba libre).</li>
          <li><strong>Vaso de Sidra:</strong> Clásico de taberna para calimocho y tragos generosos de vino.</li>
        </ul>

        <h3 style="color:var(--gold-light); margin-bottom:0.4rem; font-size:1rem;">3. Equivalencia de Medidas</h3>
        <p style="margin-bottom:1rem;">
          • 1 oz líquida ≈ 30 ml<br>
          • 1 golpe (dash) ≈ 0,8 ml<br>
          • 1 cucharilla de bar (barspoon) ≈ 5 ml
        </p>

        <button class="btn btn-gold" style="width:100%;" onclick="closeGuideModal()">Entendido</button>
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

    // FAVORITOS CON DOBLE PERSISTENCIA (LOCALSTORAGE + COOKIE)
    let favorites = loadFavorites();

    function loadFavorites() {{
      try {{
        const raw = localStorage.getItem('cocteles_favoritos');
        if (raw) return new Set(JSON.parse(raw));
      }} catch (e) {{}}

      const match = document.cookie.match(/(?:^|;\\s*)cocteles_favoritos=([^;]+)/);
      if (match) {{
        try {{
          return new Set(JSON.parse(decodeURIComponent(match[1])));
        }} catch (e) {{}}
      }}
      return new Set();
    }}

    function persistFavorites(favSet) {{
      favorites = favSet;
      const arr = Array.from(favSet);
      const jsonStr = JSON.stringify(arr);

      try {{
        localStorage.setItem('cocteles_favoritos', jsonStr);
      }} catch (e) {{}}

      try {{
        const expires = new Date(Date.now() + 365*24*60*60*1000).toUTCString();
        document.cookie = `cocteles_favoritos=${{encodeURIComponent(jsonStr)}}; expires=${{expires}}; path=/; SameSite=Lax`;
      }} catch (e) {{}}

      updateFavoritesBadge();
    }}

    function toggleFavorite(key, event) {{
      if (event) event.stopPropagation();
      const next = new Set(favorites);
      if (next.has(key)) {{
        next.delete(key);
      }} else {{
        next.add(key);
      }}
      persistFavorites(next);
      renderCards();
      if (currentCocktail && currentCocktail.key === key) {{
        syncModalFavUI(next.has(key));
      }}
    }}

    function toggleCurrentFavorite(event) {{
      if (event) event.stopPropagation();
      if (!currentCocktail) return;
      toggleFavorite(currentCocktail.key);
    }}

    function syncModalFavUI(isFav) {{
      const heroBtn = document.getElementById('mHeroFavBtn');
      if (heroBtn) {{
        heroBtn.classList.toggle('active', isFav);
        heroBtn.innerHTML = `<svg class="star-icon" viewBox="0 0 24 24" width="20" height="20" fill="${{isFav ? '#f59e0b' : 'none'}}" stroke="${{isFav ? '#f59e0b' : '#ffffff'}}" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>`;
        heroBtn.title = isFav ? 'Quitar de favoritos' : 'Guardar en favoritos';
      }}
    }}

    function updateFavoritesBadge() {{
      const countEl = document.getElementById('favFilterCount');
      if (countEl) countEl.textContent = favorites.size;
    }}

    const grid = document.getElementById('cocktailsGrid');
    const resultsCount = document.getElementById('resultsCount');
    const noResults = document.getElementById('noResults');
    const noResultsTitle = document.getElementById('noResultsTitle');
    const noResultsText = document.getElementById('noResultsText');
    const searchInput = document.getElementById('searchInput');
    const searchClear = document.getElementById('searchClear');
    const btnTop = document.getElementById('btnTop');
    const recipeModal = document.getElementById('recipeModal');
    const guideModal = document.getElementById('guideModal');

    // INICIALIZACIÓN
    function init() {{
      updateFavoritesBadge();
      renderCards();
      setupEventListeners();
      checkUrlHash();
    }}

    // RENDERIZADO DE TARJETAS
    function renderCards() {{
      const filtered = COCKTAILS_DATA.filter(c => {{
        // Filtro por favoritos
        if (activeFilter === 'favorites') {{
          if (!favorites.has(c.key)) return false;
        }} else if (activeFilter === 'spanish' && !c.is_spanish) {{
          return false;
        }} else if (activeFilter === 'sin-alcohol' && !c.sin_alcohol) {{
          return false;
        }} else if (activeFilter !== 'all' && activeFilter !== 'favorites' && activeFilter !== 'spanish' && activeFilter !== 'sin-alcohol' && c.section !== activeFilter) {{
          return false;
        }}

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
        if (activeFilter === 'favorites') {{
          noResultsTitle.textContent = 'Aún no tienes cócteles favoritos';
          noResultsText.textContent = 'Toca el icono de la estrella ⭐ en cualquier cóctel para guardarlo aquí y consultarlo rápidamente.';
        }} else {{
          noResultsTitle.textContent = 'No se encontraron cócteles';
          noResultsText.textContent = 'Prueba con otro ingrediente, nombre o limpia los filtros.';
        }}
        resultsCount.textContent = '0 recetas encontradas';
        return;
      }}

      noResults.style.display = 'none';
      if (activeFilter === 'favorites') {{
        resultsCount.textContent = `Mostrando ${{filtered.length}} ${{filtered.length === 1 ? 'cóctel favorito' : 'cócteles favoritos'}}`;
      }} else {{
        resultsCount.textContent = `Mostrando ${{filtered.length}} de ${{COCKTAILS_DATA.length}} recetas`;
      }}

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

        const isFav = favorites.has(c.key);

        card.innerHTML = `
          <div class="card-img-wrap">
            <span class="card-num">#${{String(c.num).padStart(2, '0')}}</span>
            <button class="card-fav-btn ${{isFav ? 'active' : ''}}" onclick="toggleFavorite('${{c.key}}', event)" title="${{isFav ? 'Quitar de favoritos' : 'Guardar en favoritos'}}" aria-label="Favorito">
              <svg class="star-icon" viewBox="0 0 24 24" width="16" height="16" fill="${{isFav ? '#f59e0b' : 'none'}}" stroke="${{isFav ? '#f59e0b' : '#ffffff'}}" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
            </button>
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
      badge.className = 'modal-pill-badge' + (c.sin_alcohol ? ' badge-mocktail' : (c.is_spanish ? ' badge-spanish' : ''));

      document.getElementById('mTitle').textContent = c.nombre;
      document.getElementById('mSubtitle').textContent = `${{c.base_alcohol}} · ${{c.perfil_sabor || ''}}`;
      document.getElementById('mGlass').textContent = c.cristaleria;
      document.getElementById('mMethod').textContent = c.metodo;
      document.getElementById('mIce').textContent = c.hielo;

      // Sincronizar estado de favorito en el modal
      syncModalFavUI(favorites.has(c.key));

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
        title: `${{currentCocktail.nombre}} | ${{COCKTAILS_DATA.length}} Cócteles`,
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

      // Filtros de categoría & Favoritos
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
