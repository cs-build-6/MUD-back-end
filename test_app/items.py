weapons = ['dagger', 'katana', 'knife', 'longsword', 'sabre', 'shortsword',
            'rapier', 'battle axe','club','flail','mace','quarterstaff','war hammer',
            'yo-yo','frisbee', 'boomerang']

wearables = ['robe', 'gloves', 'ring', 'amulet', 'necklace', 'boots', 'belt', 'cloak',
                'shirt','jeans', 't-shirt', 'sneakers']

skill = ['speed','strength','power', 'skill', 'invisibility','persuasion',
            'thought','nothing in particular', 'who knows what', 'mystery', 'destiny']

nouns = weapons + wearables


import random
class item:
  def __init__(self, noun=None, skill = None, item_room = None, owner = None):
    self.id = id
    self.noun = noun
    self.skill = skill
    self.item_room = item_room
    self.owner = owner 

  

class item_set:
  def __init__(self):
    self.item_dict = {}
    
  def gen_item(self):
    self.item_dict[len(self.item_dict.keys())] = item(random.choice(nouns),random.choice(skill))

  def gen_n_items(self,n):
    for i in range(n):
      self.gen_item()

