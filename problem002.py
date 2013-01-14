def fibonacci(limit=100):
  i, ii = (1,1)
  while i < limit:
    yield i
    temp = i
    i += ii
    ii = temp

total = 0
for i in fibonacci(limit=4e6):
  if i%2 == 0:
    total += i

print total