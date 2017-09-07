Truth Machine
===========
The Truth Machine challenge is to write a program that takes in user input, and on a 0 exits, and on a 1 prints the number `1` forever (until it runs out of memory or is terminated).

Here's a link to post for a full explaination and to see other entries: https://codegolf.stackexchange.com/questions/62732/implement-a-truth-machine

Solution and explaination
--------------------------
Below is the best solution I could come up with, which is 4 bytes total, along with an explaination of the code.

Here's the minified code:

`,I.E`

And below is the explained version:

```
, // Get user input and push it to the stack (this automatically
  // converts strings to integers if possible)
I // Iterate while the top of the stack is true
. // Print the top of the stack
E // End-of-iteration marker
```

Because the evaluation of whether something is true or not is in Python, we can use Python's truthiness to our advantage. In Python any integer that isn't a `0` has a truthiness value of `True`, with `0` having a truthiness value of `False`.

This means when we're evaluating our loop condition, a `0` inserted on the stack will result in the program not executing the loop, and a `1` (or any other integer) resulting in the loop body being executed, which just prints `1` forever.

