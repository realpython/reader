#!/usr/bin/env python

HAS_CLIPBOARD = False
try:
    from rich.console import Console, JustifyMethod 
    from rich.markdown import Markdown
    from rich.theme import Theme
except:
    print("please install 'rich' first !")
    sys.exit(1)

import sys
import os
try:
    import clipboard
    HAS_CLIPBOARD = True
except:
    HAS_CLIPBOARD = False

from typing import Optional
# from pygments.lexers import get_all_lexers

class MarkdownReader:
    custom_theme = Theme({
        # Headers
        "markdown.h1": "bold magenta",
        "markdown.h2": "bold green",
        "markdown.h3": "bold cyan",
        "markdown.h4": "bold yellow",
        "markdown.h5": "bold bright_black",
        "markdown.h6": "bold bright_black",
        
        # Text styles
        "markdown.paragraph": "white",
        "markdown.emphasis": "italic",
        "markdown.strong": "bold",
        "markdown.strikethrough": "strike dim",
        
        # Inline code and code blocks
        "markdown.code": "bold yellow",
        "markdown.code_block": "bold bright_yellow",
        
        # Block quote
        "markdown.block_quote": "italic cyan",
        
        # Lists
        "markdown.list_item": "dim white",
        "markdown.list_marker": "bright_magenta",
        
        # Links
        "markdown.link": "underline blue",
        "markdown.link_url": "bold blue",
        
        # Horizontal rule
        "markdown.hr": "dim",
        
        # Table styles (if used)
        "markdown.table.header": "bold magenta",
        "markdown.table.cell": "white",
        
        # Line breaks
        "markdown.line_break": "dim",
    })

    console = Console(theme=custom_theme)

    @classmethod
    def main(cls, readme_file:str = None, theme:str = 'fruity', lexer:str = None, justify:Optional[JustifyMethod] = None):
        md_text = None
        if readme_file == 'c' and HAS_CLIPBOARD:
            md_text = clipboard.paste()
        elif readme_file and os.path.isfile(readme_file):
            with open(readme_file, "r", encoding="utf-8") as f:
                md_text = f.read()
        elif readme_file:
            md_text = readme_file
        if not md_text:
            for i in ['README.md', 'readme.md', 'Readme.md', "README"]:
                candidate = os.path.join(os.path.dirname(os.path.realpath(__file__)), i)
                if os.path.isfile(candidate):
                    with open(candidate, "r", encoding="utf-8") as f:
                        md_text = f.read()
                    break

        if md_text:
            md = Markdown(md_text, inline_code_theme=theme, code_theme=theme, justify=justify)
            cls.console.print(md)
        else:
            cls.console.print(f"\n:cross_mark: [white on red blink]No Markdown file ![/]")
        

    @classmethod
    def show_all_lexers(cls):
        from pygments.lexers import get_all_lexers
        lexers = sorted(get_all_lexers(), key=lambda l: l[0].lower())
        cls.console.print("Supported Pygments lexers:\n")
        for lexer in lexers:
            name = lexer[0]
            aliases = ", ".join(lexer[1])
            exts = ", ".join(lexer[2])
            cls.console.print(f"[bold #00FFFF]{name}[/] | [bold #FFFF00]{aliases}[/] [bold #FF00EE]({exts})[/]")


    @classmethod
    def usage(cls):
        import argparse

        try:
            from licface import CustomRichHelpFormatter
        except:
            CustomRichHelpFormatter = argparse.RawTextHelpFormatter
        
        parser = argparse.ArgumentParser(prog="mk", description="Show markdown from file or clipboard with colors",formatter_class=CustomRichHelpFormatter)
        parser.add_argument('FILE', nargs='?', help='Markdown File or type "c" to get from clipboard')
        parser.add_argument('-c', '--clip', action='store_true', help='Alternative option if not use "c" as FILE argument')
        parser.add_argument('-t', '--theme', help = "Code theme, default = 'fruity'", default = 'fruity')
        parser.add_argument('-l', '--lexer', help = 'Code lexer')
        parser.add_argument('-j', '--justify', help = 'Justify method')
        parser.add_argument('-L', '--show-lexer', help = 'Show support lexers', action = 'store_true')

        if len(sys.argv) == 1:
            parser.print_help()

        args = parser.parse_args()

        if args.show_lexer:
            cls.show_all_lexers()
            sys.exit(0)

        if args.clip:
            if not HAS_CLIPBOARD:
                console.print("please install 'clipboard' first !")
                sys.exit(1)
            data = 'c'
        else:
            data = args.FILE

        valid_justify = {"left", "center", "right", "full"}
        justify = args.justify if args.justify in valid_justify else None
        cls.main(data, theme=args.theme, lexer=args.lexer, justify=justify)


if __name__ == '__main__':
    MarkdownReader.usage()











