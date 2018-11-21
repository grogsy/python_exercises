# ctci 1.3

# with builtin func
def urlfiy(string):
  return string.replace(' ', '%20')
  
# without
def urlify2(string):
  res = []
  for c in string:
    if c == ' ':
      res.append('%20')
    else:
      res.append(c)
  
  return ''.join(res)
  
def urlify3(string):
  res = ''
  for c in string:
  if c == ' ':
    res += '%20'
  else:
    res += c
    
  return res
