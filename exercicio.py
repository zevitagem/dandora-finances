# Requisitos
    # [x] Exibir 
        # [x] Bem-Vindo
        # [x] Login
        # [x] Quadras
        # [x] Horários

    # [] Registrar a opção: 
        # [] Cadastro de Usuário
        # [] Login
        # [] Close (Saída do Aplicativo)
        # [] Escolher Quadras
        # [] Feedback das Quadras
        # [] Escolher Horários
        # [] Feedback dos Horários

    # [] Lógica

# Lógica + Dados
# Estado dos Objetos
# Registrar Admin
# Checar registro
# Adicionar Quadra
# Remover Quadra
# Checar Quadra
# Adicionar Horario
# Remover Horario
# Checar Horario
# Adicionar Feedback
# Remover Feedback

# menu = createMenu()

# Inputs
    # Menu
        # Registrar a opção Cadastrar (chamando o metodo createUser)
        # op_cadUser = int(input("Opção selecionada: 1"))
        # return(op_CadUser)

        # Registrar a opção Admin (chamando o metodo Login)
        # op_Login = int(input("Opção selecionada: 2"))
        # return(op_Login)

    # Admin
        # Registrar a opção Adicionar Quadra (chamando o metodo addQuadra)
        # op_addQuadra = int(input("Opção selecionada: 1"))
        # return(op_addQuadra)

        # Registrar a opção Deletar Quadra (chamando o metodo removeQuadra)
        # op_removeQuadra = int(input("Opção selecionada: 2"))
        # return(op_removeQuadra)

    # Quadras
        # Registrar a opção Escolher Quadras Disponiveis (chamando o método choiceQuadra)
        # opcoes2 = int(input("Opção selecionada: 1"))
        # return(opcoes2)

        # Registrar a opção Feedback das Quadras (chamando o metodo feedbackQuadra)
        # opcoes2 = int(input("Opção selecionada: 1"))
        # return(opcoes2)

    # Horários
        # Registrar a opção Escolher Horários Disponiveis (chamando o método choiceTime)
        # Registrar a opção Feedback (chamando o metodo feedbacktime)

# Apresentação
def render():
    
    # Bem-Vindo
    print ()
    print ("          Bem vindo          ")
    print ()

    # Menu - Login
    print ("  1. Login - Escolha uma opção: ")
    print ()
    print ("  [1] Cadastrar um usuario")
    print ("  [2] Fazer Login")
    print ("  [Qualquer outra tecla.] Sair do aplicativo")
    print ()

    # Message: User cadastrado
    # print ("")

    # Menu - Quadras
    print ("  2. Quadras - Escolha uma opção: ")
    print ()
    print ("  [1] Escolher uma quadra  ")
    print ("  [2] Enviar um feedback  ")
    print ("  [Qualquer outra tecla.] Sair do aplicativo")
    print ()

    # Lista de Quadras
    print ("  2.1 Quadras Disponíveis - Escolha uma opção: ")
    print ()
    print ("  [1] Quadra Primária  ")
    print ("  [2] Quadra Secundária  ")
    print ("  [3] Quadra Terciária  ")
    print ("  [4] Quadra indisponível  ")
    print ()

    # Message: Quadra adicionada
    # print ("")

    # Message: Quadra removida
    # print ("")

    # Message: Feedback criado
    # print ("")

    # Menu - Horários
    print ("  3. Horários - Escolha uma opção: ")
    print ()
    print ("  [1] Escolher uma quadra  ")
    print ("  [2] Enviar um feedback  ")
    print ("  [Qualquer outra tecla.] Sair do aplicativo  ")
    print ()

    # Lista de Horários
    print ("  3.1 Horários Disponíveis - Escolha uma opção: ")
    print ()
    print ("  [1] 16:00  ")
    print ("  [2] 16:30  ")
    print ("  [3] 17:00  ")
    print ("  [4] 17:30  ")
    print ("  [5] 18:00  ")
    print ("  [6] Horário Indisponível  ")
    print ()

    # Message: Horário adicionado
    # print ("")

    # Message: Horário removido
    # print ("")

    # Message: Feedback criado
    # print ("")

render()