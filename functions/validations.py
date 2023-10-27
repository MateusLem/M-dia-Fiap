from functions.inputs import nota, retry
from functions.errors import invalid_awnser, invalid_type

def valida_nota(nota:str):
  '''
  Função que verifica se a nota informada pelo usuário pode ser transformado em float
  e se o valor informado está entre 0 e 10, retornando True em caso positivo.
  '''
  if 0 <= float(nota) <= 10:
    return True



def valida_resposta(resposta:str):
  '''
  Função que verifica se a nota informada pelo usuário pode ser transformado em int
  e se o valor informado é 1 ou 2, retornando True em caso positivo.
  '''
  if int(resposta) == 1 or int(resposta) == 2:
    return True



def executa_resposta(grupo:str, numero:int=None):
  '''
  Função que executa um loop para o input da nota do usuário e,
  em seguida, verifica sua validade.

  Caso a nota informada seja válida, a função é encerrada.
  '''
  while True:
    valor = nota(grupo, numero)
    try:
        if valida_nota(valor):
            return float(valor)
    except TypeError as e:
      invalid_type(e)
    else:
       invalid_awnser()



def refazer():
  '''
  Função que executa um loop para o input da resposta do usuário 
  para executar o programa novamente e, em seguida, verifica sua validade.

  Caso a nota informada seja válida, a função é encerrada.
  '''
  while True:
    try:
      match retry():
        case "S":
          return True
        case "N":
          return False
    except TypeError as e:
        invalid_awnser(e)