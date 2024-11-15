from __future__ import annotations

from typing import Tuple

from click import option, command
from utz import process

from qmdx.cli import args, shell_exec_opt, no_shell_opt, verbose_opt, exec_cmd_opt
from qmdx.utils import join_pipelines


@command('comm-x', short_help='comm two files after running them through a pipeline of other commands', no_args_is_help=True)
@option('-1', '--exclude-1', is_flag=True, help='Exclude lines only found in the first pipeline')
@option('-2', '--exclude-2', is_flag=True, help='Exclude lines only found in the second pipeline')
@option('-3', '--exclude-3', is_flag=True, help='Exclude lines found in both pipelines')
@option('-i', '--case-insensitive', is_flag=True, help='Case insensitive comparison')
@shell_exec_opt
@no_shell_opt
@verbose_opt
@exec_cmd_opt
@args
def main(
    exclude_1: bool,
    exclude_2: bool,
    exclude_3: bool,
    case_insensitive: bool,
    shell_executable: str | None,
    no_shell: bool,
    verbose: bool,
    exec_cmds: Tuple[str, ...],
    args: Tuple[str, ...],
):
    """Compare (`comm`) two files after running them through a pipeline of other commands."""
    if len(args) < 2:
        raise ValueError('Must provide at least two files to comm')

    *cmds, path1, path2 = args
    cmds = list(exec_cmds) + cmds
    if cmds:
        first, *rest = cmds
        join_pipelines(
            base_cmd=[
                'comm',
                *(['-1'] if exclude_1 else []),
                *(['-2'] if exclude_2 else []),
                *(['-3'] if exclude_3 else []),
                *(['-i'] if case_insensitive else []),
            ],
            cmds1=[ f'{first} {path1}', *rest ],
            cmds2=[ f'{first} {path2}', *rest ],
            verbose=verbose,
            shell=not no_shell,
            shell_executable=shell_executable,
        )
    else:
        process.run(['comm', path1, path2])
