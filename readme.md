# Média Fiap

* [Sobre](#Sobre)

* [Main](#Main)

* [Functions](#Functions)
    * [Inputs](#Inputs)
    * [Validations](#Validations)
    * [Avaliacoes](#Avaliacoes)
    * [Medias](#Medias)
    * [Menus](#Menus)
    * [Errors](#Errors)

* [Imports](#Imports)

* [Executando](#Executando)

* [Considerações](#Considerações)

* [Tecnologias](#Tecnologias)

* [Contatos](#Contatos)

<br><br>

## Sobre
Este projeto permite o cálcula das médias estimadas dos alunos da FIAP.
O projeto é capaz de estimar tanto a média mensal quanto a média anual.

## Main



## Functions

### Inputs

#### nota
```
def nota(grupo, numero):
  return input(f'Nota {grupo} {numero}\n')
```

#### menu_selecao_tipo
```
def menu_selecao_tipo():
  return input(
      "Você deseja calcular a média anual ou semestral?\n"
      "(1) Anual\n"
      "(2) Semestral\n"
  )
```

#### menu_selecao_sem
```
def menu_selecao_sem():
  return input("Informe o semestre que está (1/2)\n")
```

#### retry
```
def retry():
  return input("Deseja continuar no programa? (S/N)\n").upper()
```

### Validations

### Avaliacoes

### Medias

### Menus

### Errors




## Imports



## Executando
Siga os seguintes passos para executar o projeto:

### Clonando repositório
```
git clone https://github.com/MateusLem/Media-Fiap.git
```

### Instalando dependências
```
```

### Executando projeto
```
```

Ao iniciar o projeto, um QRcode e um link serão gerados.
Utilize qualquer um dos dois no app [Expo Go](https://expo.dev/client?utm_source=google&utm_medium=cpc&utm_content=performancemax&gclid=CjwKCAjwyNSoBhA9EiwA5aYlb02f86q0jKJ0cvHirJeDzpXetdteDIZr_Hwd8BqIC1DsMT9xAbkejxoC3ssQAvD_BwE) para executar o projeto em seu dispositivo mobile.

Quando isso acontecer, é possível pressionar "w" durante a execução no terminal para acessar a versão web do projeto.

## Considerações
Planejo fazer melhorias na interface, adicionando items como uma loja para os upgrades, efeitos exclusivos, etc.

A funcionalidade na web está prejudicada pela estilização, mas sua execução está normal. Até futuras atualizações, recomendo utilizar apenas a versão mobile.

A versão mobile funciona tanto para IOS quanto para Android
## Tecnologias 🛠️
Ferramentas utilizadas para este projeto:

- <img align="center" height="40" width="50" alt="python-icon"  src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg"> [Python](https://www.python.org/)


## Contatos 📱

<div>
        <a href="mailto:mateusdacostaleme@gmail.com">
            <img src="https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=red" target="_blank">
        </a>
        <a href="https://api.whatsapp.com/send/?phone=%2B5511960299743&text&app_absent=0" target="_blank">
            <img src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" target="_blank">
        </a>
        <a href="https://www.linkedin.com/in/mateus-da-costa-leme-35a5ab235/" target="_blank">
            <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank">
        </a>
        <a href="https://www.instagram.com/mateus.costa.leme/" target="_blank">
            <img src="https://img.shields.io/badge/Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white" target="_blank">
        </a>
    </div>
