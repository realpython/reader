"""Read the latest Real Python tutorials.

Usage:
------

    $ realpython [options] [id] [id ...]

List the latest tutorials:

    $ realpython

Read one tutorial:

    $ realpython <id>

    where <id> is the number shown when listing tutorials.

Read the latest tutorial:

    $ realpython 0


Available options are:

    -h, --help         Show this help
    -l, --show-links   Show links in text


Contact:
--------

- https://realpython.com/contact/

More information is available at:

- https://pypi.org/project/realpython-reader/
- https://github.com/realpython/reader


Version:
--------

- realpython-reader v1.1.1
"""
# Standard library imports
import sys

# Reader imports
import reader
from reader import feed, viewer


def main() -> None:
    """Read the Real Python article feed."""
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    opts = [o for o in sys.argv[1:] if o.startswith("-")]

    # Show help message
    if "-h" in opts or "--help" in opts:
        viewer.show(__doc__)
        raise SystemExit()

    # Should links be shown in the text
    show_links = "-l" in opts or "--show-links" in opts

    # Get URL from config file
    url = reader.URL

    # An article ID is given, show article
    if args:
        for article_id in args:
            article = feed.get_article(article_id, links=show_links, url=url)
            viewer.show(article)

    # No ID is given, show list of articles
    else:
        site = feed.get_site(url=url)
        titles = feed.get_titles(url=url)
        viewer.show_list(site, titles)


if __name__ == "__main__":
    main()
