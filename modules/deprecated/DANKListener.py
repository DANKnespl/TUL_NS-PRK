# Generated from ./DANKParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from ..DANKParser import DANKParser
else:
    from DANKParser import DANKParser

# This class defines a complete listener for a parse tree produced by DANKParser.
class DANKListener(ParseTreeListener):
    def __init__(self, parser):
        self.parser = parser
        self.variables = {}  
        self.execute_stack = [True]
        self.loop_stack = [False]
        

    # Enter a parse tree produced by DANKParser#print.
    def enterPrint(self, ctx:DANKParser.PrintContext):
        if not self.execute_stack[-1]:
            return
        if ctx.getChildCount()==2:
            print()
        else:
            print(self.evaluateExpression(ctx.expresion()))
        pass

    # Enter a parse tree produced by DANKParser#loop.
    def enterLoop(self, ctx:DANKParser.LoopContext):
        if not self.execute_stack[-1]:
            self.loop_stack.append(False)
            return
        self.loop_stack.append(True)
        pass

    # Exit a parse tree produced by DANKParser#loop.
    def exitLoop(self, ctx:DANKParser.LoopContext):
        if self.loop_stack[-1] == True:
            print(ctx.getChild(0))
        self.loop_stack.pop()
        self.execute_stack.pop()
        pass

    # Enter a parse tree produced by DANKParser#var_def.
    def enterVar_def(self, ctx:DANKParser.Var_defContext):
        if not self.execute_stack[-1]:
            return
        var_name = ctx.ID().getText()
        value = self.evaluateExpression(ctx.expresion())
        self.variables[var_name] = value
        pass
    

    # Exit a parse tree produced by DANKParser#var_def.
    def exitVar_def(self, ctx:DANKParser.Var_defContext):
        print(self.variables)
        pass


    # Enter a parse tree produced by DANKParser#conditional.
    def enterConditional(self, ctx:DANKParser.ConditionalContext):
        if not self.execute_stack[-1]:
            return
        condition_result = self.evaluateLogicalExpression(ctx.logical_expresion())
        self.execute_stack.append(condition_result and self.execute_stack[-1])
        pass

    # Exit a parse tree produced by DANKParser#conditional.
    def exitConditional(self, ctx:DANKParser.ConditionalContext):
        self.execute_stack.pop()
        pass


    # Enter a parse tree produced by DANKParser#params.
    def enterParams(self, ctx:DANKParser.ParamsContext):
        pass

    # Exit a parse tree produced by DANKParser#params.
    def exitParams(self, ctx:DANKParser.ParamsContext):
        pass


    # Enter a parse tree produced by DANKParser#params_2.
    def enterParams_2(self, ctx:DANKParser.Params_2Context):
        pass

    # Exit a parse tree produced by DANKParser#params_2.
    def exitParams_2(self, ctx:DANKParser.Params_2Context):
        pass


    # Enter a parse tree produced by DANKParser#fun_def.
    def enterFun_def(self, ctx:DANKParser.Fun_defContext):
        pass

    # Exit a parse tree produced by DANKParser#fun_def.
    def exitFun_def(self, ctx:DANKParser.Fun_defContext):
        pass


    # Enter a parse tree produced by DANKParser#ids.
    def enterIds(self, ctx:DANKParser.IdsContext):
        pass

    # Exit a parse tree produced by DANKParser#ids.
    def exitIds(self, ctx:DANKParser.IdsContext):
        pass


    # Enter a parse tree produced by DANKParser#ids_2.
    def enterIds_2(self, ctx:DANKParser.Ids_2Context):
        pass

    # Exit a parse tree produced by DANKParser#ids_2.
    def exitIds_2(self, ctx:DANKParser.Ids_2Context):
        pass


    # Enter a parse tree produced by DANKParser#fun_call.
    def enterFun_call(self, ctx:DANKParser.Fun_callContext):
        pass

    # Exit a parse tree produced by DANKParser#fun_call.
    def exitFun_call(self, ctx:DANKParser.Fun_callContext):
        pass
    
    # Enter a parse tree produced by DANKParser#breakpoint.
    def enterBreakpoint(self, ctx:DANKParser.BreakpointContext):
        self.loop_stack[-1] = False
        self.execute_stack.append(False)
        pass
        
    def evaluateExpression(self, ctx):
        # (expression)
        if ctx.getChild(0).getText()=="(":
            return self.evaluateExpression(ctx.getChild(1))    
        # expression OPERATOR expression
        if ctx.getChildCount()!=1:
            left = self.evaluateExpression(ctx.getChild(0))
            right = self.evaluateExpression(ctx.getChild(2))
            operator = ctx.getChild(1).getText()
            if type(left)!=type(right):
                if type("")==type(left):
                    right = str(right)
                else:
                    left = str(left)
            if type(left) == type(""):
                match operator:
                    case "+":
                        return left + right
                    case _:
                        raise RuntimeError(f"Invalid operator: '{operator}'")
            else:
                match operator:
                    case "+":
                        return left + right
                    case "-":
                        return left - right
                    case "*":
                        return left * right
                    case "/":
                        return left / right
                    case _:
                        raise RuntimeError(f"Invalid operator: '{operator}'")
        # OPERAND
        text = ctx.getText()
        if text.isdigit():
            return int(text)
        elif text.startswith('"') and text.endswith('"'):
            return text[1:-1]
        elif text in self.variables:
            return self.variables[text]
        raise RuntimeError(f"Undefined variable or invalid expression: '{text}'")
        
        
        
    def evaluateLogicalExpression(self, ctx):
        left = self.evaluateExpression(ctx.getChild(0))
        right = self.evaluateExpression(ctx.getChild(2))
        operator = ctx.getChild(1).getText()
        if type(left)!=type(right):
            if type("")==type(left):
                right = str(right)
            else:
                left = str(left)
        match operator:
            case "<":
                return left < right
            case ">":
                return left > right
            case "=":
                return left == right
            case "<=":
                return left <= right
            case ">=":
                return left >= right
            case _:
                raise RuntimeError(f"Invalid operator: '{operator}'")
        return False


del DANKParser