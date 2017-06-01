# Created for aenea using libraries from the Dictation Toolbox
# https://github.com/dictation-toolbox/dragonfly-scripts
#
# Commands for interacting with JetBrains IDEs, such as PyCharm
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

jetbrains_context = aenea.ProxyCustomAppContext(match='regex', query={'id': r'(?i)((android)?.*studio|pycharm|rubymine)'})
grammar = dragonfly.Grammar('jetbrains', context=jetbrains_context)

basics_mapping = aenea.configuration.make_grammar_commands('jetbrains', {
    'action': Key('sw-a'),
    'back': Key('aw-left'),
    'debug (continue|run)': Key('aw-r'),
    'debug (next|over)': Key('f8'),
    'debug (step|into)': Key('f7'),
    '(file|pain) close': Key('w-w'),
    'file close all': Key('sw-w'),
    'file left [<n>]': Key('c-pgup:%(n)d'),
    '(file open|open file)': Key('sw-o'),
    'file right [<n>]': Key('c-pgdown:%(n)d'),
    'follow': Key("w-b"),
    'forward': Key('aw-right'),
    'import': Key('a-enter'),
    'open class': Key('w-o'),
    'rename': Key('s-f6'),
    'pain code': Key('ctrl:down') + Key('tab/30') + Key('s-tab') + Key('ctrl:up'),
    'pain debug': Key('w-5'),
    'pain files': Key('w-1'),
    'pain (search|results)': Key('w-3'),
    'pain test': Key('w-4'),
    'split move': Key('cw-y'),
    'split new': Key('cw-t'),
    'test debug': Key('acw-d'),
    'test run': Key('cw-r'),
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
