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
checks if a statment is true and if it's false it will skip the next line

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

There are only numerals and strings kind of exist as you can print variables without values and they won't be counted as a numeral but this means spaces don't excist

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

Example 2

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
So both of these work exactly the same so as long as there are varlues on both sides of operators, it's a very free language syntax vise

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
'==' missing from if statment: [ if() 3 = 2 ] line: [ 1 ]
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
it's going to print nothing because 3 does not equal 2 but in a case of an error it skips the entire if statment and goes to the next line where it says to print 5 so it does that
