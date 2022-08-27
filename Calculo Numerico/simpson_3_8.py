from math import e, log
import numpy as np


def simpson_3_8(func, a: int, b: int, num_subint: int):
  h = (b - a)/num_subint
  print(f"h => {h}   [({b} - {a})/{num_subint}]")
  print(f"\nNúmeros =>", '|<>|'.join([str(x) for x in np.arange(a, b+h, h)]))
  cont = 0
  somatorio = 0
  for i in np.arange(a, b+h, h):
    if cont in (0, num_subint):
      somatorio += func(i)*1
    elif cont % 3 == 0:
      somatorio += func(i)*2
    else:
      somatorio += func(i)*3
    cont += 1
  print(f"\nSomatório => {somatorio}")
  print(f"\nValor aproximado: (3/8)*{h}*{somatorio} => {(3/8)*h*somatorio}")

func = lambda x: log(x**3+(e**x + 1)**(1/2), e)
a = 1
b = 4
num_subint = 6

simpson_3_8(func, a, b, num_subint)