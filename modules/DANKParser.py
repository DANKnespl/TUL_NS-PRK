# Generated from ./grammar/DANKParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,45,177,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,5,0,38,8,0,10,0,12,0,
        41,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,52,8,1,1,2,1,2,3,
        2,56,8,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,3,3,65,8,3,1,3,3,3,68,8,3,1,
        4,1,4,1,4,5,4,73,8,4,10,4,12,4,76,9,4,1,5,1,5,1,5,5,5,81,8,5,10,
        5,12,5,84,9,5,1,6,1,6,5,6,88,8,6,10,6,12,6,91,9,6,1,6,1,6,1,7,1,
        7,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,5,10,109,8,
        10,10,10,12,10,112,9,10,1,10,1,10,1,11,1,11,1,12,1,12,1,12,1,12,
        1,12,3,12,123,8,12,1,13,1,13,1,13,1,13,1,13,1,13,5,13,131,8,13,10,
        13,12,13,134,9,13,1,14,1,14,1,14,1,14,1,14,3,14,141,8,14,1,14,1,
        14,5,14,145,8,14,10,14,12,14,148,9,14,1,14,1,14,1,15,1,15,1,15,1,
        15,1,15,3,15,157,8,15,1,16,1,16,1,16,1,16,1,16,1,16,5,16,165,8,16,
        10,16,12,16,168,9,16,1,17,1,17,1,17,3,17,173,8,17,1,17,1,17,1,17,
        0,2,26,32,18,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,0,
        5,2,0,11,12,40,41,1,0,13,14,1,0,11,12,2,0,27,29,32,33,1,0,34,39,
        179,0,39,1,0,0,0,2,51,1,0,0,0,4,53,1,0,0,0,6,67,1,0,0,0,8,69,1,0,
        0,0,10,77,1,0,0,0,12,85,1,0,0,0,14,94,1,0,0,0,16,98,1,0,0,0,18,100,
        1,0,0,0,20,104,1,0,0,0,22,115,1,0,0,0,24,122,1,0,0,0,26,124,1,0,
        0,0,28,135,1,0,0,0,30,156,1,0,0,0,32,158,1,0,0,0,34,169,1,0,0,0,
        36,38,3,2,1,0,37,36,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,1,
        0,0,0,40,42,1,0,0,0,41,39,1,0,0,0,42,43,5,0,0,1,43,1,1,0,0,0,44,
        52,3,4,2,0,45,52,3,28,14,0,46,52,3,34,17,0,47,52,3,12,6,0,48,52,
        3,14,7,0,49,52,3,20,10,0,50,52,3,22,11,0,51,44,1,0,0,0,51,45,1,0,
        0,0,51,46,1,0,0,0,51,47,1,0,0,0,51,48,1,0,0,0,51,49,1,0,0,0,51,50,
        1,0,0,0,52,3,1,0,0,0,53,55,5,15,0,0,54,56,3,10,5,0,55,54,1,0,0,0,
        55,56,1,0,0,0,56,57,1,0,0,0,57,58,5,16,0,0,58,5,1,0,0,0,59,60,5,
        9,0,0,60,61,3,10,5,0,61,62,5,10,0,0,62,68,1,0,0,0,63,65,7,0,0,0,
        64,63,1,0,0,0,64,65,1,0,0,0,65,66,1,0,0,0,66,68,3,16,8,0,67,59,1,
        0,0,0,67,64,1,0,0,0,68,7,1,0,0,0,69,74,3,6,3,0,70,71,7,1,0,0,71,
        73,3,6,3,0,72,70,1,0,0,0,73,76,1,0,0,0,74,72,1,0,0,0,74,75,1,0,0,
        0,75,9,1,0,0,0,76,74,1,0,0,0,77,82,3,8,4,0,78,79,7,2,0,0,79,81,3,
        8,4,0,80,78,1,0,0,0,81,84,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,
        11,1,0,0,0,84,82,1,0,0,0,85,89,5,17,0,0,86,88,3,2,1,0,87,86,1,0,
        0,0,88,91,1,0,0,0,89,87,1,0,0,0,89,90,1,0,0,0,90,92,1,0,0,0,91,89,
        1,0,0,0,92,93,5,18,0,0,93,13,1,0,0,0,94,95,5,29,0,0,95,96,5,1,0,
        0,96,97,3,10,5,0,97,15,1,0,0,0,98,99,7,3,0,0,99,17,1,0,0,0,100,101,
        3,6,3,0,101,102,7,4,0,0,102,103,3,6,3,0,103,19,1,0,0,0,104,105,5,
        20,0,0,105,106,3,18,9,0,106,110,5,42,0,0,107,109,3,2,1,0,108,107,
        1,0,0,0,109,112,1,0,0,0,110,108,1,0,0,0,110,111,1,0,0,0,111,113,
        1,0,0,0,112,110,1,0,0,0,113,114,5,21,0,0,114,21,1,0,0,0,115,116,
        5,19,0,0,116,23,1,0,0,0,117,118,3,26,13,0,118,119,5,7,0,0,119,120,
        3,6,3,0,120,123,1,0,0,0,121,123,3,6,3,0,122,117,1,0,0,0,122,121,
        1,0,0,0,123,25,1,0,0,0,124,125,6,13,-1,0,125,126,3,6,3,0,126,132,
        1,0,0,0,127,128,10,2,0,0,128,129,5,7,0,0,129,131,3,6,3,0,130,127,
        1,0,0,0,131,134,1,0,0,0,132,130,1,0,0,0,132,133,1,0,0,0,133,27,1,
        0,0,0,134,132,1,0,0,0,135,136,5,24,0,0,136,137,5,44,0,0,137,138,
        5,45,0,0,138,140,5,22,0,0,139,141,3,30,15,0,140,139,1,0,0,0,140,
        141,1,0,0,0,141,142,1,0,0,0,142,146,5,23,0,0,143,145,3,2,1,0,144,
        143,1,0,0,0,145,148,1,0,0,0,146,144,1,0,0,0,146,147,1,0,0,0,147,
        149,1,0,0,0,148,146,1,0,0,0,149,150,5,25,0,0,150,29,1,0,0,0,151,
        152,3,32,16,0,152,153,5,7,0,0,153,154,5,29,0,0,154,157,1,0,0,0,155,
        157,5,29,0,0,156,151,1,0,0,0,156,155,1,0,0,0,157,31,1,0,0,0,158,
        159,6,16,-1,0,159,160,5,29,0,0,160,166,1,0,0,0,161,162,10,2,0,0,
        162,163,5,7,0,0,163,165,5,29,0,0,164,161,1,0,0,0,165,168,1,0,0,0,
        166,164,1,0,0,0,166,167,1,0,0,0,167,33,1,0,0,0,168,166,1,0,0,0,169,
        170,5,29,0,0,170,172,5,9,0,0,171,173,3,24,12,0,172,171,1,0,0,0,172,
        173,1,0,0,0,173,174,1,0,0,0,174,175,5,10,0,0,175,35,1,0,0,0,16,39,
        51,55,64,67,74,82,89,110,122,132,140,146,156,166,172
    ]

class DANKParser ( Parser ):

    grammarFileName = "DANKParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "','", "';'", 
                     "'('", "')'", "<INVALID>", "<INVALID>", "'*'", "'/'", 
                     "'<present>'", "'</present>'", "'<cycle>'", "'</cycle>'", 
                     "'<leave>'", "'<branch condition=\"'", "'</branch>'", 
                     "'<params>'", "'</params>'", "'<delegate name=\"'", 
                     "'</delegate>'" ]

    symbolicNames = [ "<INVALID>", "EQ", "LT", "GT", "LTE", "GTE", "NEQ", 
                      "COMMA", "SEMI", "LPAREN", "RPAREN", "PLUS", "MINUS", 
                      "MULT", "DIV", "PRINT_BEGIN", "PRINT_END", "LOOP_BEGIN", 
                      "LOOP_END", "BREAKPOINT", "CONDITIONAL_BEGIN", "CONDITIONAL_END", 
                      "PARAMS_BEGIN", "PARAMS_END", "FUNCTION_BEGIN", "FUNCTION_END", 
                      "SIGN", "NUMBER", "STRING", "ID", "WS", "COMMENT", 
                      "COND_ID", "COND_NUMBER", "COND_GT", "COND_LT", "COND_GTE", 
                      "COND_LTE", "COND_EQ", "COND_NEQ", "COND_PLUS", "COND_MINUS", 
                      "END_QUOTE_GT_COND", "COND_WS", "FUNCTION_NAME", "END_QUOTE_GT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_print = 2
    RULE_factor = 3
    RULE_term = 4
    RULE_expression = 5
    RULE_loop = 6
    RULE_var_def = 7
    RULE_operand = 8
    RULE_logical_expression = 9
    RULE_conditional = 10
    RULE_breakpoint = 11
    RULE_params = 12
    RULE_params_2 = 13
    RULE_fun_def = 14
    RULE_ids = 15
    RULE_ids_2 = 16
    RULE_fun_call = 17

    ruleNames =  [ "program", "statement", "print", "factor", "term", "expression", 
                   "loop", "var_def", "operand", "logical_expression", "conditional", 
                   "breakpoint", "params", "params_2", "fun_def", "ids", 
                   "ids_2", "fun_call" ]

    EOF = Token.EOF
    EQ=1
    LT=2
    GT=3
    LTE=4
    GTE=5
    NEQ=6
    COMMA=7
    SEMI=8
    LPAREN=9
    RPAREN=10
    PLUS=11
    MINUS=12
    MULT=13
    DIV=14
    PRINT_BEGIN=15
    PRINT_END=16
    LOOP_BEGIN=17
    LOOP_END=18
    BREAKPOINT=19
    CONDITIONAL_BEGIN=20
    CONDITIONAL_END=21
    PARAMS_BEGIN=22
    PARAMS_END=23
    FUNCTION_BEGIN=24
    FUNCTION_END=25
    SIGN=26
    NUMBER=27
    STRING=28
    ID=29
    WS=30
    COMMENT=31
    COND_ID=32
    COND_NUMBER=33
    COND_GT=34
    COND_LT=35
    COND_GTE=36
    COND_LTE=37
    COND_EQ=38
    COND_NEQ=39
    COND_PLUS=40
    COND_MINUS=41
    END_QUOTE_GT_COND=42
    COND_WS=43
    FUNCTION_NAME=44
    END_QUOTE_GT=45

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(DANKParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DANKParser.StatementContext)
            else:
                return self.getTypedRuleContext(DANKParser.StatementContext,i)


        def getRuleIndex(self):
            return DANKParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = DANKParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 555384832) != 0):
                self.state = 36
                self.statement()
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 42
            self.match(DANKParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def print_(self):
            return self.getTypedRuleContext(DANKParser.PrintContext,0)


        def fun_def(self):
            return self.getTypedRuleContext(DANKParser.Fun_defContext,0)


        def fun_call(self):
            return self.getTypedRuleContext(DANKParser.Fun_callContext,0)


        def loop(self):
            return self.getTypedRuleContext(DANKParser.LoopContext,0)


        def var_def(self):
            return self.getTypedRuleContext(DANKParser.Var_defContext,0)


        def conditional(self):
            return self.getTypedRuleContext(DANKParser.ConditionalContext,0)


        def breakpoint(self):
            return self.getTypedRuleContext(DANKParser.BreakpointContext,0)


        def getRuleIndex(self):
            return DANKParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = DANKParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.print_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.fun_def()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 46
                self.fun_call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 47
                self.loop()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 48
                self.var_def()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 49
                self.conditional()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 50
                self.breakpoint()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT_BEGIN(self):
            return self.getToken(DANKParser.PRINT_BEGIN, 0)

        def PRINT_END(self):
            return self.getToken(DANKParser.PRINT_END, 0)

        def expression(self):
            return self.getTypedRuleContext(DANKParser.ExpressionContext,0)


        def getRuleIndex(self):
            return DANKParser.RULE_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)




    def print_(self):

        localctx = DANKParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_print)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(DANKParser.PRINT_BEGIN)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 3312359315968) != 0):
                self.state = 54
                self.expression()


            self.state = 57
            self.match(DANKParser.PRINT_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(DANKParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(DANKParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(DANKParser.RPAREN, 0)

        def operand(self):
            return self.getTypedRuleContext(DANKParser.OperandContext,0)


        def PLUS(self):
            return self.getToken(DANKParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(DANKParser.MINUS, 0)

        def COND_PLUS(self):
            return self.getToken(DANKParser.COND_PLUS, 0)

        def COND_MINUS(self):
            return self.getToken(DANKParser.COND_MINUS, 0)

        def getRuleIndex(self):
            return DANKParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = DANKParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.match(DANKParser.LPAREN)
                self.state = 60
                self.expression()
                self.state = 61
                self.match(DANKParser.RPAREN)
                pass
            elif token in [11, 12, 27, 28, 29, 32, 33, 40, 41]:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 3298534889472) != 0):
                    self.state = 63
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3298534889472) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 66
                self.operand()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DANKParser.FactorContext)
            else:
                return self.getTypedRuleContext(DANKParser.FactorContext,i)


        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(DANKParser.MULT)
            else:
                return self.getToken(DANKParser.MULT, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(DANKParser.DIV)
            else:
                return self.getToken(DANKParser.DIV, i)

        def getRuleIndex(self):
            return DANKParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = DANKParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.factor()
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13 or _la==14:
                self.state = 70
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 71
                self.factor()
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DANKParser.TermContext)
            else:
                return self.getTypedRuleContext(DANKParser.TermContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(DANKParser.PLUS)
            else:
                return self.getToken(DANKParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(DANKParser.MINUS)
            else:
                return self.getToken(DANKParser.MINUS, i)

        def getRuleIndex(self):
            return DANKParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = DANKParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.term()
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11 or _la==12:
                self.state = 78
                _la = self._input.LA(1)
                if not(_la==11 or _la==12):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 79
                self.term()
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOOP_BEGIN(self):
            return self.getToken(DANKParser.LOOP_BEGIN, 0)

        def LOOP_END(self):
            return self.getToken(DANKParser.LOOP_END, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DANKParser.StatementContext)
            else:
                return self.getTypedRuleContext(DANKParser.StatementContext,i)


        def getRuleIndex(self):
            return DANKParser.RULE_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop" ):
                listener.enterLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop" ):
                listener.exitLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop" ):
                return visitor.visitLoop(self)
            else:
                return visitor.visitChildren(self)




    def loop(self):

        localctx = DANKParser.LoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(DANKParser.LOOP_BEGIN)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 555384832) != 0):
                self.state = 86
                self.statement()
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 92
            self.match(DANKParser.LOOP_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DANKParser.ID, 0)

        def EQ(self):
            return self.getToken(DANKParser.EQ, 0)

        def expression(self):
            return self.getTypedRuleContext(DANKParser.ExpressionContext,0)


        def getRuleIndex(self):
            return DANKParser.RULE_var_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_def" ):
                listener.enterVar_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_def" ):
                listener.exitVar_def(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_def" ):
                return visitor.visitVar_def(self)
            else:
                return visitor.visitChildren(self)




    def var_def(self):

        localctx = DANKParser.Var_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_var_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(DANKParser.ID)
            self.state = 95
            self.match(DANKParser.EQ)
            self.state = 96
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(DANKParser.STRING, 0)

        def ID(self):
            return self.getToken(DANKParser.ID, 0)

        def NUMBER(self):
            return self.getToken(DANKParser.NUMBER, 0)

        def COND_ID(self):
            return self.getToken(DANKParser.COND_ID, 0)

        def COND_NUMBER(self):
            return self.getToken(DANKParser.COND_NUMBER, 0)

        def getRuleIndex(self):
            return DANKParser.RULE_operand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperand" ):
                listener.enterOperand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperand" ):
                listener.exitOperand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = DANKParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_operand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 13824425984) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DANKParser.FactorContext)
            else:
                return self.getTypedRuleContext(DANKParser.FactorContext,i)


        def COND_EQ(self):
            return self.getToken(DANKParser.COND_EQ, 0)

        def COND_LT(self):
            return self.getToken(DANKParser.COND_LT, 0)

        def COND_GT(self):
            return self.getToken(DANKParser.COND_GT, 0)

        def COND_LTE(self):
            return self.getToken(DANKParser.COND_LTE, 0)

        def COND_GTE(self):
            return self.getToken(DANKParser.COND_GTE, 0)

        def COND_NEQ(self):
            return self.getToken(DANKParser.COND_NEQ, 0)

        def getRuleIndex(self):
            return DANKParser.RULE_logical_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogical_expression" ):
                listener.enterLogical_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogical_expression" ):
                listener.exitLogical_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_expression" ):
                return visitor.visitLogical_expression(self)
            else:
                return visitor.visitChildren(self)




    def logical_expression(self):

        localctx = DANKParser.Logical_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_logical_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.factor()
            self.state = 101
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1082331758592) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 102
            self.factor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONDITIONAL_BEGIN(self):
            return self.getToken(DANKParser.CONDITIONAL_BEGIN, 0)

        def logical_expression(self):
            return self.getTypedRuleContext(DANKParser.Logical_expressionContext,0)


        def END_QUOTE_GT_COND(self):
            return self.getToken(DANKParser.END_QUOTE_GT_COND, 0)

        def CONDITIONAL_END(self):
            return self.getToken(DANKParser.CONDITIONAL_END, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DANKParser.StatementContext)
            else:
                return self.getTypedRuleContext(DANKParser.StatementContext,i)


        def getRuleIndex(self):
            return DANKParser.RULE_conditional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional" ):
                listener.enterConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional" ):
                listener.exitConditional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional" ):
                return visitor.visitConditional(self)
            else:
                return visitor.visitChildren(self)




    def conditional(self):

        localctx = DANKParser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(DANKParser.CONDITIONAL_BEGIN)
            self.state = 105
            self.logical_expression()
            self.state = 106
            self.match(DANKParser.END_QUOTE_GT_COND)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 555384832) != 0):
                self.state = 107
                self.statement()
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 113
            self.match(DANKParser.CONDITIONAL_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakpointContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAKPOINT(self):
            return self.getToken(DANKParser.BREAKPOINT, 0)

        def getRuleIndex(self):
            return DANKParser.RULE_breakpoint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakpoint" ):
                listener.enterBreakpoint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakpoint" ):
                listener.exitBreakpoint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakpoint" ):
                return visitor.visitBreakpoint(self)
            else:
                return visitor.visitChildren(self)




    def breakpoint(self):

        localctx = DANKParser.BreakpointContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_breakpoint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(DANKParser.BREAKPOINT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def params_2(self):
            return self.getTypedRuleContext(DANKParser.Params_2Context,0)


        def COMMA(self):
            return self.getToken(DANKParser.COMMA, 0)

        def factor(self):
            return self.getTypedRuleContext(DANKParser.FactorContext,0)


        def getRuleIndex(self):
            return DANKParser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = DANKParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_params)
        try:
            self.state = 122
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.params_2(0)
                self.state = 118
                self.match(DANKParser.COMMA)
                self.state = 119
                self.factor()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.factor()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Params_2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(DANKParser.FactorContext,0)


        def params_2(self):
            return self.getTypedRuleContext(DANKParser.Params_2Context,0)


        def COMMA(self):
            return self.getToken(DANKParser.COMMA, 0)

        def getRuleIndex(self):
            return DANKParser.RULE_params_2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams_2" ):
                listener.enterParams_2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams_2" ):
                listener.exitParams_2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams_2" ):
                return visitor.visitParams_2(self)
            else:
                return visitor.visitChildren(self)



    def params_2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = DANKParser.Params_2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_params_2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 132
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = DANKParser.Params_2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_params_2)
                    self.state = 127
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 128
                    self.match(DANKParser.COMMA)
                    self.state = 129
                    self.factor() 
                self.state = 134
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Fun_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION_BEGIN(self):
            return self.getToken(DANKParser.FUNCTION_BEGIN, 0)

        def FUNCTION_NAME(self):
            return self.getToken(DANKParser.FUNCTION_NAME, 0)

        def END_QUOTE_GT(self):
            return self.getToken(DANKParser.END_QUOTE_GT, 0)

        def PARAMS_BEGIN(self):
            return self.getToken(DANKParser.PARAMS_BEGIN, 0)

        def PARAMS_END(self):
            return self.getToken(DANKParser.PARAMS_END, 0)

        def FUNCTION_END(self):
            return self.getToken(DANKParser.FUNCTION_END, 0)

        def ids(self):
            return self.getTypedRuleContext(DANKParser.IdsContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DANKParser.StatementContext)
            else:
                return self.getTypedRuleContext(DANKParser.StatementContext,i)


        def getRuleIndex(self):
            return DANKParser.RULE_fun_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFun_def" ):
                listener.enterFun_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFun_def" ):
                listener.exitFun_def(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFun_def" ):
                return visitor.visitFun_def(self)
            else:
                return visitor.visitChildren(self)




    def fun_def(self):

        localctx = DANKParser.Fun_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_fun_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(DANKParser.FUNCTION_BEGIN)
            self.state = 136
            self.match(DANKParser.FUNCTION_NAME)
            self.state = 137
            self.match(DANKParser.END_QUOTE_GT)
            self.state = 138
            self.match(DANKParser.PARAMS_BEGIN)
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 139
                self.ids()


            self.state = 142
            self.match(DANKParser.PARAMS_END)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 555384832) != 0):
                self.state = 143
                self.statement()
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 149
            self.match(DANKParser.FUNCTION_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ids_2(self):
            return self.getTypedRuleContext(DANKParser.Ids_2Context,0)


        def COMMA(self):
            return self.getToken(DANKParser.COMMA, 0)

        def ID(self):
            return self.getToken(DANKParser.ID, 0)

        def getRuleIndex(self):
            return DANKParser.RULE_ids

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIds" ):
                listener.enterIds(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIds" ):
                listener.exitIds(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIds" ):
                return visitor.visitIds(self)
            else:
                return visitor.visitChildren(self)




    def ids(self):

        localctx = DANKParser.IdsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_ids)
        try:
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.ids_2(0)
                self.state = 152
                self.match(DANKParser.COMMA)
                self.state = 153
                self.match(DANKParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.match(DANKParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ids_2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DANKParser.ID, 0)

        def ids_2(self):
            return self.getTypedRuleContext(DANKParser.Ids_2Context,0)


        def COMMA(self):
            return self.getToken(DANKParser.COMMA, 0)

        def getRuleIndex(self):
            return DANKParser.RULE_ids_2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIds_2" ):
                listener.enterIds_2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIds_2" ):
                listener.exitIds_2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIds_2" ):
                return visitor.visitIds_2(self)
            else:
                return visitor.visitChildren(self)



    def ids_2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = DANKParser.Ids_2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_ids_2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(DANKParser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 166
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = DANKParser.Ids_2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_ids_2)
                    self.state = 161
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 162
                    self.match(DANKParser.COMMA)
                    self.state = 163
                    self.match(DANKParser.ID) 
                self.state = 168
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Fun_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DANKParser.ID, 0)

        def LPAREN(self):
            return self.getToken(DANKParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(DANKParser.RPAREN, 0)

        def params(self):
            return self.getTypedRuleContext(DANKParser.ParamsContext,0)


        def getRuleIndex(self):
            return DANKParser.RULE_fun_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFun_call" ):
                listener.enterFun_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFun_call" ):
                listener.exitFun_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFun_call" ):
                return visitor.visitFun_call(self)
            else:
                return visitor.visitChildren(self)




    def fun_call(self):

        localctx = DANKParser.Fun_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_fun_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(DANKParser.ID)
            self.state = 170
            self.match(DANKParser.LPAREN)
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 3312359315968) != 0):
                self.state = 171
                self.params()


            self.state = 174
            self.match(DANKParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[13] = self.params_2_sempred
        self._predicates[16] = self.ids_2_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def params_2_sempred(self, localctx:Params_2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def ids_2_sempred(self, localctx:Ids_2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




