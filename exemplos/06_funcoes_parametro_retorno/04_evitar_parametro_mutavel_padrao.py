def registrar(nome, observacoes=None):
    if observacoes is None:
        observacoes = []
    observacoes.append(f"Cliente: {nome}")
    return observacoes

print(registrar("Ana"))
print(registrar("Bruno"))
