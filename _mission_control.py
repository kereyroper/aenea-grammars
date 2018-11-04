# Author: Kerey Roper
#
# Licensed under LGPL

import aenea
import aenea.configuration
from aenea import IntegerRef
from aenea.lax import Key
import dragonfly
from config import get_configuration

config = get_configuration()
context = aenea.ProxyPlatformContext('darwin')
grammar = dragonfly.Grammar('mission_control', context=context)


class Mapping(dragonfly.MappingRule):
    mapping = {
        '(works|workspace) <n>': Key("c-%(n)d"),
    }
    extras = [
        IntegerRef('n', 1, 99),
    ]


grammar.add_rule(Mapping())
if config.get('os') == 'darwin':
    grammar.load()


def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
