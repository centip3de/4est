Hack Into the Lottery
======================
This challenge is to output the number, '18446744073709551615' (otherwise known as the max number
for an unsigned 64 bit int), without having the numbers 1, 2, 4, 6, or 8 in your source code.

Link to challenge: https://codegolf.stackexchange.com/questions/110748/hack-into-a-lottery

Explaination
-------------
Below is the best solution I could come up with, which is 16 bytes total, along with an explaination of the code.

Here's the minified code:
```
D3D5+U*D3D5-^d.
```

And below is the explained version:
```
D3 // Push 3 to the stack.
D5 // Push 5 to the stack.
+  // Pop off two values on the stack, add them together, and push the result back on the stack, giving us 8.
U  // Dup the top element of the stack, giving us [8, 8].
*  // Pop off two values on the stack, multiply them together, and push the result back on the stack, giving us 64.
D3 // Push 3 on the stack.
D5 // Push 5 on the stack.
-  // Pop off two values on the stack, subtract them, and push the result back on the stack, giving us 2.
^  // Pop off two values on the stack, perform exponentiation (in this case 2^64), and push the result back on the stack, giving us 18446744073709551616.
d  // Pop off the top value on the stack, decrement it, and push the result back on the stack, giving us 18446744073709551615.
.  // Print the top of the stack
```

Since we're trying to output the largest 64 bit unsigned number, we can simply calculate this with (2^64) - 1. Now in order to calculate the numbers for that, we're going to have to be a little creative due to the constraints imposed by the problem. The way I decided to get the number '64' was to multiply 8 and 8 (due to 8^2 being not allowed because it involves a '2'). I created each '8' by adding together 3 and 5, which are numbers that we're allowed to use. To get the '2', I did something similar by subtracting 3 from 5. Finally all that we had to do was perform the exponentiation (2^64), and then using the decrement operator to subtract 1.
