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
    print('\nAST')
    print(ast, '\n')

    #Análise Semântica
    checker = Checker(ast)
    print('\nAST com anotações semânticas')
    print(ast, '\n')

    #Fim
    print('\nCompilação concluída com sucesso!')
