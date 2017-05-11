import sys
import re

token_exprs = [
    (r'[ \n\r\t]+',         None),
    (r'#.*$',       None),
    (r'[A-Z]',      'LETTER'),
    (r'\(',          'SUBEXPR'),
    (r'\)',          'SUBEXPR'),
    (r'<=>',        'ONLYIF'),
    (r'=>',         'IMPLIES'),
    (r'\+',         'AND'),
    (r'\|',         'OR'),
    (r'\^',          'XOR'),
    (r'!',          'NOT')
]

def lexer(str, number_line):
    pos = 0
    tokens = []
    while pos < len(str):
        match = None
        for token_expr in token_exprs:
            pattern, tag = token_expr
            regex = re.compile(pattern)
            match = regex.match(str, pos)
            if match:
                text = match.group(0)
                if tag:
                    token = (text, tag)
                    tokens.append(token)
                break
        if not match:
            sys.stderr.write('[line: %d][column: %d] Illegal character: %s\\n' % (number_line, pos, str[pos]))
            sys.exit(1)
        else:
            pos = match.end(0)
    return tokens