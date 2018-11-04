# Created for aenea using libraries from the Dictation Toolbox
# https://github.com/dictation-toolbox/dragonfly-scripts
#
# Commands for interacting with tmux
#
# Author: Tony Grosinger
#
# Licensed under LGPL

import aenea
import aenea.configuration
from aenea.lax import Key
from aenea.wrappers import Repeat
#from aenea.wrappers import ActionRepetition, Repeat
from aenea import IntegerRef
import dragonfly
from config import get_configuration

config = get_configuration()

if config.get('os') == 'linux':
    tmux_context = aenea.ProxyCustomAppContext(query={'executable': 'terminal'})
else:
    tmux_context = aenea.ProxyCustomAppContext(query={'id': 'terminal'})
grammar = dragonfly.Grammar('tmux', context=tmux_context)

tmux_mapping = aenea.configuration.make_grammar_commands('tmux', {
    'team (right|next) [<n>]': Key("c-b, n:%(n)d"),
    'team (left|previous) [<n>]': Key("c-b, p:%(n)d"),
    #'team test [<n>]': ActionRepetition(Key("b:%(n)d, d:%(n)d"), Repeat(extra="%(n)d"),
    'team (create|new)': Key("c-b, c"),
    'team <n>': Key("c-b, %(n)d"),
    'team rename': Key("c-b, comma"),
    'team scroll back': Key("c-b, lbracket"),
    'team switch': Key("c-b, w"),
    'team exit': Key("c-b, backslash"),
    'team detach': Key("c-b, d"),

    'team [pane] vertical': Key("c-b, percent"),
    'team [pane] horizontal': Key("c-b, dquote"),
    'team swap': Key("c-b, o"),
    'team pane up': Key("c-b, up"),
    'team pane down': Key("c-b, down"),
    'team pane left': Key("c-b, left"),
    'team pane right': Key("c-b, right"),
    'team pane close': Key("c-b, x")
})


class Mapping(dragonfly.MappingRule):
    mapping = tmux_mapping
    extras = [
        IntegerRef('n', 1, 99)
    ]
    defaults = {
        "n": 1,
    }

grammar.add_rule(Mapping())
grammar.load()


def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
