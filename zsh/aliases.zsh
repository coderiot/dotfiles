alias v='vim'
alias ..='cd ..'
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

# shortcut for python
alias py='python'

# shortcut for ipython
alias ipy="ipython"

# Python virtualenv shortcuts.
alias venv-init='virtualenv venv --no-site-packages'
alias venv-activate='source venv/bin/activate'

# color ls and grep
alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'
alias pass='vim -u $HOME/dotfiles/vim/encrypt_vimrc $HOME/.secrets/secrets.wiki'

# dont correct mv, cp, mkdir, pip
alias mv='nocorrect mv'
alias cp='nocorrect cp'
alias pip='nocorrect pip'
alias mkdir='nocorrect mkdir'
