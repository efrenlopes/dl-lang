from enum import Enum, auto

class Tag(Enum):

    #Operadores e delimitadores
    ASSIGN = auto()
    SUM = auto()
    SUB = auto()
    MUL = auto()
    EQ = auto()
    LT = auto()
    GT = auto()
    OR = auto()
    SEMI = auto()
    DOT = auto()
    LPAREN = auto()
    RPAREN = auto()

    #Outros
    EOF = auto()
    UNK = auto()

    #Literais numéricos
    LIT_INT = auto()
    LIT_REAL = auto()

    ID = auto()
        
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f'<Tag: {str(self)}>'