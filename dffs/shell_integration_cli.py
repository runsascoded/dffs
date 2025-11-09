"""CLI entry point for shell-integration command."""

from dffs.commands.shell_integration import shell_integration

def main():
    """Main entry point for shell-integration command."""
    import sys
    # Get shell argument if provided
    shell = sys.argv[1] if len(sys.argv) > 1 else None
    shell_integration(shell)

if __name__ == '__main__':
    main()
