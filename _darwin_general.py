# Author: Kerey Roper
#
# Licensed under LGPL

import aenea
import aenea.configuration
from aenea import IntegerRef
from aenea.lax import Key
import dragonfly

context = aenea.ProxyPlatformContext('darwin')
grammar = dragonfly.Grammar('darwin_general', context=context)


class Mapping(dragonfly.MappingRule):
    mapping = {
        'screenshot': Key("csw-4"),
        'select': Key("win:up"),
        'spotlight': Key("w-space"),
        'task': Key("win:down") + Key("tab"),
    }
    extras = [
        IntegerRef('n', 1, 99),
    ]


grammar.add_rule(Mapping())
grammar.load()


def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
