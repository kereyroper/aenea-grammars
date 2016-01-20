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
    Text,
)
import dragonfly

from _generic_edit import pressKeyMap

context = aenea.ProxyPlatformContext('darwin')
grammar = dragonfly.Grammar('jargon', context=context)

basics_mapping = aenea.configuration.make_grammar_commands('jargon', {
    'H (base|space)': Text('HBase'),
    })


class Basics(dragonfly.MappingRule):
    mapping = basics_mapping


grammar.add_rule(Basics())
grammar.load()


def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
