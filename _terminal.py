# Created for aenea using libraries from the Dictation Toolbox
# https://github.com/dictation-toolbox/dragonfly-scripts
#
# Commands for interacting with terminal and desktop environment
#
# Author: Tony Grosinger
#
# Licensed under LGPL

import aenea
import aenea.configuration
from aenea import Dictation, IntegerRef
from aenea.lax import Key, Text
import dragonfly
try:
    import aenea.communications
except ImportError:
    print 'Unable to import Aenea client-side modules.'
    raise

terminal_context = aenea.ProxyCustomAppContext(query={'id': 'terminal'})
grammar = dragonfly.Grammar('terminal', context=terminal_context)

terminal_mapping = aenea.configuration.make_grammar_commands('terminal', {
    # Terminal commands
    "background": Key("c-z"),
    "cancel": Key("c-c"),

    # dir is hard to say and recognize. Use something else
    'deer up': Text("cd ..") + Key("enter"),
    'deer list': Text("ls") + Key("enter"),
    'deer list all': Text("ls -lha") + Key("enter"),
    'deer list details': Text("ls -lh") + Key("enter"),
    'deer into': Text("cd "),

    "foreground": Text("fg") + Key("enter"),
    "recent": Key("c-r"),

    "grep Perl": Text("grep -P"),

    "shell connect": Text("ssh "),
    "shell disconnect": Key("enter") + Key("tilde") + Key("dot"),

    "some": Text("paste -sd+ - | bc"),

    "(cat|concatenate)": Text("cat "),
    "less": Text("less "),
    "(tail|tell)": Text("tail "),  # apparently Dragon thinks I'm a Southerner
    "tail follow": Text("tail -f "),

    '(terminal|term) clear': Text("clear") + Key("enter"),
    '(terminal|term) left [<n>]': Key("w-lbrace:%(n)d"),
    '(terminal|term) right [<n>]': Key("w-rbrace:%(n)d"),
    '(terminal|term) new [tab]': Key("w-t"),
    '(terminal|term) exit': Key("c-d"),
    '(terminal|term) close': Key("w-w"),

    # Common words
    '(pseudo|sudo|pseudo-)': Text("sudo "),
    '(apt|app) get': Text("sudo apt-get "),
    '(apt|app) get install': Text("sudo apt-get install "),

    # Postgres
    'post development': Text("psql kww_development") + Key("enter"),
    'post test': Text("psql kww_test") + Key("enter"),

    # Rails
    'bundle install': Text("bundle install") + Key("enter"),
    'bundle update': Text("bundle update") + Key("enter"),
    'rails console': Text("rails console") + Key("enter"),
    'rails console production': Text("heroku run rails console --app kww")+ Key("enter"),
    'rails console reporting': Text("heroku run rails console --app kww-report")+ Key("enter"),
    'rails console staging': Text("heroku run rails console --app kww-staging")+ Key("enter"),
    '[rails] (migrate|migration) create': Text('rails generate migration '),
    '[rails] migrate': Text("rake db:migrate"),
    '[rails] migrate rollback': Text("rake db:rollback"),
    'test coverage': Text("rake simplecov") + Key("enter"),
    'test run': Text("rake test") + Key("enter"),
})


class Mapping(dragonfly.MappingRule):
    mapping = terminal_mapping
    extras = [
        Dictation('text'),
        IntegerRef('n', 1, 999),
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
