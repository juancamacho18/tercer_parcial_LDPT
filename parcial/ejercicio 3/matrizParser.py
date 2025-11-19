# Generated from matriz.g4 by ANTLR 4.13.1
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
        4,1,12,84,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,5,0,22,8,0,10,0,12,0,25,9,0,1,0,1,
        0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,35,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,
        1,4,1,4,1,4,5,4,47,8,4,10,4,12,4,50,9,4,1,5,1,5,1,5,1,5,1,5,1,5,
        3,5,58,8,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,5,7,67,8,7,10,7,12,7,70,9,
        7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,5,9,79,8,9,10,9,12,9,82,9,9,1,9,0,
        0,10,0,2,4,6,8,10,12,14,16,18,0,0,80,0,23,1,0,0,0,2,34,1,0,0,0,4,
        36,1,0,0,0,6,40,1,0,0,0,8,43,1,0,0,0,10,57,1,0,0,0,12,59,1,0,0,0,
        14,63,1,0,0,0,16,71,1,0,0,0,18,75,1,0,0,0,20,22,3,2,1,0,21,20,1,
        0,0,0,22,25,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,26,1,0,0,0,25,
        23,1,0,0,0,26,27,5,0,0,1,27,1,1,0,0,0,28,29,3,4,2,0,29,30,5,1,0,
        0,30,35,1,0,0,0,31,32,3,6,3,0,32,33,5,1,0,0,33,35,1,0,0,0,34,28,
        1,0,0,0,34,31,1,0,0,0,35,3,1,0,0,0,36,37,5,10,0,0,37,38,5,2,0,0,
        38,39,3,8,4,0,39,5,1,0,0,0,40,41,5,3,0,0,41,42,5,10,0,0,42,7,1,0,
        0,0,43,48,3,10,5,0,44,45,5,4,0,0,45,47,3,10,5,0,46,44,1,0,0,0,47,
        50,1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,9,1,0,0,0,50,48,1,0,0,
        0,51,58,3,12,6,0,52,58,5,10,0,0,53,54,5,5,0,0,54,55,3,8,4,0,55,56,
        5,6,0,0,56,58,1,0,0,0,57,51,1,0,0,0,57,52,1,0,0,0,57,53,1,0,0,0,
        58,11,1,0,0,0,59,60,5,7,0,0,60,61,3,14,7,0,61,62,5,8,0,0,62,13,1,
        0,0,0,63,68,3,16,8,0,64,65,5,9,0,0,65,67,3,16,8,0,66,64,1,0,0,0,
        67,70,1,0,0,0,68,66,1,0,0,0,68,69,1,0,0,0,69,15,1,0,0,0,70,68,1,
        0,0,0,71,72,5,7,0,0,72,73,3,18,9,0,73,74,5,8,0,0,74,17,1,0,0,0,75,
        80,5,11,0,0,76,77,5,9,0,0,77,79,5,11,0,0,78,76,1,0,0,0,79,82,1,0,
        0,0,80,78,1,0,0,0,80,81,1,0,0,0,81,19,1,0,0,0,82,80,1,0,0,0,6,23,
        34,48,57,68,80
    ]

class matrizParser ( Parser ):

    grammarFileName = "matriz.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'='", "'print'", "'*'", "'('", 
                     "')'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "NUMERO", "WS" ]

    RULE_programa = 0
    RULE_sentencia = 1
    RULE_assignar = 2
    RULE_imprimir = 3
    RULE_expr = 4
    RULE_punto = 5
    RULE_matriz = 6
    RULE_filas = 7
    RULE_fila = 8
    RULE_numeros = 9

    ruleNames =  [ "programa", "sentencia", "assignar", "imprimir", "expr", 
                   "punto", "matriz", "filas", "fila", "numeros" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    ID=10
    NUMERO=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(matrizParser.EOF, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(matrizParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(matrizParser.SentenciaContext,i)


        def getRuleIndex(self):
            return matrizParser.RULE_programa

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = matrizParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3 or _la==10:
                self.state = 20
                self.sentencia()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
            self.match(matrizParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignar(self):
            return self.getTypedRuleContext(matrizParser.AssignarContext,0)


        def imprimir(self):
            return self.getTypedRuleContext(matrizParser.ImprimirContext,0)


        def getRuleIndex(self):
            return matrizParser.RULE_sentencia

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia" ):
                return visitor.visitSentencia(self)
            else:
                return visitor.visitChildren(self)




    def sentencia(self):

        localctx = matrizParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentencia)
        try:
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.assignar()
                self.state = 29
                self.match(matrizParser.T__0)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.imprimir()
                self.state = 32
                self.match(matrizParser.T__0)
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


    class AssignarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(matrizParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(matrizParser.ExprContext,0)


        def getRuleIndex(self):
            return matrizParser.RULE_assignar

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignar" ):
                return visitor.visitAssignar(self)
            else:
                return visitor.visitChildren(self)




    def assignar(self):

        localctx = matrizParser.AssignarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(matrizParser.ID)
            self.state = 37
            self.match(matrizParser.T__1)
            self.state = 38
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImprimirContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(matrizParser.ID, 0)

        def getRuleIndex(self):
            return matrizParser.RULE_imprimir

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImprimir" ):
                return visitor.visitImprimir(self)
            else:
                return visitor.visitChildren(self)




    def imprimir(self):

        localctx = matrizParser.ImprimirContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_imprimir)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(matrizParser.T__2)
            self.state = 41
            self.match(matrizParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def punto(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(matrizParser.PuntoContext)
            else:
                return self.getTypedRuleContext(matrizParser.PuntoContext,i)


        def getRuleIndex(self):
            return matrizParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = matrizParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.punto()
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 44
                self.match(matrizParser.T__3)
                self.state = 45
                self.punto()
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PuntoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def matriz(self):
            return self.getTypedRuleContext(matrizParser.MatrizContext,0)


        def ID(self):
            return self.getToken(matrizParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(matrizParser.ExprContext,0)


        def getRuleIndex(self):
            return matrizParser.RULE_punto

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPunto" ):
                return visitor.visitPunto(self)
            else:
                return visitor.visitChildren(self)




    def punto(self):

        localctx = matrizParser.PuntoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_punto)
        try:
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.matriz()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.match(matrizParser.ID)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 53
                self.match(matrizParser.T__4)
                self.state = 54
                self.expr()
                self.state = 55
                self.match(matrizParser.T__5)
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


    class MatrizContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def filas(self):
            return self.getTypedRuleContext(matrizParser.FilasContext,0)


        def getRuleIndex(self):
            return matrizParser.RULE_matriz

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatriz" ):
                return visitor.visitMatriz(self)
            else:
                return visitor.visitChildren(self)




    def matriz(self):

        localctx = matrizParser.MatrizContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_matriz)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(matrizParser.T__6)
            self.state = 60
            self.filas()
            self.state = 61
            self.match(matrizParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fila(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(matrizParser.FilaContext)
            else:
                return self.getTypedRuleContext(matrizParser.FilaContext,i)


        def getRuleIndex(self):
            return matrizParser.RULE_filas

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilas" ):
                return visitor.visitFilas(self)
            else:
                return visitor.visitChildren(self)




    def filas(self):

        localctx = matrizParser.FilasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_filas)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.fila()
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 64
                self.match(matrizParser.T__8)
                self.state = 65
                self.fila()
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numeros(self):
            return self.getTypedRuleContext(matrizParser.NumerosContext,0)


        def getRuleIndex(self):
            return matrizParser.RULE_fila

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFila" ):
                return visitor.visitFila(self)
            else:
                return visitor.visitChildren(self)




    def fila(self):

        localctx = matrizParser.FilaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_fila)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(matrizParser.T__6)
            self.state = 72
            self.numeros()
            self.state = 73
            self.match(matrizParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumerosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERO(self, i:int=None):
            if i is None:
                return self.getTokens(matrizParser.NUMERO)
            else:
                return self.getToken(matrizParser.NUMERO, i)

        def getRuleIndex(self):
            return matrizParser.RULE_numeros

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumeros" ):
                return visitor.visitNumeros(self)
            else:
                return visitor.visitChildren(self)




    def numeros(self):

        localctx = matrizParser.NumerosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_numeros)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(matrizParser.NUMERO)
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 76
                self.match(matrizParser.T__8)
                self.state = 77
                self.match(matrizParser.NUMERO)
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





