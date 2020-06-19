# INFORMAÇÕES GERAIS ===========================================================
vacinas = ["BCG", "Hepatite B", "Pentavalente (DTP/HB/Hib) (3)", "VIP (Poliomelite inativada) (3)",
           "Pneumocócica 10V (3)", "Vacina rotavírus humano GIPI (2)",
           "Meningocócica C conjugada (2)", "Febre amarela", "Tríplice viral", "Hepatite A", "Poliomelite oral VOP",
           "DTP", "Tetraviral ou tríplice viral + varicela",
           "Varicela atenuada", "HPV (2)"]
dosesNecessarias = [1, 1, 3, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2]
numeroDeVacinas = len(vacinas)
anoAtual = 2020
mesAtual = 6
diaAtual = 8

# INFORMAÇÕES DO PROGRAMA ======================================================
nomes = ["Marco Antonio"]
CPFs = ["12345678910"]
dosesFaltantes = [[1, 1, 2, 1, 3, 2, 1, 1, 1, 1, 1, 0, 1, 1, 1]]
vacinasAgendadas = [[["BCG", "30/05/2020"], ["Hepatite B", "01/10/2021"]]]
vacinasTomadas = [[["Hepatite A", "04/06/2020"]]]
logado = False
indiceUsuario = 0


# DEFINIÇÃO DAS FUNÇÕES AUXILIARES =============================================

def cadastroUsuario():
    # Pede o nome do usuário
    nome = input("Digite seu nome completo, ou '0' para cancelar o cadastro: ")

    # Se o usuário digitar '0', o cadastro é cancelado e ele volta para o menu
    if nome == '0':
        # Retorna uma indicação de que o cadastro não foi feito
        return False

    # Pede o CPF do usuário
    CPF = input("Digite seu CPF, ou '0' para cancelar o cadastro: ")

    # Se o usuário digitar '0', o cadastro é cancelado e ele volta para o menu
    if CPF == '0':
        # Retorna uma indicação de que o cadastro não foi feito
        return False

    # Caso o CPF já esteja na lista de CPFs cadastrados
    while CPF in CPFs:
        # Solicita que o usuário digite novamente o CPF até que o número informado seja válido
        CPF = input("O CPF digitado já foi cadastrado. Digite o CPF novamente ou '0', para cancelar o cadastro: ")
        # Se o usuário digitar '0', o cadastro é cancelado e ele volta para o menu
        if CPF == '0':
            # Retorna uma indicação de que o cadastro não foi feito
            return False

    # Adiciona o nome e o CPF nas listas de valores cadastrados, e uma lista indicando
    # que nenhuma vacina foi tomada ainda na lista de dosesFaltantes
    nomes.append(nome)
    CPFs.append(CPF)
    dosesFaltantes.append(dosesNecessarias)
    vacinasAgendadas.append([])
    vacinasTomadas.append([])

    # Retorna uma inicação de que o cadastro foi feito.
    return True


def efetuarLogin():
    global indiceUsuario
    while True:
        # Pede o Nome e o CPF
        nomeUsuario = input("Digite seu Nome Completo ou '0' para cancelar o login: ")
        if nomeUsuario == "0":
            return False

        cpfUsuario = input("Digite seu CPF ou '0' para cancelar o login: ")
        if cpfUsuario == "0":
            return False

        # Verifica se o usuário fornecido está na lista de Nomes cadastrados
        if nomeUsuario not in nomes:
            print("Usuário inválido")
            # Se não estiver, interrompe a iteração e pede o Nome e o CPF novamente
            continue
            # Caso o usuário esteja cadastrado, verifica se o CPF é correspondente
        elif cpfUsuario != CPFs[nomes.index(nomeUsuario)]:
            print("CPF inválido")
            # Caso não seja, interrompe a iteração e pede o usuário e a senha novamente
            continue
        else:
            # Por fim, se o usuário for válido e a senha for a correta, faz com que o
            # usuário seja logado
            indiceUsuario = CPFs.index(cpfUsuario)
            return True


def dataCerta(dia, mes, ano):
    return str(dia) + "/" + str(mes) + "/" + str(ano)


def dataVacina():
    while True:
        # Pede ao usuário o Ano, o Mês e a Data que ele deseja agendar sua Vacina
        anoAgendado = int(input("Digite o ano em que você queira tomar sua vacina = "))
        mesAgendado = int(input("Digite o mes em que você queira tomar sua vacina = "))
        diaAgendado = int(input("Digite o dia em que você queira tomar sua vacina = "))

        # Verifica se o Mês escolhido pelo Usuário consta no calendário (12 meses)
        if mesAgendado <= 0 or mesAgendado >= 13:
            print("Mês inválido")
            continue

        # Verifica se o Dia escolhido pelo Usuário consta no calendário
        if diaAgendado <= 0 or diaAgendado >= 32:
            print("Dia inválido")
            continue

        # Verifica se o Ano escolhido pelo Usuário é válido para agendamento, comparando com o Ano atual
        if anoAgendado < anoAtual:
            print("Não há como agendar uma vacina em um ano anterior ao atual. Por favor, digite novamente")
            continue

        # Se o Ano escolhido pelo Usuário for válido, verifica se Mês escolhido é válido,
        # comparando com o Mês atual
        elif anoAgendado == anoAtual:
            if mesAgendado < mesAtual:
                print("Não há como agendar uma vacina em um mês anterior ao atual. Por favor, digite novamente")
                continue

            # Se o Mês escolhido pelo Usuário for válido, verifica se Dia escolhido é válido,
            # comparando com o Dia atual
            elif mesAgendado == mesAtual:
                if diaAgendado < diaAtual:
                    print("Não há como agendar uma vacina em um dia anterior ao atual. Por favor, digite novamente")
                    continue

        # Transformar os retornos do Usuário em uma data convencional (dia / mês / ano)
        dataAgendada = dataCerta(diaAgendado, mesAgendado, anoAgendado)
        return dataAgendada


def nomeVacina():
    # Gera o texto para o menu de vacinas
    menuVacinas = ""
    for i in range(numeroDeVacinas):
        # Para cada vacina, coloca o número correspondente, o nome da vacina e uma quebra de linha
        menuVacinas += str(i + 1) + ". " + vacinas[i] + "\n"

    while True:
        # Pergunta ao usuário qual vacina ele quer agendar e apresenta o menu
        vacinaEscolhida = int(input("Qual vacina deseja agendar/cadastrar?\n" + menuVacinas))

        # Verifica se o usuário já tomou todas as doses da vacina selecionada
        if dosesFaltantes[indiceUsuario][vacinaEscolhida - 1] == 0:
            # Caso tenha, informa o usuário que a vacina selecionada é inválida e repete o laço
            print("Todas as doses da vacina selecionada já foram tomadas.")
            continue

        # Caso o usuário ainda não tenha tomado todas as doses da vacina selecionada, retorna o nome da vacina e o índice dela na lista de vacinas
        return vacinas[vacinaEscolhida - 1], vacinaEscolhida - 1


# PROGRAMA =====================================================================

while True:
    # Pergunta para o usuário qual ação executar
    # Se não estiver logado, pode se cadastrar, logar ou encerrar o app
    if not logado:
        acao = input("O que deseja fazer? (Digite o número desejado)\n1. Cadastro\n2. Logar\n3. Sair\n")

        if acao == "1":
            # CADASTRO
            cadastrado = cadastroUsuario()
            # Caso um novo usuário tenha sido cadastrado, é emitido um aviso ao usuário.
            if cadastrado:
                print("Usuário cadastrado com sucesso.")

        elif acao == "2":
            # LOGIN
            logado = efetuarLogin()
            if logado:
                print("Login executado.")

        elif acao == "3":
            break

    # Depois de logado, tem acesso às funcionalidades do app
    else:
        # Menu quando está logado
        acao = input("O que deseja fazer? (Digite o número desejado) \n1. Cadastrar Nova Aplicação de Vacina \n2. Agendar Aplicação de Nova Vacina \n3. Ver seus Agendamentos Atuais" +
            "\n4. Desconectar\n5. Sair\n")
        # Cadastro de vacinas
        if acao == "1":
            # Pede o nome da vacina que será cadastrada (a função também verifica se a vacina é válida)
            vacinaTomada, indiceVacina = nomeVacina()
            # Diminui 1 na quantidade de doses necessárias para a vacina escolhida e registra que a vacina foi tomada
            # no dia atual.
            dosesFaltantes[indiceUsuario][indiceVacina] -= 1
            dataMarcada = dataCerta(diaAtual, mesAtual, anoAtual)
            vacinasTomadas[indiceUsuario].append([vacinaTomada, dataMarcada])
            print("Vacina cadastrada com sucesso!\n")

        # Agendamento de vacinas
        elif acao == "2":
            # Pede a data do agendamento e o nome da vacina, e os armazena na lista de
            # vacinas agendadas do usuário.
            dataAgendada = dataVacina()
            vacinaEscolhida, _ = nomeVacina()
            vacinasAgendadas[indiceUsuario].append([vacinaEscolhida, dataAgendada])
            print("Vacina agendada com sucesso!\n")

        # Visualização dos agendamentos
        elif acao == "3":
            # Imprime as vacinas agendadas
            print("==== VACINAS AGENDADAS: =====")
            # Seleciona a lista de agendamentos do usuário que está logado.
            agendamentos = vacinasAgendadas[indiceUsuario]
            # Para cada agendamento, imprime a vacina agendada e a data correspondente.
            if agendamentos:
                for agendamento in agendamentos:
                    print("A vacina " + agendamento[0] + " está agendada para o dia " + agendamento[1] + ".")
            else:
                print("Você não tem vacinas agendadas.")

            # Imprime as vacinas tomadas
            print("\n\n==== VACINAS TOMADAS: =====")
            # Para cada vacina tomada, imprime a vacina tomada e a data correspondente.
            tomadas = vacinasTomadas[indiceUsuario]
            if tomadas:
                for tomada in tomadas:
                    print("A vacina " + tomada[0] + " foi tomada dia " + tomada[1] + ".")
            else:
                print("Você ainda não tomou nenhuma vacina.")
            print("\n\n")

        elif acao == "4":
            # Desconectar
            logado = False
            continue

        elif acao == "5":
            # Fechar programa
            break
