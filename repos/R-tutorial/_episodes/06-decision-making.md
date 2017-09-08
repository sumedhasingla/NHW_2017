---
title: "Decision making"
teaching: 5
exercises: 10
questions:
- "How do I set up an if/else statement?"
objectives:
- "Learn both the if/else and ifelse styles of setting up a decision statement"
keypoints:
- ifelse() is a great shortcut if you have a simple statement

---

#If/else two ways

The if/else statement is frequently used in programming and there are a couple of ways to do it in R.  The classical style is in the following example.

```r
x = -5
if(x > 0){
   print("Non-negative number")
} else {
   print("Negative number")
}
```
A shortcut for simple if/else statement is the ifelse function

```r
ifelse(x>0, "Non-negative number", "Negative number")
```
The if/else statement can have nesting as well

```r
if (x < 0) {
   print("Negative number")
} else if (x > 0) {
   print("Positive number")
} else {
   print("Zero")
}
```
# On your own
The Fibonacci numbers are the sequence of numbers defined by the
linear recurrence equation Fn = Fn−1 + Fn−2 where F1 = F2 = 1.  So the
first 5 terms are 1, 1, 2, 3, 5. Using a for loop and if statement,
generate the first 8 terms of the Fibonacci sequence.  No cheating by
starting off with a c(1,1) vector and adding to it :)

# Summary of functions 

Function Name | What it does
------------------------- | -------------------------
if(condition){}else{}  | Structure of if/else
ifelse(condition, true, false) | Shorter if/else option
