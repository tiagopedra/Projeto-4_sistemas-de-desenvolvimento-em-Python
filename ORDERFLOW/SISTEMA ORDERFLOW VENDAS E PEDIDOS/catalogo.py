CATEGORIAS = {
    "1": ("Camisas", "👕"),
    "2": ("Calças", "👖"),
    "3": ("Calçados", "👟"),
    "4": ("Casacos", "🧥")
}

def mostrar_categorias():
    print("\n==============================")
    print("🛍️  CATEGORIAS DISPONÍVEIS")
    print("==============================")
    print("1 - 👕 Camisas")
    print("2 - 👖 Calças")
    print("3 - 👟 Calçados")
    print("4 - 🧥 Casacos")

def categoria_por_opcao(op):
    if op in CATEGORIAS:
        return CATEGORIAS[op][0]
    return None

def _montar_produtos(grupos, categoria, preco_inicial, passo):
    produtos=[]
    preco=preco_inicial

    for nome, variantes in grupos:
        for variante in variantes:
            produtos.append((f"{nome} {variante}", categoria, round(preco,2)))
            preco+=passo

    return produtos

def gerar_produtos_iniciais():
    camisas=[
        ("Camisa social",["preta","branca"]),
        ("Camisa manga longa",["azul","cinza"]),
        ("Camisa polo",["verde","marinho"]),
        ("Camisa xadrez",["vermelha","preta"]),
        ("Camisa casual",["bege","caqui"]),
        ("Camiseta estampada",["rock","anime"]),
        ("Camiseta florida",["rosa","amarela"]),
        ("Camiseta havaiana",["azul","verde"]),
        ("Camiseta básica",["branca","preta"]),
        ("Camiseta oversized",["cinza","off white"]),
        ("Camisa streetwear",["laranja","roxa"]),
        ("Camisa de botão",["azul claro","preta"]),
        ("Camisa vintage",["marrom","verde musgo"])
    ]

    calcas=[
        ("Calça cargo",["preta","bege"]),
        ("Calça jeans",["azul","preta"]),
        ("Calça skinny",["clara","escura"]),
        ("Calça jogger",["cinza","preta"]),
        ("Calça moletom",["cinza","azul marinho"]),
        ("Calça reta",["azul","preta"]),
        ("Calça wide leg",["jeans","preta"]),
        ("Calça destroyed",["azul clara","cinza"]),
        ("Calça slim",["preta","azul"]),
        ("Calça streetwear",["grafite","verde"]),
        ("Calça casual",["caqui","bege"]),
        ("Calça alfaiataria",["preta","cinza"]),
        ("Calça utilitária",["marrom","verde"])
    ]

    calcados=[
        ("Tênis esportivo",["azul","preto"]),
        ("Tênis casual",["branco","cinza"]),
        ("Tênis corrida",["laranja","preto"]),
        ("Tênis skate",["preto","vermelho"]),
        ("Tênis retrô",["verde","branco"]),
        ("Tênis streetwear",["azul","cinza"]),
        ("Bota couro",["marrom","preta"]),
        ("Bota cano alto",["preta","marrom"]),
        ("Bota casual",["caramelo","preta"]),
        ("Coturno militar",["preto","verde"]),
        ("Coturno preto",["preto","grafite"]),
        ("Tênis premium",["branco","azul"]),
        ("Tênis academia",["cinza","preto"])
    ]

    casacos=[
        ("Casaco moletom",["preto","cinza"]),
        ("Casaco oversized",["bege","preto"]),
        ("Jaqueta jeans",["clara","escura"]),
        ("Jaqueta couro",["preta","marrom"]),
        ("Casaco corta vento",["azul","preto"]),
        ("Moletom estampado",["cinza","verde"]),
        ("Jaqueta bomber",["preta","verde"]),
        ("Casaco fleece",["marrom","azul"]),
        ("Jaqueta streetwear",["laranja","roxa"]),
        ("Casaco inverno",["cinza","preto"]),
        ("Moletom básico",["branco","preto"]),
        ("Jaqueta varsity",["azul","preta"]),
        ("Parka leve",["verde","caqui"])
    ]

    produtos=[]

    produtos.extend(_montar_produtos(camisas,"Camisas",49.90,4.0))
    produtos.extend(_montar_produtos(calcas,"Calças",89.90,5.0))
    produtos.extend(_montar_produtos(calcados,"Calçados",149.90,8.0))
    produtos.extend(_montar_produtos(casacos,"Casacos",129.90,6.0))

    return produtos