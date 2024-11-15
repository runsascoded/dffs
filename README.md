# qmdx
**Q**om**m**an**ds**: execute shell pipelines against multiple inputs, diff/compare/join results

<!-- toc -->
- [Install](#install)
- [CLIs](#CLIs)
    - [`diff-x`](#diff-x)
        - [Usage](#diff-x-usage)
        - [Examples](#diff-x-examples)
    - [`comm-x`](#comm-x)
        - [Usage](#comm-x-usage)
        - [Examples](#comm-x-examples)
    - [`git-diff-x`](#git-diff-x)
        - [Usage](#git-diff-x-usage)
        - [Examples](#git-diff-x-examples)
<!-- /toc -->

## Install <a id="install"></a>

```bash
pip install qmdx
```

## CLIs <a id="CLIs"></a>

### `diff-x` <a id="diff-x"></a>

#### Usage <a id="diff-x-usage"></a>
<!-- `bmdf diff-x` -->
```bash
diff-x
# Usage: diff-x [OPTIONS] [exec_cmd...] <path1> <path2>
#
#   Diff two files after running them through a pipeline of other commands.
#
# Options:
#   -c, --color                  Colorize the output
#   -s, --shell-executable TEXT  Shell to use for executing commands; defaults
#                                to $SHELL (/bin/bash)
#   -S, --no-shell               Don't pass `shell=True` to Python
#                                `subprocess`es
#   -U, --unified INTEGER        Number of lines of context to show (passes
#                                through to `diff`)
#   -v, --verbose                Log intermediate commands to stderr
#   -w, --ignore-whitespace      Ignore whitespace differences (pass `-w` to
#                                `diff`)
#   -x, --exec-cmd TEXT          Command(s) to execute before invoking `comm`;
#                                alternate syntax to passing commands as
#                                positional arguments
#   --help                       Show this message and exit.
```

#### Examples <a id="diff-x-examples"></a>

Given two similar JSON objects, where one is compact and the other is pretty-printed:
```bash
echo '{"a":1,"b":2}' > 1.json
echo '{"a":1,"b":3}' | jq > 2.json 
```

`diff {1,2}.json` outputs the entirety of both objects:
```diff
1c1,4
< {"a":1,"b":2}
---
> {
>   "a": 1,
>   "b": 3
> }
```

`diff-x 'jq .' {1,2}.json` pretty-prints each side before `diff`ing:
```diff
3c3
<   "b": 2
---
>   "b": 3
```

### `comm-x` <a id="comm-x"></a>

#### Usage <a id="comm-x-usage"></a>
<!-- `bmdf comm-x` -->
```bash
comm-x
# Usage: comm-x [OPTIONS] [exec_cmd...] <path1> <path2>
#
#   Compare (`comm`) two files after running them through a pipeline of other
#   commands.
#
# Options:
#   -1, --exclude-1              Exclude lines only found in the first pipeline
#   -2, --exclude-2              Exclude lines only found in the second pipeline
#   -3, --exclude-3              Exclude lines found in both pipelines
#   -i, --case-insensitive       Case insensitive comparison
#   -s, --shell-executable TEXT  Shell to use for executing commands; defaults
#                                to $SHELL (/bin/bash)
#   -S, --no-shell               Don't pass `shell=True` to Python
#                                `subprocess`es
#   -v, --verbose                Log intermediate commands to stderr
#   -x, --exec-cmd TEXT          Command(s) to execute before invoking `comm`;
#                                alternate syntax to passing commands as
#                                positional arguments
#   --help                       Show this message and exit.
```

#### Examples <a id="comm-x-examples"></a>
Given two similar lists of numbers, but in different orders:
```bash
seq 10 > 1.txt
seq 10 -2 0 > 2.txt
```

`comm` outputs gibberish, because the files aren't in sorted order:
<!-- `bmdf comm 1.txt 2.txt` -->
```bash
comm 1.txt 2.txt
# 1
# 	10
# 2
# 3
# 4
# 5
# 6
# 7
# 		8
# comm: file 2 is not in sorted order
# 	6
# 	4
# 	2
# 	0
# 9
# comm: file 1 is not in sorted order
# 10
# comm: input is not in sorted order
```

`comm-x sort` sorts each file first:
<!-- `bmdf comm-x sort 1.txt 2.txt` -->
```bash
comm-x sort 1.txt 2.txt
# 	0
# 1
# 		10
# 		2
# 3
# 		4
# 5
# 		6
# 7
# 		8
# 9
```

### `git-diff-x` <a id="git-diff-x"></a>

#### Usage <a id="git-diff-x-usage"></a>
<!-- `bmdf -- git-diff-x --help` -->
```bash
git-diff-x --help
# Usage: git-diff-x [OPTIONS] [exec_cmd...] <path>
#
#   Diff a file at two commits (or one commit vs. current worktree), optionally
#   passing both through `cmd` first
#
#   Examples:
#
#   dvc-utils diff -r HEAD^..HEAD wc -l foo.dvc  # Compare the number of lines
#   (`wc -l`) in `foo` (the file referenced by `foo.dvc`) at the previous vs.
#   current commit (`HEAD^..HEAD`).
#
#   dvc-utils diff md5sum foo  # Diff the `md5sum` of `foo` (".dvc" extension is
#   optional) at HEAD (last committed value) vs. the current worktree content.
#
# Options:
#   -c, --color                  Colorize the output
#   -r, --refspec TEXT           <commit 1>..<commit 2> (compare two commits) or
#                                <commit> (compare <commit> to the worktree)
#   -s, --shell-executable TEXT  Shell to use for executing commands; defaults
#                                to $SHELL (/bin/bash)
#   -S, --no-shell               Don't pass `shell=True` to Python
#                                `subprocess`es
#   -U, --unified INTEGER        Number of lines of context to show (passes
#                                through to `diff`)
#   -v, --verbose                Log intermediate commands to stderr
#   -w, --ignore-whitespace      Ignore whitespace differences (pass `-w` to
#                                `diff`)
#   -x, --exec-cmd TEXT          Command(s) to execute before invoking `comm`;
#                                alternate syntax to passing commands as
#                                positional arguments
#   --help                       Show this message and exit.
```

#### Examples <a id="git-diff-x-examples"></a>
Compare line-count (`wc -l`) of this README, before and after commit `8b7a761`:
<!-- `bmdf -- git-diff-x -r 8b7a761^..8b7a761 'wc -l' README.md` -->
```bash
git-diff-x -r '8b7a761^..8b7a761' 'wc -l' README.md
# 1c1
# < 16
# ---
# > 206
```


[`jq`]: https://stedolan.github.io/jq/
