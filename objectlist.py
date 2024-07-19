from random import choice

objects = [
    "yogurt",
"cup",
"kettle",
"golf cart",
"watch",
"medal",
"envelope",
"jacket",
"stamp",
"soybeans",
"olive",
"celery",
"coral",
"octopus",
"earrings",
"mussel",
"lychee",
"ladder",
"yam",
"shirt",
"rum",
"pen",
"pancake",
"cauliflower",
"car",
"tuna",
"phone",
"drill",
"bell pepper",
"bowl",
"chisel",
"snowmobile",
"sardine",
"mop",
"muffin",
"camcorder",
"sunflower seed",
"socks",
"train",
"tie",
"hazelnut",
"peeler",
"champagne",
"saw",
"calculator",
"gloves",
"smartwatch",
"magazine",
"plate",
"rock",
"paintbrush",
"starfish",
"passion fruit",
"lentils",
"pinecone",
"lobster",
"board game",
"peas",
"lemonade",
"blanket",
"turkey",
"sleeping bag",
"utility knife",
"pot",
"tape measure",
"paint roller",
"hammer",
"whiteboard",
"compass",
"game console",
"kombucha",
"white beans",
"paper clip",
"skirt",
"tangerine",
"kite",
"toy",
"power bank",
"poppy seed",
"table",
"jeans",
"oats",
"green beans",
"clipboard",
"cactus",
"blueberry",
"rhubarb",
"raspberry",
"flaxseed",
"pajamas",
"fern",
"kiwi",
"prawn",
"watermelon",
"yacht",
"pie",
"haddock",
"lemon",
"lichen",
"first aid kit",
"coat",
"phone charger",
"blackberry",
"leaf",
"oyster",
"gin",
"clamp",
"pineapple",
"boat",
"leek",
"television",
"blender",
"cutting board",
"binder",
"binoculars",
"tablet",
"level",
"chia seed",
"broccoli",
"fig",
"pencil",
"scone",
"food processor",
"trout",
"colander",
"vodka",
"pear",
"brazil nut",
"juice",
"bagel",
"sweet potato",
"skateboard",
"apricot",
"toaster",
"broom",
"lip balm",
"musical instrument",
"pistachio",
"edamame",
"seaweed",
"navy beans",
"crowbar",
"laptop",
"jet ski",
"pinto beans",
"keyboard",
"vice",
"bus",
"avocado",
"hat",
"lime",
"salmon",
"printer",
"iron",
"date",
"rice",
"mixer",
"wardrobe",
"barley",
"venison",
"sausage",
"cod",
"scrapbook",
"orange",
"spoon",
"papaya",
"cherry",
"kale",
"wrench",
"bicycle pump",
"dragon fruit",
"duck",
"beef",
"sesame seed",
"smartphone",
"shrimp",
"VR headset",
"banana",
"hairbrush",
"fork",
"fishing rod",
"cobblestone",
"beetroot",
"eggplant",
"remote control",
"book",
"bok choy",
"scarf",
"pumpkin seed",
"microwave",
"cashew",
"ironing board",
"brussels sprouts",
"shell",
"strawberry",
"hovercraft",
"camping tent",
"onion",
"motorcycle",
"adjustable wrench",
"heater",
"pillow",
"basket",
"fitness tracker",
"grape",
"doughnut",
"cream",
"pan",
"ginger",
"desk",
"computer",
"hot air balloon",
"water",
"chestnut",
"hand saw",
"jackfruit",
"cuttlefish",
"bun",
"couscous",
"sofa",
"jalapeno",
"potato",
"submarine",
"pecan",
"cabbage",
"tart",
"peanut",
"vegetable",
"carpet",
"hiking boots",
"lamp",
"peach",
"mango",
"knife",
"putty knife",
"waffle",
"highlighter",
"macadamia",
"stapler",
"tongs",
"bracelet",
"mushroom",
"whiskey",
"scallop",
"feather",
"radish",
"charger",
"model car",
"roll",
"chess set",
"smart speaker",
"chickpeas",
"umbrella",
"watercress",
"butter",
"wallet",
"tree",
"guava",
"pork",
"GPS device",
"elderberry",
"pumpkin",
"tequila",
"cheese",
"salami",
"black beans",
"ham",
"whisk",
"acorn",
"apple",
"steak",
"cornmeal",
"cucumber",
"bacon",
"crab",
"sweater",
"flower",
"soda",
"glasses",
"notebook",
"headphones",
"water bottle",
"postcard",
"airplane",
"milkshake",
"parsnip",
"necklace",
"ice cream",
"coconut",
"almond",
"handbag",
"screwdriver",
"sculpture",
"vacuum cleaner",
"milk",
"mouse",
"spatula",
"corn",
"ruler",
"smoothie",
"anchovy",
"wheat",
"cranberry",
"pliers",
"ribs",
"quinoa",
"flashlightvase",
"clock",
"sunglasses",
"segway",
"turnip",
"persimmon",
"bluetooth headset",
"trophy",
"keys",
"tea",
"refrigerator",
"newspaper",
"liqueur",
"belt",
"allen wrench",
"plum",
"robe",
"shorts",
"bed",
"squid",
"cider",
"durian",
"bread",
"beer",
"shoes",
"artichoke",
"kidney beans",
"cake",
"red beans",
"e-reader",
"ring",
"blouse",
"lettuce",
"backpack",
"speaker",
"coffee maker",
"spinach",
"shredder",
"scooter",
"measuring cup",
"projector",
"sailboat",
"walnut",
"pants",
"fan",
"moss",
"sand",
"tofu",
"wine",
"dress",
"pastry",
"chili pepper",
"bicycle",
"asparagus",
"chair",
"eel",
"cookie",
"slippers",
"pomegranate",
"canvas",
"chicken",
"digital camera",
"grapefruit",
"biscuit",
"tractor",
"garlic",
"starfruit",
"brandy",
"mirror",
"grater",
"bicycle helmet",
"file folder",
"squash",
"mackerel",
"suit",
"dustpan",
"carrot",
"clam",
"coffee",
"puzzle",
"croissant",
"brownie",
"swimsuit",
"truck",
"camera",
"lamb",
"curtain",
"tomato",
"yo-yo"
]

def rand_word():
    word = choice(objects)
    return word