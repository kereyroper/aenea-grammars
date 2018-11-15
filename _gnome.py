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

context = aenea.ProxyPlatformContext('linux')
grammar = dragonfly.Grammar('gnome', context=context)


class Mapping(dragonfly.MappingRule):
    mapping = {
        'screenshot': Key("ca-Print"),
        'search': Key("win"),
        'select': Key("alt:up"),
        'task': Key("alt:down") + Key("tab"),
    }
    extras = [
        IntegerRef('n', 1, 99),
    ]


grammar.add_rule(Mapping())
if config.get('os') == 'linux':
    grammar.load()


def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None

