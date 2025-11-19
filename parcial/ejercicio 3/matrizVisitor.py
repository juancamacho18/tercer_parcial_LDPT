# Generated from matriz.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .matrizParser import matrizParser
else:
    from matrizParser import matrizParser

# This class defines a complete generic visitor for a parse tree produced by matrizParser.

class matrizVisitor(ParseTreeVisitor):
    def __init__(self):
            self.codigo=[]     # código Python resultante
            self.tabla={}       # diccionario opcional para almacenar matrices/valores


    def visitPrograma(self, ctx:matrizParser.ProgramaContext):
        for st in ctx.sentencia():
            self.visit(st)
        return "\n".join(self.codigo)

    def visitSentencia(self, ctx:matrizParser.SentenciaContext):
        return self.visitChildren(ctx)

    def visitAssignar(self, ctx:matrizParser.AssignarContext):
        nombre = ctx.ID().getText()
        valor = self.visit(ctx.expr())

        if valor.startswith("["):
            self.tabla[nombre] = "matriz"
        elif valor.isdigit() or (valor[0] == "-" and valor[1:].isdigit()):
            self.tabla[nombre] = "numero"

        self.codigo.append(f"{nombre} = {valor}")
        return valor

    def visitImprimir(self, ctx:matrizParser.ImprimirContext):
        nombre = ctx.ID().getText()

        if nombre in self.tabla and self.tabla[nombre] == "matriz":
            self.codigo.append(f"matriz.mostrar_matriz({nombre})")
        else:
            self.codigo.append(f"print({nombre})")

        return None

    def visitExpr(self, ctx:matrizParser.ExprContext):
        puntos = ctx.punto()

        if len(puntos) == 1:
            return self.visit(puntos[0])

        izquierda = self.visit(puntos[0])

        for i in range(1, len(puntos)):
            derecha = self.visit(puntos[i])

            tipo_i = self._inferir_tipo(izquierda)
            tipo_d = self._inferir_tipo(derecha)

            if tipo_i == "matriz" and tipo_d == "matriz":
                izquierda = f"matriz.multiplicar_matrices({izquierda}, {derecha})"

            elif tipo_i == "matriz" and tipo_d == "numero":
                izquierda = f"matriz.multiplicar_escalar({izquierda}, {derecha})"

            elif tipo_i == "numero" and tipo_d == "matriz":
                izquierda = f"matriz.multiplicar_escalar({derecha}, {izquierda})"

            else:
                raise ValueError("No se puede multiplicar: tipos incompatibles")

        return izquierda

    def visitPunto(self, ctx:matrizParser.PuntoContext):
        if ctx.ID():
            return ctx.ID().getText()
        if ctx.matriz():
            return self.visit(ctx.matriz())
        return f"({self.visit(ctx.expr())})"

    def visitMatriz(self, ctx:matrizParser.MatrizContext):
        return "[" + self.visit(ctx.filas()) + "]"

    def visitFilas(self, ctx:matrizParser.FilasContext):
        return ",".join(self.visit(f) for f in ctx.fila())

    def visitFila(self, ctx:matrizParser.FilaContext):
        return "[" + self.visit(ctx.numeros()) + "]"

    def visitNumeros(self, ctx:matrizParser.NumerosContext):
        nums = [ n.getText() for n in ctx.NUMERO() ]
        return ",".join(nums)

    def _inferir_tipo(self, valor):
        if valor.startswith("["):
            return "matriz"

        if valor.replace("-", "").isdigit():
            return "numero"

        if valor in self.tabla:
            return self.tabla[valor]

        return "desconocido"