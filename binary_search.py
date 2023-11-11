import time
def bin_search(table, target, n, m):
  for j in range(m):
    left, right, i = 0, n - 1, 0
    while left <= right:
      i = left + (right - left) // 2
      if table[i][j] == target: return [i, j]
      elif table[i][j] < target: left = i + 1
      else: right = i - 1
  return [-1, -1]

def binary_search(table, target, n, m):
  data = bin_search(table, target, n, m)
  i = data[0]
  j = data[1]
  if (j != -1 and i != -1 and table[i][j] == target): return True
  else: return False

n = 8192
target = 2 * n + 1
for k in range(1, 14):
  m = pow(2, k)
  table = []
  print(m)
  for i in range(n):
    a = []
    for j in range(m):
      a.append(int((n / m) * i + j) * 2)
    table.append(a)
  t0 = time.perf_counter() # с помощью этой функции происходил счет времени работы алгоритма
  print(binary_search(table, target, n, m))
  t1 = time.perf_counter()
  print((t1 - t0)*1000)
