---
title: "Loops"
teaching: 10
exercises: 5
questions:
- "How do I make a loop?"
- "What will slow down a loop?"
objectives:
- "Learn how to make a for loop and while loop"
- "Learn some loop avoidance tricks"
keypoints:
- Avoid building a vector/matrix in a loop using concatenation
- Looping is faster now than it used to be, but avoiding loops is
  typically a good idea

---

# For loops
Looping in R has similar structure to other programs.  Basically, you can loop through anything: numbers, characters, factors, etc.

```r
a = c("one", "two", "three")
for (i in a){
  print(i)
}

a = c(1:3)
for (i in a){
  print(i)
}

# Equivalently
for (i in 1:3){
  print(i)
}
```
If you're building a vector with a for loop, it is better to create an empty vector first and fill it.  The following illustrates the two styles and introduces the proc.time() function, which can be used to time procedures in R.

```r
start = proc.time()
# Initialize with a vector of 0s
vec = rep(0, 10000)
for (i in 1:10000){
  vec[i] = i
}
proc.time() - start


start = proc.time()
# Initialize with an empty vector 
vec = c()
for (i in 1:10000){
  #concatenate on each iteration
  vec = c(vec, i)
}
proc.time() - start
```
# While loops
While loops are used when you don't know how long something will take.  For example, if I'm randomly generating trial orderings, but I have 3-4 criteria that must be met for that trial order to work in my experiment I use a while loop.  For example, no more than 3 trials of the same type in a row, etc.


```r
# Start simple
stop = 10

while (stop > 1){
  print(stop)
  stop = stop -1
}
```
Historically R has been very, very slow at looping and it is often advised to avoid loops when you can.  Matrix math tricks can often help, if you're comfortable with that, but there are also functions that can help cut down on looping.  The apply() function is a good example.  It allows you to apply an operation along one of the dimensions of an array.

```r
# I'll get row averages
a = matrix(c(1:9), nrow = 3)
apply(a, 1, mean)
# Column averages
apply(a, 2, mean)

# Standard deviation within each row
apply(a, 1, sd)

# Works on arrays also.  
b = array(c(1:12), c(2, 3, 2))
# If I want the sum across the first dimension
# then the result is in the 2:3 dimensions
apply(b, c(2:3), sum)

# If I want the sum within each of the 3rd dimensions
apply(b, 3, sum)
```
# On your own
Write the for loops that give the same results as the two apply function examples above.

# Summary of functions 

Function Name | What it does
------------------------- | -------------------------
for (x in variable){} | Basic for loop structure
while (logical){} | Basic while loop structure
sample()  | Sample data with or without replacement
apply()  |  Apply an operation along dimension(s) of an array
mean()  | Average
sum()  | Summation function
