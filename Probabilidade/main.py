from dist_discretas import *

"""
# Exemplo BINOMIAL:
p => 2%  (Prob. de um aparelho ser defeituoso) 
x => 5  (Número de aparelhos)
k => 0, 1, ..., 5  (Quantidade de aparelhos defeituosos)
"""

k = range(0, 6)
func_de_prob = {num: binomial(p=0.02, n=5, k=num) for num in k}

# a) Prob. de 0 aparelhos serem defeituoso: P(k=0)
a = binomial(p=0.02, n=5, k=0)
print(a)
# Matematicamente:
# (0.98*0.98*0.98*0.98*0.98)*(5!/0!*5!)

# b) Prob. de 2 OU + aparelhos serem defeituosos: (1 - [P(k=0)+P(k=1))
b = 1 - (binomial(p=0.02, n=5, k=0) + binomial(p=0.02, n=5, k=1))
print(b)
# Matematicamente, tem-se:
# 1 - [(0.98*0.98*0.98*0.98*0.98) + (0.02*0.98*0.98*0.98*0.98)*(5!/4!*1!)]

# c) Prob. de terem ao menos 4 defeituosos: P(k=4)+P(k=5)
c = binomial(p=0.02, n=5, k=4) + binomial(p=0.02, n=5, k=5)
print(c)
# Matematicamente, tem-se:
# (0.02*0.02*0.02*0.02*0.98)*(5!/4!*1!) + (0.02*0.02*0.02*0.02*0.02)*(5!/5!*0!)