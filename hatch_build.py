"""Hatch build hook to embed git SHA at build time."""

from pathlib import Path
from subprocess import run
from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class GitSHABuildHook(BuildHookInterface):
    """Build hook that writes git SHA to _build_info.py."""

    PLUGIN_NAME = "git-sha"

    def initialize(self, version: str, build_data: dict) -> None:
        """Write _build_info.py with current git SHA."""
        # Get git SHA
        sha = None
        try:
            result = run(
                ["git", "rev-parse", "--short", "HEAD"],
                capture_output=True,
                text=True,
                cwd=self.root,
            )
            if result.returncode == 0:
                sha = result.stdout.strip()
        except FileNotFoundError:
            pass

        # Write _build_info.py
        build_info_path = Path(self.root) / "dffs" / "_build_info.py"
        if sha:
            content = f'"""Build information (auto-generated, do not edit)."""\n\nBUILD_SHA = "{sha}"\n'
        else:
            content = '"""Build information (auto-generated, do not edit)."""\n\nBUILD_SHA = None\n'

        build_info_path.write_text(content)

        # Include the generated file in the build
        build_data.setdefault("force_include", {})[str(build_info_path)] = "dffs/_build_info.py"
