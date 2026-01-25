#!/usr/bin/env python3
"""
Test script to validate the Hugo site build and content processing.
"""
import os
import sys
import subprocess
from pathlib import Path
import glob


def test_hugo_build():
    """Test that Hugo can build the site successfully."""
    print("Testing Hugo build...")
    try:
        result = subprocess.run(
            ["hugo", "build", "--minify"],
            capture_output=True,
            text=True,
            check=True
        )
        print("✓ Hugo build successful")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Hugo build failed: {e.stderr}")
        return False
    except FileNotFoundError:
        print("✗ Hugo not found. Install with: brew install hugo")
        return False


def test_content_files_exist():
    """Test that content files exist and are valid markdown."""
    print("\nTesting content files...")
    content_dir = Path("content")

    if not content_dir.exists():
        print("✗ Content directory does not exist")
        return False

    md_files = list(content_dir.glob("*.md"))
    if len(md_files) == 0:
        print("✗ No markdown files found in content directory")
        return False

    print(f"✓ Found {len(md_files)} markdown files")

    # Check each file is readable and has basic content
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                if len(content) < 10:
                    print(f"✗ {md_file.name} appears to be empty or too short")
                    return False
        except Exception as e:
            print(f"✗ Error reading {md_file.name}: {e}")
            return False

    print(f"✓ All {len(md_files)} markdown files are readable")
    return True


def test_required_files():
    """Test that required configuration files exist."""
    print("\nTesting required files...")
    required_files = ["hugo.toml", "Makefile"]

    for file_path in required_files:
        if not Path(file_path).exists():
            print(f"✗ Required file missing: {file_path}")
            return False

    print(f"✓ All required files present")
    return True


def test_docs_directory():
    """Test that docs directory exists and has content."""
    print("\nTesting docs directory...")
    docs_dir = Path("docs")

    if not docs_dir.exists():
        print("✗ Docs directory does not exist")
        return False

    # Check for CNAME file
    cname = docs_dir / "CNAME"
    if not cname.exists():
        print("✗ CNAME file missing in docs directory")
        return False

    print("✓ Docs directory structure is valid")
    return True


def run_all_tests():
    """Run all tests and report results."""
    print("=" * 60)
    print("Running Hugo Site Tests")
    print("=" * 60)

    tests = [
        test_required_files,
        test_content_files_exist,
        test_docs_directory,
        test_hugo_build,
    ]

    results = []
    for test in tests:
        try:
            results.append(test())
        except Exception as e:
            print(f"✗ Test {test.__name__} raised exception: {e}")
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
