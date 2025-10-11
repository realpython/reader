"""Functions for displaying the Real Python feed."""

# Standard library imports
from typing import List
import os

HAS_MK = False

try:
    import rich
    from reader.mk import MarkdownReader
    HAS_MK = True
except:
    # from mk import MarkdownReader
    HAS_MK = False

def show(article: str) -> None:
    """Show one article."""
    if HAS_MK:
        MarkdownReader.main(article, theme=os.getenv('REAL_PYTHON_THEME', 'monokai'))
    else:
        print(article)

def show_list(site: str, titles: List[str]) -> None:
    """Show list of articles."""
    print(f"The latest tutorials from {site}")
    for article_id, title in enumerate(titles):
        print(f"{article_id:>3} {title}")
