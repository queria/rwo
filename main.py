#!/usr/bin/env python

import sys
import os
import urlparse
import cgi
sys.path.append(os.path.dirname(__file__))
import rwo
import data
from Cheetah import Template

MYDIR = os.path.dirname(__file__)

def tpl(template_name):
    t = Template.Template(file=MYDIR+'/tpl/'+template_name)
    t.tpldir = MYDIR+'/tpl/'
    return t

def make_list(maybe_list):
    if not isinstance(maybe_list, list):
        maybe_list = [maybe_list]
    return maybe_list

def minint(numstr, safenum):
    try:
        numstr = int(numstr)
    except ValueError:
        return safenum
    if safenum < numstr:
        return safenum
    return numstr

def maxint(numstr, safenum):
    try:
        numstr = int(numstr)
    except ValueError:
        return safenum
    if safenum > numstr:
        return safenum
    return numstr

lists = rwo.RWO(data.runes, data.words)

def index(req, selected_runes=[], selected_classes=[], clvl_min=1, clvl_max=99,
        fulltext='', runecount=0):
    """starting point - select all rw matching criterias and renders main html
    template"""
    
    selected_runes = make_list(selected_runes)
    selected_classes = make_list(selected_classes)
    
    if not selected_runes:
        selected_runes = [r.name for r in lists.all_runes()]
    if not selected_classes:
        selected_classes = [c['name'] for c in lists.all_item_classes()]

    clvl_min = maxint(clvl_min, 1)
    clvl_max = minint(clvl_max, 99)

    runecount = minint(runecount, 6)
    runecount = maxint(runecount, 0)

    t = tpl('main.html')
    t.clvl_min = clvl_min
    t.clvl_max = clvl_max
    t.runes = lists.all_runes_by_rarity()
    t.runes_selected = selected_runes
    t.item_classes = lists.all_item_classes()
    t.item_classes_selected = selected_classes
    t.fulltext = fulltext 
    t.runecount = runecount
    t.words = lists.search_words(
            selected_runes,
            selected_classes,
            clvl_min, clvl_max,
            fulltext,
            runecount)
    t.log = lists.log
    return t

def index_cgi():
    args = cgi.FieldStorage()
    print 'Content-Type: text/html'
    print ''
    print index(None,
            args.getlist('selected_runes'),
            args.getlist('selected_classes'),
            args.getfirst('clvl_min', 1),
            args.getfirst('clvl_max', 99),
            args.getfirst('fulltext', ''),
            args.getfirst('runecount', 0))

def application(environ, start_response):
    args = urlparse.parse_qs(environ['QUERY_STRING'])
    status = '200 OK'
    resp_headers = [('Content-Type', 'text/html')]
    start_response(status, resp_headers)
    return [str(index(None,
            args.get('selected_runes', []),
            args.get('selected_classes', []),
            args.get('clvl_min', [1])[0],
            args.get('clvl_max', [99])[0],
            args.get('fulltext', [''])[0],
            args.get('runecount', [1])[0])), '#'+str(os.getpid())]

if __name__ == '__main__':
    index_cgi()

