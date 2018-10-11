"""Functions for displaying the Real Python feed"""

# Support Python 2
from __future__ import print_function

# Standard library imports
from typing import List  # noqa


def show(article):  # type: (str) -> None
    """Show one article"""
    print(article)


def show_list(site, titles):  # type: (str, List[str]) -> None
    """Show list of articles"""
    print(u"The latest tutorials from {}".format(site))
    for article_id, title in enumerate(titles):
        print(u"{:>3} {}".format(article_id, title))
