print("Lithon 0.0.2 (default, Nov 12 2021, 14:34)")

with open("code.txt") as word_list:
    code_list = list(word_list.read().splitlines())

def error(tokens, line):
  print("\033[31m" + "invalid code:", tokens, "line:", line + 1, "" + "\033[0m")
  
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
    
    #functions
    while index < len(tokens):
      if tokens[index] == "print" and tokens[index + 1] == "(" and tokens[index + 2] == ")":
        is_printing = True
        tokens.pop(index)
        tokens.pop(index)
        tokens.pop(index)
        index = 0
      index += 1
    index = 0

    #Variable to value converter
    while index < len(tokens):
        for x in used_variable_names:
          if index == len(tokens) - 1 and tokens[index] == x:
            tokens.pop(index)
            tokens.insert(index, globals()[x].value)
            index = 0
            continue
          if tokens[index] == x and tokens[index + 1] != "=":
            tokens.pop(index)
            tokens.insert(index, globals()[x].value)
            index = 0
        index += 1
    index = 0

    #Calculation
    #Exponents and radicals
    while index < len(tokens) and is_calculating == True:
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

    #Variable setter
    for x in tokens:
      if index < len(tokens) - 1:
        if str(x).isalpha and tokens[index + 1] == "=":
          globals()[x] = (variable(tokens[index + 2]))
          used_variable_names.append(x)
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
  build_variable = ""
  is_building_number = False
  is_building_variable = False
  for x in code:
    if x.isnumeric():
      build_number = build_number * 10 + int(x)
      is_building_number = True
    elif is_building_number:
      tokens.append(build_number)
      build_number = 0
      is_building_number = False
    
    if x.isalpha():
      build_variable += str(x) 
      is_building_variable = True
    elif is_building_variable:
      tokens.append(build_variable)
      build_variable = ""
      is_building_variable = False

    for y in operators:
      if x == y:
        tokens.append(y)
    for y in symbols:
      if x == y:
        tokens.append(y)

  if is_building_number:
    tokens.append(build_number)
    build_number = 0
    is_building_number = False
  
  if is_building_variable:
    tokens.append(build_variable)
    build_variable = 0
    is_building_variable = False

  read_tokens = token_reader(tokens, code_line)
  if read_tokens != None:
    print("Lithon >", end=" ")
    print(" ".join(str(x) for x in read_tokens))
  code_line += 1