# add global .gitignore: git config --global core.excludesfile ~/.gitignore
# start vim with v
alias v='vim'
alias vim='vim --servername vim'

# open dir and list dirs
function cdl() {
        cd "$1"
        dir
}
