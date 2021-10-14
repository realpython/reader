"""Tests for the reader.viewer module."""

# Reader imports
from reader import viewer


#
# Tests
#
def test_show(capsys):
    """Test that show adds information to stdout."""
    text = "Lorem ipsum dolor sit amet"
    viewer.show(text)
    stdout, stderr = capsys.readouterr()
    assert stderr == ""

    # It's ok if the viewer adds some information
    assert text in stdout


def test_show_list(capsys):
    """Test that show_list shows a list of items with an ID."""
    site = "Real Python"
    things = ["pathlib", "data classes", "python 3.7", "decorators"]
    viewer.show_list(site, things)
    stdout, stderr = capsys.readouterr()
    assert stderr == ""

    # Site name is shown in header
    lines = stdout.split("\n")
    assert site in lines[0]

    # Each thing is listed preceded by a number
    for thing, line in zip(things, lines[1:]):
        line_parts = line.split()
        assert line_parts[0].isnumeric()
        assert thing in line
