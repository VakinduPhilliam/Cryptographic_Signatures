# Python Tokenizer.
# tokenize — Tokenizer for Python source.
# The tokenize module provides a lexical scanner for Python source code, implemented in Python.
# The scanner in this module returns comments as tokens as well, making it useful for implementing “pretty-printers,” including colorizers for on-screen
# displays.
#
# To simplify token stream handling, all operator and delimiter tokens and Ellipsis are returned using the generic OP token type.
# The exact type can be determined by checking the exact_type property on the named tuple returned from tokenize.tokenize().
#
#

#
# Example of a script rewriter that transforms float literals into Decimal objects:
# 

from tokenize import tokenize, untokenize, NUMBER, STRING, NAME, OP
from io import BytesIO

def decistmt(s):
    """Substitute Decimals for floats in a string of statements.

    >>> from decimal import Decimal
    >>> s = 'print(+21.3e-5*-.1234/81.7)'
    >>> decistmt(s)
    "print (+Decimal ('21.3e-5')*-Decimal ('.1234')/Decimal ('81.7'))"

    The format of the exponent is inherited from the platform C library.
    Known cases are "e-007" (Windows) and "e-07" (not Windows).  Since
    we're only showing 12 digits, and the 13th isn't close to 5, the
    rest of the output should be platform-independent.

    >>> exec(s)  #doctest: +ELLIPSIS
    -3.21716034272e-0...7

    Output from calculations with Decimal should be identical across all
    platforms.

    >>> exec(decistmt(s))
    -3.217160342717258261933904529E-7
    """
    result = []

    g = tokenize(BytesIO(s.encode('utf-8')).readline)  # tokenize the string

    for toknum, tokval, _, _, _ in g:
        if toknum == NUMBER and '.' in tokval:  # replace NUMBER tokens

            result.extend([
                (NAME, 'Decimal'),
                (OP, '('),
                (STRING, repr(tokval)),
                (OP, ')')
            ])

        else:
            result.append((toknum, tokval))

    return untokenize(result).decode('utf-8')

# 
# Example of tokenizing from the command line.
# 

def say_hello():
    print("Hello, World!")

say_hello()

# 
# The script will be tokenized to the following output where the first column is the range of the line/column coordinates where the token is found, the
# second column is the name of the token, and the final column is the value of the token (if any).
#