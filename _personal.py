# Created for aenea using libraries from the Dictation Toolbox
# https://github.com/dictation-toolbox/dragonfly-scripts
#
# Commands for inserting personal details loaded from the config file
#
# Author: Tony Grosinger
#
# Licensed under LGPL

import aenea
import aenea.configuration
from aenea.lax import Function, Text
from aenea import Choice
import dragonfly
from config import get_configuration

config = get_configuration()
if config.get('os') == 'linux':
    context = aenea.ProxyPlatformContext('linux')
else:
    context = aenea.ProxyPlatformContext('darwin')
grammar = dragonfly.Grammar('generic', context=context)

commands = {}
if "full-name" in config:
    commands['my full name'] = Text("%s" % config["full-name"])
if "last-name" in config:
    commands['my last name'] = Text("%s" % config["last-name"])
if "first-name" in config:
    commands['my first name'] = Text("%s" % config["first-name"])
if "email-address" in config:
    commands['my email'] = Text("%s" % config["email-address"])
if "company-name" in config:
    commands['company name'] = Text("%s" % config["company-name"])


class Mapping(dragonfly.MappingRule):
    mapping = aenea.configuration.make_grammar_commands('personal', commands)
    extras = []

grammar.add_rule(Mapping())
grammar.load()


def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
