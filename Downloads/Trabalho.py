anoAtual = 2020
precoHoraEstar = 3
usuariosCadastrados = ["Usuário teste"]
senhasCadastradas = ["123456"]
carrosCadastrados = [["Carro 1", "Carro 2"]]
ultimaUtilizacao = [["Nunca utilizado", [21, 10, 2019, 1]]]
saldoDisponivel = [0]
logado = False

while True:
    # Pergunta para o usuário qual ação executar
    # Se não estiver logado, pode se cadastrar, logar ou encerrar o app
    if not logado:
        acao = input("O que deseja fazer? (cadastro / logar / sair) ")
    # Depois de logado, tem acesso às funcionalidades do app
    else:
        acao = input("O que deseja fazer? (comprar creditos / consultar creditos" +
                     " / cadastrar veiculo / controle / ultima utilizacao" +
                     " / desconectar / sair) ")

    # Depois que o usuário informa o que quer fazer, a ação desejada é executada
    if acao == "cadastro":
        # CADASTRO
        # Usário
        usuarioCadastro = False
        while usuarioCadastro == False:
            usuario = input("Crie um nome de Usuário ou digite 'voltar' para cancelar o cadastro: ")

            if usuario == "voltar":
                break
            # Verificação de usuário já existente
            elif usuario in (usuariosCadastrados):
                print("Nome de Usuário já utilizado.")

            # Caracter mínimo de Usuário
            elif len(usuario) < 5:
                print("Nome de Usuário menor que 5 caractéres. Digite seu Nome de Usuário novamente.")
            else:
                usuarioCadastro = True

        if usuario == "voltar":
            continue

        # Senha
        senhaCadastro = False
        while senhaCadastro == False:
            senha = input("Crie uma senha para seu Usuário ou 'voltar' para cancelar o cadastro: ")
            if senha == "voltar":
                break
            # Confirmação de Senha
            senhaConfirmada = input("Confirme sua senha: ")
            if senhaConfirmada != senha:
                print("As senhas digitadas não são iguais, digite sua senha novamente")
            # Caracter mínimo de Senha
            elif len(senha) < 5:
                print("Senha menor que 5 caractéres. Digite sua Senha novamente.")
            elif senhaConfirmada == senha:
                senhaCadastro = True
                print("Cadastro efetuado com sucesso.")

        if senha == "voltar":
            continue

        # Inserir usuario e senha dentro da lista suspensa
        usuariosCadastrados.append(usuario)
        senhasCadastradas.append(senha)
        saldoDisponivel.append(0)
        carrosCadastrados.append([])
        ultimaUtilizacao.append([])

    elif acao == "logar":
        # LOGIN
        while not logado:
            # Pede o usuário e a senha
            usuario = input("Digite o usuário ou 'voltar' para cancelar o login: ")
            if usuario == "voltar":
                break

            senha = input("Digite a senha ou 'voltar' para cancelar o login: ")
            if senha == "voltar":
                break

            # Verifica se o usuário fornecido está na lista de cadastrados
            if usuario not in usuariosCadastrados:
                print("Usuário inválido")
                # Se não estiver, interrompe a iteração e pede o usuário e a senha novamente
                continue
            # Caso o usuário esteja cadastrado, verifica se a senha fornecida é correta
            elif senha != senhasCadastradas[usuariosCadastrados.index(usuario)]:
                print("Senha inválida")
                # Caso não seja, interrompe a iteração e pede o usuário e a senha novamente
                continue
            else:
                # Por fim, se o usuário for válido e a senha for a correta, faz com que o
                # usuário seja logado
                print("Login executado")
                logado = True
                indiceUsuario = usuariosCadastrados.index(usuario)

    elif acao == "comprar creditos":
        # Créditos
        # Solicita a quantia de créditos para o usuário, como um valor real
        valor = float(input("Digite a quantidade de creditos que deseja adicionar: "))

        # Verifica se o valor fornecido é válido (tem que ser maior que 0)
        while valor <= 0:
            valor = float(input(("Quantia inválida, digitite novamente a" +
                                 "quantidade de creditos que deseja adicionar: ")))

        # Adiciona os créditos na lista de saldos.
        # Ao logar, o nome do usuario ficou armazenado na variavel 'usuario' e, como as
        # listas são organizadas com um item por usuário, o mesmo índice que corresponde
        # ao usuário na lista de usuários cadastrados vai corresponder ao saldo deste
        # usuário na lista de saldo disponível, por isso estamos acrescentando o valor
        # no item cujo índice é o mesmo do nome do usuário na lista de usuários.
        saldoDisponivel[indiceUsuario] += valor

        # Imprime a mensagem que a operação foi bem sucedida e o novo saldo.
        print("Saldos adicionados com sucesso. O saldo atual é de R$" +
              str(saldoDisponivel[indiceUsuario]))

    elif acao == "consultar creditos":
        print("Você tem R$" + str(saldoDisponivel[indiceUsuario])
              + " de créditos disponíveis.")

    elif acao == "cadastrar veiculo":
        # Cadastro de carro
        carro = False
        placaValida = False
        while carro == False:

            while not placaValida:
                # Pede que o Usuário digite a placa correspondente a seu carro
                cadastroCarro = input(
                    "Digite a placa do seu carro ou 'voltar' para cancelar o cadastro de novo veículo: ")

                if cadastroCarro == "voltar":
                    break
                # Coloca todas as letrar em maiúscula
                cadastroCarro = cadastroCarro.upper()

                # Placas devem ter 7 dígitos
                if len(cadastroCarro) != 7:
                    print("Placa deve ter 7 caracteres. Digite novamente.")
                # Confirma se o primeiro dígito é válido (deve ser uma letra)
                elif not (cadastroCarro[0] >= 'A' and cadastroCarro[0] <= 'Z'):
                    print("O primeiro caracter da placa deve ser uma letra. Digite novamente.")
                # Confirma se o segundo dígito é válido (deve ser uma letra)
                elif not (cadastroCarro[1] >= 'A' and cadastroCarro[1] <= 'Z'):
                    print("O segundo caracter da placa deve ser uma letra. Digite novamente.")
                # Confirma se o terceiro dígito é válido (deve ser uma letra)
                elif not (cadastroCarro[2] >= 'A' and cadastroCarro[2] <= 'Z'):
                    print("O terceiro caracter da placa deve ser uma letra. Digite novamente.")
                # Confirma se o quarto dígito é válido (deve ser um número)
                elif not (cadastroCarro[3] >= '0' and cadastroCarro[3] <= '9'):
                    print("O quarto caracter da placa deve ser um número. Digite novamente.")
                # Confirma se o quinto dígito é válido (deve ser uma letra ou um número)
                elif not ((cadastroCarro[4] >= 'A' and cadastroCarro[4] <= 'Z') or (
                        cadastroCarro[4] >= '0' and cadastroCarro[4] <= '9')):
                    print("O quinto caracter da placa deve ser um número ou uma letra. Digite novamente.")
                # Confirma se o sexto dígito é válido (deve ser um número)
                elif not (cadastroCarro[5] >= '0' and cadastroCarro[5] <= '9'):
                    print("O sexto caracter da placa deve ser um número. Digite novamente.")
                # Confirma se o último dígito é válido (deve ser um número)
                elif not (cadastroCarro[6] >= '0' and cadastroCarro[6] <= '9'):
                    print("O sétimo caracter da placa deve ser um número. Digite novamente.")
                # Se chegou até aqui, a placa fornecida não foi cadastrada, tem 7 dígitos e
                # todos os dígitos são válidos, então paramos de solicitar a placa para o
                # usuário e, portanto, saímos do laço while.
                else:
                    print("Placa válida.")
                    placaValida = True

            if cadastroCarro == "voltar":
                break
            # Verifica se a placa já foi cadastrada ou não
            elif cadastroCarro in carrosCadastrados[indiceUsuario]:
                print("Carro já Cadastrado. Cadastre outro.")
                placaValida = False
            else:
                carro = True
                print("Carro cadastrado com sucesso.")

        if cadastroCarro == "voltar":
            continue
        # A placa cadastrada é adicionada na lista de placas correspondente ao usuário
        # que está logado.
        carrosCadastrados[indiceUsuario].append(cadastroCarro)
        ultimaUtilizacao[indiceUsuario].append("Nunca utilizado")

    elif acao == "controle":
        utilizacao = []
        if len(carrosCadastrados[indiceUsuario]) == 0:
            print("Você não tem carros cadastrados.")
            continue

        carro = input("Digite a placa do carro que será estacionado: ")
        carro = carro.upper()
        while carro not in carrosCadastrados[indiceUsuario]:
            carro = input("Esse carro não está cadastrado. Digitar novamente a placa: ")
            carro = carro.upper()

        ano = int(input("Digite o ano em que o carro será estacionado: "))
        while ano < anoAtual:
            ano = int(input("O ano digitado é inválido. Digite novamente: "))
        utilizacao.insert(0, ano)

        mes = int(input("Digite o mês em que carro será estacionado (1-12): "))
        while (mes > 12 or mes <= 0):
            mes = int(input("O mês não foi informado corretamente. Digite novamente o mês (1-12): "))
        utilizacao.insert(0, mes)

        dia = int(input("Digite o dia do mês em que o carro será estacionado: "))
        while (dia > 31 or dia <= 0):
            dia = int(input("O dia digitado é inválido. Digite novamente o dia: "))
        utilizacao.insert(0, dia)

        tempo = int(input("Por quantas horas deseja estacionar o veículo? (1 ou 2) "))
        while tempo != 1 and tempo != 2:
            tempo = int(input(
                "Os veículos podem ficar estacionados na vaga por 1 ou 2 horas. O tempo digitado é inválido, digite novamente: "))
        utilizacao.append(tempo)

        if saldoDisponivel[indiceUsuario] < precoHoraEstar * tempo:
            print("Você não tem saldo suficiente disponíveis. Por favor, adicione créditos."
                  + " Saldo disponível: R$" + str(saldoDisponivel[indiceUsuario]))
        else:
            saldoDisponivel[indiceUsuario] = saldoDisponivel[indiceUsuario] - precoHoraEstar * tempo
            print("Sucesso! Você tem R$" + str(saldoDisponivel[indiceUsuario]) +
                  " de saldo restante e pode estacionar seu carro por " + str(tempo) + " horas.")
            ultimaUtilizacao[indiceUsuario][carrosCadastrados[indiceUsuario].index(carro)] = utilizacao

    elif acao == "ultima utilizacao":
        # ULTIMA UTILIZAÇÃO POR VEÍCULO
        # Caso o usuário não tenha cadastrado nenhum carro ainda, a mensagem apropriada
        # é impressa.
        if len(ultimaUtilizacao[indiceUsuario]) == 0:
            print("Você não tem carros cadastrados.")
        # Caso ele tenha carros cadastrados
        else:
            # Para cada carro
            for indiceCarro, carro in enumerate(ultimaUtilizacao[indiceUsuario]):
                # Se ele cadastrou mas não utilizou o carro, a mensagem apropriada é
                # impressa.
                if ultimaUtilizacao[indiceUsuario][indiceCarro] == "Nunca utilizado":
                    print("O carro " + carrosCadastrados[indiceUsuario][indiceCarro] +
                          " nunca foi utilizado no aplicativo.")
                # Se cadastrou e utilizou, a data e a
                else:
                    print("O carro " + carrosCadastrados[indiceUsuario][indiceCarro] +
                          " foi utilizado pela última vez dia " +
                          str(ultimaUtilizacao[indiceUsuario][indiceCarro][0]) + "/" +
                          str(ultimaUtilizacao[indiceUsuario][indiceCarro][1]) + "/" +
                          str(ultimaUtilizacao[indiceUsuario][indiceCarro][2]) + " por um período de " +
                          str(ultimaUtilizacao[indiceUsuario][indiceCarro][3]) + " horas.")

    elif acao == "desconectar":
        print("Usuario desconectado")
        logado = False

    elif acao == "sair":
        print("Aplicativo encerrado")
        break