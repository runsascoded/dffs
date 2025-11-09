"""Tests for shell-integration command."""

from dffs.commands.shell_integration import shell_integration
from io import StringIO
import sys


def test_shell_integration_bash():
    """Test that shell-integration outputs bash aliases."""
    # Capture stdout
    old_stdout = sys.stdout
    sys.stdout = buffer = StringIO()

    try:
        shell_integration('bash')
        output = buffer.getvalue()

        # Check for key aliases
        assert "alias dx='diff-x'" in output
        assert "alias cx='comm-x'" in output
        assert "alias gdx='git diff-x'" in output
        assert "alias gdxs='git diff-x --cached'" in output
        assert "alias cx1='comm-x -1'" in output

        # Check for header comment
        assert "dffs shell integration" in output
    finally:
        sys.stdout = old_stdout


def test_shell_integration_filter_diff_x():
    """Test filtering to only diff-x aliases."""
    old_stdout = sys.stdout
    sys.stdout = buffer = StringIO()

    try:
        shell_integration('bash', 'diff-x')
        output = buffer.getvalue()

        # Should have diff-x aliases
        assert "alias dx='diff-x'" in output
        assert "alias dxw='diff-x -w'" in output

        # Should NOT have comm-x or git-diff-x aliases
        assert "alias cx='comm-x'" not in output
        assert "alias gdx='git diff-x'" not in output
    finally:
        sys.stdout = old_stdout


def test_shell_integration_filter_comm_x():
    """Test filtering to only comm-x aliases."""
    old_stdout = sys.stdout
    sys.stdout = buffer = StringIO()

    try:
        shell_integration('bash', 'comm-x')
        output = buffer.getvalue()

        # Should have comm-x aliases
        assert "alias cx='comm-x'" in output
        assert "alias cx1='comm-x -1'" in output

        # Should NOT have diff-x or git-diff-x aliases
        assert "alias dx='diff-x'" not in output
        assert "alias gdx='git diff-x'" not in output
    finally:
        sys.stdout = old_stdout


def test_shell_integration_filter_git_diff_x():
    """Test filtering to only git-diff-x aliases."""
    old_stdout = sys.stdout
    sys.stdout = buffer = StringIO()

    try:
        shell_integration('bash', 'git-diff-x')
        output = buffer.getvalue()

        # Should have git-diff-x aliases
        assert "alias gdx='git diff-x'" in output
        assert "alias gdxs='git diff-x --cached'" in output

        # Should NOT have diff-x or comm-x aliases
        assert "alias dx='diff-x'" not in output
        assert "alias cx='comm-x'" not in output
    finally:
        sys.stdout = old_stdout


def test_shell_integration_auto_detect():
    """Test that shell-integration auto-detects shell from environment."""
    import os
    old_shell = os.environ.get('SHELL')
    os.environ['SHELL'] = '/bin/bash'

    old_stdout = sys.stdout
    sys.stdout = buffer = StringIO()

    try:
        shell_integration(None)
        output = buffer.getvalue()

        # Should output bash aliases
        assert "alias dx='diff-x'" in output
    finally:
        sys.stdout = old_stdout
        if old_shell:
            os.environ['SHELL'] = old_shell
        else:
            os.environ.pop('SHELL', None)
