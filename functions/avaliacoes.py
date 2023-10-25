from validations import executa_resposta

def gera_checkpoint(semestre):
  if semestre == 1:

    cp = [
          executa_resposta('CP', 1),
          executa_resposta('CP', 2),
          executa_resposta('CP', 3)
          ]
  else:
    cp = [
          executa_resposta('CP', 4),
          executa_resposta('CP', 5),
          executa_resposta('CP', 6)
          ]

  cp = sorted(cp)
  return cp[1:]

def gera_sprint(semestre):
  if semestre == 1:
    return [
            executa_resposta('sprint', 1),
            executa_resposta('sprint', 2)
          ]
  else:
    return [
            executa_resposta('sprint', 3),
            executa_resposta('sprint', 4)
          ]

def gera_gs(semestre):
  if semestre == 1:
    return executa_resposta('gs', 1)
  else:
    return executa_resposta('gs', 2)