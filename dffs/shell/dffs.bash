# dffs shell integration for bash/zsh
# Install dffs: pipx install dffs
# Add to your ~/.bashrc or ~/.zshrc:
#   eval "$(dffs-shell-integration bash)"

# Core diff-x aliases (color enabled by default)
alias dx='diff-x'
alias dxc='diff-x'
alias dxn='diff-x --no-color'
alias dxw='diff-x -w'
alias dxcw='diff-x -w'
alias dxwn='diff-x -w --no-color'

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
alias gdxc='git diff-x'
alias gdxn='git diff-x --no-color'
alias gdxs='git diff-x --cached'
alias gdxcs='git diff-x --cached'
alias gdxsn='git diff-x --cached --no-color'
alias gdxr='git diff-x -r'
alias gdxcr='git diff-x -r'
alias gdxrn='git diff-x -r --no-color'
alias gdxf='git diff-x -R'
alias gdxcf='git diff-x -R'
alias gdxfn='git diff-x -R --no-color'
alias gdxw='git diff-x -w'
alias gdxcw='git diff-x -w'
alias gdxwn='git diff-x -w --no-color'
alias gdxsw='git diff-x --cached -w'
alias gdxcsw='git diff-x --cached -w'
alias gdxswn='git diff-x --cached -w --no-color'
alias gdxrw='git diff-x -rw'
alias gdxcrw='git diff-x -rw'
alias gdxrwn='git diff-x -rw --no-color'
alias gdxfw='git diff-x -Rw'
alias gdxcfw='git diff-x -Rw'
alias gdxfwn='git diff-x -Rw --no-color'
