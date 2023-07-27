#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lark import Lark, Transformer


rules = """
?value: dict
    | list
    | STRING  -> string
    | NUMBER  -> number
    | "true"  -> true
    | "false" -> false
    | "null"  -> null
list: "[" [value ( "," value)*] "]"
dict: "{" [pair ( "," pair)*] "}"
pair: STRING ":" value

%import common.ESCAPED_STRING -> STRING
%import common.NUMBER

%import common.WS
%ignore WS
"""


class MyTransformer(Transformer):
    def list(self, items):
        return list(items)
    def pair(self, key_value):
        k, v = key_value
        return k, v
    def dict(self, items):
        return dict(items)


class TreeToJson(Transformer):
    def string(self, s):
        (s,) = s
        return s[1:-1]
    def number(self, n):
        (n,) = n
        return float(n)

    list = list
    pair = tuple
    dict = dict

    null = lambda self, _: None
    true = lambda self, _: True
    false = lambda self, _: False


# json_parser = Lark(rules, start='value')
# json_parser = Lark(rules, start='value', lexer='basic')
json_parser = Lark(rules, start='value', parser='lalr')
text = '{"key": ["item0", "item1", 3.14, true, false, null, {"subkey": "subvalue"}]}'
tree = json_parser.parse(text)
# print(tree.pretty())
print(MyTransformer().transform(tree))
print(TreeToJson().transform(tree))

parser1 = Lark(r"""
        start: _NL? section+
        section: "[" NAME "]" _NL item+
        item: NAME "=" VALUE? _NL

        NAME: /\w/+
        VALUE: /./+

        %import common.NEWLINE -> _NL
        %import common.WS_INLINE
        %ignore WS_INLINE
    """, parser="lalr")


sample_conf = """
[bla]
a=Hello
this="that",4
empty=
"""

print(parser1.parse(sample_conf).pretty())
