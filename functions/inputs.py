def nota(grupo, numero):
  return input(f'Nota {grupo} {numero}\n')

def menu_selecao_tipo():
  return input(
      "Você deseja calcular a média anual ou semestral?\n"
      "(1) Anual\n"
      "(2) Semestral\n"
  )

def menu_selecao_sem():
  return input("Informe o semestre que está (1/2)\n")

def retry():
  return input("Deseja continuar no programa? (S/N)\n").upper()