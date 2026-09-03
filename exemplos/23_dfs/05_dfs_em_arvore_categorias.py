filhos = {None:[1,9],1:[2,3,4,5,6,8],2:[12],9:[10,11]}

def dfs(no, nivel=0):
    for filho in filhos.get(no, []):
        print("  "*nivel, filho)
        dfs(filho, nivel+1)

dfs(None)
