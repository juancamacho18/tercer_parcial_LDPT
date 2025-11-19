def generar_gramatica_atributos_crud(spec):
    # spec puede incluir: tipos básicos, constructs CRUD admitidos
    G = AttributeGrammar()
    G.add_nonterminal("programa", inherited_attrs=["env"], synthesized_attrs=["ok","code"])
    G.add_nonterminal("creartabla", synthesized_attrs=["ok","schema","code"])
    G.add_nonterminal("columna", synthesized_attrs=["ok","col","type"])
    G.add_nonterminal("Insert", synthesized_attrs=["ok","code"])
    G.add_nonterminal("Select", synthesized_attrs=["ok","schema","code"])
    
    G.add_production("programa -> sentencias")
    G.add_production("sentencias -> sentencia sentencias | ε")
    G.add_production("sentencia-> creartabla| Insert | Select | Update | Delete")
    G.add_production("creartabla -> 'CREATE' 'TABLE' ID '(' ColumnList ')' ';'")
    G.add_production("columna-> columna (',' columna)*")
    G.add_production("columna-> ID TYPE")
    G.add_production("Insert -> 'INSERT' 'INTO' ID '(' IDList ')' 'VALUES' '(' ExprList ')' ';'")
    
    G.add_semantic_rule("CreateTable", """
        creartabla.ok = not env.exists_table(ID)
        if creartabla.ok:
            creartabla.schema={col.name: col.type for col in ColumnList}
            env.add_table(ID, creartabla.schema)
            creartabla.code=("CREATE_TABLE", ID, creartabla.schema)
        else:
            creartabla.code= ("ERROR","table exists")
    """)
    return G
