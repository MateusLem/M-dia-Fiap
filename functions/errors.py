def generic_response(error:TypeError):
  '''
  Função que exibe uma mensagem de erro genérica, exibindo o erro ocorrido.
  '''
  print(f'Error: {error}')



def invalid_type(error:TypeError):
  '''
  Função que exibe uma mensagem de erro específico para tipo de dado inválido.
  '''
  generic_response(error)
  print("Tipo de dado inválido\n")



def invalid_awnser():
  '''
  Função que exibe uma mensagem de erro específico para respostas fora do formato.
  '''
  print("Sua resposta não condiz com o padrão definido\n")


