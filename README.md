# Real Python Feed Reader

The Real Python Feed Reader is a very simple [web feed](https://en.wikipedia.org/wiki/Web_feed) reader that can download the latest Real Python articles from the [Real Python feed](https://realpython.com/contact/#rss-atom-feed).

## Installation

You can install the Real Python Feed Reader from [PyPI](https://pypi.org/project/realpython-reader/):

    pip install realypython-reader

## How to use

The Real Python Feed Reader is a command line application. To see a list of the [latest Real Python articles](https://realpython.com/) simply call the program:

    $ realpython 
    The latest articles from Real Python (https://realpython.com/)
      0 Logging in Python
      1 The Best Python Books
      2 Conditional Statements in Python
      3 Structuring Python Programs
      4 We're Celebrating 1 Million Page Views per Month!
      5 Python Pandas: Tricks & Features You May Not Know
      6 Python Community Interview With Mariatta Wijaya
      7 Primer on Python Decorators
      8 Sets in Python
      9 The Ultimate Guide to Django Redirects
     10 Advanced Git Tips for Python Developers
     11 Python Community Interview With Mike Driscoll
     12 Dictionaries in Python
     13 Socket Programming in Python (Guide)
     14 Python Code Quality: Tools & Best Practices
     15 Documenting Python Code: A Complete Guide
     16 Fast, Flexible, Easy and Intuitive: How to Speed Up Your Pandas Projects
     17 Lists and Tuples in Python
     18 Reading and Writing CSV Files in Python
     19 Generating Random Data in Python (Guide)

To read one particular article, call the program with the numerical ID of the article as a parameter:

    $ realpython 0
    # Logging in Python

    Logging is a very useful tool in a programmer's toolbox. It can help you
    develop a better understanding of the flow of a program and discover scenarios
    that you might not even have thought of while developing.

    Logs provide developers with an extra set of eyes that are constantly looking
    at the flow that an application is going through. They can store information,
    like which user or IP accessed the application. If an error occurs, then they
    can provide more insights than a stack trace by telling you what the state of
    the program was before it arrived at the line of code where the error
    occurred.

You can also call the Real Python Feed Reader in your own Python code, by importing from the `reader` package:

    >>> from reader import feed
    >>> feed.get_titles()
    ['Logging in Python', 'The Best Python Books', ...]
    
