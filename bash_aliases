# add global .gitignore: git config --global core.excludesfile ~/.gitignore
# start vim with v
alias v='vim'

# open dir and list dirs
function cdl() {
        cd "$1"
        dir
}
