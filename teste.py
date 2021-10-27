name = "1;5;VFFVV"
questao = name.split(";")
alternativa = questao[2]
certo = 0
errado = 0

for x in alternativa:
    if(x == "V"):
        certo = certo + 1
    else:
        errado = errado + 1    

print('questão: ', questao[2], "Certos: ", certo, " // Errados: ", errado)