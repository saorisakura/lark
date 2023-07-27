from lark import Lark, Transformer, v_args

# 定义语法规则
calc_grammar = """
    ?start: sum
    sum: product (("-" | "+") product)*
    product: atom ("*" atom | "/" atom)*
    atom: NUMBER | "(" sum ")"
    %import common.NUMBER
    %import common.WS_INLINE
    %ignore WS_INLINE
"""

# 定义 AST Evaluator
@v_args(inline=True)
class CalcTransformer(Transformer):
    from operator import add, sub, mul, truediv as div

    def start(self, value):
        return value

    def sum(self, *args):
        result = args[0]
        for i in range(1, len(args), 2):
            op = args[i]
            num = args[i + 1]
            result = op(result, num)
        return result

    def product(self, *args):
        result = args[0]
        for i in range(1, len(args), 2):
            op = args[i]
            num = args[i + 1]
            result = op(result, num)
        return result

    def atom(self, value):
        if isinstance(value, int):
            return value
        else:
            return value[0]

# 创建解析器
calc_parser = Lark(calc_grammar, parser='lalr', transformer=CalcTransformer())

# 解析表达式并计算其值
result = calc_parser.parse("1 + 2 * (3 - 4) / 5")
print(result.pretty())