expressao = "((a+b) * (c-d))"
pilha = []
valida = True
for caractere in expressao:
    if caractere == "(":
        pilha.append(caractere)
    elif caractere == ")":
        if not pilha:
            valida = False
            break
        pilha.pop()
print("Válida?", valida and not pilha)
