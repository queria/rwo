#!/usr/bin/env python
import sys
import os
import re
import urllib
import json

class RuneParser(object):
    def __init__(self, filepath='', url='', debug=False):
        super(RuneParser, self).__init__()
        self.runes = []
        self.debug = debug
        self.rarity = 'common'
        if filepath:
            self._debug('RuneParser uses file '+filepath)
            self.source = open(filepath)
        elif url:
            self._debug('RuneParser uses url '+url)
            self.source = urllib.urlopen(url)
        else:
            raise 'You have to specify source file path or url!'

    def _debug(self, *args):
        if self.debug:
            print ' '.join([str(x) for x in args])
    def _debug_noline(self, *args):
        if self.debug:
            print ' '.join([str(x) for x in args]),

    def next_rarity(self):
        if self.rarity == 'common':
            self.rarity = 'semi-rare'
        elif self.rarity == 'semi-rare':
            self.rarity = 'rare'

    def parse(self):
        self._debug('start of rune parsing')
        intable = False
        afterheader = False
        rune = None
        cnt = 0
        reg_name = re.compile('<td> <a href.*>([a-zA-Z]+)</a>.*')
        reg_desc = re.compile('</td><td> <b>')
        reg_subdesc = re.compile('<b>([^<]+)</b> ([^<]+)<br />')
        reg_clvl = re.compile('<b>Ilvl/Clvl Required:</b> ([0-9]+)')
        reg_ilvlclvl = re.compile(
                '<b>Ilvl:</b> ([0-9]+) Clvl Required: ([0-9]+)')
        for line in self.source:
            cnt += 1
            if line == '<table width="80%">\n':
                intable = True
                self._debug('start at', cnt, 'with line:', line)
            elif not intable:
                pass # waiting for start of rune-table
            elif line == '</td></tr></table>\n':
                if rune:
                    self.runes.append(rune)
                    self._debug('/ rune', str(rune),' #', cnt)
                intable = False
                self._debug('finished')
                return
            elif not afterheader:
                if line == '</th></tr>\n':
                    afterheader = True
                    self._debug('afterheader #', cnt)
            elif line == '<tr>\n':
                rune = {'rarity':self.rarity}
                self._debug('- rune #', cnt)
            elif not rune:
                self._debug_noline('.')
                pass # waiting for start of next rune
            elif line == '</td></tr>\n':
                self.runes.append(rune)
                if rune['name'] in ['Amn','Um']:
                    self.next_rarity()
                self._debug('/ rune', str(rune),' #', cnt)
                rune = None
            else:
                self._debug_noline('*')
                name = reg_name.match(line)
                if name:
                    rune['name'] = name.group(1)
                elif reg_desc.match(line):
                    rune['effects'] = []
                    for e in reg_subdesc.finditer(line):
                        classes = e.group(1)
                        classes = classes[:-1]
                        classes = re.split('/', classes)
                        rune['effects'].append( {'classes':classes,
                            'effect':re.split(',', e.group(2))} )
                    lvls = reg_clvl.search(line)
                    if lvls:
                        rune['clvl'] = lvls.group(1)
                        rune['ilvl'] = lvls.group(1)
                    else:
                        lvls = reg_ilvlclvl.search(line)
                        rune['ilvl'] = lvls.group(1)
                        rune['clvl'] = lvls.group(2)

    def results(self):
        print 'runes = []'
        for r in self.runes:
            print 'runes.append( Rune("{0}", {1}, {2}, "{3}", [\n\t{4}\n\t]) )'.format(
                    r['name'],
                    r['clvl'],
                    r['ilvl'],
                    r['rarity'],
                    ',\n\t'.join( [
                        'Effect('+str(e['classes'])+','+str(e['effect'])+')' #e['classes']
                        for e in r['effects'] ])
                    )
        print ''

    def results_json(self):
        print json.dumps(self.runes)

class WordParser(object):
    def __init__(self, filepath='', url='', debug=False):
        super(WordParser, self).__init__()
        self.words = []
        self.debug = debug
        if filepath:
            self._debug('WordParser uses file '+filepath)
            self.source = open(filepath)
        elif url:
            self._debug('WordParser uses url '+url)
            self.source = urllib.urlopen(url)
        else:
            raise 'You have to specify source file path or url!'
        # regexps for rw class correction
        self.__reg_ccls = [
                (re.compile('^(Armor|Sword|Axe|Mace)$'), '\\1s'),
                (re.compile('(All )?Melee Weapons'), 'Melee'),
                (re.compile('(All )?Missile Weapons'), 'Missile'),
                (re.compile('All Weapons'), 'Weapons'),
                (re.compile('Sheilds'), 'Shields'),
                (re.compile('Xbows'), 'Crossbows'),
                (re.compile('Works:\s*'), ''),
                (re.compile('Headgears?'), 'Helms'),
                (re.compile('Scepters Clvl.*'), 'Scepters'),
                (re.compile('(.*)\.'), '\\1')
                ]

    def _debug(self, *args):
        if self.debug:
            print ' '.join([str(x) for x in args])
    def _debug_noline(self, *args):
        if self.debug:
            print ' '.join([str(x) for x in args]),

    def _strip_html(self, txt):
        return re.sub('<[^>]+>', '', txt)
        #return txt

    def _correct_classes(self, classes):
        correct = []
        for cls in classes:
            #print cls,
            for pat,rep in self.__reg_ccls:
                cls = pat.sub(rep, cls)
                #print '=>', cls,
            #print
            #if cls[-1:] != 's':
            #    print
            #    print
            #    print
            correct.append(cls)
        return correct

    def _correct_word(self, w):
        w['classes'] = self._correct_classes(w['classes'])
        if str(w['effects']) == w['effects']:
            w['effects'] = w['effects'].strip()
            if w['effects'] in ['No', 'Yes']:
                w['effects'] = ['------ MANUAL CORRECTION REQUIRED ------']
        return w

    def parse(self):
        self._debug('start of runeword parsing')
        lines_to_data = -1
        word = None
        cnt = 0
        after_runes = False
        in_desc = False
        after_desc = False
        reg_name = re.compile("<td> ?<b><a [^>]*>([a-zA-Z' ]+)</a></b>")
        reg_clvl = re.compile("Clvl Required: ?([0-9]+)")
        reg_runes = re.compile('(<p><i>[a-zA-Z]+</i>)?(<br /> )?<a [^>]+>[A-Za-z]+</a> \([0-9]+\) ?\+ <a')
        reg_rune = re.compile('<a [^>]+>([A-Za-z]+)</a> \([0-9]+\)')
        reg_desc = re.compile('</td><td> [A-Za-z0-9\+\-]+')
        for line in self.source:
            cnt += 1
            if lines_to_data > 0 :
                # before table (lines before data countdown)
                self._debug_noline('.')
                lines_to_data -= 1
            elif line == '<h2> <span class="mw-headline" id="Alphabetical_List_of_All_Runewords">Alphabetical List of All Runewords</span></h2>\n':
                #start of table
                self._debug('runeword table start')
                lines_to_data = 12
            elif lines_to_data != 0:
                # before table (waiting)
                pass
            elif line == '</table>\n':
                #end of table
                self._debug('runeword table end')
                if word:
                    self.words.append(self._correct_word(word))
                    word = None
                return
            elif line == '<tr>\n':
                #start of word
                self._debug_noline('- runeword: ')
                tmpstr = 'word from line '+str(cnt)
                word = {'name':tmpstr, 'clvl':tmpstr, 'runes':[tmpstr],
                        'classes':'class: '+tmpstr,
                        'effects':tmpstr+'\n\t',
                        'ladderonly':False}
                after_runes = False
                in_desc = False
                after_desc = False
            elif not word:
                #before word (waiting)
                pass
            elif re.match('</td><td> Ladder Only', line):
                word['ladderonly'] = True
            elif line == '</td></tr>\n':
                #end of word
                self.words.append(self._correct_word(word))
                word = None
            else:
                name = reg_name.match(line)
                if name:
                    self._debug(name.group(1))
                    word['name'] = name.group(1)
                else:
                    clvl = reg_clvl.search(line)
                    if clvl:
                        word['clvl'] = clvl.group(1)
                    if reg_runes.match(line):
                        word['runes'] = []
                        for r in reg_rune.finditer(line):
                            word['runes'].append(r.group(1))
                        after_runes = True
                    elif after_runes:
                        word['classes'] = re.sub('\s*&amp;', ',', # switch '&amp;' to comma
                            re.sub('\s*\([^\)]+\)', '', # remove (...)
                                self._strip_html(line)))
                        word['classes'] = [c.strip() for c
                                in re.split(',', word['classes'])]
                        after_runes = False
                    elif not after_desc:
                        if reg_desc.match(line):
                            in_desc = True
                            word['effects'] = self._strip_html(line)
                        elif in_desc and line == '</p>\n':
                            in_desc = False
                            after_desc = True
                            word['effects'] = [e.strip() for e
                                    in re.split('\n', word['effects'])
                                    if e]
                        elif in_desc:
                            word['effects'] += self._strip_html(line)


    def results(self):
        print 'words = []'
        for w in self.words:
            print 'words.append( Word("{0}", {1}, {2}, {3}, \n\t{4},\n\t[ {5} ]\n\t) )'.format(
                    w['name'],
                    w['clvl'],
                    w['ladderonly'],
                    str(w['runes']),
                    w['classes'],
                    'Effect('+str(w['classes'])+', '+str(w['effects'])+')'
                    )
        print ''

    def results_json(self):
        print json.dumps(self.words)

if __name__ == '__main__':
    if ('-h' in sys.argv) or ('--help' in sys.argv):
        print """This script fetches rune and runeword lists from
http://diablo2.diablowiki.net and parses them into python 
lists of objects OR into json and prints to stdout.
Also you can use local files as data source.

        -h | --help:
            display this introduction text
        -j | --json:
            output is json instead of python lists
        -rf <file> | --runefile <file>:
        -rwf <file> | --runewordfile <file>:
            use <file> as fetched source for parsing of runes/runewords
        -d | --debug:
            print debugging info from parsing

Created by Queria Sa-Tas and released in Public Domain at 27.5.2011
"""
        sys.exit(1)

    use_json = False
    use_debug = False
    file_rune = ''
    file_runeword = ''

    argidx = 0
    while argidx < len(sys.argv):
        if sys.argv[argidx] in ['-j', '--json']:
            use_json = True
        if sys.argv[argidx] in ['-d', '--debug']:
            use_debug = True
        if sys.argv[argidx] in ['-rf', '--runefile']:
            if argidx == len(sys.argv):
                raise 'Specifily rune file or don\'t use -rf switch!'
            file_rune = sys.argv[argidx+1]
        if sys.argv[argidx] in ['-rwf', '--runewordfile']:
            if argidx == len(sys.argv):
                raise 'Specifily runeword file or don\'t use -rf switch!'
            file_runeword = sys.argv[argidx+1]
        argidx += 1
            
    if file_rune:
        rp = RuneParser(filepath=file_rune, debug=use_debug)
    else:
        rp = RuneParser(url='http://diablo2.diablowiki.net/Rune_list',
                debug=use_debug)

    if file_runeword:
        rwp = WordParser(filepath=file_runeword, debug=use_debug)
    else:
        rwp = WordParser(url='http://diablo2.diablowiki.net/Runewords',
                debug=use_debug)

    rp.parse()
    rwp.parse()

    if use_json:
        if use_debug:
            print 'Json output: -----------------------------------------------'
        print '{\n"runes":'
        rp.results_json()
        print ',\n"words":'
        rwp.results_json()
        print '\n}'
    else:
        print 'from rwo import Rune, Effect, Word'
        print ''
        rp.results()
        rwp.results()

# manual corrections:


#words.append( Word("Dragon", 61, True, ['Sur', 'Lo', 'Sol'], 
#	['Armors', 'Shields'],
#      [ Effect(['Armors', 'Shields'], 
#          ['20% Chance to Cast Level 18 Venom When Struck',
#              '12% Chance To Cast Level 15 Hydra On Striking',
#              'Level 14 Holy Fire Aura When Equipped', '+360 Defense',
#              '+230 Defense Vs. Missile', '+3-5 To All Attributes (varies)',
#              '+0.375-37.125 To Strength (Based on Character Level)',
#              '+5% To Maximum Lightning Resist', 'Damage Reduced by 7']),
#        Effect(['Armors'], ['Increase Maximum Mana 5%']),
#        Effect(['Shields'], ['+50 To Mana'])
#        ]
#	) )

#words.append( Word("Fortitude", 59, True, ['El', 'Sol', 'Dol', 'Lo'], 
#    ['Weapons', 'Armors'],
#    [ Effect(['Weapons', 'Armors'], [
#        '20% Chance To Cast Level 15 Chilling Armor when Struck',
#        '+25% Faster Cast Rate', '+300% Enhanced Damage',
#        '+1 To Light Radius', '120% Damage Taken Goes To Mana',
#        'All Resistances +25-30 (varies)', '+200% Enhanced Defense',
#        '+ To Life (Based on Character Level)*']),
#        Effect(['Weapons'], [ '+9 To Minimum Damage', '+50 To Attack Rating',
#           '20% Deadly Strike', 'Hit Causes Monster To Flee 25%']),
#        Effect(['Armor'],[ '+15 Defense', 'Replenish Life +7',
#           '+5% To Maximum Lightning Resistist', 'Damage Reduced By 7'])
#          ]
#	) )

#words.append( Word("Phoenix", 65, True, ['Vex', 'Vex', 'Lo', 'Jah'], 
#	['Weapons', 'Shields'],
#      [
#          Effect(['Weapons', 'Shields'], ["100% Chance To Cast level 40 Blaze When You Level-up",
#                  "40% Chance To Cast Level 22 Firestorm On Striking",
#                  "Level 10-15 Redemption Aura When Equipped (varies)",
#                  "-28% To Enemy Fire Resistance", "+15-21 Fire Absorb (varies)",
#                  "+350-400 Defense Vs. Missile (varies)", "+350-400% Enhanced Damage (varies)"]),
#          Effect(['Weapons'], [ "Ignores Target's Defense",
#              "14% Mana Stolen Per Hit", "20% Deadly Strike"]),
#          Effect(['Shields'], [ "+50 To Life", "+5% To Maximum Lightning Resist", "+10% To Maximum Fire Resist" ])
#	]) )

#words.append( Word("Spirit", 25, True, ['Tal', 'Thul', 'Ort', 'Amn'], 
#	['Shields', 'Swords'],
#      [
#          Effect(['Shields', 'Swords'], [
#              '+2 To All Skills',
#              '+25-35% Faster Cast Rate (varies)',
#              '+55% Faster Hit Recovery',
#              '+22 To Vitality',
#              '+250 Defense Vs. Missile',
#              '+89-112 To Mana (varies)',
#              '+3-8 Magic Absorb (varies)',
#              ]),
#          Effect(['Shields'], [
#              'Cold Resist +35%',
#              'Lightning Resist +35%',
#              'Poison Resist +35%',
#              'Attacker Takes Damage of 14'
#              ]),
#          Effect(['Swords'], [
#              'Adds 1-50 Lightning Damage',
#              'Adds 3-14 Cold Damage 3 Second Duration (Normal)',
#              '+75 Poison Damage Over 5 Seconds',
#              '7% Life Stolen Per Hit'
#              ])
#        ]
#	) )
