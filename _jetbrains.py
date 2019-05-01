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
from config import get_configuration

config = get_configuration()

if config.get('os') == 'linux':
    jetbrains_context = aenea.ProxyCustomAppContext(query={'executable': 'pycharm'})
    mod = 'c'
else:
    jetbrains_context = aenea.ProxyCustomAppContext(match='regex', query={'id': r'(?i)((android)?.*studio|pycharm|rubymine)'})
    mod = 'w'
grammar = dragonfly.Grammar('jetbrains', context=jetbrains_context)

basics_mapping = aenea.configuration.make_grammar_commands('jetbrains', {
    'action': Key(mod + 's-a'),
    'back': Key(mod + 'a-left'),
    '(class open|open class)': Key(mod + '-n'),
    'debug (continue|run)': Key(mod + 'a-r'),
    'debug (next|over)': Key('f8'),
    'debug (step|into)': Key('f7'),
    '(file|pain) close': Key(mod + '-w'),
    'file close all': Key(mod + 's-w'),
    'file left [<n>]': Key('c-pgup/10:%(n)d'),
    '(file open|open file)': Key(mod + 's-n'),
    'file right [<n>]': Key('c-pgdown/10:%(n)d'),
    'follow': Key(mod + "-b"),
    'forward': Key(mod + 'a-right'),
    '(implementations|implements)': Key(mod + "a-b"),
    'import': Key('a-enter'),
    'rename': Key('s-f6'),
    'pain code': Key('ctrl:down') + Key('tab/30') + Key('s-tab') + Key('ctrl:up'),
    'pain debug': Key(mod + '-5'),
    'pain files': Key(mod + '-1'),
    'pain (search|results)': Key(mod + '-3'),
    'pain test': Key(mod + '-4'),
    'split move': Key('cw-y'),
    'split new': Key('cw-t'),
    'test debug': Key('acw-d'),
    'test run': Key('cw-r'),
    'test run current': Key('cs-r'),
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
