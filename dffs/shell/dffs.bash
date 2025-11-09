# dffs shell integration for bash/zsh
# Install dffs: pipx install dffs
# Add to your ~/.bashrc or ~/.zshrc:
#   eval "$(dffs-shell-integration bash)"

# Core diff-x aliases (color enabled by default)
alias dx='diff-x'
alias dxw='diff-x -w'

# Core comm-x aliases
alias cx='comm-x'
alias cx1='comm-x -1'
alias cx2='comm-x -2'
alias cx3='comm-x -3'
alias cx12='comm-x -12'
alias cx13='comm-x -13'
alias cx23='comm-x -23'

# Core git-diff-x aliases (color enabled by default)
alias gdx='git diff-x'
alias gdxs='git diff-x --cached'
alias gdxr='git diff-x -r'
alias gdxf='git diff-x -R'
alias gdxw='git diff-x -w'
alias gdxsw='git diff-x --cached -w'
alias gdxrw='git diff-x -rw'
alias gdxfw='git diff-x -Rw'
