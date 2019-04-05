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
from config import get_configuration

config = get_configuration()

if config.get('os') == 'linux':
    git_context = aenea.ProxyPlatformContext('linux')
else:
    git_context = aenea.ProxyCustomAppContext(query={'id': 'terminal'})
grammar = dragonfly.Grammar('git', context=git_context)

git_mapping = aenea.configuration.make_grammar_commands('git', {
    'git': Text("git"),

    'git add patch': Text("git add -p") + Key("enter"),
    'git branch list': Text("git branch -l") + Key("enter"),
    'git branch list all': Text("git branch -a") + Key("enter"),
    'git commit': Text("git commit") + Key("enter"),
    'git [commit] amend': Text("git commit --amend") + Key("enter"),
    'git [commit] amend (changes|changed)': Text("git commit --amend -a") + Key("enter"),
    'git commit (changes|changed)': Text("git commit -a") + Key("enter"),
    'git fetch [upstream]': Text("git fetch --tags upstream") + Key("enter"),
    'git fetch all': Text("git fetch --all") + Key("enter"),
    'git pull': Text("git pull") + Key("enter"),
    'git status': Text("git status") + Key("enter"),
    'git stat': Text("git show --stat") + Key("enter"),
    'git log': Text("git log "),
    'git log current': Text("git log") + Key("enter"),
    'git ref log': Text("git reflog") + Key("enter"),
    'git diff': Text("git diff "),
    'git diff current': Text("git diff") + Key("enter"),
    'git diff (cashed|cached)': Text("git diff --cached") + Key("enter"),
    'git diff origin': Text("git diff origin/master") + Key("enter"),
    'git diff upstream': Text("git diff upstream/master") + Key("enter"),
    'git rebase continue': Text("git rebase --continue") + Key("enter"),

    # https://github.com/tgrosinger/dotfiles/blob/master/.gitconfig#L15
    'git hist': Text("git hist") + Key("enter"),

    # Incomplete Commands
    'git add': Text("git add "),
    'git blame': Text("git blame "),
    'git branch': Text("git branch "),
    'git branch (create|new)': Text("git checkout -b "),
    'git checkout': Text("git checkout "),
    'git checkout origin': Text("git checkout origin/master") + Key("enter"),
    'git checkout upstream': Text("git checkout upstream/master") + Key("enter"),
    'git cherry pick': Text("git cherry-pick "),
    'git clone': Text("git clone "),
    'git interactive rebase': Text("git rebase -i "),
    'git rebase interactive': Text("git rebase -i "),
    'git rebase interactive origin': Text("git rebase -i origin/master") + Key("enter"),
    'git rebase interactive upstream': Text("git rebase -i upstream/master") + Key("enter"),
    'git rebase': Text("git rebase "),
    'git rebase origin': Text("git rebase origin/master") + Key("enter"),
    'git rebase upstream': Text("git rebase upstream/master") + Key("enter"),
    'git remote add': Text("git remote add "),
    'git reset': Text("git reset "),
    'git revert': Text("git revert "),
    'git show': Text("git show "),
    'git stash': Text("git stash") + Key("enter"),
    'git stash pop': Text("git stash pop") + Key("enter"),
    'git push': Text("git push "),
    'git push origin': Text("git push origin "),
    'git push origin force': Text("git push origin -f "),

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
