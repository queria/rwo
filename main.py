#!/usr/bin/env python

import sys
import os
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

def index(req, selected_runes=[], selected_classes=[], clvl_min=1, clvl_max=99,
        ineffect=''):
    """starting point - select all rw matching criterias and renders main html
    template"""
    lists = rwo.RWO(data.runes, data.words)

    selected_runes = make_list(selected_runes)
    selected_classes = make_list(selected_classes)
    
    if not selected_runes:
        selected_runes = [r.name for r in lists.all_runes()]
    if not selected_classes:
        selected_classes = [c['name'] for c in lists.all_item_classes()]

    clvl_min = maxint(clvl_min, 1)
    clvl_max = minint(clvl_max, 99)

    t = tpl('main.html')
    t.clvl_min = clvl_min
    t.clvl_max = clvl_max
    t.runes = lists.all_runes_by_rarity()
    t.runes_selected = selected_runes
    t.item_classes = lists.all_item_classes()
    t.item_classes_selected = selected_classes
    t.ineffect = ineffect
    t.words = lists.search_words(
            selected_runes,
            selected_classes,
            clvl_min, clvl_max,
            ineffect)
    t.log = lists.log
    return t

if __name__ == '__main__':
    index(None)

