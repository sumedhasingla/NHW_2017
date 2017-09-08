---
title: "Writing functions"
teaching: 10
exercises: 5
questions:
- "Why would I use a function and how do I set one up?"
objectives:
- "Learn how to write basic functions in R"
keypoints:
- Be careful with global variables.  Make sure all variables
  referenced in your function are either fed in or created within the function

---

# Simple functions
If you find yourself copying and pasting a chunk of code to reuse it, you should probably just write a function for that code.  Functions are also useful if you're looking to do something using the apply() function that doesn't have a function to apply already.  For example, if I want to run a regression over 10,000 voxels and save the p-value, I can create a function that spits out p-values and then use that with apply to run all of my 10,000 models at once!  It is a bit faster than looping.  First, let's look at a simple example.  Note that lists are often used to pass information out of the function using the return() function.

```r
# Simple function that determines if a number is odd

isodd = function(input){
  output = input%%2  # modulo operation from earlier
  result = output == 1
  return(result)
}
isodd(5)
isodd(6)
```
Here's an example with two input and two values output

```r
sumprod = function(val1, val2){
  sumvals = val1 + val2
  prodvals = val1*val2
  result = list()
  result$sumvals = sumvals
  result$prodvals = prodvals
  return(result)
}
sumprod(1, 5)
sumprod(4, 10)
```
One thing to be very careful about with functions is that although they are set up to take in variables to do something locally and then pass this back out to the global environment, it can (unfortunately) also use global variables.  In other words, if you already defined x in your R session and you refer to x within your function, the function will work if you forget to feed it in.

```r
x = 5
junkFunction = function(a, b){
  ax = a*x
  bx = b*x
  result = list()
  result$ax = ax
  result$bx = bx
  return(result)
}
# Even though x isn't fed in, the function grabs it from the global environment.  BE CAREFUL!!
junkFunction(3, 4)
```

# On your own
Building off the previous exercise, write a function called
makeFibonacci() that takes as input an integer and then generates that
many terms of teh Fibonacci sequence. In other words makeFibonacci(10)
would generate the first 10 terms.
