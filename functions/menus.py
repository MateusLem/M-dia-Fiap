from errors import invalid_awnser
from medias import media_semestral, media_anual
from validations import valida_resposta, refazer
from inputs import menu_selecao_sem, menu_selecao_tipo

def executa_semestre():
  while True:
    resposta = menu_selecao_sem()
    try:
        if valida_resposta(resposta):
            match int(resposta):
                case 1:
                    media_semestral(1)
                    break
                case 2:
                    media_semestral(2)
                    break
    except TypeError as e:
        invalid_awnser(e)

def menu():
  while True:
    resposta = menu_selecao_tipo()
    try:
        if valida_resposta(resposta):
            match int(resposta):
                case 1:
                    media_anual()
                    break
                case 2:
                    executa_semestre()
                    break
    except TypeError as e:
      invalid_awnser(e)

def main():
  verify = None

  while verify != "Y":
    if verify:
      break
    else:
      menu()
      verify = refazer()