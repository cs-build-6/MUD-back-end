castle_dict = {'Sights':['a flagstone floor', 'stone block walls', 'a reinforced wooden door', 
                'narrow slit windows high on wall', 'castle banners', 'lanterns along the walls', 
                'racks with weapons sharpened spears', 'tables holding feasts','a vast fireplace'],
               'Sounds':['the clink of metal', 'hammer hitting steel', 'the hiss of steam', 
               'crackle of flame', 'the grinding rasp of metal against the granite sharpening wheel', 
               'chain links clinking', 'the quiet crumple sound of leather creasing', 
               'heavy boots against the stone floor', 'grunts'],
                'Smells':['the tang of metal', 'smoke', 'cold stone', 'wax melting', 'gunpowder and a whiff of cordite', 
                'soot', 'blood', 'polished wood', 'sweat'],
                'Touch':['an icy draft','the warm glow of a fire','death in the air'],
               'Paths': [' stone door', ' wooden door', ' passageway',' doorway'],
               'Up':[' stone staircase', ' a wooden ladder', 'a hatch'],
               'Down':[' stone staircase', ' a wooden ladder', 'a trap door'],
               'How' : ['runs', 'leads', 'goes', 'bears']}

forest_dict = {'Sights':['fallen trees', 'logs', 'branches', 'twigs', 'fallen leaves', 'ferns', 'underbrush', 'moss', 'brambles', 'thickets', 'ivy', 'berry bushes', 'pine needles', 'pine cones', 'acorns', 'insects', 'rabbits', 'birds', 'squirrels', 'lizards', 'mice', 'foxes', 'spider webs', 'deer'],
               'Sounds':['branches creaking', 'feet shuffling through detritus', 'squirrels chattering', 'leaves rustling', 'wind whistling around trunks', 'wind disturbing the leaves', 'birds singing', 'insects humming', 'insects churring', 'rustle of animals rooting in underbrush', 'scrabbling of lizards on tree bark'],
                'Smells':['sweet pines', 'wildflowers', 'an earthy smell', 'animal scents', 'rotting wood', 'fresh rain', 'scents on the wind', 'wood smoke', 'wild mint', 'wild herbs', 'decay', 'bogs', 'stagnant pools of water', 'dead animals',
                          'earthy air', 'sweet berries', 'nuts', 'wild onions', 'wild mint'],
                'Touch':['the kiss of falling leaves', 'uneven ground beneath your feet', 'a tangle of roots underfoot', 'the prickle of briars', 'twigs snagging at your hair', 'the tickle of hanging moss', 'a spider web\'s strands brushing your skin'],
               'Paths': [' muddy path', 'n overgrown foot path', ' dusty track',' hidden trail'],
               'Up':[' branch ladder', 'thick dangling vine'],
               'Down':[' muddy hole', ' slippery slope'],
               'How' : ['runs', 'leads', 'goes', 'points']}

mountain_dict = {'Sights':['uneven stone', 'crags', 'jagged cliffs', 'shale', 'scree', 'granite', 'moss', 
                            'a winding treeline', 'whispy clouds', 'mist in the valley below', 
                             'sheer ravines', 'a thundering waterfall', 'deep snow', 'hawks', 'eagles',
                              'ravens', 'falcons', 'owls', 'bighorn sheep', 'rock slides'],
               'Sounds':['wind whistling along the slopes', 'animal howls', 'rustling leaves', 
               'frothing waterfalls', 'water trickling into snow melt', 'scree shifting underfoot', 
               'rockfalls', 'birds calling', 'animals pattering through the underbrush', 'branches snapping'],
                'Smells':['pine needles', 'crisp air', 'clean water', 'earthy moss', 'rotting logs', 
                'wet rock', 'wildflower blossoms'],
                'Touch':[' the cold unyielding stone', 'a sharp breeze', 'dust getting in your eyes', 
                'spongy moss underfoot', 'prickling pine needles caught in your boot', 
                'slippery shale underfoot'],
               'Paths': [' rocky path', ' stony road', ' granite track',' slppery trail'],
               'Up':[' climbable rock face', ' rocky switchback'],
               'Down':[' climbable rock face', ' rocky switchback'],
               'How' : ['runs', 'leads', 'goes', 'points']}

sewers_dict = {'Sights':['curved cement walls', 'rusted metal grates', 'pipes', 'standing water',
                'graffiti', 'mold', 'mildew', 'stagnant water', 'waterlogged garbage',
                'the beam of a flashlifht in the distance'],
               'Sounds':['dripping water', 'splashes', 'squeaking rats', 'faint echos', 
               'footsteps', 'the noise of the city above', 'street sounds', 'gurgling water', 'running water'],
                'Smells':['something indescribably awful','raw sewage','noxious fumes',
                'fetid detritis', 'foul-smelling effluent','evil-smelling' ,'rank waste'],
                'Touch':['water seeping into your boots', 'cold water soaking your clothing', 
                'rats running over your boots', 'your hand brush a slimy wall', 
                'something brush against your legs'],
               'Paths': [' tunnel', ' raised walkway', 'n archway',' slppery trail'],
               'Up':[' manhole', ' ladder'],
               'Down':[' pipe', ' rocky switchback'],
               'How' : ['runs', 'leads', 'goes', 'branches off']}


city_dict = {'Sights':['cramped wooden stalls', 'a dirty water fountain', 'a blacksmith hammering'
                        'people rushing here and there','streets overflowing with life'],
               'Sounds':['frenzied haggling', 'serious bartering', 'sellers hawking wares', 'people calling out to friends',
                'laughter', 'chickens clucking', 'creaking wagons' , 'the clop of horse hooves'],
                'Smells':['spices', 'grilling meats', 'baking bread', 'sweat', 'smoke', 'over-ripe fruit',
                 'manure', 'leather', 'perfume', 'ale'],
                'Touch':['cobbles underfoot', 'the press of the crowd'],
               'Paths': [' alleyway', ' cobbled street', ' archway',' passageway'],
               'Up':[' stone staircase', ' ladder'],
               'Down':[' stone staircase', ' ladder'],
               'How' : ['runs', 'leads', 'goes', 'branches off']}

caves_dict = {'Sights':['stone walls', 'a dirt floor', 'tree roots', 'dead leaves', 'campfire remains',
                 'animal scat', 'old bones', 'bats sleeping', 'spiders', 'webs', 'insects', 'earthworms',
                  'stalactites hanging from the ceiling', 'stalagmites protruding from the floor'],
               'Sounds':['wind whistling around stone', 'the muffled sound of wind in trees outside', 
               'echoes', 'the skitter of animals', 'insects whirring', 'bat wings fluttering', 
               'water dripping', 'a campfire crackling'],
                'Smells':['animal musk', 'rotting vegetation', 'stale air', 'stagnant standing water',
                 'the briny smell of slimy lichen', 'woodsmoke' ],
                'Touch':[' the walls closing in around you', 'your hand scraping against the wall'],
               'Paths': [' mysterious archway', ' darker cave', ' tunnel',' passageway'],
               'Up':[' stone hole', ' ladder'],
               'Down':[' crevice', ' slippery slope'],
               'How' : ['runs', 'leads', 'goes', 'branches off']}

mines_dict = {'Sights':['rough rock walls', 'thick cracked support beams' , 'dust', 'rock crumbles', 
                'old broken picks', 'bits of chain', 'rusted nails', 'old rails for carts', 
                'a rusted broken handcart',  'pools of standing water', 'a dead canary'],
               'Sounds':['distant echos', 'boots on rock', 'loose stone crumbling', 'creaking', 
               'shifting timber', 'dripping water', 'amplified sounds from outside through the rock' ,
               'heavier breathing'],
                'Smells':['stale, moist air', 'cold stone', 'must', 'mildew', 'sweat'],
                'Touch':['cold, slippery rock against your hand', 'back pain from crouching down',
                 'the slip of perspiration down the back of your neck', 
                 'your knuckles grazing the rock'],
               'Paths': [' wooden archway', ' darker cave', ' tunnel',' track'],
               'Up':[' trap door', ' ladder'],
               'Down':[' crevice', ' trap door'],
               'How' : ['runs', 'leads', 'goes', 'branches off']}

dungeon_dict = {'Sights':['shadows', 'cells', 'stone walls', 'stone floors', 'filthy straw scattered across the floor', 
                'chains fixed to walls', 'rats', 'flickering torchlight', 'iron bars', 'spiders', 
                'beetles', 'bones',  'old empty barrels'],
               'Sounds':['weeping','iron bars slamming shut', 'the creak of leather', 'chains clinking', 
               'the squeak of rats foraging','the hiss of steam', 'the crack of a whip', 
               'rattling chains', 'labored breathing', 'iron doors swinging'],
                'Smells':['desperation','smoke','decay','cold stone','decay'],
                'Touch':['the depths calling to you','the pull of the abyss','the sweat running down your forehead',
                'slightly queasy','unusual'],
               'Paths': [' passageway', 'n ominous stone archway', ' tunnel',' narrow doorway'],
               'Up':[' trap door', ' ladder'],
               'Down':[' manhole', ' trap door'],
               'How' : ['runs', 'leads', 'goes', 'branches off']}


all_regions = {'in a castle':castle_dict, 'in a forest':forest_dict, 'on a mountain' : mountain_dict,
                'in the sewers' : sewers_dict, 'in a city':city_dict, 'in an endless cave': caves_dict,
                'in an old abandoned mine': mines_dict, 'in a dungeon': dungeon_dict}