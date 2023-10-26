from avaliacoes import gera_checkpoint, gera_sprint, gera_gs

def media_nac():
  '''
  Função que o valor da NAC, que é a média das notas dos checkpoints.
  '''
  cp = gera_checkpoint()
  return (cp[0]+cp[1])/2

def media_pi():
  '''
  Função que o valor da PI, que é a média das notas das Sprints.
  '''
  spr = gera_sprint()
  return (spr[0]+spr[1])/2

def media_semestral():
  '''
  Função que a média semestra.
  '''
  nac = float(media_nac())
  pi = float(media_pi())
  gs = float(gera_gs())
  print(f'Média Semestral: {((nac * 0.2 + pi * 0.3 + gs * 0.5) * 100):.2f}')
  return (nac * 0.2 + pi * 0.3 + gs * 0.5)

def media_anual():
  '''
  Função que o valor da NAC, que é a média das notas dos checkpoints.
  '''
  s1 = media_semestral(1)
  s2 = media_semestral(2)
  print(f'Média Anual: {(s1+s2)/2}')