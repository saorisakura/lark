#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
在 Lark 中，可以使用 `|` 符号指定规则之间的优先级关系，以及使用 `^` 符号指定运算符的结合性。以下是一些常用的优先级和结合性规则：

1. 优先级规则：可以使用 `|` 符号指定规则之间的优先级顺序。例如，可以使用以下规则指定加法和乘法的优先级关系：

```
expr: term (("+" | "-") term)*
term: factor (("*" | "/") factor)*
factor: NUMBER | LPAREN expr RPAREN
```

在这个规则中，我们首先定义了 `factor` 规则，它可以匹配数字或括号中的表达式。然后我们定义了 `term` 规则，它可以匹配一个因子或一组因子之间的乘法或除法。最后，我们定义了 `expr` 规则，它可以匹配一个项或一组项之间的加法或减法。通过使用 `|` 符号，我们可以指定加法和减法的优先级高于乘法和除法。

2. 结合性规则：可以使用 `^` 符号指定运算符的结合性。例如，可以使用以下规则指定指数运算的结合性：

```
expr: term (("+" | "-") term)*
term: factor (("*" | "/") factor)*
factor: power | NUMBER | LPAREN expr RPAREN
power: factor ("^" factor)
```

在这个规则中，我们引入了一个新的规则 `power`，它可以匹配一个因子或一组因子之间的指数运算。然后，我们将 `power` 规则包括在 `factor` 规则中，以便指定指数运算的优先级和结合性。通过使用 `^` 符号，我们可以指定 `^` 运算符是右结合的，这意味着它会从右到左地结合因子。

总之，在 Lark 中，可以使用 `|` 符号指定规则之间的优先级关系，以及使用 `^` 符号指定运算符的结合性。这些规则可以帮助解析器在处理具有相同运算符的表达式时确定正确的推导路径。
"""
import json

"""
下面是使用Lark手写一门简单的脚本语言的代码示例：

首先，定义语言的语法规则，例如：

```
start: expr

expr: term
    | expr "+" term   -> add
    | expr "-" term   -> sub

term: atom
    | term "*" atom   -> mul
    | term "/" atom   -> div

atom: INT            -> int
    | FLOAT          -> float
    | ID             -> var
    | LPAREN expr RPAREN

%import common.ESCAPED_STRING -> STRING
%import common.INT
%import common.FLOAT
%import common.CNAME -> ID

%import common.WS
%import common.WS_INLINE
%ignore WS
%ignore WS_INLINE
```

这里定义了一个简单的四则运算表达式语言，支持整数、浮点数和变量的运算。其中，start规则表示整个表达式，expr规则表示表达式，term规则表示一项，atom规则表示一个元素（整数、浮点数、变量或括号括起来的表达式）。

接下来，实现语言的解释器，例如：

```python
from lark import Lark, Transformer

class EvalTransformer(Transformer):
    def add(self, args):
        return args[0] + args[1]

    def sub(self, args):
        return args[0] - args[1]

    def mul(self, args):
        return args[0] * args[1]

    def div(self, args):
        return args[0] / args[1]

    def int(self, args):
        return int(args[0])

    def float(self, args):
        return float(args[0])

    def var(self, args):
        return variables[args[0]]

    def start(self, args):
        return args[0]

variables = {}

def evaluate(expression):
    parser = Lark(grammar, parser="lalr", transformer=EvalTransformer())
    result = parser.parse(expression)
    return result

print(evaluate("2 + 3 * 4"))  # 输出14
print(evaluate("3 * (2 + 1)"))  # 输出9
```

这里实现了一个简单的语法树遍历器，根据语法规则执行表达式的计算。变量存储在全局变量variables中。

最后，定义标准库和内置函数，例如：

```python
import sys
import os

def read_file(filename):
    with open(filename, "r") as f:
        return f.read()

def write_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)

def print_file(filename):
    content = read_file(filename)
    print(content)

def list_dir(path):
    return os.listdir(path)

def mkdir(path):
    os.mkdir(path)

def getcwd():
    return os.getcwd()

def exit():
    sys.exit()

variables = {
    "read_file": read_file,
    "write_file": write_file,
    "print_file": print_file,
    "list_dir": list_dir,
    "mkdir": mkdir,
    "getcwd": getcwd,
    "exit": exit,
}
```

这里定义了一些文件操作和系统操作的函数，例如读取文件、写入文件、打印文件、列出目录、创建目录、获取当前工作目录和退出程序等。这些函数存储在变量variables中，可以在脚本中直接调用。

综合以上代码，可以得到一个简单的脚本语言解释器。
"""
import pprint
from contextlib import suppress

from lark import Lark, Transformer


def lll():
    l = [1, 2, 3]
    i = 0
    with suppress(EOFError):
        while True:
            if i >= len(l):
                break
            yield l[i]
            i += 1


for i in lll():
    print(i)

CommonLexer = """%import common.ESCAPED_STRING -> STRING
%import common.INT
%import common.FLOAT
%import common.NUMBER
%import common.LETTER
%import common.DIGIT
%import common.CNAME -> ID
%import common.NEWLINE -> _NL  # _NL is just have to be recognized and skipped by the parser.
%import common.C_COMMENT
%import common.CPP_COMMENT
%import common.WS
%ignore CPP_COMMENT
%ignore C_COMMENT
%ignore WS

FUNCTION: "function"
CLASS: "class"
IF: "if"
ELSE: "else"
WHILE: "while"
DO: "do"
FOR: "for"
LET: "let"
VAR: "var"
RETURN: "return"
BREAK: "break"
CONTINUE: "continue"
CONSTRUCTOR: "constructor"
THIS: "this"
SUPER: "super"
NULL: "null"
TRUE: "true"
FALSE: "false"
NEW: "new"
PRINT: "print"
PRINT_FILE: "print_file"
IMPORT: "import"
FROM: "from"
AS: "as"
IN: "in"
TYPEOF: "typeof"
INSTANCEOF: "instanceof"
DELETE: "delete"
TRY: "try"
CATCH: "catch"
FINALLY: "finally"
THROW: "throw"
THROWS: "throws"
VOID: "void"
INTERFACE: "interface"
EXTENDS: "extends"
IMPLEMENTS: "implements"
PACKAGE: "package"
YIELD: "yield"
AWAIT: "await"
DEBUGGER: "debugger"
ABSTRACT: "abstract"
BOOLEAN: "boolean"
BYTE: "byte"
CHAR: "char"
SHORT: "short"
CONST: "const"
INT_LITERAL: "int"
FLOAT_LITERAL: "float"
STRING_LITERAL: "string"
STRING_LITERAL_WRAP: "String"
FLOAT_LITERAL_WRAP: "Float"
INT_LITERAL_WRAP: "Integer"
CHAR_LITERAL_WRAP: "Character"
BOOLEAN_LITERAL_WRAP: "Boolean"
VOID_LITERAL_WRAP: "Void"
DOUBLE_LITERAL_WRAP: "Double"
DOUBLE: "double"
ENUM: "enum"
LONG: "long"
NATIVE: "native"
ASSERT: "assert"
SWITCH: "switch"
CASE: "case"
DEFAULT: "default"
LPAREN: "("
RPAREN: ")"
UNDERSCORE: "_"
PLUS: "+"
MINUS: "-"
PRODUCT: "*"
DIVIDE: "/"
MOD: "%"
ASSIGN: "="
PLUS_ASSIGN: "+="
MINUS_ASSIGN: "-="
PRODUCT_ASSIGN: "*="
DIVIDE_ASSIGN: "/="
MOD_ASSIGN: "%="
AND_ASSIGN: "&="
OR_ASSIGN: "|="
XOR_ASSIGN: "^="
LSHIFT_ASSIGN: "<<="
RSHIFT_ASSIGN: ">>="
URSHIFT_ASSIGN: ">>>="
AND: "&"
OR: "|"
XOR: "^"
LSHIFT: "<<"
RSHIFT: ">>"
URSHIFT: ">>>"
NOT: "!"
TILDE: "~"
QUESTION: "?"
COLON: ":"
SEMI: ";"
COMMA: ","
DOT: "."
ELLIPSIS: "..."
LBRACK: "["
RBRACK: "]"
LBRACE: "{"
RBRACE: "}"
AT: "@"
LT: "<"
GT: ">"
LTE: "<="
GTE: ">="
EQUAL: "=="
NOTEQUAL: "!="
ANDAND: "&&"
OROR: "||"
INC: "++"
DEC: "--"
ARROW: "->"
COLONCOLON: "::"

RESTRICT: "restrict"
TRANSIENT: "transient"
VOLATILE: "volatile"
FINAL: "final"
STATIC: "static"
PUBLIC: "public"
PROTECTED: "protected"
PRIVATE: "private"
"""

grammar = CommonLexer + """
start: prog

class_declaration: CLASS ID (EXTENDS type_type)? (IMPLEMENTS type_list)? class_body

class_body: LBRACE class_member RBRACE
    
class_member: SEMI
    | class_member_declaration*

class_member_declaration: function_declaration
    | field_declaration
    | class_declaration

function_declaration: type_type ID LPAREN formal_parameters RPAREN (LBRACK RBRACK)* (THROWS qualified_name_list)? function_body

function_body: block
    | SEMI

qualified_name_list: qualified_name (COMMA qualified_name)*

formal_parameters: (formal_parameter_list)?

formal_parameter_list: formal_parameter (COMMA formal_parameter)* (COMMA last_formal_parameter)?
    | last_formal_parameter

formal_parameter: variable_modifier* type_type variable_declarator_id

last_formal_parameter: variable_modifier* type_type ELLIPSIS variable_declarator_id

variable_modifier: RESTRICT
    | TRANSIENT
    | VOLATILE
    | FINAL
    | STATIC
    | PUBLIC
    | PROTECTED
    | PRIVATE

qualified_name: ID (DOT ID)*

field_declaration: variable_declarators SEMI

constructor_declaration: ID formal_parameters (THROWS qualified_name_list)? block

variable_declarators: type_type variable_declarator (COMMA variable_declarator)*

variable_declarator: variable_declarator_id ("=" variable_initializer)?

variable_declarator_id: ID (LBRACK RBRACK)*

variable_initializer: expression
    | array_initializer

array_initializer: LBRACE (variable_initializer (COMMA variable_initializer)* (COMMA)? )? RBRACE

type_argument: type_type
    | QUESTION (EXTENDS | SUPER) type_type

prog: block_statements

block: LBRACE block_statements RBRACE

block_statements: block_statement*

declaration: variable_declarators SEMI
    | function_declaration
    | class_declaration

block_statement: statement
    | declaration

statement: block
    | ASSERT expression (COLON expression)? SEMI
    | IF par_expression statement (ELSE statement)?
    | FOR LPAREN for_control RPAREN statement
    | WHILE par_expression statement
    | DO statement WHILE par_expression SEMI
    | TRY block (catch_clause+ finally_block? | finally_block)
    | SWITCH par_expression LBRACE switch_block_statement_group* switch_label* RBRACE
    | RETURN expression? SEMI
    | THROW expression SEMI
    | BREAK ID? SEMI
    | CONTINUE ID? SEMI
    | SEMI
    | expression SEMI
    | ID COLON statement

catch_clause: CATCH LPAREN variable_modifier* catch_type ID RPAREN block

catch_type: qualified_name (OR qualified_name)*

finally_block: FINALLY block

switch_block_statement_group: switch_label+ block_statement+

switch_label: CASE (expression | ID) COLON
    | DEFAULT COLON

for_control: enhanced_for_control
    | for_init? SEMI expression? SEMI expression_list?

for_init: variable_declarators
    | expression_list

enhanced_for_control: type_type variable_declarator_id COLON expression

par_expression: LPAREN expression RPAREN

expression_list: expression (COMMA expression)*

function_call: ID (DOT ID)* LPAREN expression_list? RPAREN
    | THIS LPAREN expression_list? RPAREN
    | SUPER LPAREN expression_list? RPAREN

expression: primary
    | expression DOT ( ID | function_call )
    | expression LBRACK expression RBRACK
    | function_call
    | expression(INC | DEC)
    | (PLUS|MINUS|INC|DEC) expression
    | (TILDE|NOT) expression
    | expression ("<" "<" | ">" ">" ">" | ">" ">") expression
    | expression QUESTION expression COLON expression
    | expression (operator) expression
    | primary ID ASSIGN expression

operator: ASSIGN | PLUS_ASSIGN | MINUS_ASSIGN | AND_ASSIGN | OR_ASSIGN | XOR_ASSIGN 
    | RSHIFT_ASSIGN | URSHIFT_ASSIGN | LSHIFT_ASSIGN | MOD_ASSIGN | MINUS | PLUS | PRODUCT_ASSIGN | DIVIDE_ASSIGN
    | PRODUCT | DIVIDE | MOD | LT | GT | LTE | GTE | EQUAL | NOTEQUAL | AND | OR | XOR | ANDAND | OROR

primary: LPAREN expression RPAREN
    | THIS
    | SUPER
    | literal
    | qualified_name

type_list: type_type (COMMA type_type)*

type_type: (function_type | primitive_type) (LBRACK RBRACK)*

function_type: FUNCTION type_type LPAREN type_list? RPAREN

literal: NUMBER
    | STRING
    | TRUE
    | FALSE
    | NULL

primitive_type: BOOLEAN
    | CHAR
    | BYTE
    | SHORT
    | INT_LITERAL
    | LONG
    | FLOAT_LITERAL
    | DOUBLE
    | STRING_LITERAL
    | INT_LITERAL_WRAP
    | FLOAT_LITERAL_WRAP
    | STRING_LITERAL_WRAP
    | CHAR_LITERAL_WRAP
    | BOOLEAN_LITERAL_WRAP
    | VOID_LITERAL_WRAP
    | DOUBLE_LITERAL_WRAP
    | class_type
    | VOID

class_type: UNDERSCORE|LETTER|DIGIT

creator: ID arguments

super_suffix: arguments
    | DOT ID arguments?

arguments: LPAREN expression_list? RPAREN
    
"""


text1 = """
/**
普通函数功能。
包括普通函数功能和从中间返回的功能。
*/
int foo(int a) {
    return a + a;
}

println("foo(10)=" + foo(10));

//测试return语句从中间返回
int bar(int a){
    for (int i = 0; i< a; i++){
        //println("i="+i);
        if (i >= 5){
            return i;   //在任意点返回
        }
    }
    return a;
}

println("bar(3)=" + bar(3));    //返回3，执行return a

println("bar(10)=" + bar(10));  //返回5，执行return i

/**
测试各种表达式功能。
*/

//纯字面量计算
//优先级及结合性没有问题
println(2+3*5);
println((2+3)*5);

//表达式中使用变量
int a = 10;
int b = 2;
println(a + b*b);

//关系运算
println("a == b : " + (a == b));
println("a > b : " + (a > b));

//逻辑运算
boolean c = a == b;
println("c || true || a>b : " + (c || true || a>b));
println("!c : " + !c );

//字符串类型
string str1 = "Hello ";
string str2 = "World!";
println(str1 + str2);

String str3 = null;   //可以赋值null
str1 + str3;

/**
测试几种循环语句。
包括对break的支持（只跳出一层循环)。
*/

//测试while循环
println("while loop:");
int i = 0;
while(i < 10){
    i = i+1;
    println("i="+i);
}


//测试for循环
println();
println("for loop:");
int a = 0;
for(int i = 0; i<10; i++){
    a = a + i;
    println("i="+i + ", a="+a);
}

//测试带break的while循环
println();
println("while loop, breaks when i > 5:");
i = 0;
while(i < 10){
    i = i+1;
    println("i="+i);
    if (i > 5)
        break;
}

//测试带break的for循环
println();
println("for loop, breaks when i > 5:");
a = 0;
for(int i = 0; i<10; i++){
    a = a + i;
    println("i="+i + ", a="+a);
    if (i > 5)
        break;
}

//测试嵌套循环，和break
println();
println("for loop within while loop:");
i = 0;
while (i<5){
    i = i+1;
    for (int j = 0; j< 5; j++){
        println("i="+i + ", j="+j);
        if (j>=2)
            break;
    }

    if (i >= 3){
        break;
    }
}

/*
简单的面向对象特性。
*/

class Mammal{
  //类属性
  string name = "";

  //构造方法
  Mammal(string str){
    name = str;
  }

  //方法
  void speak(){
    println("mammal " + name +" speaking...");
  }
}

Mammal mammal = Mammal("dog");           //playscript特别的构造方法，不需要用new关键字。
mammal.speak();                          //访问对象方法
println("mammal.name = " + mammal.name); //访问对象的属性


//没有构造方法，创建的时候用缺省构造方法
class Bird{
  int speed = 50;    //在缺省构造方法里初始化

  void fly(){
    println("bird flying...");
  }
}

Bird bird = Bird();              //采用缺省构造方法
println("bird.speed : " + bird.speed + "km/h");
bird.fly();

/**
测试对块作用域的支持。
*/

//全局变量
int i = 0;
println(i);  //输出：0

{
    //这里引用的是全局变量
    i = 2;
    println(i); //输出：2

    //允许在块里新创建一个同名的变量
    int i = 3;
    println(i); //输出：3
}

//重新看看全局变量的值
println(i);  //输出：2

/*
FirstClassFunction.play 函数作为一等公民。
也就是函数可以数值，赋给别的变量。
支持函数类型，即FunctionType。
*/

int foo(int a){
    println("in foo, a = " + a);
    return a;
}

int bar (function int(int) fun){
    int b = fun(6);
    println("in bar, b = " + b);
    return b;
}

function int(int) a = foo;  //函数作为变量初始化值
a(4);

function int(int) b;        
b = foo;                    //函数用于赋值语句
b(5);

bar(foo);                   //函数做为参数
"""

text = """
1 + 2 * 3;
(1 + 2) * 3;
"""


lexer = Lark(grammar, parser="lalr", lexer="basic")
for token in lexer.lex(text):
    print(token, token.type)
print('词法分析结束')
print('-' * 20)


class EvaluateTransformer(Transformer):

    def start(self, args):
        return args

    def prog(self, args):
        return args

    def block_statements(self, args):
        return args

    def block(self, args):
        return args

    def block_statement(self, args):
        return args

    def statement(self, args):
        return args

    def expression(self, args):
        if len(args) == 1:
            return args[0]
        else:
            left, op, right = args
            if op == '+':
                return left + right
            elif op == '-':
                return left - right
            elif op == '*':
                return left * right
            elif op == '/':
                return left / right
            elif op == '%':
                return left % right
            elif op == '+=':
                left += right
                return left
            elif op == '-=':
                left -= right
                return left
            elif op == '*=':
                left *= right
                return left
            elif op == '/=':
                left /= right
                return left
        return args

    def primary(self, args):
        if len(args) == 1:
            return args[0]
        else:
            return args[1]

    def operator(self, args):
        return args[0].value

    def literal(self, value):
        val = value[0]
        if val.type == 'NUMBER' and '.' not in val:
            return int(val)
        elif val.type == 'NUMBER' and '.' in val:
            return float(val)
        elif val.type == 'STRING':
            return val


parser = Lark(grammar, parser="lalr")
parser1 = Lark(grammar, parser="lalr", transformer=EvaluateTransformer())
tree = parser.parse(text)
tree1 = parser1.parse(text)
print(tree)
print(tree1)
print('语法分析结束')
