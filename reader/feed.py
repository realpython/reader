"""Interact with the Real Python feed"""
# Standard library imports
from typing import Dict, List  # noqa

# Third party imports
import feedparser
import html2text

# Reader imports
from reader import URL

_CACHED_FEEDS = dict()  # type: Dict[str, feedparser.FeedParserDict]


def _feed(url=URL):  # type: (str) -> feedparser.FeedParserDict
    """Cache contents of the feed, so it's only read once"""
    if url not in _CACHED_FEEDS:
        _CACHED_FEEDS[url] = feedparser.parse(url)
    return _CACHED_FEEDS[url]


def get_site(url=URL):  # type: (str) -> str
    """Get name and link to web site of the feed"""
    info = _feed(url).feed
    return u"{info.title} ({info.link})".format(info=info)


def get_article(article_id, links=False, url=URL):
    # type: (str, bool, str) -> str
    """Get article from feed with the given ID"""
    articles = _feed(url).entries
    try:
        article = articles[int(article_id)]
    except (IndexError, ValueError):
        max_id = len(articles) - 1
        msg = "Unknown article ID, use ID from 0 to {}".format(max_id)
        raise SystemExit("Error: {}".format(msg))

    # Get article as HTML
    try:
        html = article.content[0].value
    except AttributeError:
        html = article.summary

    # Convert HTML to plain text
    to_text = html2text.HTML2Text()
    to_text.ignore_links = not links
    text = to_text.handle(html)

    return u"# {}\n\n{}".format(article.title, text)


def get_titles(url=URL):  # type: (str) -> List[str]
    """List titles in feed"""
    articles = _feed(url).entries
    return [a.title for a in articles]
