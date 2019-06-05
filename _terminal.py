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
from config import get_configuration

config = get_configuration()
try:
    import aenea.communications
except ImportError:
    print 'Unable to import Aenea client-side modules.'
    raise

if config.get('os') == 'linux':
    terminal_context = aenea.ProxyCustomAppContext(query={'executable': 'terminal'})
else:
    terminal_context = aenea.ProxyCustomAppContext(query={'id': 'terminal'})
grammar = dragonfly.Grammar('terminal', context=terminal_context)

terminal_mapping = aenea.configuration.make_grammar_commands('terminal', {
    # Terminal commands
    "background": Text("bg") + Key("enter"),
    "cancel": Key("c-c"),

    # dir is hard to say and recognize. Use something else
    'deer back': Text("cd -") + Key("enter"),
    'deer up': Text("cd ..") + Key("enter"),
    'deer list': Text("ls") + Key("enter"),
    'deer list all': Text("ls -lha") + Key("enter"),
    'deer list details': Text("ls -lh") + Key("enter"),
    'deer list time [sorted]': Text("ls -ltr") + Key("enter"),
    'deer into': Text("cd "),
    'deer (make|create|new)': Text("mkdir "),

    "edit": Text("vim "),

    "foreground": Text("fg") + Key("enter"),
    "recent": Key("c-r"),

    "grep": Text("grep "),
    "grep Perl": Text("grep -P "),

    "process list": Text("ps aux "),
    "process IO nice": Text("ionice -c"),
    "process IO nice low": Text("ionice -c3 -p "),
    "process re nice": Text("renice -n "),
    "process re nice low": Text("renice -n 10 "),
    "process re nice hi": Text("renice -n -10 "),

    "shell [connect|into]": Text("ssh "),
    "shell disconnect": Key("enter") + Key("tilde") + Key("dot"),

    "some": Text("paste -sd+ - | bc"),

    "(cat|concatenate)": Text("cat "),
    "less": Text("less "),
    "suspend": Key("c-z"),
    "(tail|tell)": Text("tail "),  # apparently Dragon thinks I'm a Southerner
    "tail follow": Text("tail -f "),

    '(terminal|term) clear': Text("clear") + Key("enter"),
    '(terminal|term) left [<n>]': Key("w-lbrace:%(n)d"),
    '(terminal|term) right [<n>]': Key("w-rbrace:%(n)d"),
    '(terminal|term) new [tab]': Key("w-t"),
    '(terminal|term) exit': Key("c-d"),
    '(terminal|term) close': Key("w-w"),
    'cross args': Text('xargs '),

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
    'rails (migrate|migration) (create|generate)': Text('rails generate migration '),
    'rails migrate': Text("rake db:migrate"),
    'rails (migrate|migration) rollback': Text("rake db:rollback"),
    'rails migrate test': Text("rake db:migrate RAILS_ENV=test"),
    'rails (migrate|migration) rollback test': Text("rake db:rollback RAILS_ENV=test"),
    'rails test coverage': Text("rake simplecov") + Key("enter"),
    'rails test run': Text("rake test") + Key("enter"),

    # Python
    'Pip install': Text('pip install '),
    'Pip install requirements': Text('pip install -r requirements.txt') + Key("enter"),
    'Python test [run] end 2 end': Text("pytest tests/e2e") + Key("enter"),
    'Python test [run] local': Text("pytest tests/local") + Key("enter"),
    'Python test [run] integration': Text("pytest tests/local/integration") + Key("enter"),
    'Python test [run] [unit]': Text("pytest tests/local/unit") + Key("enter"),
    'serverless deploy': Text('sls deploy'),
    'virtual environment activate': Text('source venv/bin/activate') + Key("enter"),
    'virtual environment create': Text('virtualenv venv') + Key("enter"),
    'virtual environment deactivate': Text('deactivate') + Key("enter"),
    'virtual environment delete': Text('rm -rf venv'),
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
