
# Algorithms 

The repository contains 5 solved algorithms.
Each algorithm implementation is in a separate folder along with the corresponding unit tests.



## Authors

- [@Monoloqu3](https://github.com/Monoloqu3)


## License

[MIT](https://choosealicense.com/licenses/mit/)


## Requirements
* Python 3.10

## Description/Usage

[**Fib**](https://github.com/Monoloqu3/algorithms_wsb/tree/0f7ebe47c72125a27ba8b5b2a504b3acfe86c634/fib)

***Description***:

Print out the n-th entry in the fibonacci series.
The fibonacci series is an ordering of numbers where
each number is the sum of the preceeding two.
For example, the sequence [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
forms the first ten entries of the fibonacci series.

***Example/Usage:***
```Python
fib(4) # returns 3
```

[**Matrix**](https://github.com/Monoloqu3/algorithms_wsb/tree/0f7ebe47c72125a27ba8b5b2a504b3acfe86c634/matrix)

***Description***:

Write a function that accepts an integer N
and returns a NxN spiral matrix.

***Example/Usage:***

```Python
matrix(2)     
# returns 
# [[1, 2],
# [4, 3]]
matrix(3)
# returns 
# [1, 2, 3],
# [8, 9, 4],
# [7, 6, 5]]
matrix(4)
# returns 
# [[1, 2, 3, 4],
# [12, 13, 14, 5],
# [11, 16, 15, 6],
# [10, 9, 8, 7]]
```

[**Queue**](https://github.com/Monoloqu3/algorithms_wsb/tree/0f7ebe47c72125a27ba8b5b2a504b3acfe86c634/queue)

***Description***:

Create a queue data structure.  The queue
should be a class with methods 'add' and 'remove'.
Adding to the queue should store an element until it is removed.

***Example/Usage:***
```Python
q = Queue()
q.add(1)
q.remove() # returns 1
```

[**Stack**](https://github.com/Monoloqu3/algorithms_wsb/tree/0f7ebe47c72125a27ba8b5b2a504b3acfe86c634/stack)

***Description***:

Create a stack data structure.  The stack
should be a class with methods 'push', 'pop', and
'peek'.  Adding an element to the stack should
store it until it is removed.

***Example/Usage:***
```Python
s = Stack()
s.push(1)
s.push(2)
s.pop() # returns 2
s.pop() # returns 1
```
[**Vowels**](https://github.com/Monoloqu3/algorithms_wsb/tree/0f7ebe47c72125a27ba8b5b2a504b3acfe86c634/vowels)

***Description***:

Write a function that returns the number of vowels
used in a string.  Vowels are the characters 'a', 'e'
'i', 'o', and 'u'.

***Example/Usage:***
```Python
vowels('Why do you ask?') # returns 4
```
## Unit tests

***Description***:

Each algorithm has dedicated unit tests collected in `test.py` file.

***Example/Usage:***
```Python
unittest.main() # runs all tests
```



