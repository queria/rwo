from datetime import datetime

class Effect(object):
    def __init__(self, classes, properties):
        self.classes = classes
        self.properties = properties
        self.properties_lower = [p.lower() for p in properties]

class Rune(object):
    def __init__(self, name, clvl, ilvl, rarity, effects):
        self.name = name
        self.clvl = clvl
        self.rarity = rarity
        self.effects = effects

class Word(object):

    def __init__(self, name, clvl, ladder, runes, classes, effects):
        self.name = name
        self.clvl = clvl
        self.ladder = ladder
        self.runes = runes
        self.classes = classes
        self.effects = effects

    def in_effects(self, text):
        for e in self.effects:
            for p in e.properties_lower:
                if text in p:
                    return True
        return False

    def in_classes(self, classes):
        for c in self.classes:
            if c in classes:
                return True
        return False

    def from_runes(self, available_runes):
        for r in self.runes:
            if not r in available_runes:
                return False
        return True

class RWO(object):
    def __init__(self, runes, words):
        self.words = words
        self.runes = runes
        self._rune_classes = []
        self._item_classes = []
        self.log = [datetime.now()]

    def all_words(self):
        return self.words

    def all_runes(self):
        return self.runes

    def search_words(self, runes=[], classes=[], clvl_min=1, clvl_max=99,
            fulltext='', runecount=0, inname=''):
        words = self.words
        if runecount:
            words = [w for w in words if len(w.runes) == runecount]
        if runes:
            words = [w for w in words if w.from_runes(runes)]
        if classes:
            classes = self._expand_classes(classes)
            words = [w for w in words if w.in_classes(classes)]
        if clvl_min > 1:
            words = [w for w in words if w.clvl >= clvl_min]
        if clvl_max < 99:
            words = [w for w in words if w.clvl <= clvl_max]
        if fulltext:
            fulltext_lower = fulltext.lower()
            ft_inrunes = [w for w in words if
                fulltext_lower in [r.lower() for r in w.runes]]
            ft_ineffect = [w for w in words if w.in_effects(fulltext_lower)]
            ft_inname = [w for w in words if fulltext_lower in w.name.lower()]
            words = [w for w in words if (
                (w in ft_inrunes)
                or
                (w in ft_ineffect)
                or
                (w in ft_inname))]

        #return [w for w in self.words if not w in words]
        return words

    def all_runes_by_rarity(self):
        runes = {'common':[],'semi-rare':[],'rare':[]}
        for r in self.runes:
            runes[r.rarity].append(r)
        return [{'name':rn,'runes':runes[r]}
                for r,rn in [('common','common'),
                    ('semi-rare','semi-rare'),
                    ('rare', 'extremely rare')]]

    def all_item_classes(self):
        if not self._item_classes:
            self._item_classes = [
                    {'name':'Armors', 'cats':['Defence']},
                    {'name':'Shields', 'cats':['Defence']},
                    {'name':'Helms', 'cats':['Defence']},
                    {'name':'Axes', 'cats':['Weapons','Melee']},
                    {'name':'Claws', 'cats':['Weapons','Melee']},
                    {'name':'Clubs', 'cats':['Weapons','Melee']},
                    {'name':'Daggers', 'cats':['Weapons','Melee']},
                    {'name':'Hammers', 'cats':['Weapons','Melee']},
                    {'name':'Maces', 'cats':['Weapons','Melee']},
                    {'name':'Orbs', 'cats':['Weapons','Melee']},
                    {'name':'Polearms', 'cats':['Weapons','Melee']},
                    {'name':'Scepters', 'cats':['Weapons','Melee']},
                    {'name':'Spears', 'cats':['Weapons','Melee']},
                    {'name':'Staves', 'cats':['Weapons','Melee']},
                    {'name':'Swords', 'cats':['Weapons','Melee']},
                    {'name':'Wands', 'cats':['Weapons','Melee']},
                    {'name':'Bows', 'cats':['Weapons', 'Missile']},
                    {'name':'Crossbows', 'cats':['Weapons', 'Missile']}
                ]
        return self._item_classes

    def _expand_classes(self, classes):
        all = self.all_item_classes()
        expanded = []
        for c in all:
            if c['name'] in classes:
                expanded.append(c['name'])
                expanded.extend(c['cats'])
        return list(set(expanded))


