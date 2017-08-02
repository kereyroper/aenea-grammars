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

    "foreground": Text("fg") + Key("enter"),
    "recent": Key("c-r"),

    "grep Perl": Text("grep -P"),

    "shell connect": Text("ssh "),
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
    'Chi bow (builds|packages)': Text('eatsa-deploy packages -a cibo -l 5') + Key("enter"),
    'Chi bow (config|configure) (int|integration)': Text('eatsa-deploy -e int config -e cibo/common-config.yaml'),
    'Chi bow (config|configure) (prod|production)': Text('eatsa-deploy -e prod config -e cibo/common-config.yaml'),
    'Chi bow (config|configure) (stage|staging)': Text('eatsa-deploy -e stage config -e cibo/common-config.yaml'),
    'Chi bow deploy (int|integration)': Text('eatsa-deploy -e int deploy -a cibo -s all'),
    'Chi bow deploy (prod|production)': Text('eatsa-deploy -e prod deploy -a cibo -s one'),
    'Chi bow deploy (stage|staging)': Text('eatsa-deploy -e stage deploy -a cibo -s all'),
    'Chi bow list (int|integration)': Text('eatsa-deploy -e int deploy -a cibo -r') + Key("enter"),
    'Chi bow list (prod|production)': Text('eatsa-deploy -e prod deploy -a cibo -r') + Key("enter"),
    'Chi bow list (stage|staging)': Text('eatsa-deploy -e stage deploy -a cibo -r') + Key("enter"),
    'Chi bow shell (int|integration)': Text('eatsa-deploy -e int connect cibo') + Key("enter"),
    'Chi bow shell (prod|production)': Text('eatsa-deploy -e prod connect cibo') + Key("enter"),
    'Chi bow shell (stage|staging)': Text('eatsa-deploy -e stage connect cibo') + Key("enter"),
    'hub (builds|packages)': Text('eatsa-deploy packages -a hub -l 5') + Key("enter"),
    'hub (config|configure) (int|integration)': Text('eatsa-deploy -e int config -e hub/common-config.yaml'),
    'hub (config|configure) (prod|production)': Text('eatsa-deploy -e prod config -e hub/common-config.yaml'),
    'hub (config|configure) (stage|staging)': Text('eatsa-deploy -e stage config -e hub/common-config.yaml'),
    'hub deploy local': Text('eatsa-deploy deploy -a hub') + Key("enter"),
    'hub deploy (int|integration)': Text('eatsa-deploy -e int deploy -a hub -s all'),
    'hub deploy (prod|production)': Text('eatsa-deploy -e prod deploy -a hub -s one'),
    'hub deploy (stage|staging)': Text('eatsa-deploy -e stage deploy -a hub -s all'),
    'hub list local': Text('eatsa-deploy deploy -a hub -r') + Key("enter"),
    'hub list (int|integration)': Text('eatsa-deploy -e int deploy -a hub -r') + Key("enter"),
    'hub list (prod|production)': Text('eatsa-deploy -e prod deploy -a hub -r') + Key("enter"),
    'hub list (stage|staging)': Text('eatsa-deploy -e stage deploy -a hub -r') + Key("enter"),
    'hub shell local': Text('eatsa-deploy connect localdev') + Key("enter"),
    'hub shell (int|integration)': Text('eatsa-deploy -e int connect hub-shell') + Key("enter"),
    'hub shell (prod|production)': Text('eatsa-deploy -e prod connect hub-shell') + Key("enter"),
    'hub shell (stage|staging)': Text('eatsa-deploy -e stage connect hub-shell') + Key("enter"),
    'Python test [run]': Text("pytest") + Key("enter"),
    'rails console': Text("rails console") + Key("enter"),
    '[rails] (migrate|migration) create': Text('rails generate migration '),
    '[rails] migrate': Text("rake db:migrate"),
    '[rails] migrate rollback': Text("rake db:rollback"),
    'router (builds|packages)': Text('eatsa-deploy packages -a router -l 5') + Key("enter"),
    'router (config|configure) (int|integration)': Text('eatsa-deploy -e int config -e router/common-config.yaml'),
    'router (config|configure) (prod|production)': Text('eatsa-deploy -e prod config -e router/common-config.yaml'),
    'router (config|configure) (stage|staging)': Text('eatsa-deploy -e stage config -e router/common-config.yaml'),
    'router deploy local': Text('eatsa-deploy deploy -a router') + Key("enter"),
    'router deploy (int|integration)': Text('eatsa-deploy -e int deploy -a router -s all'),
    'router deploy (prod|production)': Text('eatsa-deploy -e prod deploy -a router -s one'),
    'router deploy (stage|staging)': Text('eatsa-deploy -e stage deploy -a router -s all'),
    'router list local': Text('eatsa-deploy deploy -a router -r') + Key("enter"),
    'router list (int|integration)': Text('eatsa-deploy -e int deploy -a router -r') + Key("enter"),
    'router list (prod|production)': Text('eatsa-deploy -e prod deploy -a router -r') + Key("enter"),
    'router list (stage|staging)': Text('eatsa-deploy -e stage deploy -a router -r') + Key("enter"),
    'test coverage': Text("rake simplecov") + Key("enter"),
    'test run': Text("rake test") + Key("enter"),

    # Python
    'serverless deploy': Text('sls deploy'),
    'virtual environment activate': Text('source venv/bin/activate') + Key("enter"),
    'virtual environment deactivate': Text('deactivate') + Key("enter"),
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
