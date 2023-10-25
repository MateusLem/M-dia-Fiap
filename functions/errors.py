def generic_response(error):
  print(f'Error: {error}')

def invalid_type(error):
  generic_response(error)
  print("Tipo de dado inválido\n")

def invalid_awnser(error):
  generic_response(error)
  print("Sua resposta não condiz com o padrão definido\n")


