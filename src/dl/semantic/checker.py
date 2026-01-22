from dl.lex.tag import Tag
from dl.semantic.env import Env, SymbolInfo
from dl.semantic.type import Type
from dl.tree.ast import AST
from dl.tree.nodes import Visitor, ProgramNode, BlockNode, DeclNode, AssignNode, IfNode, WriteNode, VarNode, LiteralNode, BinaryNode, ConvertNode, ExprNode


class Checker(Visitor):
    
    def __init__(self, ast: AST):
        self.__env_top = Env()
        self.has_semantic_error = False
        ast.root.accept(self)

    def __error(self, line: int, msg: str):
        self.has_semantic_error = True
        print(f'Erro semântico na linha {line}: {msg}')  
        
    def visit_program_node(self, node: ProgramNode):
        node.stmt.accept(self)
        
    def visit_block_node(self, node: BlockNode):
        pass
    
    def visit_decl_node(self, node: DeclNode):
        pass

    def visit_assign_node(self, node: AssignNode):
        pass

    def visit_if_node(self, node: IfNode):
        pass        
        
    def visit_write_node(self, node: WriteNode):
        pass
    
    def visit_var_node(self, node: VarNode):
        pass
                
    def visit_literal_node(self, node: LiteralNode):
        pass
            
    def visit_binary_node(self, node: BinaryNode):
        pass        
    
    def visit_convert_node(self, node: ConvertNode):
        pass
