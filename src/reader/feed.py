"""Interact with the Real Python feed."""
# Standard library imports
from typing import Dict, List  # noqa

# Third party imports
import feedparser
import html2text

# Reader imports
from reader import URL

_CACHED_FEEDS: Dict[str, feedparser.FeedParserDict] = {}


def _feed(url: str = URL) -> feedparser.FeedParserDict:
    """Cache contents of the feed, so it's only read once."""
    if url not in _CACHED_FEEDS:
        _CACHED_FEEDS[url] = feedparser.parse(url)
    return _CACHED_FEEDS[url]


def get_site(url: str = URL) -> str:
    """Get name and link to website of the feed."""
    info = _feed(url).feed
    return f"{info.title} ({info.link})"


def get_article(article_id: str, links: bool = False, url: str = URL) -> str:
    """Get article from feed with the given ID."""
    articles = _feed(url).entries
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


def get_titles(url: str = URL) -> List[str]:
    """List titles in feed."""
    articles = _feed(url).entries
    return [a.title for a in articles]
