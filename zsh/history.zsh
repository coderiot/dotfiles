#------------------------------
# History stuff
#------------------------------
HISTFILE=~/.zsh_history
HISTSIZE=1000
SAVEHIST=1000

# append history list to the history file; this is the default but we make sure
# because it's required for share_history.
setopt append_history

#  Prevent from putting duplicate lines in the history
setopt HIST_IGNORE_DUPS

# import new commands from the history file also in other zsh-session
setopt share_history
