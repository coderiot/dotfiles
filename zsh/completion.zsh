# matches case insensitive for lowercase
zstyle ':completion:*' matcher-list 'm:{a-z}={A-Z}'

# pasting with tabs doesn't perform completion
zstyle ':completion:*' insert-tab pending

# tab complete cd ..
zstyle ':completion:*' special-dirs true

# tab completion menu
zstyle ':completion:*' menu select yes

# not just at the end
setopt completeinword

# Fallback to built in ls colors
zstyle ':completion:*' list-colors ''
