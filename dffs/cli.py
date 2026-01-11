import click
from click import option, argument

from dffs._version import __version__


def print_version(ctx, param, value):
    """Print version and exit."""
    if not value or ctx.resilient_parsing:
        return
    click.echo(__version__)
    ctx.exit()


version_opt = option('-V', '--version', is_flag=True, callback=print_version, expose_value=False, is_eager=True, help='Show version and exit')
pipefail_opt = option('-P', '--pipefail', is_flag=True, help="Check all pipeline commands for errors (like bash's `set -o pipefail`); default only checks last command")
shell_exec_opt = option('-s', '--shell-executable', help='Shell to use for executing commands; defaults to $SHELL')
no_shell_opt = option('-S', '--no-shell', is_flag=True, help="Don't pass `shell=True` to Python `subprocess`es")
verbose_opt = option('-v', '--verbose', is_flag=True, help="Log intermediate commands to stderr")
exec_cmd_opt = option('-x', '--exec-cmd', 'exec_cmds', multiple=True, help='Command(s) to execute before invoking `comm`; alternate syntax to passing commands as positional arguments')
args = argument('args', metavar='[exec_cmd...] <path1> <path2>', nargs=-1)
