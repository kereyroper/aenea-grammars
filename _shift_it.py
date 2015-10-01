# Author: Kerey Roper
#
# Licensed under LGPL

import aenea
import aenea.configuration
from aenea.lax import Key, Text, Dictation
import dragonfly

context = aenea.ProxyPlatformContext('darwin')
grammar = dragonfly.Grammar('shift_it', context=context)


class Mapping(dragonfly.MappingRule):
    mapping = {
        # Note - mappings are different than ShiftIt defualt to be easier with Kinesys Advantage keyboard
        'shift port': Key('cw-left'),
        'shift starboard': Key('cw-right'),
        'shift top': Key('cw-up'),
        'shift bottom': Key('cw-down'),
        'shift max': Key('cw-m'),
        'shift next': Key('cw-n'),
    }


grammar.add_rule(Mapping())
grammar.load()


def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
