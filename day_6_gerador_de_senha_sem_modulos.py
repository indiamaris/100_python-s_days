
import random

from random import randint

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


def gerador_de_numeros_aleatorios(nr_numbers,numbers):
  i=0
  numeros_selecionados=''
  while i < nr_numbers:
    esculhambadora = randint(0,len(numbers)-1 )
    numeros_selecionados += numbers[esculhambadora]
    i+=1
  return numeros_selecionados


def gerador_de_letras_aleatórias(nr_letters,letters):
  i=0
  letras_selecionadas=''
  while i < nr_letters:
    esculhambadora = randint(0,len(letters)-1 )
    letras_selecionadas += letters[esculhambadora]
    i+=1
  return letras_selecionadas


def gerador_de_simbolo_aleatorios(nr_symbols,symbols):
  i=0
  simbolo_selecionados=''
  while i < nr_symbols:
    esculhambadora = randint(0,len(symbols)-1 )
    simbolo_selecionados += symbols[esculhambadora]
    i+=1
  return simbolo_selecionados


def gerador_de_senha_mediocre():
  letras = gerador_de_letras_aleatórias(nr_letters,letters)
  simbolos = gerador_de_simbolo_aleatorios(nr_symbols,symbols)
  numeros = gerador_de_numeros_aleatorios(nr_numbers,numbers)
  senha = letras + numeros + simbolos
  return senha



def senha_mixer():
  senha = gerador_de_senha_mediocre()
  i=0
  senha_mixada=''
  while i < len(senha):
    esculhambadora = randint(0,len(senha)-1 )
    senha_mixada += senha[esculhambadora]
    i+=1
  return senha_mixada



def tela_final():
  senhas = senha_mixer()
  print(f'Sua senha super forte será:\n\n {senhas}')


tela_final()
