from math import e, log, sin
import pandas as pd

"""
# Método da bisseção

</> Utilizado para aproximar o valor de uma raíz através de iterações [subintervalos];

</> Detalhadamente, tem-se:
  Seja uma função contínua f: [a, b] -> R   (em um intervalo [a,b]), 
tal que f(a) e f(b) tenham sinais opostos `f(a)*f(b) < 0`, garantindo a existência
de uma raíz nesse intervalo.
  O método da Bisseção consiste em dividir o intervalo em seu ponto médio `c = (a+b)/2`, 
e, então, checar em qual dos dois subintervalos há uma raíz. Para isso, basta verificar
se `f(a)*f(c) < 0`. Caso tenha, há pelo menos uma raíz no interv. (a, c), senão, há 
uma raíz no interv. [c, b). O procedimento é, então, repetido para o respectivo subintervalo
que contiver a raíz até que `c` aproxime a raíz com a precisão desejada.
"""


class Bissecao:
  def __init__(self, a: float, b: float, erro: float, func):
    self.infos = {
        "k": [0], "a": [a], "b": [b], "x": [a], 
        "fa": [0], "fx": [func(a)], "cond": ["--"]
    }
    self.a = a
    self.b = b
    self.erro = erro
    self.func = func
  
  def run(self, create_csv: bool = False) -> float:
    a, b = self.a, self.b
    k = 1
    parar = False
    while True:
      if parar: break

      x = (a + b) / 2
      cond = abs(x - self.infos["x"][k-1])
      if (cond < self.erro):
        parar = True

      self.infos["cond"].append(cond)
      fa = self.func(a)
      fx = self.func(x)
      self.infos["k"].append(k)
      self.infos["x"].append(x)
      self.infos["a"].append(a)
      self.infos["b"].append(b)
      self.infos["fa"].append(fa)
      self.infos["fx"].append(fx)

      if fa*fx < 0:
        b = x
      else:
        a = x
      k += 1

    print(f"\n<> Aproximação da RAÍZ => {x} \nk = {k-1} \nCond = {cond} < {self.erro}")
    
    self._create_df_csv() if create_csv else ""
    return x
  
  def _create_df_csv(self):
    df = pd.DataFrame(self.infos).set_index("k")

    # df.iloc[1:, :].to_csv("metodo_bissecao.csv", sep = ";", index = False)
    
    
f = lambda x: log(x**3+(e**x + 1)**(1/2), e)

a, b = [2, 3]
erro = 0.01

Bissecao(a, b, erro, func= f).run()