from asyncore import write


inf = 0
while (inf < 5):
    from datetime import datetime
    now = datetime.now()
    
    a = now.year #ano
    m = now.month #mês
    d = now.day #dia
    h = now.hour #hora
    mi = now.minute #minuto
    s = now.second #segundo
    
    print("Olá, seja bem vindo!")
    print("Informações abaixo: ")
    print("\n(1) Cirugia")
    print("\n(2) Exame")
    print("\n(3) Consulta")
    print("\n(4) Pós Cirugia")
    print("\n(5) Sair")
    inf      = int(input("\nQual opção deseja:"))
    inf = inf + 0
    
    if inf == 1:
        inf1 = str(input("\nNome: "))
        inf2 = str(input("\nData de nascimento: "))
        inf3 = str(input("\nTelefone: "))
        inf4 = str(input("\nSexo: "))
        inf5 = str(input("\nEndereço: "))
        inf6 = str(input("\nCPF: "))
        inf7 = str(input("\nData do procedimento: "))
        inf8 = str(input("\nHora do procedimento: "))
        
        data = print("\n{}/{}/{}".format(d,m,a)) 
        dia = inf7 - data
        print("\nfalta apenas {dia} dias para realizar o procedimento")
        
        
        arquivo = open('Cirurgia.txt','a')
        arquivo.write(
            "\nNOME: {}\nDATA DE NASCIMENTO: {}\nTELEFONE: {}".format(inf1,inf2,inf3))
        arquivo.write(
            "\nSEXO: {}\nENDEREÇO: {}\nCPF: {}".format(inf4,inf5,inf6))
        arquivo.write(
            "\nDATA DO PROCEDIMENTO: {}\nHORA DO PROCEDIMENTO: {}".format(inf7,inf8))
        arquivo.write("\n                  {}/{}/{}".format(d,m,a))
        arquivo.close()
    
    elif inf == 2:
        inf1 = str(input("\nNome: "))
        inf2 = str(input("\nData de nascimento: "))
        inf3 = str(input("\nTelefone: "))
        inf4 = str(input("\nSexo: "))
        inf5 = str(input("\nEndereço: "))
        inf6 = str(input("\nCPF: "))
        inf7 = str(input("\nData do procedimento: "))
        inf8 = str(input("\nHora do procedimento: "))
        
        data = print("\n{}/{}/{}".format(d,m,a)) 
        dia = inf7 - data
        print("\nfalta apenas {dia} dias para realizar o procedimento")

        arquivo = open('Exame.txt','a')
        arquivo.write(
            "\nNOME: {}\nDATA DE NASCIMENTO: {}\nTELEFONE: {}".format(inf1,inf2,inf3))
        arquivo.write(
            "\nSEXO: {}\nENDEREÇO: {}\nCPF: {}".format(inf4,inf5,inf6))
        arquivo.write(
            "\nDATA DO PROCEDIMENTO: {}\nHORA DO PROCEDIMENTO: {}".format(inf7,inf8))
        arquivo.write("\n                  {}/{}/{}".format(d,m,a))
        arquivo.close()
    
    elif inf == 3:
        inf1 = str(input("\nNome: "))
        inf2 = str(input("\nData de nascimento: "))
        inf3 = str(input("\nTelefone: "))
        inf4 = str(input("\nSexo: "))
        inf5 = str(input("\nEndereço: "))
        inf6 = str(input("\nCPF: "))
        inf7 = str(input("\nData do procedimento: "))
        inf8 = str(input("\nHora do procedimento: "))
        
        data = print("\n{}/{}/{}".format(d,m,a)) 
        dia = inf7 - data
        print("\nfalta apenas {dia} dias para realizar o procedimento")

        arquivo = open('Consulta.txt','a')
        arquivo.write(
            "\nNOME: {}\nDATA DE NASCIMENTO: {}\nTELEFONE: {}".format(inf1,inf2,inf3))
        arquivo.write(
            "\nSEXO: {}\nENDEREÇO: {}\nCPF: {}".format(inf4,inf5,inf6))
        arquivo.write(
            "\nDATA DO PROCEDIMENTO: {}\nHORA DO PROCEDIMENTO: {}".format(inf7,inf8))
        arquivo.write("\n                  {}/{}/{}".format(d,m,a))
        arquivo.close()

    elif inf == 4:
        inf1 = str(input("\nNome: "))
        inf2 = str(input("\nData de nascimento: "))
        inf3 = str(input("\nTelefone: "))
        inf4 = str(input("\nSexo: "))
        inf5 = str(input("\nEndereço: "))
        inf6 = str(input("\nCPF: "))
        inf7 = str(input("\nData do procedimento: "))
        inf8 = str(input("\nHora do procedimento: "))
        
        data = print("\n{}/{}/{}".format(d,m,a)) 
        dia = inf7 - data
        print("\nfalta apenas {dia} dias para realizar o procedimento")

        arquivo = open('Pós_Cirurgia.txt','a')
        arquivo.write(
            "\nNOME: {}\nDATA DE NASCIMENTO: {}\nTELEFONE: {}".format(inf1,inf2,inf3))
        arquivo.write(
            "\nSEXO: {}\nENDEREÇO: {}\nCPF: {}".format(inf4,inf5,inf6))
        arquivo.write(
            "\nDATA DO PROCEDIMENTO: {}\nHORA DO PROCEDIMENTO: {}".format(inf7,inf8))
        arquivo.write("\n                  {}/{}/{}".format(d,m,a))
        arquivo.close()

else:
    print("\nPrograma encerrado com sucesso!")

arquivo.write(caixa_editavel_1.get())