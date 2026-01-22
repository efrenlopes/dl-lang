import sys
from dl.lex.lexer import Lexer
from dl.syntax.parser import Parser
from dl.semantic.checker import Checker

if __name__ == '__main__':
    #Entrada
    if len(sys.argv) != 2:
        print('Argumentos inválidos! Esperado um caminho ' +
              'de arquivo para um programa na linguagem DL.')
        exit()
    file_input = sys.argv[1]

    #Análise Léxica
    lexer = Lexer(file_input)

    #Análise Sintática
    parser = Parser(lexer)
    ast = parser.ast
    print('\n\nAST')
    print(ast)

    #Análise Semântica
    checker = Checker(ast)
    print('\n\nAST com anotações semânticas')
    print(ast)

    #Fim
    print('\n\nCompilação concluída com sucesso!')
