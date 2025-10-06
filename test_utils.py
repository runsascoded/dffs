#!/usr/bin/env python
"""Tests for dffs.utils module."""
from dffs.utils import join_pipelines


def test_join_pipelines_success():
    """Test join_pipelines returns 0 when all commands succeed."""
    returncode = join_pipelines(
        base_cmd=['diff'],
        cmds1=['echo foo'],
        cmds2=['echo foo'],
        shell=True,
    )
    assert returncode == 0, f"Expected 0, got {returncode}"
    print("✓ test_join_pipelines_success")


def test_join_pipelines_diff_found():
    """Test join_pipelines returns 1 when diff finds differences (expected behavior)."""
    returncode = join_pipelines(
        base_cmd=['diff'],
        cmds1=['echo foo'],
        cmds2=['echo bar'],
        shell=True,
    )
    assert returncode == 1, f"Expected 1, got {returncode}"
    print("✓ test_join_pipelines_diff_found")


def test_join_pipelines_cmd1_fails():
    """Test join_pipelines returns non-zero when first pipeline command fails."""
    returncode = join_pipelines(
        base_cmd=['diff'],
        cmds1=['false'],
        cmds2=['echo bar'],
        shell=True,
    )
    assert returncode != 0, f"Expected non-zero, got {returncode}"
    print("✓ test_join_pipelines_cmd1_fails")


def test_join_pipelines_cmd2_fails():
    """Test join_pipelines returns non-zero when second pipeline command fails."""
    returncode = join_pipelines(
        base_cmd=['diff'],
        cmds1=['echo foo'],
        cmds2=['false'],
        shell=True,
    )
    assert returncode != 0, f"Expected non-zero, got {returncode}"
    print("✓ test_join_pipelines_cmd2_fails")


def test_join_pipelines_both_cmds_fail():
    """Test join_pipelines returns non-zero when both pipeline commands fail."""
    returncode = join_pipelines(
        base_cmd=['diff'],
        cmds1=['false'],
        cmds2=['false'],
        shell=True,
    )
    assert returncode != 0, f"Expected non-zero, got {returncode}"
    print("✓ test_join_pipelines_both_cmds_fail")


def test_join_pipelines_base_cmd_fails():
    """Test join_pipelines returns non-zero when base command fails."""
    returncode = join_pipelines(
        base_cmd=['false'],
        cmds1=['echo foo'],
        cmds2=['echo bar'],
        shell=True,
    )
    assert returncode != 0, f"Expected non-zero, got {returncode}"
    print("✓ test_join_pipelines_base_cmd_fails")


def test_join_pipelines_pipeline_error():
    """Test join_pipelines propagates errors from pipeline commands."""
    returncode = join_pipelines(
        base_cmd=['diff'],
        cmds1=['cat /nonexistent/file'],
        cmds2=['echo bar'],
        shell=True,
    )
    assert returncode != 0, f"Expected non-zero, got {returncode}"
    print("✓ test_join_pipelines_pipeline_error")


def test_join_pipelines_multi_stage_pipeline():
    """Test join_pipelines with multi-stage pipelines."""
    returncode = join_pipelines(
        base_cmd=['diff'],
        cmds1=['echo "foo\nbar"', 'sort'],
        cmds2=['echo "bar\nfoo"', 'sort'],
        shell=True,
    )
    assert returncode == 0, f"Expected 0, got {returncode}"
    print("✓ test_join_pipelines_multi_stage_pipeline")


def test_join_pipelines_multi_stage_pipeline_with_error():
    """Test join_pipelines with multi-stage pipeline that fails."""
    returncode = join_pipelines(
        base_cmd=['diff'],
        cmds1=['echo "foo\nbar"', 'sort', 'false'],
        cmds2=['echo "bar\nfoo"', 'sort'],
        shell=True,
    )
    assert returncode != 0, f"Expected non-zero, got {returncode}"
    print("✓ test_join_pipelines_multi_stage_pipeline_with_error")


if __name__ == '__main__':
    import sys
    import time

    tests = [
        test_join_pipelines_success,
        test_join_pipelines_diff_found,
        test_join_pipelines_cmd1_fails,
        test_join_pipelines_cmd2_fails,
        test_join_pipelines_both_cmds_fail,
        test_join_pipelines_base_cmd_fails,
        test_join_pipelines_pipeline_error,
        test_join_pipelines_multi_stage_pipeline,
        test_join_pipelines_multi_stage_pipeline_with_error,
    ]

    for test in tests:
        try:
            test()
            time.sleep(0.1)  # Small delay between tests
        except AssertionError as e:
            print(f"✗ {test.__name__}: {e}", file=sys.stderr)
            sys.exit(1)

    print("\nAll tests passed!")
