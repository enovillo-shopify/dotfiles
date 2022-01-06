# Get some defaults
source /etc/zsh/zshrc.default.inc.zsh

alias la="ls -a"
alias lla="ls -l -a"


# The following is modified from /etc/zsh/zshrc.default.inc.zsh

# Show the branch name (%b) in blue, followed by any
# additional miscellaneous (%m) info that the git
# driver provides in yellow. Typically %m will be empty.
zstyle ':vcs_info:git:*' formats $'%F{154}%b%F{yellow}%m%{\x1b[0m%} '

# %{<text>%} signals that the <text> prints with zero width, for zsh to
#   calculate the printed width of the string.
#
# Was last command successful? (  %(?.<yes>.<no>)  )
# yes => spin logo icon in blue33 (\x1b[38;5;33m)
# no  => styled x, then exit status (%?) in red
# then current directory (~) in bold (%B<text>%b)
# ...followed by git info ($vcs_info_msg_0_)
# Is the user privileged (i.e. root)? (  %(!.<yes>.<no>)  )
# yes => red #
# no  => blue33 %
state_color="\033[38;5;33m"
PROMPT=$'%(?.%{$(echo $state_color)%}꩜ .%F{red}✗%?)%f %B%~%b %{\x1b[1;138;5;33m%}$vcs_info_msg_0_%(!.%F{red}#.%{\x1b[1;38;5;33m%}\n>)%{\x1b[0m%} '
