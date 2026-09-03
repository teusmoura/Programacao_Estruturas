status = ["PENDENTE", "PAGO", "SEPARACAO", "ENVIADO"]
status.remove("PAGO")
retirado = status.pop()
print("Retirado pelo pop:", retirado)
print(status)
status.clear()
print(status)
