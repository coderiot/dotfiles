# add global .gitignore: git config --global core.excludesfile ~/.gitignore
# start vim with v
alias v='vim'
alias vim='vim --servername vim'
alias pcat='pygmentize'

# open dir and list dirs
function cdl() {
        cd "$1"
        dir
}

# history bindings
bind '"\e[5~": history-search-backward'
bind '"\e[6~": history-search-forward'

bind 'set completion-ignore-case on'
