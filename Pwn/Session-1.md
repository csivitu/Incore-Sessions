# Intro to Pwn
## Date 
Monday, 22 February 2021.
## Overview
- Intro to PWN
- How a programme works(binary programme)
- Stacks
- Registers
- Types of registers

## What Is Pwn
- Gaining illegal access to something such as a computer.
- One way is to run a command that a user did not call through binary exploitation.

## How a Programme Works
- The CPU executes a programme.
- In order to run a programme, data must be stored.(commands, variables etc.)
- This data is stored in RAM(Random Access Memory)
- The CPU uses RAM in place of the hard disc because it is much faster to access
- RAM can be visualised as a large collection of memory cells of one byte each. 
- Each memory cell has a unique address(like a list has indices). 
- Most variables stored are greater than one byte, hence each variable’s address is identified as the address of the first byte.
- Memory addresses are defined by the hardware. A 64 bit processor can access 2^64 memory addresses and a 32 bit processor can access 2^32 memory addresses. However, the RAM need not necessarily be of that size.
- A programme divides the RAM into four major parts:
  * Code: This is where the instructions for the program are stored.
  * Heap: For dynamic memory allocation. (MALLOC) 
  * Data: Stores global variables and constants.
  * Stack: stores local variables

## Stacks
- It is a linear data structure where the addition and removal of items can take place only from one end. This end is known as the “top” and the opposite end is known as the “base”.
- The two operations you can perform on a stack are:
  * Push: inserting item into stack(always from the top)
  * Pop: removing an item from the stack(always from the top)
- A stack grows when loops are nested. 
- The more the recursion the larger the stack
- Maximum recursion depth indicates the size of the stack.

## Registers
- Registers are storage spaces inside of a processor. 
- They are similar to the cells of RAM but much faster. 
- We use registers over RAM because they are faster to access.
- A processor takes instructions, stores data in registers and then runs the instructions

## Types of registers
- RIP(register instruction pointer)
  * An RIP holds the memory addresses of the current instruction being executed.
- RBP(register base pointer)
  * The pointer which points to the base of the stack.
- RSP(register stack pointer)
  * Pointer which points to the top of a stack.


