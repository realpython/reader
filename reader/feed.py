from typing import List
import feedparser
import html2text
import reader

_CACHED_FEED = feedparser.FeedParserDict()


def _feed() -> feedparser.FeedParserDict:
    """Cache contents of the feed, so it's only read once"""
    if not _CACHED_FEED:
        _CACHED_FEED.update(feedparser.parse(reader.URL))
    return _CACHED_FEED


def get_site() -> str:
    """Get name and link to web site of the feed"""
    info = _feed().feed
    return f"{info.title} ({info.link})"


def get_article(article_id: str) -> str:
    """Get article from feed with the given ID"""
    articles = _feed().entries
    try:
        article = articles[int(article_id)]
    except (IndexError, ValueError):
        raise SystemExit("Error: Unknown article ID")

    html = article.content[0].value
    text = html2text.html2text(html)
    return f"# {article.title}\n\n{text}"


def get_titles() -> List[str]:
    """List titles in feed"""
    articles = _feed().entries
    return [a.title for a in articles]
