# Tercer Parcial
---------------------------
# Primer punto

El archivo funcion.py contiene una funcion que construye una gramatica de atributos para un lenguaje CRUD simplificado:

-programa

-creartabla

-columna

-Insert

-Select

esta función construye no terminales con atributos heredados y sintetizados declarado de esta manera
funcion

    G.add_nonterminal("programa", inherited_attrs=["env"], synthesized_attrs=["ok","code"])
    G.add_nonterminal("creartabla", synthesized_attrs=["ok","schema","code"])

las producciones del lenguaje CRUD

    G.add_production("programa -> sentencias")
    G.add_production("sentencias -> sentencia sentencias | ε")
    G.add_production("creartabla -> 'CREATE' 'TABLE' ID '(' ColumnList ')' ';'")

Estas reglas verifican consistencia semántica como:

-existencia de tablas

-duplicacion

-esquemas validos

---------------------------
# Segundo punto
La gramatica para calcular el valor punto de dos matrices de dimensiones diferentes:

    programa -> sentencias
    
    sentencias -> sentencia sentencias
    sentencias -> ε
    
    sentencia -> asignar ';'
    sentencia -> imprimir ';'
    
    asignar -> ID '=' expr
    
    imprimir -> 'print' ID
    
    expr -> expr_mul
    
    expr_mul -> expr_mul '*' expr_atom
    expr_mul -> expr_atom
    
    expr_punto -> matriz
    expr_punto -> ID
    expr_punto -> '(' expr ')'
    
    matriz -> '[' filas ']'
    
    filas -> fila
    filas -> fila ',' filas
    
    fila -> '[' numeros ']'
    
    numeros -> numero
    numeros -> numero ',' numeros
    
    numero -> ENTERO 
    numero -> REAL
    
Ejemplo de definicion de matrices y de uso

    A=[[1,2], [3,4], [7,2]]
    B=[[3,2], [1,7], [8,3]]
    
    C= A * B

---------------------------
# Tercer punto

la implementación del punto 2 usando ANTLR4

contiene:

-tokens

-reglas lexicas

-reglas sintacticas 

Estructura del ejercicio:
ejercicio3/
│── funcion.py                 
│── gramatica.txt             
│── matriz.g4                  
│── matrizVisitor.py           
│── matrizParser.py          
│── matrizLexer.py             
│── matriz.py                 
│── main.py                    
│── matrices.txt

este ejercicio ademas utiliza una libreria de calculo de multiplicacion de matrices 'matriz.py' para poder utilizar como funciones dentro del programa principal.

Lo que este ejercicio busca es implementar la gramatica.g4 adaptada para usarse en el ANTLR4 para lenguaje objetivo python

para ejecutar dependiendo que python usas puede ser

>python main.py

o

>python3 main.py

el archivo main ya contiene el archivo de "matrices.txt" que es donde se hacen las pruebas para las matrices, ahi se puede editar y probar para mirar el resultado del calculo (tener en cuenta siempre la estructura para trabajar, siempre se asigna un ID para una matriz).
Ejemplo de salida:

        Código generado:
        
        A=[[1,2],[3,4]]
        
        B=[[5,6],[7,8]]
        
        C=A*B
        
        print(C)
        
        
        Salida del programa:
        [[19, 22], [43, 50]]




