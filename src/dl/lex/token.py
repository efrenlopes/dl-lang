from dl.lex.tag import Tag

class Token:
    
    def __init__(self, tag: Tag, lexeme: str, line: int):
        self.tag = tag
        self.lexeme = lexeme
        self.line = line

    def __str__(self):
        return f"<{self.tag}, '{self.lexeme}'>"

    def __repr__(self):
        return f'<Token: {str(self)} at line {self.line}>'