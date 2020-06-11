# Graphical Data Structures - Union Disjoint Sets

Many problems that involve a set of items and their relations can be modeled in a natural way using graphical data structures.  
However the way of representation makes a lot of difference in runtime as well as storage complexity of these data structures.

Union Disjoint Set is just another candidate which helps us with a better and efficient representation in some cases of graphical interpretation of related items.

This data structures shine where we need to connect items which are initially disconnected, and at the same time find if two items are connected directly or indirectly.

**Note: Best Complexity for finding connected components in a graph is O(V+E), this is given by Tarjan's Algorithm.**  

## The Operations  

We then define two operations :
- `Union(A,B)` : This will connect item A to item B
- `Find(A,B)` : This will tell if A and B are somehow connected or not.

Initial implementation is basically the fact that lets say we have a set of elements, tagged 1-10.  
We define an array `Arr[1..10]` such that `Arr[i]` = i (i.e, `Arr[2] = 2, Arr[5] = 5,...`and so on).


- Then we define `Union(A,B)` as making `Arr[B] = Arr[A]`
- `Find(A,B)` as checking if `A[A] == A[B]`

So our DS class looks something like this:

```python
##Union Disjoint Data Structure

class UnionDisjoinSet:
	def __init__(self,A):
		self.arr = A

	def union(self,a,b):
		tag = self.arr[a]
		for i in range(len(self.arr)):
			if self.arr[i] == tag: #elements in A's set
				self.arr[i] = self.arr[b]

	def find(self,a,b):
		return self.arr[a] == self.arr[b]

```
This will be super inefficient, complexity is O(n^2) .

We clearly need to improve on this. But how?

## Rooting

We define the idea of parent, child and root in our graph.

- Parent is the node which is on an upper level and is connected to a node called it's child node on a lower level.
- Initally parent of all nodes in our array is the node number itself, hence `Parent(A) = Arr[A]`.
- We define `Root(A)` as a special element of the subset who is parent of itself.

Using these ideas we change the `Union(A,B)` and `Find(A,B)`.

We now define `Union(A,B)` to set `Parent(Root(A))` equal to `Root(B)`.
And similar to this, `Find(A,B)` becomes nothing but checking if `Root(A) == Root(B)`.

```python
##Union Disjoint Data Structure

class UnionDisjoinSet:
	def __init__(self,A):
		self.arr = A

	def root(self,a):
		if self.arr[a] == a:
			return a
		else:
			return self.root(self.arr[a])

	def union(self,a,b):
		self.arr[self.root(a)] = self.root(b)

	def find(self,a,b):
		return self.root(a) == self.root(b)

```

This gives us no improvement at all, infact its slower as we may get imbalanced trees with horrible complexity.  
We clearly need to tune `Union(A,B)` in such a way that after applying this operation, final tree we get is balanced.

## Weighted Union

This is what we do to take care of having a balanced tree after `Union(A,B)` operation.
We keep a record of how many elements each of our subset have, then while performing the `Union(A,B)` operation, we check which of the subset out of the two has lesser number of elements, and once we find that out, we simply join root of this subset to root of other subset.  

This way we keep our tree balanced. And we loved balanced tree becuase we love logarithmic complexity!

```python
##Union Disjoint Data Structure

class UnionDisjoinSet:
	def __init__(self,A):
		self.arr = A
		self.size = [1 for _ in range(len(A))] #initial size of all subsets is 1

	def root(self,a):
		if self.arr[a] == a:
			return a
		else:
			return self.root(self.arr[a])

	def union(self,a,b): #weighted union
		if(self.size[self.root(a)] >= self.size[self.root(b)]):
			self.arr[self.root(a)] = self.root(b)
			self.size[self.root(a)] += self.size[self.root(b)]
		else:
			self.arr[self.root(b)] = self.root(a)
			self.size[self.root(b)] += self.size[self.root(a)]

	def find(self,a,b):
		return self.root(a) == self.root(b)

```
## The Competitve Trick! - Path Compression

Sometimes all it takes to win a contest is a little insight, Quite honestly thats the only thing that makes difference between individuals.
Like this little trick is also an insight but we will se how effective this will endup to be.

First improvement we can do to our utility class is improving `Root(A)`.Its recursive and intuitve but slow, lets first turn it into iterative equivalent.

```python
	def root(self,a):
		index = a
		while(self.arr[index] != index):
			index = self.arr[index]
		return index
```
Note how we point index to its parent in each iteration, current complexity of doing this is O(# of levels), which in our case of weighted union disjoint set is log(n).

Now the little insight, **how about instead of pointing current index to its parent node, we rather point it to its grand parent?**  

```python
	def root(self,a):
		index = a
		while(self.arr[index] != index):
			index = self.arr[self.arr[index]]
		return index
```
We have now reduced our complexity from O(log(n)) to O(log*(n)).

`log*(n)` is called as the iterative log function, which is mathematically equivalent to log(log(log(........log(n)))).  
This function increases so slowly that its works like a pseudo constant function.

## Applications

- This data structure is widely used to detect cycles in undirected graphs. 
- Its a part of Kruskal's MST algorithm.
- Used in Social Information Network analysis. (LinkedIn)
- Used to find connected components in graph.


## Mini Project

- Microsoft Internship 2020  (OffCampus)

We define a network of N natural numbers except 1, In this network, each of the elements is connected to the elements who are its divisors.  
For example, 6 is connected to 2 and 3. 2 and 3 in turn are connected to all of their multiples upto N.

You will be asked `Q` questions, in each question you will be two numbers `A` and `B`. You need to tell if they are connected to each other or not.

`1 <= Q <= 10^5`  
`1 <= N <= 10^5`  
`1 <= A, B <= N, A != B`  

- [Monk's BDay Treat](https://www.hackerearth.com/challenges/competitive/code-monk-graph-theory-i/algorithm/monks-birthday-treat/)

