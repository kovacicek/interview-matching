## Problem


Suppose there are n apartments and n applicants. Each aplicant ranks the apartment in order of
preference, and the apartment has a ranking for all the applicants in the same way.
A match is any matching in a complete bipartite graph between the apartment and the applicant. 
It is called near-perfect if an applicant `i` and an apartment `j` do not exist such that the applicant prefers
`j` to his current apartment, and the apartment prefers `i` to its current tenant.
The goal is to compute one near-perfect set of matches from the `2n` stated preferences. 


## Example 1


Let's assign numbers from 1 to n to our applicants and apartments.
Inputs for each applicant or apartment are given in a line, 
where first number denotes their identifier and the remaining integers are their preferences.
First matrix, denotes applicant preferences and second apartment preferences.


Applicant preferences: 
```
1 4 3 1 2
2 2 1 3 4
3 1 3 4 2
4 4 3 1 2
```

Apartment preferences:
```
1 3 2 4 1
2 2 3 1 4
3 3 1 2 4
4 3 2 4 1
```

Our task is to find a set of matchings in which no two matches are found . Or in this case,

```
1 3
2 2
3 1
4 4
```





## Example 2

#### Input:

Apartment preferences:
```
1 3 4 2 1 6 7 5
2 6 4 2 3 5 1 7
3 6 3 5 7 2 4 1
4 1 6 3 2 4 7 5
5 1 6 5 3 4 7 2
6 1 7 3 4 5 6 2
7 5 6 2 4 3 7 1
```

Applicant preferences:
```
1 4 5 3 7 2 6 1
2 5 6 4 7 3 2 1
3 1 6 5 4 3 7 2
4 3 5 6 7 2 4 1
5 1 7 6 4 3 5 2
6 6 3 7 5 2 4 1
7 1 7 4 2 6 5 3
```

#### Output:

```
1 4
2 3
3 1
4 5
5 6
6 2
7 7
```


## Task


0. Design an algorithm which finds a set of near-perfect matches 
(NOTE: Design an algorithm in a way that an applicant proposes and apartment accepts or rejects.).

1. Design a parametrized test for example 1., 2. and/or additional cases.

2. Design a unit tests for edge cases.


## Open Questions

* Does the solution run in reasonable time? How fast and why?

* How would you deploy this application to production? Explain the design.

* Which design pattern could we apply in our design if we would need to extend our algorithm?
    * What do we need to adapt in our code to implement it?



## Answers and comments

There are two approaches submitted depending on the required complexity, execution time and processing power.

First approach is using python integrated items with reduces complexity.
Idea behind is 'who comes first has advantage', but with slight recalculation later on in the process 
in order to be able to replace potential tenant due to apartment preferences.
Nothing classy but I believe it does the job.
First test case works just fine, but second one is not passing for some reason.

Validation of the matrix is added before processing and it consists of:
matrix is not square matrix
matrix contains elements which are not ints
matrix contains integers which are not in range 1:N
matrix rows contains duplicates
With validation edge cases are covered

Stress tests could be testing with matrices with N = 100, 1000, 100000, ...
They are not implemented but matrices can be easily created with numpy, passed in the algorithm 
and results can be applied in test case. But it will be like creating test case for that specific output.
Actually we don't require to validate output but to check execution time.


Second approach is by weighted sums with goal of getting optimised result where in general 
'happiness/score' will be higher
Rearrange matrices in form:
    apl \ app
      1 2 3 4
    1
    2
    3
    4
multiply matrices element by element (not matrix multiplication) and get weighted sums.
There are few paths from this point on which can be used.
One of them is to proceed with machine learning and complex computations.
In that case we need to normalise matrices (put all numbers in range 0:1 by dividing by NxN)
Second one is to start from picking the highest products in weighted matrix. 
first test case will return
  2  2  9  4
  9 16  4  3
  16 3 12  8
  4  1  3  8
i.e. in first test case first pick 16 from position 2, 0
eliminate row 2 and column 0 and continue the process
...

Happy to discuss this approach!


Open Answers:
*
Solution for small number of items run in reasonable time (can be tested simply in jupyter notebook with timeit). 
For large number of items it would run fairly ok as complexity is not high and corner cases are covered.

*
Not sure how you need this application to be used
We can simply use s3 lambda. Creating servers with just one endpoint is not a great option.
If you want something 'fancy' for this docker image can be created, pushed to aws, adding cmd line arguments,
adding python as an entry point can simply run this. Various options...

*
Not sure how your code looks like, this can be standalone feature
