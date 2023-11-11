import time

def exp_search(table, i, j, n, target):
  st = 1
  while (i + st < n and table[i + st][j] < target): st *= 2
  left = i + st // 2 + 1
  right = min(n - 1, i + st)
  while (left <= right):
    mid = left + (right - left) // 2
    if table[mid][j] == target: return mid
    elif table[mid][j] < target: left = mid + 1
    else: right = mid - 1
  return left

def diagonal_search_epx_acc(table, target, n, m):
  i, j = 0, m - 1
  while (i >= 0 and i < n and j >= 0 and j < m):
    if (table[i][j] == target): return True
    elif (table[i][j] < target):
      if (i < n - 2):
        i = exp_search(table, i, j, n, target)
      else: i += 1
    else: j -= 1
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
  print(diagonal_search_epx_acc(table, target, n, m))
  t1 = time.perf_counter()
  print((t1 - t0) * 1000)
