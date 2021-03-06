from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        #print
        self.lexer.add('PRINT', r'print')
        #parenthesis
        self.lexer.add('OPEN_PAREN',r'\(')
        self.lexer.add('CLOSE_PAREN',r'\)')
        #semi colon
        self.lexer.add('SEMI_COLON', r'\;')
        #operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        #number
        self.lexer.add('NUMBER', r'\d+')
        #ignore spaces
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()