from functions.avaliacoes import gera_checkpoint, gera_sprint, gera_gs

def media_nac():
  '''
  Função que calcula o valor da NAC, que é a média das notas dos checkpoints.
  '''
  cp = gera_checkpoint()
  return (cp[0]+cp[1])/2

def media_pi():
  '''
  Função que calcula o valor da PI, que é a média das notas das Sprints.
  '''
  spr = gera_sprint()
  return (spr[0]+spr[1])/2

def media_semestral():
  '''
  Função que calcula a média semestral.

  O peso das notas são:

  - NAC = 20%

  - PI = 20%

  - GS = 60%

  O resultado é multiplicado por 10 para refletir a nota exibida no boletim.
  '''
  nac = float(media_nac())
  print(f'Média dos Checkpoints: {nac*10}')
  pi = float(media_pi())
  print(f'Média das Sprints: {pi*10}')
  gs = float(gera_gs())
  print(f'Nota da Global: {gs*10}')
  print(f'Média Semestral: {((nac * 0.2 + pi * 0.2 + gs * 0.6) * 10):.2f}')
  return (nac * 0.2 + pi * 0.3 + gs * 0.5)

def media_anual():
  '''
  Função que o valor da média anual, que é a média da soma das médias semestrais.
  '''
  s1 = media_semestral()
  s2 = media_semestral()
  print(f'Média Anual: {((s1 * 0.4 +s2 * 0.6)*10):.2f}')