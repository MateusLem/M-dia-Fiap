from inputs import nota, retry
from errors import invalid_awnser, invalid_type

def valida_nota(nota):
  if 0 <= float(nota) <= 10:
    return True

def valida_resposta(resposta):
    if int(resposta) == 1 or int(resposta) == 2:
        return True

def executa_resposta(grupo, numero):
  while True:
    valor = nota(grupo, numero)
    try:
        if valida_nota(valor):
            return float(valor)
    except TypeError as e:
      invalid_type(e)
    except:
       invalid_awnser(e)

def refazer():
  while True:
    try:
        match retry():
            case "S":
                return False
            case "N":
                return True
    except TypeError as e:
        invalid_awnser(e)