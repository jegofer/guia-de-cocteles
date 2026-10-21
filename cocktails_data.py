# -*- coding: utf-8 -*-
"""
Base de datos exhaustiva y profesional de los 50 cócteles explicados paso a paso.
"""

COCKTAILS = [
    {
        "num": 1,
        "key": "gin_tonic",
        "nombre": "Gin-tonic",
        "sin_alcohol": False,
        "base_alcohol": "Ginebra",
        "metodo": "Construido en copa",
        "cristaleria": "Copa balón",
        "tiempo_min": 3,
        "perfil_sabor": "Cítrico, botánico y refrescante",
        "hielo": "Cubos macizos de gran tamaño",
        "ingredientes": [
            "50 ml de ginebra (estilo London Dry o botánica)",
            "200 ml de tónica neutra o premium muy fría",
            "1 espiral (twist) de piel de lima o limón",
            "Hielo abundante de cubos gruesos"
        ],
        "preparacion": [
            "Llena la copa balón hasta arriba con cubos de hielo macizo y remueve suavemente con la cuchara imperial para enfriar el cristal. Desecha el agua residual.",
            "Vierte con precisión los 50 ml de ginebra sobre el hielo para que se oxigene y atempere.",
            "Añade la tónica vertiéndola lentamente y muy pegada al hielo (o deslizándola por la espiral de la cuchara) para conservar la máxima efervescencia de la burbuja.",
            "Remueve una sola vez de abajo hacia arriba con delicadeza.",
            "Frota la piel del cítrico por el borde de la copa para liberar sus aceites esenciales y deposítala dentro."
        ],
        "consejo_bartender": "La clave del gin-tonic perfecto no es el adorno, sino la temperatura y el hielo: jamás machaques la fruta dentro ni uses tónica a temperatura ambiente, pues desgasifica la copa al instante."
    },
    {
        "num": 2,
        "key": "mojito",
        "nombre": "Mojito",
        "sin_alcohol": False,
        "base_alcohol": "Ron blanco",
        "metodo": "Macerado y construido",
        "cristaleria": "Vaso alto (collins / highball)",
        "tiempo_min": 5,
        "perfil_sabor": "Dulce, herbal y cítrico",
        "hielo": "Hielo picado (crushed ice)",
        "ingredientes": [
            "50 ml de ron blanco cubano",
            "30 ml de zumo de lima recién exprimido",
            "2 cucharaditas de azúcar blanco de caña (o 20 ml de jarabe de azúcar)",
            "8 a 10 hojas de hierbabuena fresca",
            "60 ml de soda o agua con gas fría",
            "Ramita de hierbabuena y rueda de lima para decorar"
        ],
        "preparacion": [
            "En el fondo del vaso alto, coloca el azúcar y el zumo de lima recién exprimido. Remueve hasta diluir el azúcar.",
            "Palmada suave a las hojas de hierbabuena entre las manos para despertar los aceites esenciales y añádelas al vaso.",
            "Presiona la hierbabuena con el mortero muy sutilmente durante 5 segundos; no la rompas ni la tritures para evitar notas amargas.",
            "Añade el ron blanco y llena el vaso hasta la mitad con hielo picado. Remueve con cuchara imperial para integrar.",
            "Completa con más hielo picado hasta arriba y corona con la soda fría.",
            "Decora con una generosa rama de hierbabuena y una rodaja de lima."
        ],
        "consejo_bartender": "Golpea el manojo de hierbabuena contra el dorso de tu mano justo antes de colocarlo como adorno: el aroma al acercar la copa a la nariz transformará la experiencia del trago."
    },
    {
        "num": 3,
        "key": "sangria",
        "nombre": "Sangría tradicional",
        "sin_alcohol": False,
        "base_alcohol": "Vino tinto y licor",
        "metodo": "Macerado y refrescado",
        "cristaleria": "Copa de vino grande o jarra",
        "tiempo_min": 10,
        "perfil_sabor": "Frutal, dulce y especiado",
        "hielo": "Cubos de hielo grandes",
        "ingredientes": [
            "100 ml de vino tinto joven afrutado (Garnacha o Tempranillo)",
            "15 ml de licor de naranja (tipo triple seco o Cointreau)",
            "15 ml de brandy español",
            "20 ml de zumo de naranja natural",
            "1 cucharadita de azúcar",
            "30 ml de refresco de naranja o gaseosa",
            "Fruta fresca troceada (naranja, manzana y melocotón)"
        ],
        "preparacion": [
            "En una jarra o copa grande, añade la fruta cortada en dados pequeños junto con el azúcar, el brandy y el licor de naranja.",
            "Deja macerar la mezcla de 10 a 15 minutos para que la fruta absorba los licores y suelte su jugo natural.",
            "Vierte el vino tinto y el zumo de naranja recién exprimido. Remueve enérgicamente.",
            "Añade abundante hielo y finaliza con un toque de gaseosa o refresco de limón/naranja para aportar frescor y vivacidad.",
            "Sirve procurando que cada copa reciba dados de fruta macerada."
        ],
        "consejo_bartender": "No uses un vino de baja calidad creyendo que la fruta lo ocultará; elige un tinto joven sin barrica, jugoso y aromático, para que la sangría resulte redonda y equilibrada."
    },
    {
        "num": 4,
        "key": "tinto_de_verano",
        "nombre": "Tinto de verano",
        "sin_alcohol": False,
        "base_alcohol": "Vino tinto",
        "metodo": "Construido en vaso",
        "cristaleria": "Copa balón o vaso ancho de sidra",
        "tiempo_min": 2,
        "perfil_sabor": "Refrescante, ligero y afrutado",
        "hielo": "Abundante hielo en roca",
        "ingredientes": [
            "100 ml de vino tinto joven (Tempranillo o Mencía)",
            "100 ml de gaseosa tradicional o refresco de limón",
            "1 rodaja de limón o naranja fresca",
            "Hielo abundante hasta llenar la copa"
        ],
        "preparacion": [
            "Llena generosamente una copa balón o vaso ancho con cubos de hielo de buena densidad.",
            "Vierte primero el vino tinto hasta la mitad del vaso.",
            "Añade la misma proporción de gaseosa (para un perfil seco) o refresco de limón (para un perfil cítrico y dulce).",
            "Mueve suavemente con la cuchara una sola vez de abajo hacia arriba para homogeneizar sin romper la burbuja.",
            "Introduce una rodaja de limón en el lateral del vaso."
        ],
        "consejo_bartender": "El secreto de un tinto de verano memorable de taberna es servir tanto el vino como el mezclador extremadamente fríos de la nevera antes de servir sobre el hielo."
    },
    {
        "num": 5,
        "key": "aperol_spritz",
        "nombre": "Aperol spritz",
        "sin_alcohol": False,
        "base_alcohol": "Aperol y vino espumoso",
        "metodo": "Construido en copa",
        "cristaleria": "Copa de vino grande",
        "tiempo_min": 3,
        "perfil_sabor": "Agridulce, cítrico y chispeante",
        "hielo": "Cubos gruesos",
        "ingredientes": [
            "60 ml de Aperol",
            "90 ml de cava brut o prosecco muy frío",
            "30 ml de soda o agua con gas",
            "1 rodaja de naranja fresca",
            "1 aceituna verde manzanilla (opcional, estilo veneciano)"
        ],
        "preparacion": [
            "Coloca abundante hielo en una copa grande de vino blanco.",
            "Sigue la regla veneciana del 3-2-1: vierte primero el cava o prosecco (3 partes / 90 ml).",
            "Añade el Aperol con un movimiento circular (2 partes / 60 ml) para que comience a teñir la mezcla.",
            "Termina con un chorrito de soda o sifón (1 parte / 30 ml).",
            "Integra con un toque de cuchara sin agitar y decora con una media luna de naranja."
        ],
        "consejo_bartender": "Poner el vino espumoso antes que el licor evita que el Aperol se deposite pesadamente en el fondo, logrando un color naranja brillante y una mezcla perfecta sin perder gas."
    },
    {
        "num": 6,
        "key": "agua_de_valencia",
        "nombre": "Agua de Valencia",
        "sin_alcohol": False,
        "base_alcohol": "Cava, ginebra y vodka",
        "metodo": "Construido y refrescado",
        "cristaleria": "Copa de cóctel o copa de champán",
        "tiempo_min": 5,
        "perfil_sabor": "Cítrico, dulce y potente",
        "hielo": "Cubos de hielo en jarra",
        "ingredientes": [
            "100 ml de zumo de naranja natural recién exprimido y colado",
            "100 ml de cava brut bien frío",
            "25 ml de ginebra",
            "25 ml de vodka",
            "1 cucharadita de azúcar blanco (opcional, al gusto)"
        ],
        "preparacion": [
            "Exprime naranjas frescas de temporada y cuela el zumo para eliminar la pulpa gruesa.",
            "En una jarra con hielo (o directamente en vaso mezclador), vierte el zumo de naranja, la ginebra y el vodka. Añade el azúcar y remueve hasta disolver.",
            "Incorpora el cava lentamente para no generar exceso de espuma.",
            "Remueve con calma usando una cuchara larga.",
            "Sirve en copas frías decorando con una fina rodaja de naranja."
        ],
        "consejo_bartender": "Jamás utilices zumo industrial envasado; el alma auténtica de este cóctel creado en la Cervecería Madrid de Valencia en 1959 reside en la acidez y frescura de la naranja natural recién exprimida."
    },
    {
        "num": 7,
        "key": "rebujito",
        "nombre": "Rebujito",
        "sin_alcohol": False,
        "base_alcohol": "Vino fino o manzanilla",
        "metodo": "Construido en vaso",
        "cristaleria": "Vaso de tubo o copa ancha",
        "tiempo_min": 2,
        "perfil_sabor": "Seco, herbal y muy refrescante",
        "hielo": "Abundante hielo macizo",
        "ingredientes": [
            "60 ml de vino Manzanilla de Sanlúcar o Fino de Jerez",
            "120 ml de refresco de lima-limón (tipo Sprite o Seven Up)",
            "2 ramitas de hierbabuena fresca",
            "Hielo abundante"
        ],
        "preparacion": [
            "Llena el vaso con hielo compacto hasta el borde.",
            "Vierte el vino fino o manzanilla.",
            "Añade el refresco de lima-limón suavemente, manteniendo una proporción aproximada de 1 parte de vino por 2 de refresco.",
            "Introduce unas hojas de hierbabuena en el vaso, golpeándolas previamente para abrir su aroma.",
            "Remueve sutilmente una sola vez."
        ],
        "consejo_bartender": "La hierbabuena no se machaca: se introduce entera entre los hielos. Esto aromatiza cada sorbo sin amargar el final seco y salino de la manzanilla."
    },
    {
        "num": 8,
        "key": "negroni",
        "nombre": "Negroni",
        "sin_alcohol": False,
        "base_alcohol": "Ginebra, vermut rojo y Campari",
        "metodo": "Refrescado (removido)",
        "cristaleria": "Vaso bajo (old fashioned / rocks)",
        "tiempo_min": 3,
        "perfil_sabor": "Amargo, herbal y equilibrado",
        "hielo": "Un cubo grande y macizo",
        "ingredientes": [
            "30 ml de ginebra seca",
            "30 ml de Campari (bitter rojo)",
            "30 ml de vermut rojo dulce (dulce de buena calidad)",
            "1 media luna o piel de naranja fresca"
        ],
        "preparacion": [
            "Coloca hielo abundante en un vaso mezclador o directamente en el vaso bajo de servicio con un gran cubo de hielo.",
            "Añade a partes iguales la ginebra, el Campari y el vermut rojo.",
            "Remueve con la cuchara de bar durante unos 20 a 30 segundos para enfriar e integrar los tres licores permitiendo la dilución justa.",
            "Si usaste vaso mezclador, cuela sobre el vaso bajo con hielo nuevo.",
            "Exprime la piel de naranja sobre la superficie del cóctel para perfumar y deposítala dentro."
        ],
        "consejo_bartender": "La regla de oro del Negroni es la precisión matemática: proporciones 1:1:1 idénticas y un hielo de alta densidad que no agüe prematuramente la complejidad amarga del trago."
    },
    {
        "num": 9,
        "key": "margarita",
        "nombre": "Margarita",
        "sin_alcohol": False,
        "base_alcohol": "Tequila blanco o reposado",
        "metodo": "Agitado simple (shake)",
        "cristaleria": "Copa coupette o copa margarita",
        "tiempo_min": 4,
        "perfil_sabor": "Cítrico, salino y vibrante",
        "hielo": "Hielo en cubos para la coctelera",
        "ingredientes": [
            "50 ml de tequila 100% agave",
            "25 ml de licor de naranja (Cointreau o triple seco)",
            "25 ml de zumo de lima recién exprimido",
            "5 ml de jarabe de agave o azúcar (opcional, para equilibrar)",
            "Sal fina para el borde de la copa",
            "1 rodaja de lima para decorar"
        ],
        "preparacion": [
            "Pasa media lima por el borde exterior de la copa y apóyala sobre un plato con sal fina para crear un escarchado fino solo por la mitad del reborde.",
            "Llena la coctelera con hielo abundante.",
            "Añade el tequila, el licor de naranja y el zumo de lima colado.",
            "Cierra la coctelera y agita enérgicamente durante 12 a 15 segundos hasta que el metal esté escarchado por fuera.",
            "Realiza un colado simple o doble colado vertiendo el líquido frío en la copa preparada.",
            "Adorna con una rodaja de lima en el borde no salado."
        ],
        "consejo_bartender": "Escarba solo la mitad del borde de la copa con sal; de este modo quien lo bebe puede elegir cuándo alternar tragos con o sin toque salino según su preferencia."
    },
    {
        "num": 10,
        "key": "daiquiri",
        "nombre": "Daiquiri clásico",
        "sin_alcohol": False,
        "base_alcohol": "Ron blanco",
        "metodo": "Agitado simple (shake)",
        "cristaleria": "Copa cóctel (coupette o martini)",
        "tiempo_min": 3,
        "perfil_sabor": "Cítrico, seco y aterciopelado",
        "hielo": "Cubos para coctelera",
        "ingredientes": [
            "50 ml de ron blanco ligero",
            "25 ml de zumo de lima recién exprimido y filtrado",
            "15 ml de jarabe simple de azúcar (proporción 1:1)",
            "1 rueda fina de lima para decorar"
        ],
        "preparacion": [
            "Enfría previamente la copa coupette llenándola de hielo mientras preparas el cóctel.",
            "En la coctelera, vierte el ron blanco, el zumo de lima fresco y el jarabe de azúcar.",
            "Llena la coctelera de cubos de hielo hasta tres cuartas partes.",
            "Bate con fuerza y ritmo durante 12 segundos.",
            "Descarta el hielo de la copa para que esté bien helada.",
            "Cuela el cóctel a través de un colador fino (doble colado) para atrapar pequeñas esquirlas de hielo.",
            "Decora con una rueda flotante de lima."
        ],
        "consejo_bartender": "El Daiquiri es la prueba del algodón del bartender: si el zumo de lima no está recién exprimido del día, el equilibrio entre el dulce y el ron se arruina por completo."
    },
    {
        "num": 11,
        "key": "marianito",
        "nombre": "Marianito (vermut preparado)",
        "sin_alcohol": False,
        "base_alcohol": "Vermut rojo",
        "metodo": "Refrescado en vaso",
        "cristaleria": "Vaso bajo o copa de vermut",
        "tiempo_min": 2,
        "perfil_sabor": "Herbal, especiado y con final seco",
        "hielo": "Dos cubos macizos",
        "ingredientes": [
            "60 ml de vermut rojo tradicional",
            "15 ml de ginebra seca",
            "5 ml de Campari o bitter rojo",
            "2 gotas de bitter Angostura",
            "Un toque de sifón o soda (opcional)",
            "1 aceituna rellena y 1 rodaja de naranja"
        ],
        "preparacion": [
            "Coloca dos buenos cubos de hielo en el vaso bajo.",
            "Añade el vermut rojo, la ginebra, el Campari y las gotas de Angostura.",
            "Remueve con suavidad durante 10 segundos con la cuchara para aclimatar y amalgamar los ingredientes.",
            "Si deseas aligerarlo, añade un golpe breve de sifón o soda fría.",
            "Remata con una aceituna ensartada en palillo y media rodaja de naranja."
        ],
        "consejo_bartender": "El Marianito es el rey del aperitivo en el norte de España: la ginebra le aporta nervio y estructura al vermut sin enmascarar sus botánicos artesanales."
    },
    {
        "num": 12,
        "key": "pina_colada",
        "nombre": "Piña colada",
        "sin_alcohol": False,
        "base_alcohol": "Ron blanco",
        "metodo": "Agitado enérgico o batido",
        "cristaleria": "Copa huracán o vaso alto",
        "tiempo_min": 4,
        "perfil_sabor": "Tropical, cremoso y dulce",
        "hielo": "Hielo picado o cubos",
        "ingredientes": [
            "50 ml de ron blanco",
            "50 ml de crema o leche de coco espesa",
            "100 ml de zumo de piña natural (sin azúcares añadidos)",
            "10 ml de zumo de lima fresca (toque de balance)",
            "Triángulo de piña fresca y cereza al marrasquino"
        ],
        "preparacion": [
            "Coloca el ron blanco, la crema de coco, el zumo de piña y el zumo de lima en una coctelera con mucho hielo picado (o en batidora eléctrica).",
            "Agita con intensidad durante 20 segundos hasta que la textura emulsione y gane cuerpo cremoso y sedoso.",
            "Vierte todo el contenido sin colar (con el hielo) en una copa tipo huracán.",
            "Coloca en el borde una cuña de piña fresca y una cereza de cóctel."
        ],
        "consejo_bartender": "Añade siempre un chorrito diminuto (10 ml) de zumo de lima: la acidez natural corta la pesadez de la crema de coco y equilibra el dulzor haciéndola mucho más bebible."
    },
    {
        "num": 13,
        "key": "espresso_martini",
        "nombre": "Espresso martini",
        "sin_alcohol": False,
        "base_alcohol": "Vodka y licor de café",
        "metodo": "Agitado enérgico (shake)",
        "cristaleria": "Copa coupette o martini",
        "tiempo_min": 4,
        "perfil_sabor": "Tostado, café expreso y dulce sedoso",
        "hielo": "Cubos grandes y secos",
        "ingredientes": [
            "50 ml de vodka",
            "30 ml de licor de café (tipo Kahlúa o Tía María)",
            "30 ml de café expreso recién hecho (caliente o templado)",
            "10 ml de jarabe de azúcar (ajustar según el gusto)",
            "3 granos de café tostado para coronar"
        ],
        "preparacion": [
            "Prepara un café expreso corto e intenso en cafetera italiana o de espresso.",
            "Llena la coctelera con abundante hielo macizo.",
            "Vierte de inmediato el vodka, el licor de café, el jarabe y el café expreso.",
            "Agita con máxima energía durante 15 segundos: el contraste térmico y la presión formarán una espuma cremosa inconfundible.",
            "Cuela rápidamente con colador fino sobre la copa helada.",
            "Coloca suavemente tres granos de café sobre la espuma en el centro."
        ],
        "consejo_bartender": "Los tres granos de café sobre la espuma simbolizan la salud, la riqueza y la felicidad según la tradición de la hospitalidad italiana. Agita con fuerza para crear la densa crema que los sostiene a flote."
    },
    {
        "num": 14,
        "key": "moscow_mule",
        "nombre": "Moscow mule",
        "sin_alcohol": False,
        "base_alcohol": "Vodka",
        "metodo": "Construido en vaso",
        "cristaleria": "Jarra de cobre o vaso bajo",
        "tiempo_min": 3,
        "perfil_sabor": "Picante de jengibre, fresco y cítrico",
        "hielo": "Hielo picado abundante",
        "ingredientes": [
            "50 ml de vodka",
            "15 ml de zumo de lima fresca",
            "120 ml de cerveza de jengibre (ginger beer con gas)",
            "1 rodaja de lima",
            "1 ramita de menta fresca"
        ],
        "preparacion": [
            "Llena la emblemática jarra de cobre con hielo picado hasta el borde.",
            "Añade el vodka y el zumo de lima recién exprimido.",
            "Rellena con la cerveza de jengibre fría vertiéndola suavemente.",
            "Remueve con un movimiento delicado de abajo hacia arriba para unificar.",
            "Añade un poco más de hielo picado para formar un pequeño volcán y decora con la ramita de menta y la rodaja de lima."
        ],
        "consejo_bartender": "Usa siempre cerveza de jengibre fermentada ('ginger beer') y no refresco suave ('ginger ale'); el picante característico de la raíz de jengibre es la esencia de este trago."
    },
    {
        "num": 15,
        "key": "caipirinha",
        "nombre": "Caipiriña",
        "sin_alcohol": False,
        "base_alcohol": "Cachaça",
        "metodo": "Macerado y construido",
        "cristaleria": "Vaso bajo (old fashioned)",
        "tiempo_min": 4,
        "perfil_sabor": "Rústico, cítrico y dulce",
        "hielo": "Hielo picado o cubos medianos",
        "ingredientes": [
            "60 ml de cachaça brasileña",
            "1 lima entera madura",
            "2 cucharadas de azúcar blanco de caña",
            "Hielo picado abundante"
        ],
        "preparacion": [
            "Lava la lima, retira los dos extremos y el nervio blanco central (columela) para evitar amargor.",
            "Corta la lima en 8 trozos o dados y colócala en el fondo del vaso bajo con la piel hacia abajo.",
            "Añade las 2 cucharadas de azúcar por encima de la fruta.",
            "Machaqua con el mortero firmemente pero sin desgarrar la piel exterior, extrayendo el zumo y disolviéndolo con el azúcar.",
            "Llena el vaso con hielo picado hasta desbordar ligeramente.",
            "Vierte la cachaça por encima y remueve bien de abajo a arriba con la cuchara para que el azúcar se reparta uniformemente."
        ],
        "consejo_bartender": "Retirar la médula blanca del interior de la lima es el paso que separa una caipiriña amateur y amarga de una auténtica delicia brasileña de coctelería."
    },
    {
        "num": 16,
        "key": "cuba_libre",
        "nombre": "Cuba libre",
        "sin_alcohol": False,
        "base_alcohol": "Ron añejo o dorado",
        "metodo": "Construido en vaso",
        "cristaleria": "Vaso alto (highball)",
        "tiempo_min": 2,
        "perfil_sabor": "Acaramelado, avainillado y cítrico",
        "hielo": "Cubos macizos hasta el tope",
        "ingredientes": [
            "50 ml de ron dorado o añejo de calidad",
            "120 ml de refresco de cola frío",
            "15 ml de zumo de lima fresca recién exprimido",
            "2 gajos de lima",
            "Hielo abundante"
        ],
        "preparacion": [
            "Llena el vaso de tubo o highball por completo con cubos de hielo de gran tamaño.",
            "Exprime un gajo de lima directamente sobre el hielo y echa el zumo (unos 15 ml).",
            "Vierte el ron dorado.",
            "Añade el refresco de cola despacio inclinando ligeramente el vaso para no malgastar el gas carbónico.",
            "Remueve una sola vez e introduce el segundo gajo de lima dentro del vaso."
        ],
        "consejo_bartender": "Un 'Cuba libre' no es un simple ron-cola: el zumo de lima fresco exprimido en directo es indispensable para cortar el dulzor del caramelo del refresco."
    },
    {
        "num": 17,
        "key": "tom_collins",
        "nombre": "Tom Collins",
        "sin_alcohol": False,
        "base_alcohol": "Ginebra",
        "metodo": "Construido en vaso",
        "cristaleria": "Vaso alto (collins)",
        "tiempo_min": 3,
        "perfil_sabor": "Limonada chispeante y botánica",
        "hielo": "Cubos alargados o macizos",
        "ingredientes": [
            "50 ml de ginebra (estilo London Dry u Old Tom)",
            "30 ml de zumo de limón recién exprimido",
            "20 ml de jarabe de azúcar simple",
            "60 ml de soda o agua con gas",
            "1 rodaja de limón y una cereza de cóctel"
        ],
        "preparacion": [
            "En el vaso Collins, vierte la ginebra, el zumo de limón colado y el jarabe simple.",
            "Remueve con la cuchara para mezclar la base agridulce.",
            "Rellena el vaso con cubos de hielo hasta el tope.",
            "Completa con la soda bien fría.",
            "Realiza un suave movimiento vertical con la cuchara para levantar la mezcla.",
            "Adorna con una rodaja de limón insertada y una guinda marrasquino."
        ],
        "consejo_bartender": "Es la madre de los tragos largos con ginebra: piensa en él como en una limonada casera para adultos extremadamente chispeante y refrescante."
    },
    {
        "num": 18,
        "key": "dry_martini",
        "nombre": "Dry martini",
        "sin_alcohol": False,
        "base_alcohol": "Ginebra y vermut seco",
        "metodo": "Refrescado (removido)",
        "cristaleria": "Copa de cóctel clásica (martini)",
        "tiempo_min": 3,
        "perfil_sabor": "Seco, limpio, mineral y potente",
        "hielo": "Cubos macizos en vaso mezclador",
        "ingredientes": [
            "60 ml de ginebra London Dry de primera calidad",
            "10 ml de vermut blanco seco (tipo Noilly Prat)",
            "1 aceituna verde sin hueso o un twist de corteza de limón"
        ],
        "preparacion": [
            "Asegúrate de que la copa cónica esté congelada teniéndola en el congelador 15 minutos antes.",
            "Llena el vaso mezclador con hielo abundante y compacto.",
            "Vierte el vermut seco y la ginebra.",
            "Remueve con suavidad y fluidez durante 30 segundos continuos para enfriar a temperaturas bajo cero sin crear burbujas de aire.",
            "Cuela con el colador gusanillo en la copa martini helada.",
            "Añade una aceituna pinchada en una brocheta o retuerce una piel de limón sobre la superficie para aromatizar con sus aceites."
        ],
        "consejo_bartender": "Nunca lo batas en coctelera a menos que te lo pida James Bond: el agitado enturbia el líquido y llena de astillas de hielo un cóctel cuya belleza reside en su transparencia cristalina."
    },
    {
        "num": 19,
        "key": "paloma",
        "nombre": "Paloma",
        "sin_alcohol": False,
        "base_alcohol": "Tequila blanco",
        "metodo": "Construido en vaso",
        "cristaleria": "Vaso alto con borde escarchado",
        "tiempo_min": 3,
        "perfil_sabor": "Cítrico, pomelo amargo y salino",
        "hielo": "Cubos de hielo grandes",
        "ingredientes": [
            "50 ml de tequila blanco 100% agave",
            "15 ml de zumo de lima fresca",
            "100 ml de refresco de pomelo rosado (o zumo de pomelo con toque de soda)",
            "1 pizca de sal marina",
            "1 gajo de pomelo rosado para decorar"
        ],
        "preparacion": [
            "Pasa un gajo de lima por la mitad del borde del vaso y pásalo por sal gruesa o sal con chile.",
            "Llena el vaso con cubos de hielo.",
            "Vierte el tequila blanco, el zumo de lima y añade una pequeña pizca de sal dentro.",
            "Completa con el refresco de pomelo frío hasta el borde.",
            "Remueve delicadamente para integrar.",
            "Decora con un gajo de pomelo rosado encajado en el borde."
        ],
        "consejo_bartender": "La sal no es solo para el borde: añadir una micro-pizca disuelta dentro potencia la dulzura del pomelo y neutraliza el exceso de amargor cítrico."
    },
    {
        "num": 20,
        "key": "old_fashioned",
        "nombre": "Old fashioned",
        "sin_alcohol": False,
        "base_alcohol": "Bourbon o whisky de centeno",
        "metodo": "Construido y refrescado",
        "cristaleria": "Vaso bajo (old fashioned / rocks)",
        "tiempo_min": 4,
        "perfil_sabor": "Amaderado, dulce sutil y aromático",
        "hielo": "Una gran roca o esfera de hielo",
        "ingredientes": [
            "60 ml de bourbon o rye whiskey",
            "1 terrón de azúcar blanco (o 5 ml de jarabe simple)",
            "3 golpes de amargo de Angostura",
            "1 cucharadita de agua con gas o soda",
            "Piel de naranja fresca y cereza al marrasquino"
        ],
        "preparacion": [
            "En el vaso bajo, coloca el terrón de azúcar y empápalo con los 3 golpes de Angostura y la cucharadita de soda.",
            "Con la cuchara o el mortero, disuelve por completo el azúcar hasta formar una pasta homogénea.",
            "Coloca una roca de hielo grande y compacta en el centro del vaso.",
            "Vierte la mitad del whisky (30 ml) y remueve durante 15 segundos con la cuchara imperial.",
            "Añade los otros 30 ml de whisky y vuelve a remover otros 15 segundos para lograr la dilución perfecta.",
            "Retuerce la piel de naranja sobre el vaso liberando su aceite cítrico y añádela como guarnición."
        ],
        "consejo_bartender": "La paciencia al remover es el alma del Old fashioned: no bebas deprisa, este cóctel evoluciona sorbo a sorbo a medida que el hielo se funde lentamente."
    },
    {
        "num": 21,
        "key": "manhattan",
        "nombre": "Manhattan",
        "sin_alcohol": False,
        "base_alcohol": "Whisky de centeno y vermut rojo",
        "metodo": "Refrescado (removido)",
        "cristaleria": "Copa cóctel (coupette o martini)",
        "tiempo_min": 3,
        "perfil_sabor": "Rico, especiado, licoroso y herbal",
        "hielo": "Cubos macizos en vaso mezclador",
        "ingredientes": [
            "50 ml de whisky de centeno (Rye) o bourbon",
            "25 ml de vermut rojo dulce italiano",
            "2 golpes de bitter Angostura",
            "1 cereza al marrasquino de calidad para decorar"
        ],
        "preparacion": [
            "Coloca hielo abundante en el vaso mezclador.",
            "Vierte el whisky, el vermut dulce y los golpes de Angostura.",
            "Remueve enérgicamente con la cuchara de bar durante unos 25 segundos para alcanzar una temperatura helada y textura sedosa.",
            "Cuela con el gusanillo directamente en una copa de cóctel previamente enfriada.",
            "Deposita una guinda o cereza amarena en el fondo de la copa."
        ],
        "consejo_bartender": "Prefiere siempre un whisky de centeno (Rye): sus notas de pimienta y cereal seco contrastan de maravilla con el azúcar especiado del vermut rojo."
    },
    {
        "num": 22,
        "key": "whisky_sour",
        "nombre": "Whisky sour",
        "sin_alcohol": False,
        "base_alcohol": "Bourbon o whisky escocés",
        "metodo": "Agitado simple (shake)",
        "cristaleria": "Vaso bajo (rocks) o copa coupette",
        "tiempo_min": 4,
        "perfil_sabor": "Cítrico, sedoso y avainillado",
        "hielo": "Cubos en coctelera y vaso",
        "ingredientes": [
            "50 ml de whisky bourbon",
            "25 ml de zumo de limón recién exprimido y colado",
            "20 ml de jarabe de azúcar simple",
            "15 ml de clara de huevo o albúmina (opcional, para espuma sedosa)",
            "1 rodaja de naranja y 1 cereza de cóctel"
        ],
        "preparacion": [
            "Si usas clara de huevo, haz primero un 'dry shake': agita en la coctelera todos los ingredientes sin hielo durante 10 segundos para espumar.",
            "Añade hielo abundante a la coctelera.",
            "Vuelve a agitar enérgicamente durante otros 12 a 15 segundos para enfriar.",
            "Cuela sobre un vaso bajo con un cubo de hielo grande (o en copa coupette helada sin hielo).",
            "Decora con una rodaja de naranja y dos gotas de angostura sobre la crema blanca."
        ],
        "consejo_bartender": "La clara de huevo no aporta sabor a huevo: actúa como un emulsionante molecular que otorga una textura cremosa inigualable que suaviza la fuerza del destilado."
    },
    {
        "num": 23,
        "key": "cosmopolitan",
        "nombre": "Cosmopolitan",
        "sin_alcohol": False,
        "base_alcohol": "Vodka cítrico y triple seco",
        "metodo": "Agitado simple (shake)",
        "cristaleria": "Copa cóctel (martini)",
        "tiempo_min": 3,
        "perfil_sabor": "Frutos rojos, cítrico y seco",
        "hielo": "Hielo en cubos para agitar",
        "ingredientes": [
            "40 ml de vodka al limón (citron) o vodka neutro",
            "20 ml de licor de naranja (Cointreau o triple seco)",
            "20 ml de zumo de arándanos rojos (cranberry)",
            "15 ml de zumo de lima fresca",
            "1 twist de piel de naranja o lima"
        ],
        "preparacion": [
            "Enfría la copa martini con hielo o manteniéndola en el congelador.",
            "En la coctelera con hielo, vierte el vodka, el licor de naranja, el zumo de arándanos y el zumo de lima.",
            "Agita intensamente durante 12 segundos.",
            "Desecha el hielo de la copa y cuela con doble colador para retener cristales de hielo flotantes.",
            "Flamea levemente o retuerce la piel de naranja sobre la superficie para aromatizar la copa."
        ],
        "consejo_bartender": "El color debe ser de un rosa pálido y translúcido muy elegante, no un rojo intenso opaco; no te excedas con el zumo de arándanos para respetar el balance seco de la lima."
    },
    {
        "num": 24,
        "key": "san_francisco",
        "nombre": "San Francisco",
        "sin_alcohol": True,
        "base_alcohol": "Sin alcohol (0,0%)",
        "metodo": "Agitado enérgico (shake)",
        "cristaleria": "Vaso alto (highball) escarchado",
        "tiempo_min": 4,
        "perfil_sabor": "Frutal, dulce, cítrico y tropical",
        "hielo": "Cubos de hielo",
        "ingredientes": [
            "40 ml de zumo de naranja natural",
            "30 ml de zumo de limón recién exprimido",
            "30 ml de zumo de piña natural",
            "20 ml de zumo de melocotón",
            "15 ml de sirope de granadina",
            "Azúcar y granadina para escarchar el borde",
            "1 rodaja de naranja y 1 cereza"
        ],
        "preparacion": [
            "Humedece el borde del vaso con un poco de granadina y pásalo por azúcar para crear un festivo ribete rosado.",
            "En una coctelera con mucho hielo, introduce los cuatro zumos (naranja, limón, piña y melocotón).",
            "Agita vigorosamente durante 15 segundos para generar una espuma densa y frutal.",
            "Llena el vaso escarchado con cubos de hielo frescos y cuela los zumos agitados.",
            "Vierte despacio la granadina por el centro: al ser más densa, caerá al fondo creando un espectacular efecto bicolor degradado.",
            "Decora con la rodaja de naranja y una guinda en el borde."
        ],
        "consejo_bartender": "Es el cóctel sin alcohol más emblemático de la historia hostelera de España: la magia reside en verter la granadina al final sin remover para lucir ese degradado de atardecer."
    },
    {
        "num": 25,
        "key": "bloody_mary",
        "nombre": "Bloody Mary",
        "sin_alcohol": False,
        "base_alcohol": "Vodka y zumo de tomate",
        "metodo": "Refrescado / escanciado (roll)",
        "cristaleria": "Vaso alto (highball)",
        "tiempo_min": 5,
        "perfil_sabor": "Salado, umami, picante y especiado",
        "hielo": "Cubos enteros",
        "ingredientes": [
            "50 ml de vodka",
            "100 ml de zumo de tomate de calidad",
            "15 ml de zumo de limón recién exprimido",
            "3 golpes de salsa Worcestershire (Perrins)",
            "2 o 3 gotas de salsa picante Tabasco",
            "1 pizca de sal de apio y pimienta negra molida",
            "1 tallo fresco de apio con hojas para remover y decorar"
        ],
        "preparacion": [
            "En un vaso alto o mezclador, vierte el zumo de limón, las salsas Worcestershire y Tabasco, la sal de apio y la pimienta.",
            "Añade el vodka y el zumo de tomate bien frío.",
            "Agrega cubos de hielo y pásalo suavemente de un vaso a otro dos o tres veces (técnica 'rolling') para oxigenar sin aguar en exceso.",
            "Sirve en el vaso alto con hielo limpio.",
            "Introduce el tallo de apio fresco para que sirva tanto de adorno como de agitador natural."
        ],
        "consejo_bartender": "Nunca agites un Bloody Mary en coctelera como si fuera un margarita: la agitación rompe las fibras del tomate y lo vuelve aguado y espumoso. El método escanciado conserva su textura densa."
    },
    {
        "num": 26,
        "key": "cremaet",
        "nombre": "Carajillo quemado (cremaet)",
        "sin_alcohol": False,
        "base_alcohol": "Ron añejo flameado y café",
        "metodo": "Flameado y servido en capas",
        "cristaleria": "Vaso pequeño de cristal térmico",
        "tiempo_min": 6,
        "perfil_sabor": "Café tostado, canela, cítrico y licoroso",
        "hielo": "Sin hielo (trago caliente)",
        "ingredientes": [
            "40 ml de ron añejo (o brandy)",
            "1 taza de café expreso corto bien caliente",
            "2 cucharaditas de azúcar moreno o blanco",
            "1 ramita pequeña de canela",
            "1 trozo de piel de limón",
            "3 granos de café enteros"
        ],
        "preparacion": [
            "En el vaso térmico de cristal, coloca el ron, el azúcar, la piel de limón, la canela y los granos de café.",
            "Calienta la mezcla en el microondas o con el vaporizador de la cafetera hasta que esté muy caliente.",
            "Prende fuego a la superficie con un encendedor y remueve despacio con una cucharilla metálica durante 1 minuto para quemar parte del alcohol e infusionar los aromas.",
            "Apaga la llama tapando el vaso con un platillo metálico.",
            "Extrae un café expreso muy caliente y viértelo lentamente sobre el dorso de la cuchara pegado a la pared del cristal.",
            "Observa cómo se forman tres capas perfectas: el licor dorado abajo, el café negro en medio y la crema tostada arriba."
        ],
        "consejo_bartender": "El secreto del trifásico perfecto valenciano es la densidad: el licor dulce caliente es denso y retiene al café arriba si lo dejas caer gota a gota por el cristal."
    },
    {
        "num": 27,
        "key": "americano",
        "nombre": "Americano",
        "sin_alcohol": False,
        "base_alcohol": "Campari y vermut rojo",
        "metodo": "Construido en vaso con soda",
        "cristaleria": "Vaso bajo (rocks) o vaso medio",
        "tiempo_min": 2,
        "perfil_sabor": "Amargo, chispeante y aromático",
        "hielo": "Cubos macizos",
        "ingredientes": [
            "30 ml de Campari",
            "30 ml de vermut rojo dulce",
            "60 ml de soda o agua con gas muy fría",
            "1 rodaja de naranja fresca",
            "1 piel de limón"
        ],
        "preparacion": [
            "Llena el vaso con cubos de hielo hasta el borde.",
            "Vierte el Campari y el vermut rojo a partes iguales.",
            "Añade la soda fría para abrir los aromas y reducir la graduación alcohólica.",
            "Remueve delicadamente de abajo hacia arriba con la cuchara una sola vez.",
            "Adorna con una rodaja de naranja y exprime la piel de limón sobre la copa."
        ],
        "consejo_bartender": "Es el hermano ligero del Negroni (inventado antes que este, cuando los turistas estadounidenses pedían suavizar el cóctel Milano-Torino con un toque de soda)."
    },
    {
        "num": 28,
        "key": "pisco_sour",
        "nombre": "Pisco sour",
        "sin_alcohol": False,
        "base_alcohol": "Pisco",
        "metodo": "Agitado simple (shake)",
        "cristaleria": "Vaso bajo o copa coupette",
        "tiempo_min": 4,
        "perfil_sabor": "Cítrico, floral, potente y sedoso",
        "hielo": "Cubos para coctelera",
        "ingredientes": [
            "60 ml de pisco quebranta o acholado",
            "30 ml de zumo de lima recién exprimido",
            "20 ml de jarabe de azúcar simple",
            "15 ml de clara de huevo",
            "2 gotas de bitter Angostura para la espuma"
        ],
        "preparacion": [
            "Pon en la coctelera el pisco, el zumo de lima, el jarabe y la clara de huevo.",
            "Agita 10 segundos sin hielo para emulsionar la clara.",
            "Llena con bastante hielo y vuelve a batir fuertemente durante 15 segundos hasta sentir el frío en las manos.",
            "Cuela en dos tiempos sobre una copa helada sin hielo.",
            "Deja reposar 5 segundos para que la espuma blanca y densa suba a la superficie.",
            "Deja caer dos gotas de Angostura sobre la crema para aromatizar cada trago."
        ],
        "consejo_bartender": "Las gotas de Angostura en la superficie no son decoración estética: neutralizan el sutil olor inicial de la clara cruda y desprenden un aroma cautivador al beber."
    },
    {
        "num": 29,
        "key": "bellini",
        "nombre": "Bellini",
        "sin_alcohol": False,
        "base_alcohol": "Cava o prosecco y melocotón",
        "metodo": "Construido en copa",
        "cristaleria": "Copa flauta de champán",
        "tiempo_min": 3,
        "perfil_sabor": "Dulce, frutal, sedoso y burbujeante",
        "hielo": "Ingredientes muy fríos sin hielo",
        "ingredientes": [
            "50 ml de puré de melocotón blanco natural muy frío",
            "100 ml de cava brut o prosecco bien frío",
            "Unas gotas de zumo de limón o granadina (opcional)"
        ],
        "preparacion": [
            "Tritura melocotones maduros pelados hasta obtener un puré fino y déjalo enfriar en la nevera.",
            "Vierte el puré de melocotón en el fondo de una copa flauta fría.",
            "Añade despacio la mitad del cava espumoso.",
            "Remueve con la cuchara imperial muy suavemente para disolver el puré con la burbuja.",
            "Rellena con el resto del cava hasta llenar la copa y sirve de inmediato."
        ],
        "consejo_bartender": "Creado por Giuseppe Cipriani en el mítico Harry's Bar de Venecia: la clave es que ambos ingredientes estén a punto de congelación para no requerir hielo que agüe el puré."
    },
    {
        "num": 30,
        "key": "mimosa",
        "nombre": "Mimosa",
        "sin_alcohol": False,
        "base_alcohol": "Cava o vino espumoso y naranja",
        "metodo": "Construido en copa",
        "cristaleria": "Copa flauta de champán",
        "tiempo_min": 2,
        "perfil_sabor": "Cítrico, chispeante y refrescante",
        "hielo": "Sin hielo (bebidas muy frías)",
        "ingredientes": [
            "75 ml de zumo de naranja natural recién exprimido y colado",
            "75 ml de cava brut o champán muy frío",
            "1 espiral de piel de naranja"
        ],
        "preparacion": [
            "Cuela el zumo de naranja natural para retirar cualquier resto de pulpa.",
            "En una copa flauta inclinada a 45 grados, vierte primero el cava frío hasta la mitad.",
            "Rellena la otra mitad con el zumo de naranja con un flujo continuo y delicado.",
            "La propia efervescencia del cava mezclará ambos líquidos sin necesidad de remover.",
            "Adorna con una fina piel de naranja en el borde."
        ],
        "consejo_bartender": "Vierte el cava antes del zumo: si viertes el zumo primero, al echar el cava se formará una erupción de espuma volcánica que desbordará la copa y perderá toda la burbuja."
    },
    {
        "num": 31,
        "key": "tequila_sunrise",
        "nombre": "Tequila sunrise",
        "sin_alcohol": False,
        "base_alcohol": "Tequila blanco y naranja",
        "metodo": "Construido en capas",
        "cristaleria": "Vaso alto (highball)",
        "tiempo_min": 3,
        "perfil_sabor": "Dulce, cítrico y afrutado",
        "hielo": "Cubos macizos",
        "ingredientes": [
            "50 ml de tequila blanco",
            "100 ml de zumo de naranja natural recién exprimido",
            "15 ml de sirope de granadina",
            "1 rodaja de naranja y 1 cereza de cóctel"
        ],
        "preparacion": [
            "Llena el vaso alto con cubos de hielo limpios.",
            "Vierte el tequila blanco y a continuación el zumo de naranja.",
            "Remueve ligeramente ambos ingredientes para unificarlos en un tono amarillo luminoso.",
            "Vierte despacio la granadina pegada al borde interior del vaso.",
            "Deja que repose durante 30 segundos sin remover: la densidad del almíbar formará el icónico amanecer rojo, naranja y dorado.",
            "Decora con la rodaja de naranja y la cereza ensartadas."
        ],
        "consejo_bartender": "No caigas en la tentación de removerlo antes de llevarlo a la mesa: el placer visual del Tequila sunrise está en apreciar las capas degradadas antes del primer sorbo."
    },
    {
        "num": 32,
        "key": "sex_on_the_beach",
        "nombre": "Sex on the beach",
        "sin_alcohol": False,
        "base_alcohol": "Vodka y licor de melocotón",
        "metodo": "Construido o agitado simple",
        "cristaleria": "Vaso alto (highball o huracán)",
        "tiempo_min": 3,
        "perfil_sabor": "Muy frutal, dulce y tropical",
        "hielo": "Abundante hielo en roca",
        "ingredientes": [
            "40 ml de vodka",
            "20 ml de licor de melocotón (peach schnapps)",
            "40 ml de zumo de naranja",
            "40 ml de zumo de arándanos rojos (cranberry)",
            "1 rodaja de naranja"
        ],
        "preparacion": [
            "Llena el vaso alto con cubos de hielo hasta arriba.",
            "Vierte el vodka, el licor de melocotón y el zumo de naranja. Remueve.",
            "Añade despacio por encima el zumo de arándanos para crear un bonito contraste de colores.",
            "Decora con una rodaja de naranja fresca en el borde del vaso."
        ],
        "consejo_bartender": "Un clásico indiscutible de las vacaciones estivales en las costas españolas: utiliza siempre zumos de calidad para que no resulte empalagoso."
    },
    {
        "num": 33,
        "key": "lumumba",
        "nombre": "Lumumba",
        "sin_alcohol": False,
        "base_alcohol": "Brandy o coñac y batido de cacao",
        "metodo": "Construido en vaso",
        "cristaleria": "Vaso de tubo o copa ancha",
        "tiempo_min": 2,
        "perfil_sabor": "Chocolateado, cremoso y espirituoso",
        "hielo": "Cubos gruesos",
        "ingredientes": [
            "50 ml de brandy español (tipo Solera Reserva) o coñac",
            "150 ml de batido de chocolate frío (tipo Cacaolat o similar)",
            "Cacao en polvo o canela molida para espolvorear",
            "Hielo abundante"
        ],
        "preparacion": [
            "Llena el vaso de tubo con hielo compacto.",
            "Vierte la dosis de brandy español sobre el hielo.",
            "Rellena con el batido de chocolate bien frío.",
            "Remueve con la cuchara imperial hasta lograr un color uniforme de chocolate con leche brillante.",
            "Espolvorea una pizca sutil de canela o cacao puro por encima."
        ],
        "consejo_bartender": "Este trago nostálgico de las barras españolas de los años 70 y 80 resurge con fuerza si empleas un buen brandy envejecido en barricas de jerez y batido con alto porcentaje de cacao."
    },
    {
        "num": 34,
        "key": "gimlet",
        "nombre": "Gimlet",
        "sin_alcohol": False,
        "base_alcohol": "Ginebra y cordial de lima",
        "metodo": "Agitado o refrescado",
        "cristaleria": "Copa cóctel (coupette)",
        "tiempo_min": 3,
        "perfil_sabor": "Cítrico punzante, botánico y seco",
        "hielo": "Cubos en coctelera",
        "ingredientes": [
            "60 ml de ginebra (estilo London Dry)",
            "30 ml de cordial de lima (o 20 ml de zumo de lima fresca con 10 ml de almíbar simple)",
            "1 rodaja de lima para decorar"
        ],
        "preparacion": [
            "Enfría la copa cóctel.",
            "Vierte en la coctelera la ginebra y el cordial o zumo de lima con azúcar.",
            "Añade hielo abundante y bate con energía durante 12 segundos.",
            "Cuela con colador de malla fina sobre la copa bien fría.",
            "Deposita una rueda fina de lima flotando en el centro."
        ],
        "consejo_bartender": "El Gimlet original naval británico usaba cordial embotellado para combatir el escorbuto en alta mar. En casa, una combinación de zumo de lima fresco y almíbar ofrece un sabor infinitamente más vivo."
    },
    {
        "num": 35,
        "key": "black_russian",
        "nombre": "Black Russian",
        "sin_alcohol": False,
        "base_alcohol": "Vodka y licor de café",
        "metodo": "Construido con hielo",
        "cristaleria": "Vaso bajo (old fashioned / rocks)",
        "tiempo_min": 2,
        "perfil_sabor": "Café intenso, dulce y alcohólico",
        "hielo": "Cubos macizos grandes",
        "ingredientes": [
            "50 ml de vodka",
            "25 ml de licor de café (Kahlúa o licor artesano)",
            "Hielo abundante en roca"
        ],
        "preparacion": [
            "Coloca cubos de hielo grandes en el vaso bajo.",
            "Vierte primero el vodka.",
            "Añade a continuación el licor de café.",
            "Remueve lentamente durante 15 segundos para enfriar e integrar ambos licores.",
            "Sirve tal cual, sin garnish o con una cereza opcional."
        ],
        "consejo_bartender": "Un trago directo y robusto perfecto para la sobremesa: con solo dos botellas tienes un clásico nocturno sofisticado e infalible."
    },
    {
        "num": 36,
        "key": "white_russian",
        "nombre": "White Russian",
        "sin_alcohol": False,
        "base_alcohol": "Vodka, licor de café y crema",
        "metodo": "Construido en capas",
        "cristaleria": "Vaso bajo (old fashioned / rocks)",
        "tiempo_min": 3,
        "perfil_sabor": "Cremoso, café con leche dulce y sedoso",
        "hielo": "Cubos macizos",
        "ingredientes": [
            "50 ml de vodka",
            "25 ml de licor de café",
            "30 ml de nata líquida (crema para café o leche evaporada bien fría)",
            "Hielo en cubos"
        ],
        "preparacion": [
            "Llena el vaso bajo con cubos de hielo.",
            "Vierte el vodka y el licor de café, removiéndolos brevemente.",
            "Vierte la nata líquida despacio sobre el dorso de una cuchara para que flote en la superficie formando un manto blanco sobre el fondo oscuro.",
            "Sirve con una pajita corta para que el comensal decida cuándo mezclar las capas."
        ],
        "consejo_bartender": "Inmortalizado por 'El Nota' en la película El Gran Lebowski: procura que la nata esté semimontada o muy fría para que el efecto visual bicolor permanezca flotando intacto."
    },
    {
        "num": 37,
        "key": "french_75",
        "nombre": "French 75",
        "sin_alcohol": False,
        "base_alcohol": "Ginebra, zumo de limón y cava",
        "metodo": "Agitado y completado con cava",
        "cristaleria": "Copa flauta",
        "tiempo_min": 3,
        "perfil_sabor": "Cítrico, elegante, seco y efervescente",
        "hielo": "Cubos para coctelera",
        "ingredientes": [
            "30 ml de ginebra",
            "15 ml de zumo de limón fresco",
            "10 ml de jarabe de azúcar simple",
            "60 ml de cava brut muy frío",
            "1 espiral de piel de limón"
        ],
        "preparacion": [
            "En la coctelera con hielo, vierte la ginebra, el zumo de limón y el jarabe de azúcar.",
            "Bate enérgicamente durante 10 segundos.",
            "Cuela con colador fino en una copa flauta helada.",
            "Rellena con el cava brut despacio para coronar la copa con fina burbuja.",
            "Introduce la espiral de limón dentro de la flauta."
        ],
        "consejo_bartender": "Bautizado por el cañón de campaña francés de 75 mm de la Primera Guerra Mundial por su sorprendente pegada: entra como una caricia gracias al cava y la limonada."
    },
    {
        "num": 38,
        "key": "dark_and_stormy",
        "nombre": "Dark and stormy",
        "sin_alcohol": False,
        "base_alcohol": "Ron oscuro especiado y ginger beer",
        "metodo": "Construido en capas con hielo",
        "cristaleria": "Vaso alto (highball)",
        "tiempo_min": 3,
        "perfil_sabor": "Especiado, picante de jengibre y melaza",
        "hielo": "Cubos enteros",
        "ingredientes": [
            "50 ml de ron oscuro (tipo Black Seal o añejo oscuro)",
            "100 ml de cerveza de jengibre (ginger beer picante)",
            "15 ml de zumo de lima fresca",
            "1 gajo de lima para decorar"
        ],
        "preparacion": [
            "Llena el vaso alto con cubos de hielo.",
            "Vierte el zumo de lima y la cerveza de jengibre fría hasta tres cuartas partes del vaso.",
            "Vierte con delicadeza el ron oscuro sobre la superficie dejando que flote como una tormenta sombría sobre el fondo dorado.",
            "Coloca el gajo de lima en el borde.",
            "Sírvelo sin mezclar para que el comensal admire el contraste antes de remover con su pajita."
        ],
        "consejo_bartender": "El ron oscuro debe tener cuerpo y notas de melaza tostada: al flotar simula una nube de tormenta marina sobre el mar embravecido."
    },
    {
        "num": 39,
        "key": "caipiroska",
        "nombre": "Caipiroska",
        "sin_alcohol": False,
        "base_alcohol": "Vodka",
        "metodo": "Macerado y construido",
        "cristaleria": "Vaso bajo (old fashioned)",
        "tiempo_min": 4,
        "perfil_sabor": "Cítrico limpio, dulce y refrescante",
        "hielo": "Hielo picado abundante",
        "ingredientes": [
            "50 ml de vodka neutro",
            "1 lima fresca cortada en dados",
            "2 cucharaditas de azúcar blanco",
            "Hielo picado hasta el borde"
        ],
        "preparacion": [
            "Corta la lima en dados pequeños desechando la parte central blanca.",
            "Coloca los dados en el fondo del vaso bajo junto al azúcar.",
            "Maja con el mortero con firmeza para extraer el jugo sin triturar la corteza.",
            "Rellena el vaso con hielo picado hasta arriba.",
            "Vierte el vodka y remueve enérgicamente de abajo hacia arriba para que el azúcar se disuelva por completo.",
            "Corona con más hielo picado y una pajita corta."
        ],
        "consejo_bartender": "Es la alternativa cosmopolita a la caipiriña: el vodka, al ser un alcohol neutro, deja todo el protagonismo a la pureza del zumo de lima y el azúcar crujiente."
    },
    {
        "num": 40,
        "key": "amaretto_sour",
        "nombre": "Amaretto sour",
        "sin_alcohol": False,
        "base_alcohol": "Licor Amaretto y zumo de limón",
        "metodo": "Agitado simple (shake)",
        "cristaleria": "Vaso bajo (rocks)",
        "tiempo_min": 3,
        "perfil_sabor": "Almendra tostada, cítrico y agridulce",
        "hielo": "Cubos en coctelera y vaso",
        "ingredientes": [
            "50 ml de licor Amaretto (Disaronno)",
            "30 ml de zumo de limón recién exprimido y colado",
            "10 ml de bourbon (opcional, para dar cuerpo seco)",
            "15 ml de clara de huevo (opcional)",
            "1 rodaja de limón y 1 cereza al marrasquino"
        ],
        "preparacion": [
            "Pon en la coctelera el Amaretto, el zumo de limón y el chorrito de bourbon con la clara.",
            "Agita 10 segundos sin hielo para formar la crema y luego 15 segundos con hielo abundante.",
            "Cuela sobre el vaso bajo con un cubo de hielo grueso.",
            "Decora con la rodaja de limón y la cereza sobre la espuma sedosa."
        ],
        "consejo_bartender": "Añadir un golpe pequeño (10 ml) de bourbon o whisky es el truco maestro de los mejores bartenders: equilibra el dulzor del licor de almendra y aporta una redondez fabulosa."
    },
    {
        "num": 41,
        "key": "bramble",
        "nombre": "Bramble",
        "sin_alcohol": False,
        "base_alcohol": "Ginebra y licor de mora",
        "metodo": "Construido sobre hielo picado",
        "cristaleria": "Vaso bajo (rocks)",
        "tiempo_min": 4,
        "perfil_sabor": "Moras silvestres, cítrico y botánico",
        "hielo": "Hielo picado abundante",
        "ingredientes": [
            "45 ml de ginebra seca",
            "20 ml de zumo de limón recién exprimido",
            "15 ml de jarabe de azúcar simple",
            "15 ml de licor de mora (crème de mûre)",
            "2 moras frescas y 1 rodaja de limón"
        ],
        "preparacion": [
            "En la coctelera con hielo, agita la ginebra, el zumo de limón y el jarabe de azúcar durante 10 segundos.",
            "Llena el vaso bajo con abundante hielo picado.",
            "Cuela la mezcla sobre el hielo picado.",
            "Vierte despacio el licor de mora por encima en forma circular: goteará entre el hielo creando un precioso sangrado púrpura.",
            "Decora con dos moras frescas ensartadas y una rodaja de limón."
        ],
        "consejo_bartender": "Creado por Dick Bradsell en Londres en los años 80: el licor de mora debe flotar al final sin mezclarse para que al beber se combinen las capas ácidas y dulces."
    },
    {
        "num": 42,
        "key": "mai_tai",
        "nombre": "Mai Tai",
        "sin_alcohol": False,
        "base_alcohol": "Ron añejo, ron blanco y triple seco",
        "metodo": "Agitado simple (shake)",
        "cristaleria": "Vaso bajo (double old fashioned)",
        "tiempo_min": 4,
        "perfil_sabor": "Almendra, naranja, ron tostado y lima",
        "hielo": "Hielo picado abundante",
        "ingredientes": [
            "30 ml de ron blanco",
            "30 ml de ron añejo o jamaicano",
            "15 ml de licor de naranja (Cointreau o curaçao)",
            "15 ml de sirope de almendra (orgeat)",
            "25 ml de zumo de lima fresca",
            "1 ramita de menta y media lima vaciada"
        ],
        "preparacion": [
            "Coloca en la coctelera con hielo el ron blanco, el licor de naranja, el sirope de almendra y el zumo de lima.",
            "Agita con intensidad durante 12 segundos.",
            "Vierte todo (incluyendo el hielo) en el vaso bajo grande.",
            "Corona flotando por encima los 30 ml de ron añejo para un aroma tostado inicial.",
            "Decora con la ramita de menta y la cáscara de lima invertida imitando una pequeña isla tropical."
        ],
        "consejo_bartender": "Mai Tai significa 'fuera de este mundo' en tahitiano: el orgeat (jarabe de almendra) aporta la cremosidad vegetal que define su personalidad inimitable."
    },
    {
        "num": 43,
        "key": "sea_breeze",
        "nombre": "Sea breeze",
        "sin_alcohol": False,
        "base_alcohol": "Vodka, arándanos y pomelo",
        "metodo": "Construido en vaso con hielo",
        "cristaleria": "Vaso alto (highball)",
        "tiempo_min": 2,
        "perfil_sabor": "Cítrico, frutos rojos y final seco",
        "hielo": "Cubos grandes hasta arriba",
        "ingredientes": [
            "50 ml de vodka",
            "80 ml de zumo de arándanos rojos (cranberry)",
            "40 ml de zumo de pomelo rosado recién exprimido",
            "1 rodaja de lima o pomelo"
        ],
        "preparacion": [
            "Llena el vaso alto con cubos de hielo macizo.",
            "Vierte el vodka.",
            "Añade el zumo de arándanos y el zumo de pomelo.",
            "Remueve con la cuchara imperial para homogeneizar el tono rubí brillante.",
            "Decora con una rodaja de lima en el borde."
        ],
        "consejo_bartender": "Una de las combinaciones más depuradas y refrescantes que existen: el pomelo aporta el punto de acidez amarga que mitiga el dulzor de los arándanos."
    },
    {
        "num": 44,
        "key": "kir_royale",
        "nombre": "Kir Royale",
        "sin_alcohol": False,
        "base_alcohol": "Crema de cassis y cava",
        "metodo": "Construido directo en copa",
        "cristaleria": "Copa flauta de champán",
        "tiempo_min": 2,
        "perfil_sabor": "Grosella negra, elegante y burbujeante",
        "hielo": "Sin hielo (bebidas muy frías)",
        "ingredientes": [
            "15 ml de crema de cassis (licor de grosella negra de Dijon)",
            "130 ml de cava brut o champán muy frío",
            "1 mora o frambuesa fresca en el fondo (opcional)"
        ],
        "preparacion": [
            "En una copa flauta fría, vierte en el fondo la dosis de crema de cassis.",
            "Inclina levemente la copa y vierte el cava brut despacio para que la burbuja suba teñida de un lujoso color púrpura aterciopelado.",
            "No necesita remover: las finas burbujas integran ambos líquidos.",
            "Si lo deseas, deja caer una mora fresca al fondo de la copa."
        ],
        "consejo_bartender": "No abuses de la crema de cassis: solo debe teñir sutilmente el cava y dejar una suave caricia frutal sin volver empalagoso el vino espumoso."
    },
    {
        "num": 45,
        "key": "mint_julep",
        "nombre": "Mint julep",
        "sin_alcohol": False,
        "base_alcohol": "Bourbon y hierbabuena",
        "metodo": "Macerado y construido",
        "cristaleria": "Vaso metálico de julepe o vaso bajo",
        "tiempo_min": 4,
        "perfil_sabor": "Menta fresca, roble tostado y caramelo",
        "hielo": "Abundante hielo picado (montaña de hielo)",
        "ingredientes": [
            "60 ml de bourbon whisky",
            "8 a 10 hojas de menta fresca",
            "15 ml de jarabe de azúcar simple",
            "Montaña de hielo picado",
            "Un ramillete frondoso de menta para coronar"
        ],
        "preparacion": [
            "En el vaso metálico o de cristal, deposita la menta y el jarabe simple.",
            "Presiona delicadamente con el mortero para liberar el aceite mentolado sin machacar en exceso.",
            "Llena el vaso hasta la mitad con hielo picado y vierte la mitad del bourbon. Remueve con la cuchara hasta que el exterior del vaso empiece a sudar frío.",
            "Llena con más hielo picado hasta el borde y vierte el resto del bourbon.",
            "Corona con una cúpula de hielo picado y un ramillete generoso de menta espolvoreado con una nube de azúcar glas."
        ],
        "consejo_bartender": "El vaso metálico de julepe no es capricho: transmite el frío de inmediato formando una capa de escarcha blanca helada en el exterior que mantiene el trago gélido durante horas."
    },
    {
        "num": 46,
        "key": "sol_y_sombra",
        "nombre": "Sol y sombra",
        "sin_alcohol": False,
        "base_alcohol": "Anís dulce y brandy español",
        "metodo": "Construido directo",
        "cristaleria": "Copa de licor o vaso corto tradicional",
        "tiempo_min": 2,
        "perfil_sabor": "Anisado, dulce, cálido y amaderado",
        "hielo": "Sin hielo o con 1 cubito al gusto",
        "ingredientes": [
            "25 ml de anís dulce (tipo Anís del Mono)",
            "25 ml de brandy español (tipo Solera Reserva)",
            "Hielo opcional según preferencia"
        ],
        "preparacion": [
            "En la copa pequeña o vasito de chupito ancho, vierte el anís dulce (el 'sol').",
            "Añade a continuación en partes iguales el brandy español (la 'sombra').",
            "Remueve con un ligero giro de muñeca para amalgamar la transparencia anisada con la tonalidad caoba del brandy.",
            "Degusta a temperatura ambiente o añade una piedra de hielo para disfrutarlo con trago largo y fresco."
        ],
        "consejo_bartender": "Es el trago castizo por excelencia de los bares y tabernas históricas de España: el anís aporta el azúcar floral y el brandy la estructura añeja de roble."
    },
    {
        "num": 47,
        "key": "sidecar",
        "nombre": "Sidecar",
        "sin_alcohol": False,
        "base_alcohol": "Brandy o coñac y licor de naranja",
        "metodo": "Agitado simple (shake)",
        "cristaleria": "Copa cóctel (coupette) escarchada",
        "tiempo_min": 3,
        "perfil_sabor": "Cítrico, naranja dulce, roble y seco",
        "hielo": "Cubos para la coctelera",
        "ingredientes": [
            "50 ml de coñac o brandy español",
            "20 ml de licor de naranja (Cointreau o triple seco)",
            "20 ml de zumo de limón recién exprimido y colado",
            "Azúcar blanco para escarchar el borde",
            "1 twist de piel de naranja"
        ],
        "preparacion": [
            "Pasa un gajo de limón por la mitad del borde de la copa y pásalo por azúcar para crear un ribete dulce.",
            "En la coctelera con hielo, vierte el coñac o brandy, el licor de naranja y el zumo de limón.",
            "Bate enérgicamente durante 12 segundos.",
            "Cuela con doble colador fino sobre la copa preparada.",
            "Perfuma la copa con el twist de naranja y déjalo caer dentro."
        ],
        "consejo_bartender": "El ribete de azúcar en el borde exterior contrasta de forma magistral con la acidez vivaz del limón y la solera profunda del destilado."
    },
    {
        "num": 48,
        "key": "irish_coffee",
        "nombre": "Café irlandés (Irish coffee)",
        "sin_alcohol": False,
        "base_alcohol": "Whisky irlandés, café y nata",
        "metodo": "Construido en capas templadas",
        "cristaleria": "Copa de cristal templado",
        "tiempo_min": 5,
        "perfil_sabor": "Café tostado caliente, whisky y nata sedosa",
        "hielo": "Sin hielo (cóctel caliente)",
        "ingredientes": [
            "40 ml de whisky irlandés",
            "120 ml de café solo caliente recién hecho",
            "1 a 2 cucharaditas de azúcar moreno",
            "40 ml de nata líquida fría ligeramente semimontada",
            "Cacao puro en polvo o ralladura de nuez moscada"
        ],
        "preparacion": [
            "Templa la copa con agua caliente durante 1 minuto y vacíala.",
            "Añade el azúcar moreno y el whisky irlandés en el fondo.",
            "Vierte el café caliente y remueve bien hasta que el azúcar se disuelva íntegramente.",
            "Bate la nata líquida en un bote o con varilla durante 15 segundos hasta que espese pero siga siendo líquida.",
            "Vierte la nata lentamente sobre el dorso de una cuchara caliente sobre la superficie del café.",
            "Espolvorea una pizca de cacao en polvo sobre la crema blanca."
        ],
        "consejo_bartender": "No bebas con pajita ni mezcles la nata con el café: el placer inimitable del auténtico café irlandés consiste en tomar el café caliente y alcohólico a través de la capa de nata fría."
    },
    {
        "num": 49,
        "key": "padrino",
        "nombre": "Padrino (Godfather)",
        "sin_alcohol": False,
        "base_alcohol": "Whisky escocés y licor de almendra",
        "metodo": "Construido y refrescado",
        "cristaleria": "Vaso bajo (old fashioned / rocks)",
        "tiempo_min": 2,
        "perfil_sabor": "Ahumado, almendra dulce y aterciopelado",
        "hielo": "Una roca de hielo grande",
        "ingredientes": [
            "45 ml de whisky escocés (Blended o Single Malt suave)",
            "25 ml de licor Amaretto",
            "1 roca de hielo grande",
            "1 twist de piel de naranja (opcional)"
        ],
        "preparacion": [
            "Coloca una roca de hielo grande y limpia en el vaso bajo.",
            "Vierte el whisky escocés.",
            "Añade el licor Amaretto.",
            "Remueve pausadamente con la cuchara de bar durante unos 20 segundos para que ambos licores se fundan y se enfríen.",
            "Si lo deseas, pasa una piel de naranja por el borde del vaso para aportar una nota cítrica fresca."
        ],
        "consejo_bartender": "Con solo dos ingredientes, el Padrino demuestra la magia del equilibrio: la turba y la madera del whisky escocés quedan abrazadas por la golosidad de la almendra dulce."
    },
    {
        "num": 50,
        "key": "laguna_azul",
        "nombre": "Laguna azul (Blue lagoon)",
        "sin_alcohol": False,
        "base_alcohol": "Vodka y licor de curaçao azul",
        "metodo": "Construido en vaso con hielo",
        "cristaleria": "Vaso alto (highball) o copa huracán",
        "tiempo_min": 3,
        "perfil_sabor": "Cítrico, naranja dulce y electrizante",
        "hielo": "Cubos macizos",
        "ingredientes": [
            "40 ml de vodka",
            "20 ml de licor Blue Curaçao (curaçao azul)",
            "15 ml de zumo de limón recién exprimido",
            "100 ml de refresco de lima-limón (Sprite o gaseosa)",
            "1 rodaja de limón y 1 cereza de cóctel"
        ],
        "preparacion": [
            "Llena el vaso alto con cubos de hielo hasta arriba.",
            "Vierte el vodka, el licor Blue Curaçao y el zumo de limón recién exprimido.",
            "Rellena despacio con el refresco de lima-limón frío.",
            "Remueve suavemente con la cuchara para repartir el espectacular color azul eléctrico.",
            "Decora con una rodaja de limón encajada en el borde y una cereza de cóctel."
        ],
        "consejo_bartender": "Creado por Andy MacElhone en el Harry's New York Bar de París: su impactante color azul tropical y su perfil cítrico lo convierten en un éxito garantizado en fiestas y reuniones caseras."
    },
    {
        "num": 51,
        "key": "calimocho",
        "nombre": "Calimocho (Kalimotxo)",
        "sin_alcohol": False,
        "base_alcohol": "Vino tinto y refresco de cola",
        "metodo": "Construido en el vaso con hielo",
        "cristaleria": "Vaso de sidra o vaso alto",
        "tiempo_min": 2,
        "perfil_sabor": "Afrutado, dulce, burbujeante y refrescante",
        "hielo": "Abundantes cubos macizos",
        "ingredientes": [
            "100 ml de vino tinto joven (con buen cuerpo)",
            "100 ml de refresco de cola bien frío",
            "Abundante hielo macizo en cubos",
            "1 rodaja de limón fresco (opcional: toque de licor de mora)"
        ],
        "preparacion": [
            "Llena un vaso ancho de sidra o vaso alto con abundante hielo macizo hasta arriba.",
            "Vierte primero el vino tinto joven.",
            "Añade despacio el refresco de cola frío para no romper la burbuja.",
            "Remueve con un solo movimiento suave de cuchara de abajo hacia arriba para integrar.",
            "Decora con una rodaja de limón fresco en el interior o en el borde."
        ],
        "consejo_bartender": "Nacido en el Puerto Viejo de Algorta en los años 70: la proporción áurea es 50/50, servido obligatoriamente con hielo muy abundante para que no pierda frescura ni carbónico."
    }
]
