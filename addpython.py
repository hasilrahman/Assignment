def add_string(str1):
  length = len(str1)
  if length > 5:
    if str1[-3:] == 'python':
      str1 += 'java'
    else:
      str1 += 'php'
  return str1
print(add_string('php'))
print(add_string('java'))
print(add_string('python'))