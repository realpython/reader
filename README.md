# Real Python Feed Reader

The Real Python Feed Reader is a very simple [web feed](https://en.wikipedia.org/wiki/Web_feed) reader that can download the latest Real Python tutorials from the [Real Python feed](https://realpython.com/contact/#rss-atom-feed).

## Installation

You can install the Real Python Feed Reader from [PyPI](https://pypi.org/project/realpython-reader/):

    pip install realypython-reader

## How to use

The Real Python Feed Reader is a command line application. To see a list of the [latest Real Python tutorials](https://realpython.com/) simply call the program:

    $ realpython
    The latest tutorials from Real Python (https://realpython.com/)
     0 Splitting, Concatenating, and Joining Strings in Python
     1 Image Segmentation Using Color Spaces in OpenCV + Python
     2 Python Community Interview With Mahdi Yusuf
     3 Absolute vs Relative Imports in Python
     4 Top 10 Must-Watch PyCon Talks
     5 Logging in Python
     6 The Best Python Books
     7 Conditional Statements in Python
     8 Structuring Python Programs
     9 We're Celebrating 1 Million Page Views per Month!
    10 Python Pandas: Tricks & Features You May Not Know
    11 Python Community Interview With Mariatta Wijaya
    12 Primer on Python Decorators
    13 Sets in Python
    14 The Ultimate Guide to Django Redirects
    15 Advanced Git Tips for Python Developers
    16 Python Community Interview With Mike Driscoll
    17 Dictionaries in Python
    18 Socket Programming in Python (Guide)
    19 Python Code Quality: Tools & Best Practices

To read one particular tutorial, call the program with the numerical ID of the tutorial as a parameter:

    $ realpython 0
    # Splitting, Concatenating, and Joining Strings in Python

    There are few guarantees in life: death, taxes, and programmers needing to
    deal with strings. Strings can come in many forms. They could be unstructured
    text, usernames, product descriptions, database column names, or really
    anything else that we describe using language.

    With the near-ubiquity of string data, it's important to master the tools of
    the trade when it comes to strings. Luckily, Python makes string manipulation
    very simple, especially when compared to other languages and even older
    versions of Python.

    [... The full text of the article ...]

You can also call the Real Python Feed Reader in your own Python code, by importing from the `reader` package:

    >>> from reader import feed
    >>> feed.get_titles()
    ['Splitting, Concatenating, and Joining Strings in Python', ...]

