def fatorial(x):
  value = 1
  for cont in range(x, 0, -1):
    value *= cont
  return value


def combination(m:int, n:int):
  return fatorial(m) / (fatorial(n) * fatorial(m-n))


def round_value(num_de_casas: int = 7):
    def run_func(f):
        def arredonda(*args, **kwargs):
            result = f(*args, **kwargs)
            return round(result, num_de_casas)
        return arredonda
    return run_func