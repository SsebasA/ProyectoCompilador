from arpeggio import PTNodeVisitor


class SemanticMistake(Exception):

    def __init__(self, message):
        super().__init__(f'Semantic error: {message}')


class SemanticVisitor(PTNodeVisitor):

    RESERVED_WORDS = ["true", "false", "var", "if", "else"]
    BIN_OCT_HEX_LIM = 2**31

    def __init__(self, parser, **kwargs):
        super().__init__(**kwargs)
        self.__parser = parser
        self.__symbol_table = []

    def position(self, node):
        return self.__parser.pos_to_linecol(node.position)

    @property
    def symbol_table(self):
        return self.__symbol_table
    
    def visit_decl_variable(self, node, children):
        name = node.value
        if name in self.RESERVED_WORDS:
            raise SemanticMistake(
                'Reserved word not allowed as var name at position'
                f'{self.position(node)} => {name}'
            )
        if name in self.__symbol_table:
            raise SemanticMistake(
                'Duplicate variable declaration at position'
                f'{self.position(node)} => {name}'
            )
        self.__symbol_table.append(name)
    
    def visit_lhs_variable(self, node, children):
        name = node.value
        if name not in self.__symbol_table:
            raise SemanticMistake(
                'Assignment to undeclared variable at position '
                f'{self.position(node)} => {name}'
            )
        
    
    def visit_decimal(self, node, children):
        value = int(node.value) 
        if value >= 2 ** 31:
            raise SemanticMistake(
                'Out of range decimal integer literal at position '
                f'{self.position(node=node)} => {value}'
            )
        
    def visit_rhs_variable(self, node, children):
        name = node.value
        if name not in self.__symbol_table:
            raise SemanticMistake(
                'Undeclared variable reference at position '
                f'{self.position(node)} => {name}'
            )
    
    def visit_binary(self, node, children):
        literal = node.value
        value = literal[2:]
        binary = int(value, 2)
        if binary >= self.BIN_OCT_HEX_LIM:
            raise SemanticMistake(
                'Binary exceed 2^31 at position '
                f'{self.position(node)} => {value}'
            )
    
    def visit_octal(self, node, children):
        literal = node.value
        value = literal[2:]
        octal = int(value, 8)
        if octal >= self.BIN_OCT_HEX_LIM:
             raise SemanticMistake(
                'Octal exceed 2^31 at position '
                f'{self.position(node)} => {value}'
            )
    
    def visit_hex(self, node, children):
        literal = node.value
        value = literal[2:]
        hexadecimal = int(value, 16)
        if hexadecimal >= self.BIN_OCT_HEX_LIM:
             raise SemanticMistake(
                'Hexadecimal exceed 2^31 at position '
                f'{self.position(node)} => {value}'
            )
    
    
