"""Functions for displaying the Real Python feed."""

# Standard library imports
from typing import List


def show(article: str) -> None:
    """Show one article."""
    print(article)


def show_list(site: str, titles: List[str]) -> None:
    """Show list of articles."""
    print(f"The latest tutorials from {site}")
    for article_id, title in enumerate(titles):
        print(f"{article_id:>3} {title}")
