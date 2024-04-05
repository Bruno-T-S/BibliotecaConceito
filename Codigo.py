from FuncoesEBibliotecas import *

LimparTerminal()

SENHAS = ["Provisório"]
ListaFuncionarios = []
ListaLivros = []
ListaRevistas = []
ListaJornais = []



adm = False
Login = False

while True:
    SENHAS[0] = Criptografar(input("Seja bem vindo ao Sistema da Biblioteca.\nInsira uma senha para a conta de Administrador, que tem ID 0: "))
    LimparTerminal()
    if (Criptografar(input("Repita a senha: ")) == SENHAS[0]):
        print("Senha validada com sucesso!")
        break
    else:
        print("Senhas não conferem.")
        time.sleep(0.5)
    LimparTerminal()

LimparTerminal()
Pergunta = Criptografar(input("Insira uma frase de segurança (Esse texto será utilizada para recuperar a sua senha caso você esqueça-a): "))
LimparTerminal()


while True: #Loop do programa. 
    # Tela de Login
    LimparTerminal()
    while not Login:
        LimparTerminal()
        ID = EntradaInteiraMaiorIgualQueZero("Digite o seu ID para assim fazer o login no sistema: ")
        LimparTerminal()
        if ID == 0:
            #Pessoa está tentando logar no perfil de adm
                LimparTerminal()
                if (Criptografar(input("Digite sua senha: ")) == SENHAS[0]):
                    LimparTerminal()
                    print("Acesso Liberado.")
                    adm = True
                    Login = True
                    LimparTerminal()
                else:
                    LimparTerminal()
                    if (input("Senha incorreta.\n\nSe deseja redefinir a senha digite 1. Se não, apenas pressione enter para voltar ao início: ") == '1'):
                        for j in range(3, 0, -1):
                            LimparTerminal()
                            if (Criptografar(input("Digite a Frase de Segurança: ")) == Pergunta):
                                SENHAS[0] = Criptografar(input("Redefina sua senha: "))
                                LimparTerminal()
                                break
                            else:
                                print(f"Tente novamente (Restam {j-1} tentativas)")
                            LimparTerminal()
                    LimparTerminal()

        elif (ID < len(SENHAS) and (ID > 0)):
            LimparTerminal()
            if (Criptografar(input("Digite sua senha: ")) == SENHAS[ID]):
                print("Acesso Liberado.") #Podemos adicionar uma variável {nome[ID]} e colocarmos algo como "Acesso Liberado Pedro"
                Login = True
                LimparTerminal()
            else:
                print("Acesso Negado.")
        else:
            print("ID não cadastrado.") 
            time.sleep(1)   
        
    LimparTerminal()        

    while True:
        LimparTerminal()        
        Decisao = EntradaDecisao("Escolha o que deseja fazer:\n0 - SAIR DO SISTEMA\n1 - Verificar, Adicionar e Editar Clientes\n2 - Empréstimo de Livro, Jornal ou Revista\n\nOPÇÕES DE ADMINISTRADOR\n\n3 - Verificar, Adicionar e Editar Funcionários\n4 - Verificar, Adicionar e Editar Livros, Jornais e Revistas\n\n", 5)
        LimparTerminal()
    
        if (Decisao > 2 and not adm):
            print("Acesso Negado. Você não possui funcionalidades de Administrador.")
            time.sleep(1)

        elif (Decisao == 1):
            pass
        
        elif (Decisao == 2):
            pass

        elif (Decisao == 3):
            if (len(SENHAS) == 1):
                if (input(("Não existem funcionários no sistema. Deseja adicionar agora (S/N)? ")).lower() == "s"):
                    while True:
                        LimparTerminal()
                        ListaFuncionarios.append(PreencherDadosFuncionario())
                        ID = len(SENHAS) 
                        LimparTerminal()
                        VerificarSenhas(SENHAS, f"Insira uma senha para o funcionário de ID {ID}: ", ID)
                        LimparTerminal()   
                        if (input("Deseja adicionar outro funcionário ao sistema (S/N)? ").lower() != "s"):
                            break
                    LimparTerminal()

            else:
                while True:
                    LimparTerminal()
                    Decisao = EntradaDecisao("Escolha o que deseja fazer:\n\n0 - Sair deste Menu\n1 - Exibir Funcionários\n2 - Adicionar Funcionário\n3 - Editar Funcionário\n4 - Remover Funcionário\n\n", 4)
                    LimparTerminal()
                    time.sleep(1)

                    if (Decisao == 1):
                        EscreverFuncionarios(ListaFuncionarios)
                        input("Pressione qualquer tecla para sair. ")
                        LimparTerminal()

                    elif (Decisao == 2):
                        while True:
                            LimparTerminal()
                            ListaFuncionarios.append(PreencherDadosFuncionario())
                            ID = len(SENHAS) 
                            LimparTerminal()
                            VerificarSenhas(SENHAS, f"Insira uma senha para o funcionário de ID {ID}: ", ID)
                            LimparTerminal()   
                            if (input("Deseja adicionar outro funcionário ao sistema (S/N)? ").lower() != "s"):
                                break
                        LimparTerminal()
                    
                    elif (Decisao == 3):
                        while True:
                            EscreverFuncionarios(ListaFuncionarios)
                            if not (ListaFuncionarios == []):
                                ID = EntradaInteiraMaiorQueZero("Digite o ID do funcionário que deseja editar: ")
                                print("\n")

                                if (ID < len(SENHAS)):
                                    break
                                else:
                                    print("ID não cadastrado.")
                                    time.sleep(1)
                                    LimparTerminal()
                            else:
                                break

                        ListaFuncionarios[ID-1] = PreencherDadosFuncionario()
                        LimparTerminal()
                        EditarSenhas(SENHAS, f"Insira uma senha para o funcionário de ID {ID}: ", ID)

                    elif (Decisao == 4):
                        if not (ListaFuncionarios == []):
                            while True:
                                EscreverFuncionarios(ListaFuncionarios)
                                ID = EntradaInteiraMaiorQueZero("Digite o ID do funcionário que deseja remover: ")
                                print("\n")
                                if (ID < len(SENHAS)):
                                    break
                                else:
                                    print("ID não cadastrado.")
                                    time.sleep(1)
                                    LimparTerminal()

                            if (input("Você tem certeza que deseja prosseguir (S/N)? Essa ação não pode ser desfeita: ").lower() == "s"):
                                ListaFuncionarios.pop(ID-1)  
                                SENHAS.pop(ID)
                        else:
                            print("Não há funcionários cadastrados.")
                            time.sleep(2)
                            LimparTerminal()

                    elif (Decisao == 0): 
                        break

        elif (Decisao == 4):
            if (ListaLivros == ListaJornais and ListaJornais == ListaRevistas and ListaRevistas == 0 and input("Você não possui nenhum livro, jornal ou revista registrado no sistema. Deseja adicionar agora (S/N)? ").lower() == "s"):
                LimparTerminal()
                AdicionarPapel(ListaLivros, ListaRevistas, ListaJornais)
            else:
                while True:
                    Decisao = EntradaDecisao("Escolha o que deseja fazer:\n\n0 - Sair deste Menu\n1 Exibir Materiais\n2 - Adicionar Material ao Sistema\n3 - Jogar Material Fora\n4 - Editar Atributos de um Material\n\n", 4)
                    LimparTerminal()

                    if (Decisao == 0):
                        break

                    elif (Decisao == 1):
                        EscreverMateriais(ListaLivros, ListaRevistas, ListaJornais)
                    
                    if (Decisao == 2):
                        AdicionarPapel(ListaLivros, ListaRevistas, ListaJornais)

                    if (Decisao == 3):
                        JogarFora(ListaLivros, ListaRevistas, ListaJornais)

        elif (Decisao == 0):
            Login = False
            adm = False
            break