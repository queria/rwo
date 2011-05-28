from rwo import Rune, Effect, Word

runes = []
runes.append( Rune("El", 11, 11, "common", [
	Effect(['Weapon'],['+50 AR', ' +1 Light Radius']),
	Effect(['Armor', 'Helm', 'Shield'],['+1 Light Radius', ' +15 Defense'])
	]) )
runes.append( Rune("Eld", 11, 11, "common", [
	Effect(['Weapon'],['+75% Damage vs. Undead', ' +50 Attack Rating vs. Undead *']),
	Effect(['Armor', 'Helm'],['Lowers Stamina drain by 15%']),
	Effect(['Shield'],['+7% Blocking'])
	]) )
runes.append( Rune("Tir", 13, 13, "common", [
	Effect(['Weapon'],['+2 Mana Per Kill']),
	Effect(['Armor', 'Helm', 'Shield'],['+2 Mana Per Kill.'])
	]) )
runes.append( Rune("Nef", 13, 13, "common", [
	Effect(['Weapon'],['Knockback']),
	Effect(['Armor', 'Helm', 'Shield'],['+30 Defense vs. Missile'])
	]) )
runes.append( Rune("Eth", 15, 15, "common", [
	Effect(['Weapon'],['-25% Target Defense']),
	Effect(['Armor', 'Helm', 'Shield'],['Regenerate Mana 15%'])
	]) )
runes.append( Rune("Ith", 15, 15, "common", [
	Effect(['Weapon'],['+9 to Maximum Damage']),
	Effect(['Armor', 'Helm', 'Shield'],['15% Damage Taken Goes to Mana'])
	]) )
runes.append( Rune("Tal", 17, 17, "common", [
	Effect(['Weapon'],['75 Poison damage over 5 seconds']),
	Effect(['Armor', 'Helm', 'Shield'],['+35% Poison Resistance'])
	]) )
runes.append( Rune("Ral", 19, 19, "common", [
	Effect(['Weapon'],['+5-30 Fire Damage']),
	Effect(['Armor', 'Helm', 'Shield'],['+35% Fire Resistance'])
	]) )
runes.append( Rune("Ort", 21, 21, "common", [
	Effect(['Weapon'],['+1-50 Lightning Damage']),
	Effect(['Armor', 'Helm', 'Shield'],['+35% Lightning Resistance'])
	]) )
runes.append( Rune("Thul", 23, 23, "common", [
	Effect(['Weapon'],['+3-14 Cold Damage (Cold Length 3 seconds)']),
	Effect(['Armor', 'Helm', 'Shield'],['+35% Cold Resistance'])
	]) )
runes.append( Rune("Amn", 25, 25, "common", [
	Effect(['Weapon'],['7% Life Stolen Per Hit']),
	Effect(['Armor', 'Helm', 'Shield'],['Attacker takes 14 damage'])
	]) )
runes.append( Rune("Sol", 27, 27, "semi-rare", [
	Effect(['Weapon'],['+9 to Minimum Damage']),
	Effect(['Armor', 'Helm', 'Shield'],['-7 Damage Taken'])
	]) )
runes.append( Rune("Shael", 29, 29, "semi-rare", [
	Effect(['Weapon'],['Faster Attack Rate (+20)']),
	Effect(['Armor', 'Helm'],['Faster Hit Recovery (+20)']),
	Effect(['Shields'],['Faster Block Rate (+20)'])
	]) )
runes.append( Rune("Dol", 31, 31, "semi-rare", [
	Effect(['Weapon'],['25% Chance that Hit Causes Monster to Flee']),
	Effect(['Armor', 'Helm', 'Shield'],['+7 Replenish Life'])
	]) )
runes.append( Rune("Hel", 0, 33, "semi-rare", [
	Effect(['Weapon'],['-20% Requirements']),
	Effect(['Armor', 'Helm', 'Shield'],['-15% Requirements'])
	]) )
runes.append( Rune("Io", 35, 35, "semi-rare", [
	Effect(['Weapon'],['+10 Vitality']),
	Effect(['Armor', 'Helm', 'Shield'],['+10 Vitality'])
	]) )
runes.append( Rune("Lum", 37, 37, "semi-rare", [
	Effect(['Weapon'],['+10 Energy']),
	Effect(['Armor', 'Helm', 'Shield'],['+10 Energy'])
	]) )
runes.append( Rune("Ko", 39, 39, "semi-rare", [
	Effect(['Weapon'],['+10 Dexterity']),
	Effect(['Armor', 'Helm', 'Shield'],['+10 Dexterity'])
	]) )
runes.append( Rune("Fal", 41, 41, "semi-rare", [
	Effect(['Weapon'],['+10 Strength']),
	Effect(['Armor', 'Helm', 'Shield'],['+10 Strength'])
	]) )
runes.append( Rune("Lem", 43, 43, "semi-rare", [
	Effect(['Weapon'],['+75% Extra Gold from Monsters']),
	Effect(['Armor', 'Helm', 'Shield'],['+50% Extra Gold from Monsters'])
	]) )
runes.append( Rune("Pul", 45, 45, "semi-rare", [
	Effect(['Weapon'],['+75% Damage to Demons', ' +100 AR against Demons'])
	]) )
runes.append( Rune("Um", 47, 47, "semi-rare", [
	Effect(['Weapon'],['25% Chance of Open Wounds']),
	Effect(['Armor', 'Helm'],['+15% Resist All']),
	Effect(['Shields'],['+22% Resist All'])
	]) )
runes.append( Rune("Mal", 49, 49, "rare", [
	Effect(['Weapon'],['Prevent Monster Healing']),
	Effect(['Armor', 'Helm', 'Shield'],['Reduce Magic Damage by 7'])
	]) )
runes.append( Rune("Ist", 51, 51, "rare", [
	Effect(['Weapon'],['+30% Better Chance of Finding Magical Items']),
	Effect(['Armor', 'Helm', 'Shield'],['+25% Better Chance of Finding Magical Items'])
	]) )
runes.append( Rune("Gul", 53, 53, "rare", [
	Effect(['Weapon'],['+20% AR']),
	Effect(['Armor', 'Helm', 'Shield'],['+5 to Max Resist Poison'])
	]) )
runes.append( Rune("Vex", 55, 55, "rare", [
	Effect(['Weapon'],['7% Mana Leech']),
	Effect(['Armor', 'Helm', 'Shield'],['+5 to Max Fire Resist'])
	]) )
runes.append( Rune("Ohm", 57, 57, "rare", [
	Effect(['Weapon'],['+50% Damage']),
	Effect(['Armor', 'Helm', 'Shield'],['+5 to Max. Resist Cold'])
	]) )
runes.append( Rune("Lo", 59, 59, "rare", [
	Effect(['Weapon'],['20% Chance of Deadly Strike']),
	Effect(['Armor', 'Helm', 'Shield'],['+5 to Max. Resist Lightning'])
	]) )
runes.append( Rune("Sur", 61, 61, "rare", [
	Effect(['Weapon'],['20% Chance of Hit Blinds Target']),
	Effect(['Armor', 'Helm'],['+5% total Mana']),
	Effect(['Shields'],['+50 Mana'])
	]) )
runes.append( Rune("Ber", 63, 63, "rare", [
	Effect(['Weapon'],['20% Chance of Crushing Blow']),
	Effect(['Armor', 'Helm', 'Shield'],['Damage Reduced by 8%'])
	]) )
runes.append( Rune("Jah", 65, 65, "rare", [
	Effect(['Weapon'],['Ignores Target Defense']),
	Effect(['Armor', 'Helm'],['+5% of total Hit Points']),
	Effect(['Shields'],['+50 Hit Points'])
	]) )
runes.append( Rune("Cham", 67, 67, "rare", [
	Effect(['Weapon'],['32% Chance of Hit Freezing Target for 3 seconds']),
	Effect(['Armor', 'Helm', 'Shield'],['Cannot be Frozen'])
	]) )
runes.append( Rune("Zod", 69, 69, "rare", [
	Effect(['Weapon'],['Indestructible']),
	Effect(['Armor', 'Helm', 'Shield'],['Indestructible'])
	]) )

words = []
words.append( Word("Ancient's Pledge", 21, False, ['Ral', 'Ort', 'Tal'], 
	['Shields'],
	[ Effect(['Shields'], ['+43% Cold Resistance', '+48% Fire/Lightning/Poison Resistance', '10% Damage Taken Goes to Mana', '+50% ED']) ]
	) )
words.append( Word("Beast", 63, False, ['Ber', 'Tir', 'Um', 'Mal', 'Lum'], 
	['Axes', 'Hammers', 'Scepters'],
	[ Effect(['Axes', 'Hammers', 'Scepters'], ['Level 9 Fanaticism Aura When Equipped', '+40% Increased Attack Speed', '+240-270% Enhanced Damage (varies)', '20% Chance of Crushing Blow', '25% Chance of Open Wounds', '+3 To Werebear', '+3 To Lycanthropy', 'Prevent Monster Heal', '+25-40 To Strength (varies)', '+10 To Energy', '+2 To Mana After Each Kill', 'Level 13 Summon Grizzly (5 Charges)']) ]
	) )
words.append( Word("Black", 35, False, ['Thul', 'Io', 'Nef'], 
	['Clubs', 'Hammers', 'Maces'],
	[ Effect(['Clubs', 'Hammers', 'Maces'], ['+120% Enhanced Damage', '+200 to Attack Rating', '+3-14 Cold Damage (3 sec)', '15% Increased Attack Speed', 'Knockback', '12 Level 4 Corpse Explosion Charges', '40% Chance of Crushing Blow', '-2 Magic Damage +10 to Vitality']) ]
	) )
words.append( Word("Bone", 47, False, ['Sol', 'Um', 'Um'], 
	['Armors'],
	[ Effect(['Armors'], ['15% Chance To Cast level 10 Bone Armor When Struck', '15% Chance To Cast level 10 Bone Spear On Striking', '+2 To Necromancer Skill Levels', '+100-150 To Mana (varies)', 'All Resistances +30', 'Damage Reduced By 7']) ]
	) )
words.append( Word("Bramble", 61, False, ['Ral', 'Ohm', 'Sur', 'Eth'], 
	['Armors'],
	[ Effect(['Armors'], ['Level 15-21 Thorns Aura When Equipped (varies)', '+50% Faster Hit Recovery', '+100% To Poison Skill Damage', '+300 Defense', 'Increase Maximum Mana 5%', 'Regenerate Mana 15%', '+5% To Maximum Cold Resist', 'Fire Resist +30%', 'Poison Resist +100%', '+13 Life After Each Kill', 'Level 13 Spirit of Barbs (33 Charges)']) ]
	) )
words.append( Word("Brand", 65, True, ['Jah', 'Lo', 'Mal', 'Gul'], 
	['Missile'],
	[ Effect(['Missile'], ['35% Chance To Cast Level 14 Amplify Damage When Struck', '100% Chance To Cast Level 18 Bone Spear On Striking', '+260-340% Enhanced Damage (varies)', "Ignore Target's Defense", '20% Bonus to Attack Rating', '+280-330% Damage To Demons (varies)', '20% Deadly Strike  Prevent Monster Heal', 'Knockback', 'Fires Explosive Arrows or Bolts (15)']) ]
	) )
words.append( Word("Breath of the Dying", 69, False, ['Vex', 'Hel', 'El', 'Eld', 'Zod', 'Eth'], 
	['Weapons'],
	[ Effect(['Weapons'], ['50% Chance To Cast Level 20 Poison Nova When You Kill An Enemy', 'Indestructible', '+60% Increased Attack Speed', '+350-400% Enhanced Damage (varies)', '+200% Damage To Undead', '-25% Target Defense', '+50 To Attack Rating', '+50 To Attack Rating Against Undead', '7% Mana Stolen Per Hit', '12-15% Life Stolen Per Hit (varies)', 'Prevent Monster Heal', '+30 To All Attributes', '+1 To Light Radius', 'Requirements -20%']) ]
	) )
words.append( Word("Call to Arms", 57, False, ['Amn', 'Ral', 'Mal', 'Ist', 'Ohm'], 
	['Weapons'],
	[ Effect(['Weapons'], ['+1 To All Skills', '+40% Increased Attack Speed', '+200-240% Enhanced Damage (varies)', 'Adds 5-30 Fire Damage', '7% Life Stolen Per Hit', '+1-6 To Battle Command', '+1-6 To Battle Orders', '+1-4 To Battle Cry', 'Prevent Monster Heal', 'Replenish Life +12', '30% Better Chance of Getting Magic Items']) ]
	) )
words.append( Word("Chains of Honor", 63, False, ['Dol', 'Um', 'Ber', 'Ist'], 
	['Armors'],
	[ Effect(['Armors'], ['+2 To All Skills', '+200% Damage To Demons', '+100% Damage To Undead', '8% Life Stolen Per Hit', '+70% Enhanced Defense', '+20 To StrengthReplenish Life +7', 'All Resistances +65', 'Damage Reduced By 8%', '25% Better Chance of Getting Magic Items']) ]
	) )
words.append( Word("Chaos", 57, False, ['Fal', 'Ohm', 'Um'], 
	['Claws'],
	[ Effect(['Claws'], ['9% Chance To Cast Level 11 Frozen Orb On Striking', '11% Chance To Cast Level 9 Charged Bolt On Striking', '+35% Increased Attacked Speed', '+240-290% Enhanced Damage (varies)', 'Adds 216-471 Magic Damage', '25% Chance of Open Wounds', '+1 To Whirlwind', '+10 To Strength', '+15 Life After Each Demon Kill']) ]
	) )
words.append( Word("Crescent Moon", 47, False, ['Shael', 'Um', 'Tir'], 
	['Axes', 'Polearms', 'Swords'],
	[ Effect(['Axes', 'Polearms', 'Swords'], ['10% Chance To Cast Level 17 Chain Lightning On Striking', '7% Chance To Cast Level 13 Static Field On Striking', '+20% Increased Attack Speed', '+220-260% Enhanced Damage (varies)', "Ignore Target's Defense", '-35% To Enemy Lightning Resistance', '25% Chance of Open Wounds', '+9-11 Magic Absorb (varies)', '+2 To Mana After Each Kill', 'Level 18 Summon Spirit Wolf (30 Charges)']) ]
	) )
words.append( Word("Death", 55, True, ['Hel', 'El', 'Vex', 'Ort', 'Gul'], 
	['Swords', 'Axes'],
	[ Effect(['Swords', 'Axes'], ['100% Chance To Cast Level 44 Chain Lightning When You Die', '25% Chance To Cast Level 18 Glacial Spike On Attack', 'Indestructible', '+300-385% Enhanced Damage (varies)', '20% Bonus To Attack Rating', '+50 To Attack Rating Adds 1-50 Lightning Damage', '7% Mana Stolen Per Hit', '50% Chance of Crushing Blow', '+(0.5 per Character Level) 0.5-49.5% Deadly Strike (Based on Character Level)', '+1 To Light Radius', 'Level 22 Blood Golem (15 Charges)', 'Requirements -20%']) ]
	) )
words.append( Word("Delirium", 51, False, ['Lem', 'Ist', 'Io'], 
	['Helms'],
	[ Effect(['Helms'], ['1% Chance To Cast lvl 50 Delirium When Struck', '10% Chance To Cast lvl 14 Mind Blast When Struck', '20% Chance To Cast lvl 13 Terror When Struck', '33% Chance To Cast lvl 18 Confuse On Striking', '+2 To All Skills', '+261 Defense', '+10 To Vitality', '50% Extra Gold From Monsters', '25% Better Chance of Getting Magic Items', 'Level 17 Attract (60 Charges)']) ]
	) )
words.append( Word("Destruction", 65, True, ['Vex', 'Lo', 'Ber', 'Jah', 'Ko'], 
	['Polearms', 'Swords'],
	[ Effect(['Polearms', 'Swords'], ['23% Chance To Cast Level 12 Volcano On Striking', '5% Chance To Cast Level 23 Molten Boulder On Striking', '100% Chance To Cast level 45 Meteor When You Die', '15% Chance To Cast Level 22 Nova On Attack', '+350% Enhanced Damage', "Ignore Target's Defense", 'Adds 100-180 Magic Damage', '7% Mana Stolen Per Hit', '20% Chance Of Crushing Blow', '20% Deadly Strike', 'Prevent Monster Heal', '+10 To Dexterity']) ]
	) )
words.append( Word("Doom", 67, False, ['Hel', 'Ohm', 'Um', 'Lo', 'Cham'], 
	['Axes', 'Hammers', 'Polearms'],
	[ Effect(['Axes', 'Hammers', 'Polearms'], ['5% Chance To Cast Level 18 Volcano On Striking', 'Level 12 Holy Freeze Aura When Equipped', '+2 To All Skills', '+45 Increased Attack Speed', '+280-320% Enhanced Damage (varies)', '-57% To Enemy Cold Resistance', '20% Deadly Strike', '25% Chance of Open Wounds', 'Prevent Monster Heal', 'Freezes Target', 'Requirements -20%']) ]
	) )
words.append( Word("Dragon", 61, True, ['Sur', 'Lo', 'Sol'], 
	['Armors', 'Shields'],
      [ Effect(['Armors', 'Shields'], 
          ['20% Chance to Cast Level 18 Venom When Struck',
              '12% Chance To Cast Level 15 Hydra On Striking',
              'Level 14 Holy Fire Aura When Equipped', '+360 Defense',
              '+230 Defense Vs. Missile', '+3-5 To All Attributes (varies)',
              '+0.375-37.125 To Strength (Based on Character Level)',
              '+5% To Maximum Lightning Resist', 'Damage Reduced by 7']),
        Effect(['Armors'], ['Increase Maximum Mana 5%']),
        Effect(['Shields'], ['+50 To Mana'])
        ]
	) )
words.append( Word("Dream", 65, True, ['Io', 'Jah', 'Pul'], 
	['Helms', 'Shields'],
	[ Effect(['Helms', 'Shields'], ['10% Chance To Cast Level 15 Confuse When Struck', 'Level 15 Holy Shock Aura When Equipped', '+20-30% Faster Hit Recovery (varies)', '+30% Enhanced Defense', '+150-220 Defense (varies)', '+10 To Vitality', 'Increase Maximum Life 5% (Helms Only)', '+50 To Life (Shields Only)', '+0.625-61.875 To Mana (Based On Character Level)', 'All Resistances +5-20 (varies)', '12-25% Better Chance of Getting Magic Items (varies)']) ]
	) )
words.append( Word("Duress", 47, False, ['Shael', 'Um', 'Thul'], 
	['Armors'],
	[ Effect(['Armors'], ['+150-200% Enhanced Defense', '15% faster hit Recovery', '+15% Fire Resistance', '+45% Cold Resistance', '+15% Lightning Resistance', '+15% Poison Resistance', '+10-25% Enhanced Damage', '+37-133 Cold Damage', '+15% Crushing Blow', '+33% Open Wounds', '20% Faster Stamina Drain']) ]
	) )
words.append( Word("Edge", 25, True, ['Tir', 'Tal', 'Amn'], 
	['Missile'],
	[ Effect(['Missile'], ['Level 15 Thorns Aura When Equipped', '+35% Increased Attack Speed', '+320-380% Damage To Demons (varies)', '+280% Damage To Undead', '+75 Poison Damage Over 5 Seconds', '7% Life Stolen Per Hit', 'Prevent Monster Heal', '+5-10 To All Attributes (varies)', '+2 To Mana After Each Kill', 'Reduces All Vendor Prices 15%']) ]
	) )
words.append( Word("Enigma", 65, False, ['Jah', 'Ith', 'Ber'], 
	['Armors'],
	[ Effect(['Armors'], ['+2 To All Skills', '+45% Faster Run/Walk', '+1 To Teleport', '+750-775 Defense (Varies)', '+ (0.75 Per Character Level) +0-74.25 To Strength (Based On Character Level)', 'Increase Maximum Life 5%', 'Damage Reduced By 8%', '+14 Life After Each Kill', '15% Damage Taken Goes To Mana', '+ (1 Per Character Level) +1-99% Better Chance of Getting Magic Items (Based On Character Level)']) ]
	) )
words.append( Word("Enlightenment", 45, False, ['Pul', 'Ral', 'Sol'], 
	['Armors'],
	[ Effect(['Armors'], ['5% Chance To Cast Level 15 Blaze When Struck', '5% Chance To Cast level 15 Fire Ball On Striking', '+2 To Sorceress Skill Levels', '+1 To Warmth', '+30% Enhanced Defense', 'Fire Resist +30%', 'Damage Reduced By 7']) ]
	) )
words.append( Word("Eternity", 63, False, ['Amn', 'Ber', 'Ist', 'Sol', 'Sur'], 
	['Melee'],
	[ Effect(['Melee'], ['Indestructible', '+276% Enhanced Damage', '+9 To Minimum Damage', '7% Life Stolen Per Hit', '20% Chance of Crushing Blow', 'Hit Blinds Target', 'Slows Target By 33%', 'Replenish Mana 16%', 'Cannot Be Frozen', '30% Better Chance Of Getting Magic Items', 'Level 8 Revive (88 Charges)']) ]
	) )
words.append( Word("Exile", 57, False, ['Vex', 'Ohm', 'Ist', 'Dol'], 
	['Shields'],
	[ Effect(['Shields'], ['15% Chance To Cast Level 5 Life Tap On Striking', 'Level 13-16 Defiance Aura When Equipped', '+2 To Offensive Auras (Paladin Only)', '+30% Faster Block Rate', 'Freezes Target', '+220-260% Enhanced Defense (varies)', 'Replenish Life +7', '+5% To Maximum Cold Resist', '+5% To Maximum Fire Resist', '25% Better Chance Of Getting Magic Items', 'Repairs 1 Durability every 4 seconds']) ]
	) )
words.append( Word("Faith", 65, True, ['Ohm', 'Jah', 'Lem', 'Eld'], 
	['Missile'],
	[ Effect(['Missile'], ['Level 12-15 Fanaticism Aura When Equipped (varies)', '+1-2 To All Skills (varies)', '+330% Enhanced Damage', "Ignore Target's Defense", '300% Bonus To Attack Rating', '+75% Damage To Undead', '+50 To Attack Rating Against Undead', '+120 Fire Damage', 'All Resistances +15', '10% Reanimate As: Returned', '75% Extra Gold From Monsters']) ]
	) )
words.append( Word("Famine", 65, False, ['Fal', 'Ohm', 'Ort', 'Jah'], 
	['Axes', 'Hammers'],
	[ Effect(['Axes', 'Hammers'], ['+30% Increased Attack Speed', '+320-370% Enhanced Damage', "Ignore Target's Defense", 'Adds 180-200 Magic Damage', 'Adds 50-200 Fire Damage', 'Adds 51-250 Lightning Damage', 'Adds 50-200 Cold Damage', '12% Life Stolen Per Hit', 'Prevent Monster Heal', '+10 To Strength']) ]
	) )
words.append( Word("Fortitude", 59, True, ['El', 'Sol', 'Dol', 'Lo'], 
    ['Weapons', 'Armors'],
    [ Effect(['Weapons', 'Armors'], [
        '20% Chance To Cast Level 15 Chilling Armor when Struck',
        '+25% Faster Cast Rate', '+300% Enhanced Damage',
        '+1 To Light Radius', '120% Damage Taken Goes To Mana',
        'All Resistances +25-30 (varies)', '+200% Enhanced Defense',
        '+ To Life (Based on Character Level)*']),
        Effect(['Weapons'], [ '+9 To Minimum Damage', '+50 To Attack Rating',
            '20% Deadly Strike', 'Hit Causes Monster To Flee 25%']),
        Effect(['Armor'],[ '+15 Defense', 'Replenish Life +7',
            '+5% To Maximum Lightning Resistist', 'Damage Reduced By 7'])
          ]
	) )
words.append( Word("Fury", 65, False, ['Jah', 'Gul', 'Eth'], 
	['Melee'],
	[ Effect(['Melee'], ['+209% Enhanced Damage', '40% Increased Attack Speed', 'Prevent Monster Heal', '66% Chance Of Open Wounds', '33% Chance Of Deadly Strike', 'Ignores Target Defense', '-25% Target Defense', '+20% Attack Rating', '6% Life Stolen Per Hit', '+5 To Frenzy (Barbarian Only)']) ]
	) )
words.append( Word("Gloom", 47, False, ['Fal', 'Um', 'Pul'], 
	['Armors'],
	[ Effect(['Armors'], ['15% Chance To Cast Level 3 Dim Vision When Struck', '+10% Faster Hit Recovery', '+170-230% Enhanced Defense (varies)', '+10 To Strength', 'All Resistances +45', 'Half Freeze Duration', '5% Damage Taken Goes To Mana', '-3 To Light Radius']) ]
	) )
words.append( Word("Grief", 59, True, ['Eth', 'Tir', 'Lo', 'Mal', 'Ral'], 
	['Swords', 'Axes'],
	[ Effect(['Swords', 'Axes'], ['35% Chance To Cast Level 15 Venom On Striking', '+30-40% Increased Attack Speed (varies)', 'Damage +340-400 (varies)', "Ignore Target's Defense", '-25% Target Defense', '+(1.875 per character level) 1.875-185.625%', 'Damage To Demons (Based on Character Level)', 'Adds 5-30 Fire Damage', '-20-25% To Enemy Poison Resistance (varies)', '20% Deadly Strike', 'Prevent Monster Heal', '+2 To Mana After Each Kill', '+10-15 Life After Each Kill (varies)']) ]
	) )
words.append( Word("Hand of Justice", 67, False, ['Sur', 'Cham', 'Amn', 'Lo'], 
	['Weapons'],
	[ Effect(['Weapons'], ['100% Chance To Cast Level 36 Blaze When You Level-Up', '100% Chance To Cast Level 48 Meteor When You Die', 'Level 16 Holy Fire Aura When Equipped', '+33% Increased Attack Speed', '+280-330% Enhanced Damage', "Ignore Target's Defense", '7% Life Stolen Per Hit', '-20% To Enemy Fire Resistance', '20% Deadly Strike', 'Hit Blinds Target', 'Freezes Target']) ]
	) )
words.append( Word("Harmony", 39, True, ['Tir', 'Ith', 'Sol', 'Ko'], 
	['Missile'],
	[ Effect(['Missile'], ['Level 10 Vigor Aura When Equipped', '+200-275% Enhanced Damage (varies)', '+9 To Min &amp; Max Damage', 'Adds 55-160 Lightning Damage', 'Adds 55-160 Cold &amp; Fire Damage', '+2-6 To Valkyrie (varies)', '+10 To Dexterity', 'Regenerate Mana 20%', '+2 To Mana After Each Kill', '+2 To Light Radius', 'Level 20 Revive (25 Charges)']) ]
	) )
words.append( Word("Heart of the Oak", 55, False, ['Ko', 'Vex', 'Pul', 'Thul'], 
	['Staves', 'Maces'],
	[ Effect(['Staves', 'Maces'], ['+3 To All Skills', '+40% Faster Cast Rate', '+75% Damage To Demons', '+100 To Attack Rating Against Demons', 'Adds 3-14 Cold Damage', '7% Mana Stolen Per Hit', '+10 To Dexterity', 'Replenish Life +20', 'Increase Maximum Mana 15%', 'All Resistances +30-40 (varies)', 'Level 4 Oak Sage (25 Charges)', 'Level 14 Raven (60 Charges)', '+50% Damage To Undead']) ]
	) )
words.append( Word("Holy Thunder", 23, False, ['Eth', 'Ral', 'Ort', 'Tal'], 
	['Scepters'],
	[ Effect(['Scepters'], ['Level 7 Chain Lightning 60 charges', '-25% Target Defense', '+60% Enhanced Damage', '+75 Poison Damage over 7 secs', '+5% Maximum Lightning Resistance', '+60% Lightning Resistance', '+21-110 Lightning Damage', '+5-30 Fire Damage', '+3 to Holy Shock', '150% Damage vs. Undead']) ]
	) )
words.append( Word("Honor", 27, False, ['Amn', 'El', 'Ith', 'Tir', 'Sol'], 
	['Melee'],
	[ Effect(['Melee'], ['+160% Enhanced Damage', '+250 Attack Rating', '+9 Minimum Damage', '+9 Maximum Damage', '25% Deadly Strike', '7% Life Stolen per Hit', '+1 to all skill levels', '+2 Mana per kill', '+1 Light Radius', 'Replenish life +10', '+10 to Strength']) ]
	) )
words.append( Word("Ice", 65, True, ['Amn', 'Shael', 'Jah', 'Lo'], 
	['Missile'],
	[ Effect(['Missile'], ['100% Chance To Cast Level 40 Blizzard When You Level-up', '25% Chance To Cast Level 22 Frost Nova On Striking', 'Level 18 Holy Freeze Aura When Equipped', '+20% Increased Attack Speed', '+140-210% Enhanced Damage (varies)', "Ignore Target's Defense", '+25-30% To Cold Skill Damage (varies)', '-20% To Enemy Cold Resistance', '7% Life Stolen Per Hit', '20% Deadly Strike', '3.125-309.375 Extra Gold From Monsters (Based on Character Level)']) ]
	) )
words.append( Word("Infinity", 63, True, ['Ber', 'Mal', 'Ber', 'Ist'], 
	['Polearms'],
	[ Effect(['Polearms'], ['50% Chance To Cast Level 20 Chain Lightning When You Kill An Enemy', 'Level 12 Conviction Aura When Equipped', '+35% Faster Run/Walk', '+255-325% Enhanced Damage (varies)', '-(45-55)% To Enemy Lightning Resistance (varies)', '40% Chance of Crushing Blow', 'Prevent Monster Heal', '0.5-49.5 To Vitality (Based on Character Level)', '30% Better Chance of Getting Magic Items', 'Level 21 Cyclone Armor (30 Charges)']) ]
	) )
words.append( Word("Insight", 27, True, ['Ral', 'Tir', 'Tal', 'Sol'], 
	['Polearms', 'Staves'],
	[ Effect(['Polearms', 'Staves'], ['Level 10-17 Meditation Aura When Equipped (varies)', '+35% Faster Cast Rate', '+200-260% Enhanced Damage (varies)', '+9 To Minimum Damage', '180-250% Bonus to Attack Rating (varies)', 'Adds 5-30 Fire Damage', '+75 Poison Damage Over 5 Seconds', '+1-6 To Critical Strike (varies)', '+5 To All Attributes', '+2 To Mana After Each Kill', '23% Better Chance of Getting Magic Items']) ]
	) )
words.append( Word("King's Grace", 25, False, ['Amn', 'Ral', 'Thul'], 
	['Swords', 'Scepters'],
	[ Effect(['Swords', 'Scepters'], ['+100% Enhanced Damage', '+150 Attack Rating', '+100 Attack Rating vs. Undead', '150% Damage vs. Undead', '+100 Attack Rating vs. Demons', '200% Damage vs. Demons', '7% life steal', '+3-14 Cold damage (3 sec)', '+5-30 Fire Damage']) ]
	) )
words.append( Word("Kingslayer", 53, False, ['Mal', 'Um', 'Gul', 'Fal'], 
	['Swords', 'Axes'],
	[ Effect(['Swords', 'Axes'], ['+30% Increased Attack Speed', '+230-270% Enhanced Damage (varies)', '-25% Target Defense', '20% Bonus To Attack Rating', '33% Chance of Crushing Blow', '50% Chance of Open Wounds', '+1 To Vengeance', 'Prevent Monster Heal', '+10 To Strength', '40% Extra Gold From Monsters']) ]
	) )
words.append( Word("Last Wish", 65, True, ['Jah', 'Mal', 'Jah', 'Sur', 'Jah', 'Ber'], 
	['Axes', 'Hammers', 'Swords'],
	[ Effect(['Axes', 'Hammers', 'Swords'], ['6% Chance To Cast Level 11 Fade When Struck', '10% Chance To Cast Level 18 Life Tap On Striking', '20% Chance To Cast Level 20 Charged Bolt On Attack', 'Level 17 Might Aura When Equipped', '+330-375% Enhanced Damage (varies)', "Ignore Target's Defense", '60-70% Chance of Crushing Blow (varies)', 'Prevent Monster Heal Hit Blinds Target', '+(0.5 per character level)', '0.5-49.5% Chance of Getting Magic Items (Based on Character Level)']) ]
	) )
words.append( Word("Lawbringer", 43, True, ['Amn', 'Lem', 'Ko'], 
	['Hammers', 'Scepters', 'Swords'],
	[ Effect(['Hammers', 'Scepters', 'Swords'], ['20% Chance To Cast Level 15 Decrepify On Striking', 'Level 16-18 Sanctuary Aura When Equipped (varies)', '-50% Target Defense', 'Adds 150-210 Fire Damage', 'Adds 130-180 Cold Damage', '7% Life Stolen Per Hit', 'Slain Monsters Rest In Peace', '+200-250 Defense Vs. Missile (varies)', '+10 To Dexterity', '75% Extra Gold From Monsters']) ]
	) )
words.append( Word("Leaf", 19, False, ['Tir', 'Ral'], 
	['Staves'],
	[ Effect(['Staves'], ['+5-30 Fire Damage', '+2 mana per kill', '+3 to Fire Skills', '+33% Cold Resistance', '+3 Inferno', '+3 Fire Bolt', '+3 Warmth']) ]
	) )
words.append( Word("Lionheart", 41, False, ['Hel', 'Lum', 'Fal'], 
	['Armors'],
      [ Effect(['Armors'], ['-15% Requirements', '+20% Enhanced Damage',
        '+30% to All Resistances', '+50 Hit Points', '+10 Energy',
        '+20 Vitality', '+15 Dexterity', '+25 Strength']) ]
	) )
words.append( Word("Lore", 27, False, ['Ort', 'Sol'], 
	['Helms'],
	[ Effect(['Helms'], ['+1 to all skill levels', '+2 Mana per Kill', 'Lowers Damage by 7', '30% Lightning Resistance', '+10 Energy', '+2 Light Radius']) ]
	) )
words.append( Word("Malice", 15, False, ['Ith', 'El', 'Eth'], 
	['Melee'],
	[ Effect(['Melee'], ['+33% Enhanced Damage', '+9 Maximum Damage', '+50 to Attack Rating', '100% Chance of Open wounds', '-100 to Monster Defense per Hit', 'Prevents Monster Heal', '-25% Target Defense', 'Drain Life -5']) ]
	) )
words.append( Word("Melody", 39, False, ['Shael', 'Ko', 'Nef'], 
	['Bows', 'Crossbows'],
	[ Effect(['Bows', 'Crossbows'], ['+300% Damage vs. Undead', '+50% Enhanced Damage', '+10 Dexterity', '20% Increased Attack Speed', 'Knockback', '+3 Bow and Crossbow Skills', '+3 Slow Missiles', '+3 Dodge', '+3 Critical Strike']) ]
	) )
words.append( Word("Memory", 37, False, ['Lum', 'Io', 'Sol', 'Eth'], 
	['Staves'],
	[ Effect(['Staves'], ["Lowers Target's Defense by 25%", '33% Faster Cast Rate', '+3 Sorceress Skill Levels', '+50% Enhanced Defense', '-7 Magic Damage', '+20% Max Mana', '+9 Minimum Damage', '+10 Energy', '+10 Vitality', '+2 Static Field', '+2 Energy Shield']) ]
	) )
words.append( Word("Myth", 25, False, ['Hel', 'Amn', 'Nef'], 
	['Armors'],
	[ Effect(['Armors'], ['3% Chance To Cast Level 1 Howl When Struck', '10% Chance To Cast Level 1 Taunt On Striking', '+2 To Barbarian Skill Levels', '+30 Defense Vs. Missile', 'Replenish Life +10', 'Attacker Takes Damage of 14', 'Requirements -15%']) ]
	) )
words.append( Word("Nadir", 13, False, ['Nef', 'Tir'], 
	['Helms'],
	[ Effect(['Helms'], ['Level 13 Cloak of Shadows (9 charges)', '+50% Enhanced Defense', '+2 mana per kill', '-3 light radius', '+30 Defense vs. missile', '+10 Defense', '+5 Strength', '-33% gold from monsters']) ]
	) )
words.append( Word("Oath", 59, True, ['Shael', 'Pul', 'Mal', 'Lum'], 
	['Axes', 'Maces', 'Swords'],
	[ Effect(['Axes', 'Maces', 'Swords'], ['30% Chance To Cast Level 20 Bone Spirit On Striking', 'Indestructible', '+50% Increased Attack Speed', '+210-340% Enhanced Damage (varies)', '+75% Damage To Demons', '+100 To Attack Rating Against Demons', 'Prevent Monster Heal', '+10 To Energy', '+10-15 Magic Absorb (varies)', 'Level 16 Heart of Wolverine (20 Charges)', 'Level 17 Iron Golem (14 Charges)']) ]
	) )
words.append( Word("Obedience", 41, True, ['Hel', 'Ko', 'Thul', 'Eth', 'Fal'], 
	['Polearms'],
	[ Effect(['Polearms'], ['30% Chance To Cast Level 21 Enchant When You Kill An Enemy', '40% Faster Hit Recovery', '+370% Enhanced Damage', '-25% Target Defense', 'Adds 3-14 Cold Damage 3 Second Duration (Normal)', '-25% To Enemy Fire Resistance', '40% Chance of Crushing Blow', '+200-300 Defense (varies)', '+10 To Strength &amp; Dexterity', 'All Resistances +20-30 (varies)', 'Requirements -20%']) ]
	) )
words.append( Word("Passion", 43, False, ['Dol', 'Ort', 'Eld', 'Lem'], 
	['Weapons'],
	[ Effect(['Weapons'], ['+25% Increased Attack Speed', '+160-210% Enhanced Damage', '50-80% Bonus To Attack Rating', '+75% Damage To Undead', '+50 To Attack Rating Against Undead', 'Adds 1-50 Lightning Damage', '+1 To Berserk', '+1 To Zeal', 'Hit Blinds Target +10', 'Hit Causes Monster To Flee 25%', '75% Extra Gold From Monsters', 'Level 3 Heart of Wolverine (12 Charges)']) ]
	) )
words.append( Word("Peace", 29, False, ['Shael', 'Thul', 'Amn'], 
	['Armors'],
	[ Effect(['Armors'], ['4% Chance To Cast Level 5 Slow Missiles When Struck', '2% Chance To Cast level 15 Valkyrie On Striking', '+2 To Amazon Skill Levels', '+20% Faster Hit Recovery', '+2 To Critical Strike', 'Cold Resist +30%', 'Attacker Takes Damage of 14']) ]
	) )
words.append( Word("Phoenix", 65, True, ['Vex', 'Vex', 'Lo', 'Jah'], 
	['Weapons', 'Shields'],
      [
          Effect(['Weapons', 'Shields'], ["100% Chance To Cast level 40 Blaze When You Level-up",
                  "40% Chance To Cast Level 22 Firestorm On Striking",
                  "Level 10-15 Redemption Aura When Equipped (varies)",
                  "-28% To Enemy Fire Resistance", "+15-21 Fire Absorb (varies)",
                  "+350-400 Defense Vs. Missile (varies)", "+350-400% Enhanced Damage (varies)"]),
          Effect(['Weapons'], [ "Ignores Target's Defense",
              "14% Mana Stolen Per Hit", "20% Deadly Strike"]),
          Effect(['Shields'], [ "+50 To Life", "+5% To Maximum Lightning Resist", "+10% To Maximum Fire Resist" ])
	]) )
words.append( Word("Pride", 67, True, ['Cham', 'Sur', 'Io', 'Lo'], 
	['Polearms'],
	[ Effect(['Polearms'], ['25% Chance To Cast Level 17 Fire Wall When Struck', 'Level 16-20 Concentration Aura When Equipped (varies)', '260-300% Bonus To Attack Rating (varies)', '+1-99% Damage To Demons (Based on Character Level)', 'Adds 50-280 Lightning Damage', '20% Deadly Strike', 'Hit Blinds Target', 'Freezes Target +3', '+10 To Vitality', 'Replenish Life +8', '1.875-185.625% Extra Gold From Monsters (Based on Character Level)']) ]
	) )
words.append( Word("Principle", 55, False, ['Ral', 'Gul', 'Eld'], 
	['Armors'],
	[ Effect(['Armors'], ['100% Chance To Cast Level 5 Holy Bolt On Striking', '+2 To Paladin Skill Levels', '15% Slower Stamina Drain', '+5% To Maximum Poison Resist', 'Fire Resist +30%']) ]
	) )
words.append( Word("Prudence", 49, False, ['Mal', 'Tir'], 
	['Armors'],
	[ Effect(['Armors'], ['+25% Faster Hit Recovery', '+140-170% Enhanced Defense (varies)', 'All Resistances +25-35 (varies)', 'Damage Reduced by 3', 'Magic Damage Reduced by 17', '+2 To Mana After Each Kill', '+1 To Light Radius', 'Repairs Durability 1 In 4 Seconds']) ]
	) )
words.append( Word("Radiance", 27, False, ['Nef', 'Sol', 'Ith'], 
	['Helms'],
	[ Effect(['Helms'], ['15% Melee Damage Taken Goes to Mana', '+75% Enhanced Defense', 'Magic Damage Reduced by 3', 'Physical Damage Reduced by 7', '+30 Defense vs. Missiles', '+33 Mana', '+10 Energy', '+10 Vitality', '+5 Light Radius']) ]
	) )
words.append( Word("Rain", 49, False, ['Ort', 'Mal', 'Ith'], 
	['Armors'],
	[ Effect(['Armors'], ['5% Chance To Cast Level 15 Cyclone Armor When Struck', '5% Chance To Cast Level 15 Twister On Striking', '+2 To Druid Skills', '+100-150 To Mana (varies)', 'Lightning Resist +30%', 'Magic Damage Reduced By 7', '15% Damage Taken Goes to Mana']) ]
	) )
words.append( Word("Rhyme", 29, False, ['Shael', 'Eth'], 
	['Shields'],
	[ Effect(['Shields'], ['Cannot be Frozen', '40% Faster Block Rate', '20% Increased Chance of Blocking', 'Regenerate Mana 15%', '+25% to all Resistances', '+25% to Magic Find', '+50% Extra Gold from Monsters']) ]
	) )
words.append( Word("Rift", 53, True, ['Hel', 'Ko', 'Lem', 'Gul'], 
	['Polearms', 'Scepters'],
	[ Effect(['Polearms', 'Scepters'], ['20% Chance To Cast Level 16 Tornado On Striking', '16% Chance To Cast Level 21 Frozen Orb On Attack', '20% Bonus To Attack Rating', 'Adds 160-250 Magic Damage', 'Adds 60-180 Fire Damage', '+5-10 To All Stats (varies)', '+10 To Dexterity', '38% Damage Taken Goes To Mana', '75% Extra Gold From Monsters', 'Level 15 Iron Maiden (40 Charges)', 'Requirements -20%']) ]
	) )
words.append( Word("Sanctuary", 49, False, ['Ko', 'Ko', 'Mal'], 
	['Shields'],
	[ Effect(['Shields'], ['+20% Faster Hit Recovery', '+20% Faster Block Rate', '20% Increased Chance of Blocking', '+130-160% Enhanced Defense (varies)', '+250 Defense vs. Missile', '+20 To Dexterity', 'All Resistances +50-70 (varies)', 'Magic Damage Reduced By 7', 'Level 12 Slow Missiles (60 Charges)']) ]
	) )
words.append( Word("Silence", 55, False, ['Dol', 'Eld', 'Hel', 'Ist', 'Tir', 'Vex'], 
	['Weapons'],
	[ Effect(['Weapons'], ['+200% Enhanced Damage', '175% Damage vs. Undead', '+50 to Attack Rating Against Undead', '11% Mana Steal', 'Hit Blinds Target', '20% Faster Hit Recovery', '+2 to All Skills', 'All Resistances +75', '20% Increased Attack Speed', '+2 to Mana After Each Kill', 'Hit Causes Monster to Flee 25%', 'Requirements -20%', '30% Better Magic Find']) ]
	) )
words.append( Word("Smoke", 37, False, ['Nef', 'Lum'], 
	['Armors'],
	[ Effect(['Armors'], ['Level 6 Weaken, 18 charges', '+20% Faster Hit Recovery', '-1 to Light Radius', '+75% Enhanced Defense', '+50% to all Resistances', '+280 Defense vs. Missiles', '+10 to Energy']) ]
	) )
words.append( Word("Spirit", 25, True, ['Tal', 'Thul', 'Ort', 'Amn'], 
	['Shields', 'Swords'],
      [
          Effect(['Shields', 'Swords'], [
              '+2 To All Skills',
              '+25-35% Faster Cast Rate (varies)',
              '+55% Faster Hit Recovery',
              '+22 To Vitality',
              '+250 Defense Vs. Missile',
              '+89-112 To Mana (varies)',
              '+3-8 Magic Absorb (varies)',
              ]),
          Effect(['Shields'], [
              'Cold Resist +35%',
              'Lightning Resist +35%',
              'Poison Resist +35%',
              'Attacker Takes Damage of 14'
              ]),
          Effect(['Swords'], [
              'Adds 1-50 Lightning Damage',
              'Adds 3-14 Cold Damage 3 Second Duration (Normal)',
              '+75 Poison Damage Over 5 Seconds',
              '7% Life Stolen Per Hit'
              ])
        ]
	) )
words.append( Word("Splendor", 37, False, ['Eth', 'Lum'], 
	['Shields'],
	[ Effect(['Shields'], ['+1 To All Skills', '+10% Faster Cast Rate', '+20% Faster Block Rate', '+60-100% Enhanced Defense (varies)', '+10 To Energy', 'Regenerate Mana 15%', '50% Extra Gold From Monsters', '20% Better Chance of Getting Magic Items', '+3 To Light Radius']) ]
	) )
words.append( Word("Stealth", 17, False, ['Tal', 'Eth'], 
	['Armors'],
	[ Effect(['Armors'], ['25% Faster Casting Rate', '25% Faster Hit Recovery', '25% Faster run/walk speed', '-3 magical damage taken', '+15% Mana Regeneration Rate', '+30% Poison Resistance', '+15% Maximum Stamina', '+6 Dexterity']) ]
	) )
words.append( Word("Steel", 13, False, ['Tir', 'El'], 
	['Sword', 'Axes', 'Maces'],
	[ Effect(['Sword', 'Axes', 'Maces'], ['+20% Enhanced Damage', '+3 Minimum Damage', '+3 Maximum Damage', '+50 Attack Rating', '50% Chance of Open Wounds', '+1 light radius', '+2 mana per kill', '25% Increased Attack Speed']) ]
	) )
words.append( Word("Stone", 47, False, ['Shael', 'Um', 'Pul', 'Lum'], 
	['Armors'],
	[ Effect(['Armors'], ['+60% Faster Hit Recovery', '+250-290% Enhanced Defense (varies)', '+300 Defense Vs. Missile', '+16 To Strength', '+16 To Vitality', '+10 To Energy', 'All Resistances +15', 'Level 16 Molten Boulder (80 Charges)', 'Level 16 Clay Golem (16 Charges)']) ]
	) )
words.append( Word("Strength", 25, False, ['Amn', 'Tir'], 
	['Melee'],
	[ Effect(['Melee'], ['+35% Enhanced Damage', '25% chance of Crushing Blow', '7% life steal', '+2 mana per kill', '+10 vitality', '+20 strength']) ]
	) )
words.append( Word("Treachery", 43, False, ['Shael', 'Thul', 'Lem'], 
	['Armors'],
	[ Effect(['Armors'], ['5% Chance To Cast Level 15 Fade When Struck', '25% Chance To Cast level 15 Venom On Striking', '+2 To Assassin Skills', '+45% Increased Attack Speed', '+20% Faster Hit Recovery', 'Cold Resist +30%', '50% Extra Gold From Monsters']) ]
	) )
words.append( Word("Venom", 49, False, ['Tal', 'Dol', 'Mal'], 
	['Weapons'],
	[ Effect(['Weapons'], ['288 Poison Damage Over 6 Seconds', 'Hit Causes Monster To Flee 25%', 'Prevent Monster Heal', "Ignore Target's Defense", '7% Mana Stolen Per Hit', 'Level 15 Poison Explosion (27 Charges)', 'Level 13 Poison Nova (11 Charges)']) ]
	) )
words.append( Word("Voice of Reason", 43, True, ['Lem', 'Ko', 'El', 'Eld'], 
	['Maces', 'Swords'],
	[ Effect(['Maces', 'Swords'], ['15% Chance To Cast Level 13 Frozen Orb On Striking', '18% Chance To Cast Level 20 Ice Blast On Striking', '+50 To Attack Rating', '+220-350% Damage To Demons', '+355-375% Damage To Undead (varies)', '+50 To Attack Rating Against Undead', 'Adds 100-220 Cold Damage', '-24% To Enemy Cold Resistance', '+10 To Dexterity', 'Cannot Be Frozen', '75% Extra Gold From Monsters', '+1 To Light Radius']) ]
	) )
words.append( Word("Wealth", 43, False, ['Lem', 'Ko', 'Tir'], 
	['Armors'],
	[ Effect(['Armors'], ['100% Better Chance of Getting Magic Items', '300% Extra Gold From Monsters', '+2 to Mana After Each Kill', '+10 to Dexterity']) ]
	) )
words.append( Word("White", 35, False, ['Dol', 'Io'], 
	['Wands'],
	[ Effect(['Wands'], ['Hit causes monster to flee 25%', '20% Faster Cast Rate', 'Magic Damage Reduced by 4', '+13 to mana', '+10 to vitality', '+3 to Poison and Bone Skills', '+4 to Skeleton Mastery', '+2 to Bone Spear', '+3 to Bone Armor']) ]
	) )
words.append( Word("Wind", 61, False, ['Sur', 'El'], 
	['Melee'],
	[ Effect(['Melee'], ['10% Chance To Cast Level 9 Tornado On Striking', '+20% Faster Run/Walk', '+40% Increased Attack Speed', '+15% Faster Hit Recovery', '+120-160% Enhanced Damage (varies)', '-50% Target Defense', '+50 To Attack Rating', 'Hit Blinds Target', '+1 To Light Radius', 'Level 13 Twister (127 Charges)']) ]
	) )
words.append( Word("Wrath", 63, True, ['Pul', 'Lum', 'Ber', 'Mal'], 
	['Missile'],
	[ Effect(['Missile'], ['30% Chance To Cast Level 1 Decrepify On Striking', '5% Chance To Cast Level 10 Life Tap On Striking', '+375% Damage To Demons', '+100 To Attack Rating Against Demons', '+250-300% Damage To Undead (varies)', 'Adds 85-120 Magic Damage', 'Adds 41-240 Lightning Damage', '20% Chance of Crushing Blow', 'Prevent Monster Heal', '+10 To Energy', 'Cannot Be Frozen']) ]
	) )
words.append( Word("Zephyr", 21, False, ['Ort', 'Eth'], 
	['Bows', 'Crossbows'],
	[ Effect(['Bows', 'Crossbows'], ['7% Chance to Cast Slvl 1 Twister When Struck', '+33% Enhanced Damage', '+1-50 lightning damage', 'Increased Attack Speed (25)', '-25% Target Defense', 'Faster Run (25)', '+25 Defense', '+66 Attack Rating']) ]
	) )

