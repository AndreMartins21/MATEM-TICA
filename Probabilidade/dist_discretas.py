from Matematica.uteis import fatorial, combination, round_value
from math import e


# DISTRIBUIÇÕES PROBABILÍSTICAS:

@round_value(10)
def binomial(p, n, k=1) -> float:
    """
  Sucesso e fracasso.
  Identificar a prob de sucesso (ocorrência de um evento).
  Exemplo: Jogar moeda (Ou dará cara [sucesso] ou coroa [fracasso])
    """
    num_sucesso = p ** k
    fracassos = (1 - p) ** (n - k)
    ordenacoes = combination(n, k)

    return ordenacoes * num_sucesso * fracassos


@round_value(8)
def geometrica(p, k) -> float:
    """
  Probabilidade de encontrar sucesso em k tentativas.
  Ex: Qual a prob de eu acertar a 5° questão em uma prova com 50
  questões e 4 alternativas cada.
  `geometrica(p = 1/4, k = 5)`
  """
    potenc = (1 - p) ** (k - 1)

    return p * potenc


@round_value(8)
def bin_negativa(p, x, k=2) -> float:
    """
  Generalização da Geométrica.
  Ex: Qual a probabilidade de jogar uma moeda 9 vezes para se obter 3 caras (sucessos)?
  Se a prob de cara for de 0.4, então:
  `bin_negativa(p = 0.4, x = 9, k = 3)`
  """
    potenc = (1 - p) ** (x - k)
    result = combination(x - 1, k - 1) * (p ** k) * potenc

    return result


@round_value(8)
def hipergeo(K, x, M, n) -> float:
    """
  K: N° de sucessos na população
  x: N° de sucessos na amostra
  M: Número total da população
  n: Tamanho da amostra
  """
    numerador = combination(K, x) * combination(M - K, n - x)
    denominador = combination(M, n)

    return numerador / denominador


@round_value(8)
def poisson(p, n, k) -> float:
    """
  p = Probabilidade de sucesso
  n = Tamanho da população
  k = Número de sucessos

  <> Usado quando trata-se de Tempo, Área.
  p pequeno e n grande
  """

    media = n * p  # Esperança da binomial
    prod = e ** (-media) * (media ** k)

    return prod / fatorial(k)
