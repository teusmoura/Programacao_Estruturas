registros = [(1,"Informática",None),(2,"Periféricos",1),(12,"Acessórios",2),(9,"Serviços",None)]
ids_pais = {pai for _,_,pai in registros if pai is not None}
folhas = [(idc,nome) for idc,nome,_ in registros if idc not in ids_pais]
print(folhas)
