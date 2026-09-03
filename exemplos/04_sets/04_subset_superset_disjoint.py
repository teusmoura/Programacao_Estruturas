essenciais = {"usb", "essencial"}
mouse = {"usb", "escritorio", "essencial"}
energia = {"energia"}
print(essenciais.issubset(mouse))
print(mouse.issuperset(essenciais))
print(mouse.isdisjoint(energia))
