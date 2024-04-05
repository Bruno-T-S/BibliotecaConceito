# Só uma ideia. Utilizar esse arquivo para colocar todas as funções e bibliotecas que iremos utilizar. Depois podemos importar somente ele.

from Classes import *

from hashlib import sha256

import time
import os

def LimparTerminal():
  time.sleep(0.4)
  os.system('cls' if os.name == 'nt' else 'clear') # Detecta se é Windows (se sim, usa o comando 'cls') ou se é baseado em Unix (Linux ou MacOS) e usa o comando 'clear'.
# Essa função limpa o terminal. Código de exemplo:
# print("Oi")
# LimparTerminal()

def Criptografar(texto):
  return sha256((texto).encode()).hexdigest()

def EntradaInteira(mensagem):
  while True:
    try:
      x = int(input(mensagem))
    except:
      print("Entrada inválida. Tente novamente.\n")
    else:
      return x      

def EntradaInteiraMaiorQueZero(mensagem):
  while True:
    try:
      x = int(input(mensagem))
      if (x<=0):
        raise 
    except:
      print("Entrada inválida. Tente novamente.\n")
    else:
      return x
    
def EntradaInteiraMaiorIgualQueZero(mensagem):
  while True:
    try:
      x = int(input(mensagem))
      if (x<0):
        raise 
    except:
      print("Entrada inválida. Tente novamente.\n")
    else:
      return x
    
def EntradaDecisao(mensagem, limite:int):
  while True:
    try:
      x = int(input(mensagem))
      if (x<0 or x>limite):
        raise 
    except:
      print("Entrada inválida. Tente novamente.")
      LimparTerminal()
    else:
      return x
        

def EntradaFloatMaiorQueZero(mensagem):
  while True:
    try:
      x = float(input(mensagem))
      if (x<0):
        raise 
    except:
      print("Entrada inválida. Tente novamente.\n")
    else:
      return x
    
def EntradaCPF(mensagem): #Funciona tbm para telefone
  while True:
    try:
      x = int(input(mensagem))
      if not (len (str(x)) == 11):
        raise 
    except:
      print("Entrada inválida. Tente novamente.\n")
    else:
      return x


def VerificarSenhas(ListaSenhas, Mensagem, ID):
  while True:
    ListaSenhas.append(Criptografar(input(Mensagem)))
    LimparTerminal()
    if (Criptografar(input("Repita a senha: ")) == ListaSenhas[ID]):
        print("Senha validada com sucesso!")
        break
    else:
        print("Senhas não conferem.")
        ListaSenhas.pop()
    LimparTerminal()

def EditarSenhas(ListaSenhas, Mensagem, ID):
  while True:
    Senha = (Criptografar(input(Mensagem)))
    LimparTerminal()
    if (Criptografar(input("Repita a senha: ")) == Senha):
      print("Senha validada com sucesso!")
      ListaSenhas[ID] = (Senha)
      LimparTerminal()
      break
    else:
      print("Senhas não conferem.")
      LimparTerminal()

def FormatarCPF(CPF):
  CPF = str(CPF)
  return f'{CPF[:3]}.{CPF[3:6]}.{CPF[6:9]}-{CPF[9:]}'

def FormatarTelefone(Telefone):
  Telefone = str(Telefone)
  return f'({Telefone[:2]}){" "}{Telefone[2:7]}-{Telefone[7:]}'

def FormatarSalario(Salario):
  return f'R$ {Salario:.2f}'

#Classes de Preenchimento de Dados


#Classes de Pessoas

class Humano:
  def __init__(self,nome:str ,cpf:int, email:str, telefone:int, endereco:str):
      self.nome=nome    #nome
      self._cpf=cpf    #CPF
      self._email=email    #email
      self._telefone=telefone    #telefone
      self._endereco=endereco    #endereço
  
  def ExibirInformacoes(self):
    return f"Nome: {self.nome} | CPF: {FormatarCPF(self._cpf)} | Email: {self._email} | Telefone: {FormatarTelefone(self._telefone)} | Endereço: {self._endereco} | " 

class Funcionario(Humano):
  def __init__(self, nome:str, cpf:int, email:str, telefone:int, endereco:str, salario:float, horas:int):
    super().__init__(nome, cpf, email, telefone, endereco)
    self.__salario=salario   
    self.__horas=horas   
  
  def ExibirInformacoes(self):
    return super().ExibirInformacoes() + f"Salário: {FormatarSalario(self.__salario)} | Carga Horária: {self.__horas}"
  
class Papel:
  def __init__(self, titulo:str, ano:str):
    self.titulo = titulo
    self.ano = ano
  def ExibirInformacoes(self):
    return f"Título: {self.titulo} | Ano: {self.ano} | "

class Livro(Papel):
  def __init__(self, titulo:str, ano:str, volume:int, editora:str):
    super().__init__(titulo, ano)
    self.volume = volume
    self.editora = editora
  def ExibirInformacoes(self):
    return super().ExibirInformacoes() + f"Volume: {self.volume} | Editora: {self.editora}"
  
class Revista(Papel):
  def __init__(self, titulo: str, ano: str, revista:str, semana:int):
    super().__init__(titulo, ano)
    self.revista = revista
    self.semana = semana
  def ExibirInformacoes(self):
    return super().ExibirInformacoes() + f"Revista: {self.revista} | Semana de Publicação: {self.semana}"
  
class Jornal(Papel):
  def __init__(self, titulo: str, ano: str, jornal:str, data:str):
    super().__init__(titulo, ano)
    self.jornal = jornal
    self.data = data
  def ExibirInformacoes(self):
    return super().ExibirInformacoes() + f"Jornal: {self.jornal} | Data: {self.data}"


#Aqui acabam as Classes


def PreencherDadosFuncionario():
  while True:
    Nome = input("Digite o Nome do Funcionário: ")
    CPF = EntradaCPF("Digite o CPF: ")
    Email = input("Digite o Email: ")
    Telefone = EntradaCPF("Digite o Telefone: ")
    Endereco = input("Digite o Endereço: ")
    Salario = EntradaFloatMaiorQueZero("Digite o Salário: ")
    CargaHoraria = EntradaInteiraMaiorQueZero("Digite a Carga Horária: ")
    if(input("Os dados acima estão corretos (S/N)? ").lower() == "s"):
      break
    LimparTerminal()
  LimparTerminal()
  return Funcionario(Nome, CPF, Email, Telefone, Endereco, Salario, CargaHoraria)

def EscreverFuncionarios(ListaFuncionarios):

  if (ListaFuncionarios == []):
    print("Não há funcionários cadastrados.")
    time.sleep(2)
    LimparTerminal()
  else:
    contador = 1
    for funcionario in ListaFuncionarios:
        print(f"ID do Funcionário: {contador}\n{funcionario.ExibirInformacoes()}\n\n")
        contador += 1
#Funções Comuns: 

def AdicionarPapel(ListaLivros, ListaRevistas, ListaJornais):
  while True:
    Decisao = EntradaDecisao("Deseja adicionar um Livro (1), uma Revista (2) ou um Jornal (3)? ", 3)
    LimparTerminal()

    if (Decisao == 1):
      while True:
        Titulo = input("Digite o Título: ")
        Ano = input("Digite o Ano: ")
        Volume = EntradaInteiraMaiorIgualQueZero(input("Digite o Volume: "))
        Editora = input("Digite a Editora: ")
        Quantidade = EntradaInteiraMaiorQueZero(input("Digite a Quantidade no Acervo: "))

        if (input("Os dados acima estão corretos (S/N)? ").lower() == "s"):
          break

        LimparTerminal()

      LimparTerminal()
      ListaLivros.append(Livro(Titulo, Ano, Volume, Editora))
      ListaLivros.append(Quantidade)
    
    if (Decisao == 2):
      while True:
        Titulo = input("Digite o Título: ")
        Ano = input("Digite o Ano: ")
        Revista = input("Digite a Revista: ")
        Semana = EntradaInteiraMaiorQueZero(input("Digite a Semana: "))
        Quantidade = EntradaInteiraMaiorQueZero(input("Digite a Quantidade no Acervo: "))

        if (input("Os dados acima estão corretos (S/N)? ").lower() == "s"):
          break

        LimparTerminal()

      LimparTerminal()
      ListaRevistas.append(Revista(Titulo, Ano, Revista, Semana))
      ListaRevistas.append(Quantidade)

    if (Decisao == 3):
      while True:
        Titulo = input("Digite o Título: ")
        Ano = input("Digite o Ano: ")
        jornal = input("Digite o Jornal: ")
        Data = EntradaInteiraMaiorQueZero(input("Digite a Data (DD/MM): "))
        Quantidade = EntradaInteiraMaiorQueZero(input("Digite a Quantidade no Acervo: "))

        if (input("Os dados acima estão corretos (S/N)? ").lower() == "s"):
          break

        LimparTerminal()

      LimparTerminal()
      ListaJornais.append(Jornal(Titulo, Ano, jornal, Data))
      ListaJornais.append(Quantidade)

    if (input("Deseja adicionar um material à biblioteca novamente (S/N)? ".lower != "s")):
      break

def EscreverLivros(ListaLivros):
  if (ListaLivros == []):
      print("Não há livros para serem exibidos.\n")
  else:
      print("Lista de Livros:\n")
      contador = 0
      for i in range(len(ListaLivros), 2):
        print(f"ID do Livro, na Lista de Livros: {contador}\n{ListaLivros[i].ExibirInformacoes()}")
        contador += 1

def EscreverRevistas(ListaRevistas):
  if (ListaRevistas == []):
      print("Não há revistas para serem exibidas.\n")
  else:
      print("Lista de Revistas:\n")
      contador = 0
      for i in range(len(ListaRevistas), 2):
          print(f"ID da Revista: {contador}\n{ListaRevistas[i].ExibirInformacoes()}")
          contador += 1 

def EscreverJornais(ListaJornais):
  if (ListaJornais == []):
      print("Não há jornais para serem exibidos.\n")
  else:
      print("Lista de Jornais:\n")
      contador = 0
      for i in range(len(ListaJornais), 2):
          print(f"ID do Jornal: {contador}\n{ListaJornais[i].ExibirInformacoes()}")
          contador += 1 

def EscreverMateriais(ListaLivros, ListaRevistas, ListaJornais):
  EscreverLivros(ListaLivros)
  EscreverRevistas(ListaRevistas)
  EscreverJornais(ListaJornais)

  input("Pressione qualquer tecla para continuar. ")
  LimparTerminal()
        
def JogarFora(ListaLivros, ListaRevistas, ListaJornais):
  Decisao = EntradaDecisao("Deseja jogar fora um Livro (1), uma Revista (2) ou um Jornal (3)? ", 3)
  LimparTerminal()
  if (Decisao == 1):
    if (ListaLivros == []):
      print("Não há livros para serem editados.")
    else:
      EscreverLivros()
      escolha = EntradaInteiraMaiorIgualQueZero("Selecione o ID do livro que deseja jogar fora: ")
      while True:
        quantidade = EntradaInteiraMaiorQueZero("Selecione quantos exemplares deseja jogar fora:")


def VerificarEAdicionarClientes():
  pass

def EmprestarLivro():
  pass

#Funções ADM: 
def EditarFuncionarios(): 
  pass

def EditarLivros():
  pass

def EditarClientes():
  VerificarEAdicionarClientes()
  pass
