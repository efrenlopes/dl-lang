## Para rodar o projeto, entre na pasta do projeto e rode
```bash
PYTHONPATH=src python -m dl ./test/prog.dl
```


## Gramática Projeto completo da linguagem DL
```bnf
<PROGRAM>   ::= "programa" <id> <BLOCK>
<BLOCK>     ::= "inicio" <STMTS> "fim"
<STMTS>     ::= <STMT> ";" <STMTS> | ε
<STMT>	    ::= <BLOCK> | <DECL> | <ASSIGN> | <WRITE> | <IF>
<DECL>      ::= <type> <id>
<ASSIGN>    ::= <id> "=" <EXPR>
<WRITE>     ::= "escreva" "(" <EXPR> ")"
<IF>        ::= "se" "(" <EXPR> ")" <STMT>
<EXPR>      ::= <EXPR> "|" <EQUAL> | <EQUAL>
<EQUAL>     ::= <EQUAL> "==" <REL> | <REL>
<REL>       ::= <REL> "<" <ARITH> | <REL> ">" <ARITH> | <ARITH>
<ARITH>     ::= <ARITH> "+" <TERM> | <ARITH> "-" <TERM> | <TERM>
<TERM>      ::= <TERM> "*" <FACTOR>
<FACTOR>    ::= "(" <EXPR> ")" | <id> | <lit_int> | <lit_real> | <lit_bool>
<letter>    ::= "a" | "b" | ... | "z" | "A" | "B" | ... "Z" | "_"
<digit>     ::= "0" | "1" | ... | "9"
<id>        ::= <letter> (<letter> | <digit>)*
<lit_int>   ::= <digit>+
<lit_real>  ::= <digit>+ "." <digit>+ 
<lit_bool>  ::= "verdade" | "falso"
<type>      ::= "inteiro" | "real" | "booleano"
```