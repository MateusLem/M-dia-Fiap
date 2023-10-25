from avaliacoes import gera_checkpoint, gera_sprint, gera_gs

def media_nac(semestre):
  cp = gera_checkpoint(semestre)
  return (cp[0]+cp[1])/2

def media_pi(semestre):
  spr = gera_sprint(semestre)
  return (spr[0]+spr[1])/2

def media_semestral(semestre):
  nac = float(media_nac(semestre))
  pi = float(media_pi(semestre))
  gs = float(gera_gs(semestre))
  print(f'Média Semestre {semestre}: {((nac * 0.2 + pi * 0.3 + gs * 0.5) * 100):.2f}')
  return (nac * 0.2 + pi * 0.3 + gs * 0.5)

def media_anual():
  s1 = media_semestral(1)
  s2 = media_semestral(2)
  print(f'Média Anual: {(s1+s2)/2}')