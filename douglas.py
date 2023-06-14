def menu():
    print("Bem vindo")
    print("Escolha uma opção")
    print("[1] Cadastrar um usuario")
    print("[2] Fazer Login")
    print("[Qualquer outra tecla.] Sair do aplicativo")
    opcoes = int(input("Opção selecionada: "))
    return(opcoes)

def menu2():
    print("Bem vindo")
    print("Escolha uma opção")
    print("[1] Escolher uma quadra")
    print("[2] Enviar um feedback")
    print("[Qualquer outra tecla.] Sair do aplicativo")
    opcoes2 = int(input("Opção selecionada: "))
    return(opcoes2)

def menuadmin():
    print("Bem vindo")
    print("Voce logou como administrador")
    print("Escolha uma opção")
    print("[1] Adicionar uma quadra")
    print("[2] Remover uma quadra")
    print("[Qualquer outra tecla.] Sair do aplicativo")
    opcoes3 = int(input("Opção selecionada: "))
    return(opcoes3)

def addquadra():
    quadra1 = []
    quadra2 = []
    quadra3 = []
    quadra = input("Digite o numero da quadra que voce gostaria de agendar um horario e dia: ")
    if quadra == 1:
        add1 = input('Adicione um horario em quadra 1')
        quadra1.append(add1)
    elif quadra == 2:
        add2 = input('Adicione um horario em quadra 2')
        quadra2.append(add2)
    elif quadra == 3:
        add3 = input('Adicione um horario em quadra 3')      
        quadra3.append(add3)
    else:
        print("Numero de quadra desconhecido")
    return()

def removerquadra():
    quadra = input("Digite o numero da quadra que voce gostaria de remover: ")    

def _login():
    login = input("usuario: ")
    senha = getpass(prompt='Senha: ')
    return(login, senha)

def b_usuario(Login, senha):
    usuario1 = []  
    try: 
        with open('usuarios.txt', 'r+',) as aqui:
            for line in aqui:
                line = line.strip(',')
                usuario1.append(line.split())
            for usuario1 in usuario1:
                nome = usuario1[0]
                password = usuario1[1]           
                if login == nome and password == senha:
                    return True
    except FileNotFoundError:
        return False
    
while(True):
    estrutura = menu()
    system('cls')
    if estrutura == 1:
        login, senha = _login()
        if login == senha:
            print("Seu login não pode ser igual a senha.") 
        user = b_usuario(login, senha)
        if user == True:
            print("O usuario já existe!!!!")
        else: 
            with open('usuarios.txt', 'a+',) as aqui:
                aqui.writelines(f'{login} {senha}\n')  
            print("Cadastro concluido")
            exit
    elif estrutura == 2:
        login, senha = _login()
        user = b_usuario(login, senha)
        if login == 'admin' and user == True:
            estrutura3 = menuadmin() 
            if estrutura3 == 1:
                adquadra =  addquadra()
                print (addquadra)
            elif estrutura3 == 2:
                remoquadra = removerquadra()
                print (remoquadra)
            else:
                system('cls')
                print (f"Voce saiu do menu ADMINISTRADOR")
        elif user == True:
            print("Login realizado com successo")
            estrutura2 = menu2()
            if estrutura2 == 1:
                horquadras = ['16:00', '16:30', '17:00', '17:30']
                print("Quadras disponiveis:")
                print("[1] Quadra 1")
                print("[2] Quadra 2")
                print("[3] Quadra 3")             
                opquadra = int(input("Quadra escolhida: "))
                if opquadra == 1: 
                    print(horquadras)
                    escoqua = input("escolha um horario: ")
                    for a in horquadras:
                        if a == escoqua:
                            print(f"Horario {a} escolhido") 
                            horquadras.remove(escoqua)
                        else:
                            print("Horario inexistente")   
                elif opquadra == 2: 
                    print(horquadras)
                    escoqua = input("escolha um horario: ")
                    for a in horquadras:
                        if a == escoqua:
                            print(f"Horario {a} escolhido") 
                            horquadras.remove(escoqua)  
                        else:
                            print("Horario inexistente") 
                elif opquadra == 3: 
                    print(horquadras)
                    escoqua = input("escolha um horario: ")
                    for a in horquadras:
                        if a == escoqua:
                            print(f"Horario {a} escolhido") 
                            horquadras.remove(escoqua) 
                        else:
                            print("Horario inexistente") 
                else:
                    print(f"Quadra inexistente") 
            elif estrutura2 == 2:
                print("Escolha uma quadra para dar feedback")
                print("Quadras disponiveis:")
                print("[1] Quadra 1")
                print("[2] Quadra 2")
                print("[3] Quadra 3") 
                quadrasss = int(input("Quadra escolhida: "))
                if quadrasss == 1:
                    quadrasss = input("Seu feedback: ")
                elif quadrasss == 2:
                    quadrasss = input("Seu feedback: ")
                elif quadrasss == 3:
                    quadrasss = input("Seu feedback: ")
                else:
                    print("Quadra inexistente")
            exit
        else:
            print("usuario ou senha errado!!")
    else:
        print("Ty, for use")
        break