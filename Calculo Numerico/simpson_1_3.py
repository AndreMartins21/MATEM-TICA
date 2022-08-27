from math import e
import numpy as np


def simpson_1_3(func, a: int, b: int, num_subint: int):
  h = (b - a)/num_subint
  print(f"h => {h}   [({b} - {a})/{num_subint}]")
  print(f"\nNumbers =>", '|<>|'.join([str(x) for x in np.arange(a, b+h, h)]))
  cont = 0
  somatorio = 0
  for i in np.arange(a, b+h, h):
    if cont in (0, num_subint):
      somatorio += func(i)*1
    elif cont % 2 == 0:
      somatorio += func(i)*2
    else:
      somatorio += func(i)*4
    cont += 1
  print(f"\nSomatório => {somatorio}")
  print(f"\nValor aproximado: (1/3)*{h}*{somatorio} => {(1/3)*h*somatorio}")

func = lambda x: (x*e**(2*x))/(1+2*x)**2

a = 0
b = 3
num_subint = 6

simpson_1_3(func, a, b, num_subint)
