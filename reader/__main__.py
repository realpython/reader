"""Read the latest Real Python tutorials

Usage:
------

List the latest tutorials:

    $ realpython

Read one tutorial:

    $ realpython <id>

    where <id> is the number shown when listing tutorials.

Read the latest tutorial:

    $ realpython 0


Contact:
--------

- https://realpython.com/contact/

More information is available at:

- https://pypi.org/project/realpython-reader/
- https://github.com/realpython/reader
"""
# Standard library imports
import sys

# Reader imports
from reader import feed
from reader import viewer


def main() -> None:
    """Read the Real Python article feed"""
    # Show help message
    if "-h" in sys.argv or "--help" in sys.argv:
        viewer.show(__doc__)
        return

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
