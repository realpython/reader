"""Interact with the Real Python feed"""
# Standard library imports
from typing import Dict, List

# Third party imports
import feedparser
import html2text

# Reader imports
from reader import URL
_CACHED_FEEDS: Dict[str, feedparser.FeedParserDict] = dict()


def _feed() -> feedparser.FeedParserDict:
    """Cache contents of the feed, so it's only read once"""
    if URL not in _CACHED_FEEDS:
        _CACHED_FEEDS[URL] = feedparser.parse(URL)
    return _CACHED_FEEDS[URL]


def get_site() -> str:
    """Get name and link to web site of the feed"""
    info = _feed().feed
    return f"{info.title} ({info.link})"


def get_article(article_id: str, links: bool = False) -> str:
    """Get article from feed with the given ID"""
    articles = _feed().entries
    try:
        article = articles[int(article_id)]
    except (IndexError, ValueError):
        max_id = len(articles) - 1
        msg = f"Unknown article ID, use ID from 0 to {max_id}"
        raise SystemExit(f"Error: {msg}")

    # Get article as HTML
    try:
        html = article.content[0].value
    except AttributeError:
        html = article.summary

    # Convert HTML to plain text
    to_text = html2text.HTML2Text()
    to_text.ignore_links = not links
    text = to_text.handle(html)

    return f"# {article.title}\n\n{text}"


def get_titles() -> List[str]:
    """List titles in feed"""
    articles = _feed().entries
    return [a.title for a in articles]
