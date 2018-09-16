import sys

from reader import feed
from reader import viewer


def main() -> None:
    """Read the Real Python article feed"""
    # An article ID is given, show article
    if len(sys.argv) > 1:
        article = feed.get_article(sys.argv[1])
        viewer.show(article)

    # No ID is given, show list of articles
    else:
        site = feed.get_site()
        titles = feed.get_titles()
        viewer.show_list(site, titles)


if __name__ == "__main__":
    main()
