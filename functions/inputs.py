def nota(grupo:str, numero:int= None):
  '''
  Função de input da nota do usuário.

  Caso o número da avaliação seja informada, ela será exibida no input.

  Retorna a nota informada.
  '''
  if numero:
    return input(f'Nota {grupo} {numero}\n')
  else:
    return input(f'Nota {grupo}\n')

def menu_selecao_tipo():
  '''
  Função de input que funciona como menu para 
  seleção do tipo de média.

  Retorna a resposta informada.
  '''
  return input(
      "Você deseja calcular a média anual ou semestral?\n"
      "(1) Anual\n"
      "(2) Semestral\n"
  )


def retry():
  '''
  Função de input que permite ao usuário decidir 
  se deseja continuar ou encerrar o programa.
  
  Retorna a resposta informada.
  '''
  return input("Deseja continuar no programa? (S/N)\n").upper()