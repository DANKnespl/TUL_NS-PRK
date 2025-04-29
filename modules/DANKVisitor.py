# Generated from DANKParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .DANKParser import DANKParser
else:
    from DANKParser import DANKParser

# This class defines a complete generic visitor for a parse tree produced by DANKParser.

class DANKVisitor(ParseTreeVisitor):
    def __init__(self, parser):
        self.parser = parser
        self.variables = {} 
        self.functions = {}
        self.execute_stack = [True]
        self.loop = False



    # Visit a parse tree produced by DANKParser#program.
    def visitProgram(self, ctx:DANKParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DANKParser#statement.
    def visitStatement(self, ctx:DANKParser.StatementContext):
        if hasattr(self, 'execute_stack') and not self.execute_stack[-1]:
            return
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DANKParser#print.
    def visitPrint(self, ctx: DANKParser.PrintContext):
        if ctx.getChildCount() == 2:
            print()
        else:
            value = self.visit(ctx.expression())
            print(value)
        return None



    # Visit a parse tree produced by DANKParser#factor.
    def visitFactor(self, ctx:DANKParser.FactorContext):
        if ctx.getChild(0).getText()=="-":
            value = self.visitChildren(ctx)
            
            if isinstance(value, str):
                return value[::-1]
            else:
                return -value
        if ctx.getChildCount()!=1:
            return self.visit(ctx.getChild(1))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DANKParser#term.
    def visitTerm(self, ctx:DANKParser.TermContext):
        value = self.visit(ctx.factor(0))
        operator_counter = 0
        child_count = ctx.getChildCount()
        match child_count:
            case 1:
                return value
            case _:
                child_count = child_count - 1
                while operator_counter < child_count/2:
                    right = self.visit(ctx.factor(1 + operator_counter))
                    operator = ctx.getChild(1 + 2*operator_counter).getText()

                    if type(value) != type(right):
                        if isinstance(value, str):
                            right = str(right)
                        else:
                            value = str(value)
                    if isinstance(value, str):
                        self.raise_error(ctx, f"Invalid string operator: '{operator}'")
                    match operator:
                        case "*":
                            value =  value * right
                        case "/": 
                            if right !=0:
                                value = value / right
                            else:
                                self.raise_error(ctx, f"Division by zero") 
                        case _:
                            self.raise_error(ctx, f"Unknown operator: '{operator}'")
                    operator_counter+=1
        return value
        
    # Visit a parse tree produced by DANKParser#expression.
    def visitExpression(self, ctx: DANKParser.ExpressionContext):
        value = self.visit(ctx.term(0))
        operator_counter = 0
        child_count = ctx.getChildCount()
        match child_count:
            case 1:
                return value
            case _:
                child_count = child_count - 1
                while operator_counter < child_count/2:
                    right = self.visit(ctx.term(1 + operator_counter))
                    operator = ctx.getChild(1 + 2*operator_counter).getText()

                    # type coercion
                    if type(value) != type(right):
                        if isinstance(value, str):
                            right = str(right)
                        else:
                            value = str(value)
                    if isinstance(value, str):
                        match operator:
                            case "+": 
                                value = value + right
                            case "-": 
                                value = value + right[::-1]
                            case _: 
                                self.raise_error(ctx, f"Invalid string operator: '{operator}'")
                    else:
                        match operator:
                            case "+": 
                                value = value + right
                            case "-": 
                                value = value - right
                            case _: 
                                self.raise_error(ctx, f"Unknown operator: '{operator}'")
                    operator_counter+=1
        return value
        
    # Visit a parse tree produced by DANKParser#var_def.
    def visitVar_def(self, ctx: DANKParser.Var_defContext):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expression())  # Call the expression visitor
        self.variables[var_name] = value
        #print("Current Variables:", self.variables)
        return None

    # Visit a parse tree produced by DANKParser#operand.
    def visitOperand(self, ctx:DANKParser.OperandContext):
        text = ctx.getText()
        if text.isdigit():
            return float(text)
        elif text.startswith('"') and text.endswith('"'):
            return text[1:-1]
        elif text in self.variables:
            return self.variables[text]
        else:
            self.raise_error(ctx, f"Undefined variable or invalid expression: '{text}'")


    # Visit a parse tree produced by DANKParser#logical_expression.
    def visitLogical_expression(self, ctx: DANKParser.Logical_expressionContext):
        left = self.visit(ctx.getChild(0))
        operator = ctx.getChild(1).getText()
        right = self.visit(ctx.getChild(2))

        #print(left, operator, right)
        # type coercion
        if isinstance(left, str) != isinstance(right, str):
            if isinstance(left, str):
                right = str(right)
            else:
                left = str(left)
        match operator:
            case "<": return left < right
            case ">": return left > right
            case "=": return left == right
            case "<=": return left <= right
            case ">=": return left >= right
            case "~": return left != right
            case _: self.raise_error(f"Invalid logical operator: '{operator}'")
            



    # Visit a parse tree produced by DANKParser#conditional.
    def visitConditional(self, ctx: DANKParser.ConditionalContext):        
        condition_result = self.visit(ctx.logical_expression())
        if condition_result:
            for stmt in ctx.statement():
                self.visit(stmt)
        return None


    # Visit a parse tree produced by DANKParser#loop.
    def visitLoop(self, ctx: DANKParser.LoopContext):
        self.loop = True
        self.execute_stack.append(True)

        while self.loop:
            for stmt in ctx.statement():
                self.visit(stmt)

        # Cleanup after loop ends
        self.loop = False
        self.execute_stack.pop()
        return None

    # Visit a parse tree produced by DANKParser#breakpoint.
    def visitBreakpoint(self, ctx: DANKParser.BreakpointContext):
        self.loop = False
        self.execute_stack.append(False)
        return None



    # Visit a parse tree produced by DANKParser#params.
    def visitParams(self, ctx:DANKParser.ParamsContext):
        tmp = []
        if ctx.params_2():
            tmp.extend(self.visit(ctx.params_2()))
        tmp.extend([self.visit(ctx.factor())])
        return tmp


    # Visit a parse tree produced by DANKParser#params_2.
    def visitParams_2(self, ctx:DANKParser.Params_2Context):
        tmp = []
        if ctx.params_2():
            tmp.extend(self.visit(ctx.params_2()))
        tmp.extend([self.visit(ctx.factor())])
        return tmp

    # Visit a parse tree produced by DANKParser#fun_def.
    def visitFun_def(self, ctx:DANKParser.Fun_defContext):
        function_name= ctx.FUNCTION_NAME().getText()
        ids_ctx = ctx.ids()
        param_names = []
        if ids_ctx:
            param_names = self.visit(ctx.ids())
        if len(param_names) != len(set(param_names)):
            self.raise_error(ctx, f"Conflicting parameter identifiers in function: '{function_name}'")
        body = ctx.statement()
        
        self.functions[function_name] = {
            "params": param_names,
            "body": body
        }
        #print("Current Functions:", self.functions)
        return None


    # Visit a parse tree produced by DANKParser#ids.
    def visitIds(self, ctx:DANKParser.IdsContext):
        tmp = []
        if ctx.ids_2():
            tmp.extend(self.visit(ctx.ids_2()))
        tmp.extend([ctx.ID().getText()])
        return tmp


    # Visit a parse tree produced by DANKParser#ids_2.
    def visitIds_2(self, ctx:DANKParser.Ids_2Context):
        tmp = []
        if ctx.ids_2():
            tmp.extend(self.visit(ctx.ids_2()))
        tmp.extend([ctx.ID().getText()])
        return tmp

    # Visit a parse tree produced by DANKParser#fun_call.
    def visitFun_call(self, ctx:DANKParser.Fun_callContext):
        function_name= ctx.ID().getText()
        params_ctx = ctx.params()
        param_values = []
        if params_ctx:
            param_values = self.visit(ctx.params())
        if function_name in self.functions.keys() and len(self.functions[function_name]["params"])==len(param_values):
            fun = self.functions[function_name]
            variable_copy = self.variables.copy()
            function_copy = self.functions.copy()
            self.variables = {}
            execute_stack_copy = self.execute_stack.copy()
            loop_copy = self.loop
            self.execute_stack = [True]
            self.loop = False
            for iter,_ in enumerate(fun["params"]):
                self.variables[fun["params"][iter]] = param_values[iter]
            
            for iter,_ in enumerate(fun["body"]):
                self.visit(fun["body"][iter])
            
            for iter,_ in enumerate(fun["params"]):
                if fun["params"][iter] in variable_copy.keys():
                    self.variables[fun["params"][iter]] = variable_copy[fun["params"][iter]] 
                else:
                    self.variables.pop(fun["params"][iter])
            
            self.execute_stack = execute_stack_copy.copy()
            if "ret" in self.variables.keys():
                variable_copy["ret"] = self.variables["ret"]
            self.variables = variable_copy.copy()
            self.loop = loop_copy
            self.functions = function_copy.copy()
        else: 
            self.raise_error(ctx, f"Undefined function: '{function_name}', with {len(param_values)} parameters")
        #print("post Function variables: ",self.variables)
        return None


    def raise_error(self, ctx, message):
        start = ctx.start
        raise RuntimeError(f"Error at line {start.line}:{start.column}: {message}\nNear: '{ctx.getText()}'")
del DANKParser
