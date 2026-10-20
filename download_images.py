import urllib.request
import urllib.parse
import json
import time
import os

os.makedirs('images', exist_ok=True)

cocktails_search = [
    (1, 'gin_tonic', 'Gin tonic cocktail glass', 'Gin and tonic on the rocks'),
    (2, 'mojito', 'Mojito cocktail mint lime', 'Mojito cocktail'),
    (3, 'sangria', 'Sangria cocktail glass', 'Sangria glass fruit'),
    (4, 'tinto_de_verano', 'Tinto de verano', 'Red wine spritzer glass'),
    (5, 'aperol_spritz', 'Aperol Spritz cocktail', 'Aperol spritz glass'),
    (6, 'agua_de_valencia', 'Agua de Valencia cocktail', 'Mimosa cocktail orange'),
    (7, 'rebujito', 'Rebujito cocktail', 'Manzanilla sherry glass'),
    (8, 'negroni', 'Negroni cocktail glass', 'Negroni orange slice'),
    (9, 'margarita', 'Margarita cocktail glass', 'Classic margarita lime'),
    (10, 'daiquiri', 'Classic Daiquiri cocktail', 'Daiquiri cocktail coupette'),
    (11, 'marianito', 'Vermouth cocktail olive', 'Vermut rojo con aceituna'),
    (12, 'pina_colada', 'Pina Colada cocktail', 'Piña colada pineapple glass'),
    (13, 'espresso_martini', 'Espresso martini cocktail', 'Espresso martini glass'),
    (14, 'moscow_mule', 'Moscow mule copper mug', 'Moscow mule cocktail'),
    (15, 'caipirinha', 'Caipirinha cocktail', 'Caipirinha lime cachaça'),
    (16, 'cuba_libre', 'Cuba libre cocktail', 'Rum and coke lime'),
    (17, 'tom_collins', 'Tom Collins cocktail', 'Gin collins cocktail lemon'),
    (18, 'dry_martini', 'Dry martini cocktail olive', 'Martini glass olive'),
    (19, 'paloma', 'Paloma cocktail grapefruit', 'Paloma tequila grapefruit'),
    (20, 'old_fashioned', 'Old Fashioned cocktail', 'Whiskey Old Fashioned glass'),
    (21, 'manhattan', 'Manhattan cocktail glass', 'Manhattan cherry cocktail'),
    (22, 'whisky_sour', 'Whiskey sour cocktail', 'Whiskey sour foam'),
    (23, 'cosmopolitan', 'Cosmopolitan cocktail glass', 'Cosmopolitan cranberry cocktail'),
    (24, 'san_francisco', 'Fruit mocktail glass', 'Tropical mocktail cocktail'),
    (25, 'bloody_mary', 'Bloody Mary cocktail', 'Bloody Mary celery glass'),
    (26, 'cremaet', 'Carajillo cremaet coffee', 'Cremaet carajillo'),
    (27, 'americano', 'Americano cocktail campari', 'Americano campari vermouth'),
    (28, 'pisco_sour', 'Pisco sour', 'Pisco sour cocktail glass'),
    (29, 'bellini', 'Bellini cocktail peach', 'Bellini prosecco peach'),
    (30, 'mimosa', 'Mimosa cocktail orange', 'Mimosa champagne flute'),
    (31, 'tequila_sunrise', 'Tequila sunrise cocktail', 'Tequila sunrise grenadine'),
    (32, 'sex_on_the_beach', 'Sex on the beach cocktail', 'Sex on the beach drink'),
    (33, 'lumumba', 'Lumumba cocktail brandy', 'Chocolate liqueur cocktail'),
    (34, 'gimlet', 'Gimlet cocktail lime', 'Gimlet gin lime'),
    (35, 'black_russian', 'Black Russian cocktail', 'Black Russian vodka kahlua'),
    (36, 'white_russian', 'White Russian cocktail', 'White Russian cream cocktail'),
    (37, 'french_75', 'French 75 cocktail', 'French 75 champagne cocktail'),
    (38, 'dark_and_stormy', 'Dark and stormy cocktail', 'Dark and stormy ginger beer'),
    (39, 'caipiroska', 'Caipiroska cocktail', 'Vodka caipiroska lime'),
    (40, 'amaretto_sour', 'Amaretto sour cocktail', 'Amaretto sour lemon'),
    (41, 'bramble', 'Bramble cocktail', 'Bramble gin blackberry'),
    (42, 'mai_tai', 'Mai Tai', 'Mai Tai tiki cocktail'),
    (43, 'sea_breeze', 'Sea breeze cocktail', 'Sea breeze cranberry vodka'),
    (44, 'kir_royale', 'Kir Royale cocktail', 'Kir Royale cassis champagne'),
    (45, 'mint_julep', 'Mint julep cocktail', 'Mint julep bourbon cup'),
    (46, 'sol_y_sombra', 'Brandy glass snifter', 'Brandy snifter glass'),
    (47, 'sidecar', 'Sidecar cocktail glass', 'Sidecar cognac orange'),
    (48, 'irish_coffee', 'Irish coffee glass', 'Irish coffee whipped cream'),
    (49, 'padrino', 'Whiskey on the rocks', 'Godfather cocktail amaretto'),
    (50, 'laguna_azul', 'Blue lagoon cocktail glass', 'Blue curacao cocktail glass')
]

def search_url(query):
    url = f'https://commons.wikimedia.org/w/api.php?action=query&format=json&generator=search&gsrsearch={urllib.parse.quote(query)}&gsrnamespace=6&gsrlimit=5&prop=imageinfo&iiprop=url|size&iiurlwidth=800'
    req = urllib.request.Request(url, headers={'User-Agent': 'CocktailBookBuilder/2.0 (contact@editorial-gastronomica.org)'})
    try:
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            for pid, pdata in pages.items():
                title = pdata.get('title', '').lower()
                if any(ext in title for ext in ['.jpg', '.jpeg', '.png']):
                    return pdata['imageinfo'][0].get('thumburl') or pdata['imageinfo'][0].get('url')
    except Exception as e:
        pass
    return None

def download_file(url, target_path):
    req = urllib.request.Request(url, headers={'User-Agent': 'CocktailBookBuilder/2.0 (contact@editorial-gastronomica.org)'})
    with urllib.request.urlopen(req, timeout=12) as resp:
        content = resp.read()
        with open(target_path, 'wb') as f:
            f.write(content)

for num, key, q1, q2 in cocktails_search:
    target_file = f'images/{num:02d}_{key}.jpg'
    if os.path.exists(target_file) and os.path.getsize(target_file) > 1000:
        print(f'[{num:02d}/50] Already exists: {target_file}')
        continue
    
    img_url = search_url(q1)
    if not img_url:
        img_url = search_url(q2)
    
    if img_url:
        try:
            download_file(img_url, target_file)
            size = os.path.getsize(target_file)
            print(f'[{num:02d}/50] Downloaded {key}: {size} bytes')
        except Exception as e:
            print(f'[{num:02d}/50] Failed download {key}: {e}')
    else:
        print(f'[{num:02d}/50] Could not find image for {key}')
    time.sleep(0.2)

print('Finished downloading images!')
