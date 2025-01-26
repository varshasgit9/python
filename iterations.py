Iteration is the process of repeating a set of instructions or a block of code for a specified number of times or until a certain condition is met. It allows you to perform a task repeatedly, making it a fundamental concept in programming.

In iteration, a loop is created that executes a set of instructions repeatedly until a termination condition is reached. The loop can be controlled by a counter, a condition, or a combination of both.

Types of Iteration:

1. Finite iteration: The loop iterates for a fixed number of times.
2. Infinite iteration: The loop iterates indefinitely until a termination condition is met.
3. Conditional iteration: The loop iterates until a certain condition is met.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Python iterations:
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1. For Loop

Used to iterate over a sequence (such as a list, tuple, or string) or a range of values.


fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

2. While Loop

Used to iterate as long as a certain condition is true.


i = 0
while i < 5:
    print(i)
    i += 1

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

3. Nested Loop

Used to iterate over two or more sequences or ranges.


colors = ['red', 'green', 'blue']
shapes = ['circle', 'square', 'triangle']
for color in colors:
    for shape in shapes:
        print(color, shape)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

4. Loop Control Statements
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

- break: Used to exit a loop prematurely.
- continue: Used to skip the current iteration and move on to the next one.
- pass: Used as a placeholder when a statement is required syntactically, but no execution of code is necessary.


for i in range(5):
    if i == 3:
        break
    print(i)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

5. Enumerate

Used to iterate over a sequence and have an automatic counter/index.


fruits = ['apple', 'banana', 'cherry']
for i, fruit in enumerate(fruits):
    print(i, fruit)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

6. Zip

Used to iterate over two or more sequences in parallel.


colors = ['red', 'green', 'blue']
shapes = ['circle', 'square', 'triangle']
for color, shape in zip(colors, shapes):
    print(color, shape)
