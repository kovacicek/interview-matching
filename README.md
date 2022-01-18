## Problem


Suppose there are n apartments and n applicants. Each aplicant ranks the apartment in order of
preference, and the apartment has a ranking for all the applicants in the same way. A match is any matching in a complete bipartite graph between the apartment and the applicant. It is called near-perfect if an applicant `i` and an apartment `j` do not exist such that the applicant prefers `j` to his current apartment, and the apartment prefers `i` to its current tenant. The goal is to compute one near-perfect set of matches from the `2n` stated preferences. 


## Example 1


Let's assign numbers from 1 to n to our applicants and apartments. Inputs for each applicant or apartment are given in a line, where first number denotes their identifier and the remaining integers are their preferences. First matrix, denotes applicant preferences and second apartment preferences.


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


NOTE: Design an algorithm in a way that an applicant proposes and apartment accepts or rejects.


0. Design an algorithm which finds a set of near-perfect matches.

1. Design a parametrized test for example 1., 2. and/or additional cases.

2. Design a unit tests for edge cases.


## Open Questions

* Does the solution run in reasonable time? How fast and why?

* How would you deploy this application to production? Explain the design.

* Which design pattern could we apply in our design if we would need to extend our algorithm?
    * What do we need to adapt in our code to implement it?
