"""A command module for Dragonfly, for controlling the native Slack client.

-----------------------------------------------------------------------------
Licensed under the LGPL3.

"""

import aenea
from aenea import Config, Section, Item, AppContext, Grammar, MappingRule, IntegerRef, Dictation, Choice

from aenea import (
    Key,
    Text,
)
from config import get_configuration

config = get_configuration()

slack_config = Config("Slack")
slack_config.usernames = Section("Username Mappings")
slack_config.usernames.map = Item(
    {
        "All": "all",
        "Channel": "channel"
    }
)

slack_config.load()

class NavigationRule(MappingRule):
    mapping = {
        "move up [<n>]":                                    Key("a-up:%(n)d"),
        "move down [<n>]":                                  Key("a-down:%(n)d"),
        "(channel|chat) leave":                             Text("/leave") + Key("enter:2"),
        "(channel|chat) join":                              Key("w-k"),
    }

    extras = [
        IntegerRef("n", 1, 10),
    ]

    defaults = {
        "n": 1,
    }

class ChatRule(MappingRule):
    mapping = {
        "at <user>":     Text("@%(user)s "),
        "send":          Key("enter"),
    }

    extras = [
        Choice("user", slack_config.usernames.map),
    ]


# winContext = AppContext(executable="slack")
if config.get('os') == 'linux':
    context = aenea.ProxyCustomAppContext(executable="slack")
else:
    context = aenea.ProxyCustomAppContext(query={'id': 'slack'})

grammar = Grammar("slack_general", context=context)
grammar.add_rule(NavigationRule())
grammar.add_rule(ChatRule())
grammar.load()

# Unload function which will be called by natlink at unload time.
def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None

