"""Real Python feed reader

Import the `feed` module to work with the Real Python feed:

    >>> from reader import feed
    >>> feed.get_titles()
    ['Logging in Python', 'The Best Python Books', ...]

See https://github.com/realpython/reader/ for more information
"""
# Version of realpython-reader package
__version__ = "0.1.1"

# URL of Real Python feed
URL = "https://realpython.com/atom.xml"
