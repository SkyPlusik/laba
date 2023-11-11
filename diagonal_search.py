import time

def diagonal_search(table, target, n, m):
  i, j = 0, m - 1
  while (i >= 0 and i < n and j >= 0 and j < m):
    if (table[i][j] == target):
      return True
    elif (table[i][j] < target):
      i += 1
    else:
      j -= 1
  return False

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
  t0 = time.perf_counter()
  print(diagonal_search(table, target, n, m))
  t1 = time.perf_counter()
  print((t1 - t0)*1000)
