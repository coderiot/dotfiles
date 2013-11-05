alias v='vim'
alias ...='cd ../..'
alias ....='cd ../../..'

alias vim='vim --servername vim'
alias pcat='pygmentize -f terminal256 -O style=monokai -g'

# change to parent dir
alias cd..='cd ..'

# start vimwiki
alias wiki='vim -c +VimwikiIndex'

# start diary and create Note for today
alias diary='vim -c +VimwikiMakeDiaryNote'

# Python virtualenv shortcuts.
alias venv-init='virtualenv venv -p /usr/local/bin/python --no-site-packages'
alias venv-activate='source venv/bin/activate'
