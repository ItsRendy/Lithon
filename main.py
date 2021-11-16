print("Lithon 0.1.2 (default, Nov 16 2021, 23:32)")

with open("code.txt") as word_list:
    code_list = list(word_list.read().splitlines())

variables = {}

def error(line, error):
  #General
  if error == 1:
    print("\033[31m" + "invalid code: [", code_list[line], "] line: [", line + 1, "]" + "\033[0m")
  #If statment
  if error == 2:
    print("\033[31m" + "'==' or '!=' missing from if statment: [", code_list[line], "] line: [", line + 1, "]" + "\033[0m")
  #Inputs
  if error == 3:
    print("\033[31m" + "invalid input data type: [", code_list[line], "] line: [", line + 1, "]" + "\033[0m")
  if error == 4:
    print("\033[31m" + "input variable cannot be a numeral: [", code_list[line], "] line: [", line + 1, "]" + "\033[0m")

def token_reader(tokens, line):
  index = 0
  number = 0
  is_calculating = False
  is_printing = False
  if_statment = False
  is_input = False

  try:
    for x in tokens:
      for y in operators:
        if x == y:
          is_calculating = True

    #Variable to value converter
    while index < len(tokens):
        for x in used_variable_names:
          if index == len(tokens) - 1 and tokens[index] == x:
            tokens.pop(index)
            tokens.insert(index, variables[x])
            index = 0
            continue
          if tokens[index] == x and tokens[index + 1] != "=":
            tokens.pop(index)
            tokens.insert(index, variables[x])
            index = 0
        index += 1
    index = 0
    
    #functions
    #print
    while index < len(tokens):
      if tokens[index] == "print" and tokens[index + 1] == "(" and tokens[index + 2] == ")":
        is_printing = True
        tokens.pop(index)
        tokens.pop(index)
        tokens.pop(index)
        index = 0
        break
      index += 1
    index = 0

    #if statments
    while index < len(tokens):
      if tokens[index] == "if" and tokens[index + 1] == "(" and tokens[index + 2] == ")":
        if_statment = True
        tokens.pop(index)
        tokens.pop(index)
        tokens.pop(index)
        index = 0
        break
      index += 1
    index = 0

    #input
    while index < len(tokens):
      if tokens[index] == "input" and tokens[index + 1] == "(" and tokens[index + 4] == ")":
        is_input = True
        input_variable = tokens[index + 2]
        input_type = tokens[index + 3]
        if input_type < 1 or input_type > 3 or isinstance(input_type, int) == False:
          error(line, 3)
          return
        if isinstance(input_variable, int) or isinstance(input_variable, float):
          error(line, 4)
          return
        tokens.pop(index)
        tokens.pop(index)
        tokens.pop(index)
        tokens.pop(index)
        tokens.pop(index)
        index = 0
        break
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
          variables[x] = tokens[index + 2]
          used_variable_names.append(x)
      index += 1
    index = 0 

    
    #If statment funktion
    while index < len(tokens):
      if if_statment == True:
        if "==" in tokens or "!=" in tokens:
          if tokens[index] == "==":
            if tokens[index - 1] == tokens[index + 1]:
              break
            else:
              return False
          if tokens[index] == "!=":
            if tokens[index - 1] != tokens[index + 1]:
              break
            else:
              return False
        else:
          error(line, 2)
          return
      index += 1
    index = 0

    #Input funktion
    while index < len(tokens) + 1:
      if is_input == True:
        if len(tokens) == 0:
          input_text = "input:"
        else:
          input_text = " ".join(str(x) for x in tokens) 
        input_text = input_text.ljust(len(input_text) + 1)
        if input_type == 1:
          Input = str(input(input_text))
        if input_type == 2:
          Input = float(input(input_text))
        if input_type == 3:
          Input = int(input(input_text))
        variables[input_variable] = Input
        used_variable_names.append(input_variable)
        tokens = []
        break
      index += 1
    index = 0

  except:
    error(line, 1)
    return
  if is_printing:
    return tokens

#Tokens creator
code_line = 0
stop = None
used_variable_names = []
operators = ["+", "-", "*", "/", "^", "'"]
symbols = ["(", ")"]
for code in code_list:
  tokens = []
  build_number = 0
  build_variable = ""
  build_symbol = ""
  is_building_number = False
  is_building_variable = False
  is_building_symbol = False

  for x in code:
    if x.isnumeric():
      build_number = build_number * 10 + int(x)
      is_building_number = True
    elif is_building_number:
      tokens.append(build_number)
      build_number = 0
      is_building_number = False
    
    if x.isalpha() or x == "_":
      build_variable += str(x) 
      is_building_variable = True
    elif is_building_variable:
      tokens.append(build_variable)
      build_variable = ""
      is_building_variable = False
    
    if x == "=" or x == "!":
      build_symbol += str(x) 
      is_building_symbol = True
    elif is_building_symbol:
      tokens.append(build_symbol)
      build_symbol = ""
      is_building_symbol = False

    for y in symbols:
      if x == y:
        tokens.append(y)
    for y in operators:
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

  if is_building_symbol:
    tokens.append(build_symbol)
    build_symbol = ""
    is_building_symbol = False

  read_tokens = token_reader(tokens, code_line)

  #checks if statments
  if read_tokens == False:
    stop = code_line + 1

  #prints stuff
  if read_tokens != None and read_tokens != False and code_line != stop:
    stop = None
    print("Lithon >", end=" ")
    print(" ".join(str(x) for x in read_tokens))
  code_line += 1