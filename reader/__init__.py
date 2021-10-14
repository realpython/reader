"""Real Python feed reader.

Import the `feed` module to work with the Real Python feed:

    >>> from reader import feed
    >>> feed.get_titles()
    ['Logging in Python', 'The Best Python Books', ...]

See https://github.com/realpython/reader/ for more information.
"""
from configparser import ConfigParser
from importlib import resources

# Version of realpython-reader package
__version__ = "1.0.0"

# Read URL of feed from config file
cfg = ConfigParser()
with resources.path("reader", "config.cfg") as path:
    cfg.read(str(path))

URL = cfg.get("feed", "url")
