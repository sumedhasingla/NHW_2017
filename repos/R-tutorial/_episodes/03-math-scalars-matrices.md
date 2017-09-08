---
title: "Math with scalars and matrices"
teaching: 10
exercises: 5
questions:
- "How do I work with matrices?"
- "How do I create sequences of numbers?"
- "What are the logical operators?"
objectives:
- "Learn how matrix math works in R"
- "Learn how to create sequences"
keypoints:
- Most math is what you'd expect it to be, except matrix multiplication
- The diag() function is multipurpose (Extract or replace the diagonal of a matrix, or construct a diagonal matrix)

---

# Basic math with scalars and matrices
In the previous section we saw scalar math works in the usual way, but here are a couple of extras.

```r
3 + 2
3 - 2
3 / 2
3 * 2
3 %% 2 # modulus 3 mod 2
3^2
# You can also use
3**2
sqrt(3)
```
Matrix math is a bit cumbersome!  Three key strokes for  the multiplication symbol...oh well.  

```r
a = matrix(c(1, 2, 3, 2, 1, 2, 2, 2, 1), nrow = 3)
a
# transpose
t(a)
# multiplication
a%*%a
# inverse 
solve(a)
```
Extracting parts of a matrix is similar to other programs.

```r
a = matrix(c(1:9), nrow = 3)
a
# First row
a[1,]
# First column
a[,1]
# Second and third entry of the third row
a[3, 2:3]
```

# Creating sequences
I've been using, for example, code like c(1:9) to create sequences, but there are other options.

```r
# sequence from 1 to 9
seq(1, 9)
# sequence from 1 to 9 in increments of 2
seq(1, 9, 2)
# sequence that count from 1 to 9 in increments such that the vector has a length of 11
seq(1, 9, length.out = 11)
```

# Logical operators
The usual logical operators are available as well.

```r
a = c(1, 2, 3)
b = c(2, 2, 1)

a<b
a<=b
a>b
a!=b
a==b
```
You can also combine using and/or.

```r
c = c(4, 2, 1)

(a==b) & (b==c)

(a==b) | (b==c)
```
Handily (at least I think so) if you try to do math with a vector of TRUE/FALSE, the data are treated as 1/0 (1=TRUE)

```r
d = (a==b)
2*d
```
You can use logical operators to pull out parts of a matrix or change the matrix

```r
a = matrix(1:9, nrow = 3)
# Values in a that are larger than 3
a[a>3]
# Change values larger than 3 to 0
a[a>3] = 0
a
```

# On your own
Create a matrix with 3s on the main diagonal and 0s elsewhere and invert it.  Above you created an array called array.ex that is basically two 4x3 matrices stacked in the third dimension. Multiply together the first 4x3 matrix and the transpose of the second 4x3 matrix.

# Summary of functions 

Function Name | What it does
------------------------- | -------------------------
%% | Modulus
^ or ** | raise a number to a power
sqrt | square root
t() | Transpose of a matrix
%*% | Matrix multiplication
solve() | Matrix inverse
a[b,] | extract bth row from matrix, a
a[,b] | extract bth column from matrix, a
<, <=, >, >=, ==,!= | Logical operators
&, \| | "And" and "Or"
