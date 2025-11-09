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
        assert "alias gdxc='git diff-x -c'" in output
        assert "alias cx1='comm-x -1'" in output

        # Check for header comment
        assert "dffs shell integration" in output
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
