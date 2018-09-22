"""Tests for the reader.feed module"""
# Standard library imports
import os.path

# Third party imports
import pytest

# Reader imports
from reader import feed

# Current directory
HERE = os.path.dirname(__file__)


@pytest.fixture
def monkeypatch_feed(monkeypatch):
    """Use local file instead of downloading feed from web"""
    local_path = os.path.join(HERE, "realpython_20180919.xml")
    monkeypatch.setattr(feed, "URL", local_path)
    return local_path


@pytest.fixture
def monkeypatch_summary_feed(monkeypatch):
    """Use local file instead of downloading feed from web"""
    local_path = os.path.join(HERE, "realpython_descriptions_20180919.xml")
    monkeypatch.setattr(feed, "URL", local_path)
    return local_path


#
# Tests
#
def test_site(monkeypatch_feed):
    """Test that we can read the site title and link"""
    expected = "Real Python (https://realpython.com/)"
    assert feed.get_site() == expected


def test_article_title(monkeypatch_feed):
    """Test that title is added at top of article"""
    article_id = 0
    title = feed.get_titles()[article_id]
    article = feed.get_article(article_id)

    assert article.strip("# ").startswith(title)


def test_article(monkeypatch_feed):
    """Test that article is returned"""
    article_id = 2
    article_phrases = [
        "logging.info('This is an info message')",
        "By using the `level` parameter",
        "  * `level`: The root logger",
    ]
    article = feed.get_article(article_id)

    for phrase in article_phrases:
        assert phrase in article


def test_titles(monkeypatch_feed):
    """Test that titles are found"""
    titles = feed.get_titles()

    assert len(titles) == 20
    assert titles[0] == "Absolute vs Relative Imports in Python"
    assert titles[9] == "Primer on Python Decorators"


def test_summary(monkeypatch_summary_feed):
    """Test that summary feeds can be read"""
    article_id = 1
    summary_phrases = [
        "Get the inside scoop",
        "this list of\ninformative videos",
    ]
    summary = feed.get_article(article_id)

    for phrase in summary_phrases:
        assert phrase in summary


def test_invalid_article_id(monkeypatch_feed):
    """Test that invalid article ids are handled gracefully"""
    article_id = "wrong"
    with pytest.raises(SystemExit):
        feed.get_article(article_id)
