from functions.validations import executa_resposta

def gera_checkpoint():
  '''
  Função que junta as notas dos checkpoints do semestre e retorna uma lista com as notas válidas.

  As apenas as duas notas mais altas são retornadas.
  '''
  cp = [
          executa_resposta('CP', 1),
          executa_resposta('CP', 2),
          executa_resposta('CP', 3)
        ]
  cp = sorted(cp)

  return cp[1:]

def gera_sprint():
  '''
  Função que retorna uma lista com as notas das Sprints do semestre.
  '''
  return [
            executa_resposta('Sprint', 1),
            executa_resposta('Sprint', 2)
          ]

def gera_gs():
  '''
  Função retorna a nota da Global Solution do semestre.
  '''
  return executa_resposta('Global Solution')