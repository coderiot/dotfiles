autoload -U colors && colors

autoload -Uz vcs_info

zstyle ':vcs_info:*' stagedstr "%{$fg_bold[green]%}●%{$reset_color%}"
zstyle ':vcs_info:*' unstagedstr "%{$fg_bold[yellow]%}●%{$reset_color%}"
zstyle ':vcs_info:*' check-for-changes true
zstyle ':vcs_info:(sv[nk]|bzr):*' branchformat '%b%F{1}:%F{11}%r'
zstyle ':vcs_info:*' enable git svn
precmd () {
    RPROMPT=""
    if [[ -z $(git ls-files --other --exclude-standard 2> /dev/null) ]] {
        zstyle ':vcs_info:*' formats '[%F{green}%b%c%u%F{cyan}]%f'
    } else {
       zstyle ':vcs_info:*' formats '[%F{green}%b%c%u%F{red}●%F{cyan}]%f'
    }

    vcs_info
}

setopt prompt_subst
local vcsi="\${vcs_info_msg_0_}"
PROMPT="%{$fg[red]%}%n%{$reset_color%}@%{$fg[green]%}%m %{$fg_bold[magenta]%}%1~ %{$reset_color%}%{$fg[cyan]%}${vcsi}%{$fg[cyan]%}%#%{$reset_color%} "

# remove previous rprompts
setopt transientrprompt

# make sure zsh starts in command mode
function zle-line-init {
    zle -K viins
    zle reset-prompt
}

zle -N zle-line-init

# display if zsh in normal mode
function zle-keymap-select {
    VIM_PROMPT="%{$fg_bold[yellow]%} [% NORMAL]% %{$reset_color%}"
    RPS1="${${KEYMAP/vicmd/$VIM_PROMPT}/(main|viins)/} $EPS1"
    RPS2=$RPS1
    zle reset-prompt
}

zle -N zle-keymap-select

# clear rprompt
function zle-line-finish {
    RPROMPT=""
    zle reset-prompt
}

zle -N zle-line-finish
