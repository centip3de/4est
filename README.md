# 4est
-----
4est (or Forest) is a stack based language written in Python with code golfing in mind. Examples can be found in the examples folder.

## Overview
* 4est is a stack based language where all OPs are a single character in order to facilitate code golfing. * 4est uses implict pushing to the stack, where all literals (Integers, Strings, Booleans, etc.) are pushed onto the stack immediately when they're "declared".
* Likewise, the results of computations or operations are also pushed onto the stack.
* The entire language save for blocks (e.g. iteration blocks, if blocks, etc.) is written in reverse polish notation.
* There are no variables in 4est.

## OPs:

|OP|Description|
--|---------------
|`.`| Prints the top of the stack to stdout (does not pop the top element of the stack)
|`,`| Get user input and push it to the top of the stack. Numbers are automatically converted to integers.
|`D<int>`| Push a number down on the stack.
|`"<str>"`| Push a string down on the stack
|`U`| Duplicate the top element of the stack, e.g. `[a]` -> `[a, a]`
|`S`| Swap the two top elements of the stack, e.g. `[a, b]` -> `[b, a]`
|`C`| Clear out the stack, e.g. `[a, b, c]` -> `[]`
|`$`| Clear all but the bottom element of the stack, e.g. `[a, b, c]` -> `[a]`
|`+`| Pop off the top two elements of the stack, add them together, then push the result back on the stack
|`-`| Pop off the top two elements of the stack, subtract them, then push the result back on the stack
|`*`| Pop off the top two elements of the stack, multiply them, then push the result back on the stack
|`/`| Pop off the top two elements of the stack, divide them, then push the result back on the stack
|`^`| Pop off the top two elements of the stack, perform the exponentiation, then push the result back on the stack
|`%`| Pop off the top two elements of the stack, perform modulo, then push the result back on the stack
|`=`| Pop off the top two elements of the stack, compare them, then push the result back on the stack
|`!`| Pop off the top element of the stack, negate it, then push the result back on the stack
|`O`| Pop off the top element of the stack
|`?`| Pop off the top element of the stack, if it's true, execute the inner block. If it's false, execute the else block.
|`#`| If the previous if-statement resulted in a false, execute this inner block.
|`;`| End-if, required at the end of every if-statement (a correct if-statement looks like: `?<statements>#<statements>;`)
|`I`| Iteration block, peeks at the top element of the stack, if it's true, execute the inner block. Repeat while the top of the stack is true (note -- the top of the stack only has to be true/false when the loop condition is being evaluated again). If it's false, skip the inner block.
|`E`| End iteration token, required at the end of every iteration block (a correct iteration statement looks like: `I<statements>E`)
|`T`| Pushes boolean `True` value onto the stack
|`F`| Pushes boolean `False` value onto the stack
|`|`| Pops off the top two elements of the stack, performs a logical or on them, then pushes the result back on the stack
|`&`| Pops off the top two elements of the stack, performs a logical and on them, then pushes the result back on the stack

## Example:


### Fizzbuzz:

Below is a fully documented example of FizzBuzz, along with a minified version:
```
 , // Get input
 U // Dup input
 D0 // Push down 0
 = // Compare the input to 0
 ! // Negate the comparison
 I // Iterate until the stack is 0
     O // Pop off that equality
     U // Duplicate the top of the stack so we don't clober shit
     D3 // Push down 3 for comparison
     S // Swap the top two for accurate modulo
     % // Check if the number is divisible by 3, push result on stack
     D0 // Push down 0 for comparison
     = // Pop off the previous 2 and push on equality result
     ? // If the top of the stack is True
         O // Pop off the equality result
         U // Dup the top of the stack so we don't clober
         D5 // Push down 5 for comparison
         % // Modulo the last two numbers (check if divisible by 5)
         S // Swap the top two for accurate modulo
         D0 // Push down 0 for comparison
         = // Perform equality
         ? // If this is also divisible by 5 push "Fizzbuzz"
             O // Pop off the equality result
             "FizzBuzz" // Push FizzBuzz to the top of the stack,
                        // to be printed if this is divisible by 3 and 5
         # // If this isn't divisible by 5
             "Fizz" // If this is divisble only by 3,
                    // we need to push "Fizz" to the top of the stack
         ; // Endif
     # // If this isn't divisible by 3
         O // Pop off the equality result
         U // Dup the top of the stack so we don't clober
         D5 // Push down 5 for comparison
         S // Swap the top two for accurate modulo
         % // Modulo the last two numbers (check if divisible by 5)
         D0 // Push down 0 for comparison
         = // Perform equality
         ? // If this is divisible by 5 push "Buzz"
             O // Pop off the equality result
             "Buzz"
         # // Else
             O // Pop off the equality result
             // Don't push anything, we want to print the number
             // here if it isn't divisible by 5 or 3
         ; // End if
     ; // End if
     . // Print the output
     $ // Remove all but the bottom of the stack
       // (to clear off everything except the "root" number)
     D1 // Add 1 to subract
     S // Swap so we don't get a negative
     - // Perform the subraction
     U // Dup the result
     D0 // Push down 0
     = // See if the current amount is equal to 0
     ! // Negate the comparison
 E // End loop
 ```


Minified version:
 ```
,UD0=!IOUD3S%D0=?OUD5S%D0=?O"FizzBuzz"#"Fizz";#OUD5S%D0=?O"Buzz"#O;;.$D1S-UD0=!E
```
