---
title: "How data are stored"
teaching: 10
exercises: 5
questions:
- "Characters? Numerics? Factors?"
objectives:
- "Learn the difference between character, factor and numeric input"
- "Learn how to convert between data types "
- "Learn difference between matrix, array, list and data.frame"
keypoints:
- Factors may seem confusing at first, but will prove to be useful
- The matrix is just a special array
- Lists are useful for collecting objects of various length
- Data frames are sort of like lists, but all components have the same length

---

# Different classes of variables

There are four main data types used in R: numeric, character, factor and logical.  Although numeric, character and logical tend to be more intuitive, factor can often be confusing and sometimes bad things happen if you don't realize something is a factor.  First I'll show each one and then I'll explain what this factor business is.


```r
# You can use the class() function to see what type of data R thinks you have

# Numbers (almost) always default to numeric
y = c(1,2,3,4)       # a vector of numbers
class(y)

# Character
names = c("Anne", "Sean", "Lilly", "Logan") # a vector of strings
# Check the class of names()
class(names)

# Factors
gender = c("m", "f", "m", "f", "m","m", "f")  # here it is a character
gender.factor = as.factor(gender)        
gender.factor
class(gender)
class(gender.factor)

# Logicals
# I'll cover how you generate T/F values in the next section
#  but the TRUE/FALSE input in R are special and are automatically 
#  recognized as logical values.  Importantly, don't use quotes!
b = c(TRUE, FALSE, TRUE, TRUE)
class(b)
```
The reason R has factors relates to the main purpose of R: run statistical analyses.  In many models you run with categorical variables, there's a specific baseline comparison that makes the most sense.  For example, if I ran a model with three groups, adhd, bipolar and controls, I might prefer my regression coefficients use the control group as the reference and that's exactly what factors do, they allow you to set the reference.  

Probably the place you'll find this the most useful is when using ggplot.  If you want to change the order in which levels are plotted (say in a set of boxplots), releveling a factor into the order you'd like is the solution.  There will be an example later on.


```r
group = factor(c("adhd", "bipolar", "ctrl"))
# without doing anything, adhd is listed first, meaning it is the baseline
group

# use relevel to change reference
relevel(group, ref = "ctrl")
```
Sometimes after reading in data it will automatically change things into factors that you wish were numbers.  Be very careful when you do this!  You must first convert to a character and then a numeric, otherwise it will use the level value as the value.  

```r
# Common mistake
# Going from factor to number
num.vec = as.factor(c(1.2, 1.4, 1.6))
num.vec

# Wrong way
as.numeric(num.vec)

# Correct way
as.numeric(as.character(num.vec))
```

# Matrices, lists, arrays and data frames
So far you've only been looking at vectors of numbers, but you'll often want to put a bunch of vectors together and there are multiple options including list, matrix, array, and  data frame.  The first three are found in many software packages, but the data frame is a special structure that makes the data much more useful for a lot of different R functions, including plotting and data manipulation.

The list is best for things of varying lengths.  Function output is typically put in a list.  This is analogous to the MATLAB structure.

Matrices are two dimensional and are best if you're working with an actual matrix.  For example a matrix of fMRI data where the columns correspond to different voxels.  If you plan on using matrix math, you'll want the data to be in a matrix.

Arrays can be multidimensional.

Data frames have columns with different meanings, or variables.  It is basically a list where the lengths of the entries are the same.  Data for input into regression analyses or plotting are typically put into data frames.


```r
mat.ex = matrix(c(1,2,3,4,5,6), nrow = 2)
dim(mat.ex)
mat.ex

array.ex = array(c(1:24), c(4, 3, 2))
dim(array.ex)
array.ex

list.ex = list()
list.ex$a = c(1:10)
list.ex$b = c(45:70)
list.ex$c = factor(c("a1", "b1", "c1"))
list.ex$d = as.character(c("bat", "cat", "bird", "dog"))
length(list.ex)
list.ex
# you can pull out one element of the list using $
list.ex$d

col1 = c(1:10)
col2 = c(21:30)
col3 = rep(c("a1", "b1"), each = 5)
data.frame.ex = data.frame(col1, col2, col3)
data.frame.ex
dim(data.frame.ex)
names(data.frame.ex)
# you can pull columns of a data frame out using the column name
data.frame.ex$col1
# you can also add a new column to a pre-existing data frame
data.frame.ex$col4 = rep(c("m", "f"), 5)
data.frame.ex

# you can easily convert a matrix to a data.frame and add names
df.ex2 = matrix(1:18, ncol = 3)
df.ex2 = data.frame(df.ex2)
names(df.ex2) = c("col1", "col2", "col3")
df.ex2
```

It is easy to construct diagonal matrices and extract diagonals from matrices in R.  The same command is use.

```r
a = matrix(1:9, nrow = 3)
diag(a)

diag(c(1,2,3))

# you can even change the diagonal of the matrix
# Here I'll change it to 1s
a
diag(a) = 1
a
```

# On your own
Relevel only allows you to change the baseline level of a factor, but for plotting in ggplot you'll often want to change the overall order of the levels of a factor.  For the following, use the factor function and the "levels" option within it (look at the help for more details) to change the following factor so the levels are in the order: ctrl, bipolar, adhd.

```r
group = factor(c("adhd", "bipolar", "ctrl"))
```

Secondly, with the rep command I used above, make sure you understand what it is doing differently when I add the "each" option.

# Summary of functions 

Function Name | What it does
------------------------- | -------------------------
class | Tells you the data type
as.factor/as.character/as.numeric | set data type to factor/character/numeric
special values: TRUE, FALSE, NA | Use without quotes when creating data to indicate logical or missing data
relevel | Change the order of levels of a factor
matrix| How to create a matrix
array | How to create an array
data.frame | How to create a data frame
list | How to create a list
names | How to access names of data.frame (for viewing or changing)
dim | How to look at the dimension of your matrix/array/data.frame
length|  How to look at lengths of vectors/lists/etc
? | How you get help, eg. ?matrix will give the help for as.matrix
rep | repeat things.  Note how I used each, vs when I didn't use each

