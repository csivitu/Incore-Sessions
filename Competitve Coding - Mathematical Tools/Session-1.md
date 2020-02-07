# Mathematical Tools for Competitve Coding

## Motivation

Some problems might need a lot of work to even get started with, others can't even be solved if certain mathematical tricks are not known to the contestant beforehand.  
Some improve the computation speed in general, others help you reduce amount of code you need to write in order to achieve same result.

## Topics discussed

- Modular/Binary/Squaring exponenetiation
- Stars and Bars
- Euclidean Algorithm and Linear Diophantine Equations

<hr>

## Modular/Binary/Squaring exponenetiation

Idea here is really simple. If you have to evaluate an expression a^b, the normal way of doing it will lead to a runtime complexity of O(n) or O(exponent). We can achieve much better (Logarithmic).

Idea is to write a^b as (a^(b/2))^2 (considering b is even)  
or,  
as a\*(a^(b/2))^2 (considering b to be odd)

This can be done recursivley as:

```python
#Non modular version, power by squaring only.

def mod_pow(base,exp):
	if exp == 1:
		return base
	elif exp == 0:
		return 1
	else:
		halfAns = mod_pow(base,exp//2)
		if(exp%2==0):
			return halfAns**2
		else:
			return base*(halfAns**2)

```

I really hope you guys know that recursive things take up lot of extra memory. Hence, we can do it in a better way (iteratively with a little bit magic).

```python
#Non modular iterative version, power by squaring only.

def mod_pow(base,exp):
	binExp = bin(exp)[2:]
	ans = 1
	for d in binExp:
		if(d=='1'):
			ans*=base
		base=base*base
	return ans

```

### Note : Python has `pow(base,exp,mod)` method inbuilt <3

## Stars and Bars

Problems that envolve you two arrange N similar items into K unique boxes can be solved by an extended version of simple Binomial Coefficient, also known and Stars and Bars method.

Above statement boils to number of solutions of an equation:

```maths
 A + B + C = N , where A,B,C,N are all non negative integers.
```

For example, X + Y = 3,  
Here N = 3, and K = 2 (No. of variables/boxes)

```maths
We can visualize it as *|** , **|* , ***| ans so on.

Problem hence reduces to take out N items out of N+K-1 items, which can be given by Combination(N+K-1,N) or Combination(N+K-1,K-1)

Given: Combination(n,r) = n!/((r!)(n-r)!)
```

This formula also gives the ways to take out K numbers in a sorted order out of a range of 1 to N. I encourage you folks to try to prove it.

Related Problem: Two Arrays [https://codeforces.com/problemset/problem/1288/C]

## Euclidean Algorithm and Linear Diophantine Equations

Euclid gave what is also known as first ever documented algorithm known to Mankind, An algorithm to find GCD/HCF of two numbers.  
Python has `math.gcd(a,b)` where as C/C++, GNU GCC (not Clang or MinGW) has `_gcd(a,b)` builtin.

### Bézout's identity — Let a and b be integers with greatest common divisor d. Then, there exist integers x and y such that ax + by = d. More generally, the integers of the form ax + by are exactly the multiples of d.

This identity is widely used in contest coding with different flavours and style, bottom line however reamins same, that if GCD(a,b) = 1, the expression aX+bY can assume any value, otherwise it cannot.

<hr>

## Mini Project
Read about extended Euclidean algorithm, modular inverse and use of number `10^9+7` in competitve coding.

