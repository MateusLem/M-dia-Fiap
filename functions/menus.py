from functions.errors import invalid_awnser
from functions.medias import media_semestral, media_anual
from functions.validations import valida_resposta, refazer
from functions.inputs import menu_selecao_tipo

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
                    media_semestral()
                    break
    except TypeError as e:
      invalid_awnser(e)

def main():
  verify = True

  while verify:
    menu()
    verify = refazer()