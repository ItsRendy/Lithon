print("Lithon 0.0.2 (default, Nov 12 2021, 14:34)")

with open("code.txt") as word_list:
    code_list = list(word_list.read().splitlines())

def error(tokens, line):
  print("\033[31m" + "invalid code:", tokens, "line:", line + 1, "" + "\033[0m")
  
alfabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
used_variable_names = []
operators = ["+", "-", "*", "/", "^", "'"]
symbols = ["=", "(", ")"]

class variable:
  def __init__(self, value):
    self.value = value

def token_reader(tokens, line):
  index = 0
  number = 0
  is_calculating = False
  is_printing = False
 
  try:
    for x in tokens:
      for y in operators:
        if x == y:
          is_calculating = True

    while index < len(tokens):
      if tokens[index] == "p" and tokens[index + 1] == "(" and tokens[index + 2] == ")":
        is_printing = True
        tokens.pop(index)
        tokens.pop(index)
        tokens.pop(index)
        index = 0
      index += 1
    index = 0

    while index < len(tokens):
      for y in used_variable_names:
        if tokens[index] == y:
          tokens.pop(index)
          tokens.insert(index, globals()[y].value)
          index = 0
      index += 1
    index = 0
          
    while index < len(tokens) and is_calculating == True:
      #Exponents and radicals
      if tokens[index] == "^":
        number += tokens[index - 1] ** tokens[index + 1] 
        tokens.pop(index - 1)
        tokens.pop(index - 1)
        tokens.pop(index - 1)
        tokens.insert(index - 1, number)
        index = 0
      if tokens[index] == "'":
        number += tokens[index - 1] ** (1/tokens[index + 1])
        tokens.pop(index - 1)
        tokens.pop(index - 1)
        tokens.pop(index - 1)
        tokens.insert(index - 1, number)
        index = 0
      number = 0
      index += 1
    index = 0

    #Multiplication and division
    while index < len(tokens) and is_calculating == True:
      if tokens[index] == "*":
        number += tokens[index - 1] * tokens[index + 1] 
        tokens.pop(index - 1)
        tokens.pop(index - 1)
        tokens.pop(index - 1)
        tokens.insert(index - 1, number)
        index = 0
      if tokens[index] == "/":
        number += tokens[index - 1] / tokens[index + 1] 
        tokens.pop(index - 1)
        tokens.pop(index - 1)
        tokens.pop(index - 1)
        tokens.insert(index - 1, number)
        index = 0
      number = 0
      index += 1
    index = 0
    
    #Addition and Subtraction
    while index < len(tokens) and is_calculating == True:
      if tokens[index] == "+":
        number += tokens[index - 1] + tokens[index + 1] 
        tokens.pop(index - 1)
        tokens.pop(index - 1)
        tokens.pop(index - 1)
        tokens.insert(index - 1, number)
        index = 0
      if tokens[index] == "-":
        number += tokens[index - 1] - tokens[index + 1] 
        tokens.pop(index - 1)
        tokens.pop(index - 1)
        tokens.pop(index - 1)
        tokens.insert(index - 1, number)
        index = 0
      number = 0
      index += 1
    index = 0

    for x in tokens:
      for y in alfabet:
        if x == y and tokens[index + 1] == "=":
          globals()[y] = (variable(tokens[index + 2]))
          used_variable_names.append(y)
      index += 1
    index = 0 
  except:
    error(tokens, line)
    return
  if is_printing:
    return tokens

#Tokens and user input
code_line = 0
for code in code_list:
  tokens = []

  build_number = 0
  is_building_number = False
  for x in code:
    if x.isnumeric():
      build_number = build_number * 10 + int(x)
      is_building_number = True
    elif is_building_number:
      tokens.append(build_number)
      build_number = 0
      is_building_number = False

    for y in operators:
      if x == y:
        tokens.append(y)
    for y in symbols:
      if x == y:
        tokens.append(y)
    for y in alfabet:
      if x == y:
        tokens.append(y)

  if is_building_number:
    tokens.append(build_number)
    build_number = 0
    is_building_number = False

  read_tokens = token_reader(tokens, code_line)
  if read_tokens != None:
    print("Lithon >", end=" ")
    print(" ".join(str(x) for x in read_tokens))
  code_line += 1