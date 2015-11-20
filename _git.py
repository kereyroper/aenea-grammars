# Created for aenea using libraries from the Dictation Toolbox
# https://github.com/dictation-toolbox/dragonfly-scripts
#
# Commands for interacting with Git
#
# Author: Tony Grosinger
#
# Licensed under LGPL

import aenea
import aenea.configuration
from aenea.lax import Key
from aenea import Text
import dragonfly

git_context = aenea.ProxyCustomAppContext(query={'id': 'terminal'})
grammar = dragonfly.Grammar('git', context=git_context)

git_mapping = aenea.configuration.make_grammar_commands('git', {
    'git': Text("git"),

    'git amend': Text("git commit --amend") + Key("enter"),
    'git commit': Text("git commit") + Key("enter"),
    'git commit (changes|changed)': Text("git commit -a") + Key("enter"),
    'git fetch': Text("git fetch upstream") + Key("enter"),
    'git fetch all': Text("git fetch --all") + Key("enter"),
    'git pull': Text("git pull") + Key("enter"),
    'git branches': Text("git branch -l") + Key("enter"),
    'git status': Text("git status") + Key("enter"),
    'git stat': Text("git show --stat") + Key("enter"),
    'git log': Text("git log") + Key("enter"),
    'git push': Text("git push") + Key("enter"),
    'git diff': Text("git diff "),
    'git diff current': Text("git diff") + Key("enter"),
    'git diff (cashed|cached)': Text("git diff --cached") + Key("enter"),
    'git diff upstream': Text("git diff upstream/master") + Key("enter"),

    # https://github.com/tgrosinger/dotfiles/blob/master/.gitconfig#L15
    'git hist': Text("git hist") + Key("enter"),

    # Incomplete Commands
    'git add': Text("git add "),
    'git blame': Text("git blame "),
    'git checkout': Text("git checkout "),
    'git checkout upstream': Text("git checkout upstream/master") + Key("enter"),
    'git cherry pick': Text("git cherry-pick "),
    'git interactive rebase': Text("git rebase -i "),
    'git rebase interactive': Text("git rebase -i "),
    'git rebase': Text("git rebase "),
    'git rebase upstream': Text("git rebase upstream/master") + Key("enter"),
    'git revert': Text("git revert "),
    'git show': Text("git show "),
    'git stash': Text("git stash") + Key("enter"),
    'git stash pop': Text("git stash pop") + Key("enter"),
    'git push to': Text("git push"),

    # SVN Commands
    'git trunk': Text("git checkout trunk-svn") + Key("enter"),
    'git SVN pull': Text("git svn rebase") + Key("enter"),
    'git SVN rebase interactive': Text("git rebase -i trunk-svn") + Key("enter"),
    'git SVN rebase': Text("git rebase trunk-svn") + Key("enter"),
})


class Mapping(dragonfly.MappingRule):
    mapping = git_mapping

grammar.add_rule(Mapping())
grammar.load()


def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
