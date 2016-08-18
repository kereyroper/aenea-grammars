# Created for aenea using libraries from the Dictation Toolbox
# https://github.com/dictation-toolbox/dragonfly-scripts
#
# Commands for writing in the Ruby programming language
#
# Author: Kerey Roper
#
# Licensed under LGPL

import aenea
import aenea.configuration
from aenea.lax import Key, Function
from aenea import (
    IntegerRef,
    Text,
    Dictation,
)
from format import format_snake_case, format_pascal_case
import dragonfly


def create_class(text):
    Text('class %s' % format_pascal_case(text)).execute()
    Key('left').execute()


def create_module(text):
    Text('module %s' % format_pascal_case(text)).execute()
    Key('left').execute()


def create_public_function(text):
    Text('def %s()' % format_snake_case(text)).execute()
    Key('left').execute()


ruby_mapping = aenea.configuration.make_grammar_commands('ruby', {
    'new class [named] <text>': Function(create_class),
    'new module [named] <text>': Function(create_module),
    'new [public] (function|func) [named] <text>': Function(create_public_function),
    'comment': Key("escape, i") + Text("# "),
    '(ruby dock|(doc|documentation) string)': Text('##') + Key('enter'),

    # ruby
    "true": Text("true"),
    "false": Text("false"),
    '(none|null|nil)': Text("nil"),

    # not ported
    'print line': Text("print()") + Key("left"),
    "class method": Text("@classmethod\n"),
    "(def|define)": Text("def "),
    "(dict|dictionary)": Text("dict("),
    "set": Text("set("),
    'array': Key("lbracket, enter, enter, up, tab"),
    "sum": Text("sum("),
    "(len|length)": Text("len("),
    "list": Text("list("),
    "tuple": Text("tuple("),
    "is instance": Text("isinstance("),
    "init": Text("__init__("),
    "self dot": Text("self."),
    "iter items": Text(".iteritems("),
    "string join": Key("apostrophe, right")+Text(".join("),
})


class Ruby(dragonfly.MappingRule):
    mapping = ruby_mapping
    extras = [
        Dictation('text'),
        IntegerRef('n', 1, 999),
    ]


def get_grammar(context):
    ruby_grammar = dragonfly.Grammar('ruby', context=context)
    ruby_grammar.add_rule(Ruby())
    return ruby_grammar
