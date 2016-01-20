# Created for aenea using libraries from the Dictation Toolbox
# https://github.com/dictation-toolbox/dragonfly-scripts
#
# Commands for interacting with PyCharm
# Other commands are covered by using Vim emulation
#
# Author: Kerey Roper
#
# Licensed under LGPL

import aenea
import aenea.configuration
from aenea.lax import Key, Function
from aenea import (
    Dictation,
    IntegerRef,
    Text,
    Choice
)
import dragonfly

from _generic_edit import pressKeyMap

pycharm_context = aenea.ProxyCustomAppContext(query={'id': 'pycharm'})
grammar = dragonfly.Grammar('pycharm', context=pycharm_context)

basics_mapping = aenea.configuration.make_grammar_commands('pycharm', {
    'back': Key('aw-left'),
    'file close': Key('w-w'),
    'file left [<n>]': Key('c-pgup:%(n)d'),
    '(file open|open file)': Key('sw-o'),
    'file right [<n>]': Key('c-pgdown:%(n)d'),
    'follow': Key("w-b"),
    'forward': Key('aw-right'),
    'open class': Key('w-o'),
    'refs': Key('a-f7'),
    })


class Basics(dragonfly.MappingRule):
    mapping = basics_mapping
    extras = [
        Dictation('text'),
        IntegerRef('n', 1, 999),
        IntegerRef('n2', 1, 999),
    ]
    defaults = {
        "n": 1,
    }


grammar.add_rule(Basics())
grammar.load()


def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
