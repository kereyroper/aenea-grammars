# Created for aenea using libraries from the Dictation Toolbox
# https://github.com/dictation-toolbox/dragonfly-scripts
#
# Commands for interatcting with Chrome. Requires the Vimium extension.
# http://vimium.github.io/
#
# Author: Tony Grosinger
#
# Licensed under LGPL

import aenea
import aenea.configuration
from aenea.lax import Key, Text, Dictation
from aenea import (
    IntegerRef
)
import dragonfly
from config import get_configuration

config = get_configuration()


if config.get('os') == 'linux':
    chrome_context = aenea.ProxyAppContext(executable="chromium")
else:
    chrome_context = aenea.ProxyCustomAppContext(query={'id': 'chrome'})
grammar = dragonfly.Grammar('chrome', context=chrome_context)

window_mapping = {
    # Tab navigation
    'page (previous|left) [<n>]': Key("c-pgup:%(n)d"),
    'page (next|right) [<n>]': Key("c-pgdown:%(n)d"),
    'page <n>': Key("w-%(n)d"),
    'page new': Key("w-t"),
    'page reopen': Key("ws-t"),
    'page close': Key("w-w"),
    'page back': Key("s-h"),
    'page forward': Key("s-l"),
    'refresh': Key("r"),
    'link': Key("f"),
    'link new': Key("s-f"),

    #  Moving around
    'more': Key("c-e:10"),
    'less': Key("c-y:10"),
    'top': Key("g, g"),
    'bottom': Key("s-g"),
    'back': Key("s-h"),
    'forward': Key("s-l"),

    #  Searching
    'find <text>': Key("escape, slash") + Text("%(text)s") + Key("enter"),
    'next': Key("n"),
    'prev|previous': Key("N"),

    # Stuff below here is general Chrome, not Vimium specific
    # Debugger
    'continue': Key("f8"),
    'over': Key("f10"),
    'step into': Key("f11"),
    'step out': Key("s-f11"),

    # Tab to window extension
    'page detach': Key("as-x"),
}

gmail_mapping = {
    'open': Key("o"),
    'inbox': Key("g, i"),
    '[go to] label <text>': Key("g, l") + Text("%(text)s") + Key("enter"),
    '(earl|early|earlier)': Key("j"),
    '(late|later)': Key("k"),
}


class Mapping(dragonfly.MappingRule):
    mapping = window_mapping
    extras = [
        IntegerRef('n', 1, 99),
        Dictation('text'),
    ]
    defaults = {
        "n": 1,
    }

class MappingMail(dragonfly.MappingRule):
     mapping = gmail_mapping
     extras = [
        Dictation('text')
     ]


grammar.add_rule(Mapping())
grammar.add_rule(MappingMail())
grammar.load()


def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
