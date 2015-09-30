# Created for aenea using libraries from the Dictation Toolbox
# https://github.com/dictation-toolbox/dragonfly-scripts
#
# Author: Kerey Roper
#
# Licensed under LGPL

import aenea
import aenea.configuration
import aenea.proxy_contexts

from aenea.lax import Key, Text, Dictation
from aenea import (
    IntegerRef
)
import dragonfly

from pprint import pprint


pprint(aenea.proxy_contexts._get_context())
pprint(aenea.proxy_contexts._server_info())


def unload():
    pass
