# Lithon
This is a very basic and bad work in progress programming language based on python

## Documentation
### Functions and if statments:

**print:**
displays that line of code in the console

Example:

input:
```
print() 3 + 2
```
output:
```
5
```

**if:**
if you use == it will check if a statement is true and if it's false it will skip the next line and if you use != it will check if a statement is false and if it's true it will skip the next line

Example 1:

input:
```
if() 2 == 2
print() 3
print() 4
```

output:
```
3
4
```

Example 2:

input:
```
if() 2 == 3
print() 3
print() 4
```
output:
```
4
```

**input:**
it asks the user something with a promt

Example:

input:
```
input(a 3) Write a number
print() Your number times 2 is a * 2
```
and if we enter 3

output:
```
Write a number 3
Your number times 2 is 6
```
so the a in input() is the variable you want the input to be stored in
and the 3 is the data type where 1 = string 2 = float and 3 = integer

the text after input() is the promt you want to ask the user if there is no promt it will default to "input:"

### Counting:

**operators:**

" + " = addition

" - " = subtraktion

" * " = multiplication

" / " = division

" ^ " = exponents

" ' " = radicals

Example:

input:
```
print() 9 ' 2 
```

output:
```
3
```

### Variables:

variables can be any name made up of letters and underscores as long as it doesn't have the same name as a funtion or if statments

Example:

input:
```
a = 2 * 2
print() a
```

output:
```
4
```

### Data Types

There are only numerals, and strings kind of exist as you can print variables without a numeral value

Example 1:

input:
```
a = Hello
print() a
```
output:
```
Hello
```

Example 2:

input:
```
a = Hello World
print() a
```
output:
```
Hello
```
it only prints "Hello" as Hello World gets split up into different variables so World is by it's own and does nothing
but you can print things like this

Example 3:

input:
```
print() Hello World
```
output:
```
Hello World
```
### Syntax:

The syntax is very loose as you can put almost anything anywhere as long as there are values on both sides of an operator, so can you put you functions and if statments anywhere in the code

Example 1:

input:
```
print() 4
```
output:
```
4
```

Example 2:

input:
```
4 print()
```
output:
```
4
```
So both of these work exactly the same so as long as there are values on both sides of operators, it's a very free language syntax vise

### Errors:

In case of an error so will it print an error in the console and skip that line and continue on

Example 1:

input:
```
if() 3 = 2
print() 5
```
output:
```
'==' or '!=' missing from if statement: [ if() 3 = 2 ] line: [ 1 ]
5
```
Example 2:

input:
```
if() 3 == 2
print() 5
```
output:
```

```
it's going to print nothing because 3 does not equal 2 but in a case of an error it skips the entire if statement and goes to the next line where it says to print 5 so it does that
