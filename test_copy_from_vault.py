#!/usr/bin/env python3
"""
Unit tests for copy_from_vault.py functions.
"""
import os
import tempfile
import shutil
from pathlib import Path
import sys

# Import functions from copy_from_vault
from copy_from_vault import (
    convert_to_frontmatter,
    convert_internal_links,
    copy_file,
)


def test_convert_internal_links():
    """Test that Obsidian-style links are converted to markdown links."""
    print("Testing convert_internal_links...")

    # Create a temporary file with Obsidian-style links
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
        f.write("This is a link to [[Another Document]].\n")
        f.write("This is a custom link [[Document Name|custom text]].\n")
        temp_file = f.name

    try:
        convert_internal_links(temp_file)

        with open(temp_file, 'r') as f:
            content = f.read()

        # Check that standard link was converted
        assert "[Another Document](/another-document)" in content, \
            "Standard Obsidian link not converted correctly"

        # Check that custom link was converted
        assert "[custom text](/document-name)" in content, \
            "Custom Obsidian link not converted correctly"

        print("✓ convert_internal_links test passed")
        return True

    except AssertionError as e:
        print(f"✗ convert_internal_links test failed: {e}")
        return False

    finally:
        os.unlink(temp_file)


def test_convert_to_frontmatter():
    """Test that Obsidian metadata is converted to Hugo frontmatter."""
    print("\nTesting convert_to_frontmatter...")

    # Create a temporary file with Obsidian-style metadata
    content = """# Test Title

This is the content.

---
Created: [[2024-01-15]]
"""

    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
        f.write(content)
        temp_file = f.name

    try:
        convert_to_frontmatter(temp_file)

        with open(temp_file, 'r') as f:
            result = f.read()

        # Check that frontmatter was created
        assert result.startswith("---"), "Frontmatter not created"
        assert "title: Test Title" in result, "Title not in frontmatter"
        assert "date:" in result, "Date not in frontmatter"

        print("✓ convert_to_frontmatter test passed")
        return True

    except AssertionError as e:
        print(f"✗ convert_to_frontmatter test failed: {e}")
        return False

    finally:
        os.unlink(temp_file)


def test_copy_file_with_publish_tag():
    """Test that files with #blog/publish tag are copied."""
    print("\nTesting copy_file with publish tag...")

    # Create a temporary file with publish tag
    with tempfile.TemporaryDirectory() as temp_dir:
        source_file = os.path.join(temp_dir, "test.md")
        with open(source_file, 'w') as f:
            f.write("# Test\n\nContent #blog/publish")

        dest_dir = os.path.join(temp_dir, "dest")
        os.makedirs(dest_dir)

        copied, copied_path = copy_file(source_file, dest_dir)

        if not copied:
            print("✗ File with publish tag was not copied")
            return False

        if not os.path.exists(copied_path):
            print("✗ Copied file does not exist")
            return False

        print("✓ copy_file with publish tag test passed")
        return True


def test_copy_file_without_publish_tag():
    """Test that files without #blog/publish tag are not copied."""
    print("\nTesting copy_file without publish tag...")

    with tempfile.TemporaryDirectory() as temp_dir:
        source_file = os.path.join(temp_dir, "test.md")
        with open(source_file, 'w') as f:
            f.write("# Test\n\nContent without publish tag")

        dest_dir = os.path.join(temp_dir, "dest")
        os.makedirs(dest_dir)

        copied, copied_path = copy_file(source_file, dest_dir)

        if copied:
            print("✗ File without publish tag was copied (should not be)")
            return False

        print("✓ copy_file without publish tag test passed")
        return True


def run_all_tests():
    """Run all unit tests."""
    print("=" * 60)
    print("Running copy_from_vault.py Unit Tests")
    print("=" * 60)

    tests = [
        test_convert_internal_links,
        test_convert_to_frontmatter,
        test_copy_file_with_publish_tag,
        test_copy_file_without_publish_tag,
    ]

    results = []
    for test in tests:
        try:
            results.append(test())
        except Exception as e:
            print(f"✗ Test {test.__name__} raised exception: {e}")
            import traceback
            traceback.print_exc()
            results.append(False)

    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    passed = sum(results)
    total = len(results)
    print(f"Passed: {passed}/{total}")

    if passed == total:
        print("\n✓ All tests passed!")
        return 0
    else:
        print(f"\n✗ {total - passed} test(s) failed")
        return 1


if __name__ == "__main__":
    sys.exit(run_all_tests())
