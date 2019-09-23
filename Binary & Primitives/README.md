# Binary & Primitive Questions

## Number of Bits

Given a positive integer as input, count the number of 1s in the binary representation of the number.
```
16 -> 1
32 -> 1
15 -> 4
```

## Parity

Parity of the number of ones in the binary representation of a number. If the parity is odd, return 1.

The linear solution is straight-forward. We can, however, do better than **O(n)** run-time in multiple ways. The time-complexity of the solution can be improved by adopting different algorithms. Superior complexities that can be achieved are **O(k)**, where 'k' is the number of set bits, **O(n/L)** where 'L' is the length of a look-up table and **O(log(n))**.

## Clear Last Bit

Given a number, return a number with its right most set bit cleared.

```
15 -> 14
```

The binary representation of 15 is '1111'. Upon clearing the right most bit, the number becomes '1110' which is 14 in decimal.

## Isolate Last Bit

Isolate the right most set bit of a number.

## Right Propagation

Propagate the right most set bit in **O(1)** time.

```
100100 -> 100111
010000 -> 011111
```

## Remainder

Write a function that accepts an arbitrary positive integer and a power of 2 as parameters, and returns the remainder when the integer is divided by the power of 2. Try to solve this in **O(1)** time.

## Divisible By 2

Implement a function that returns true if a number is divisible by a **power** of 2 in **O(1)** time.
