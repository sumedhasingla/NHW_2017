---
title: "Reading in data"
teaching: 10
exercises: 5
questions:
- "What is the fastest way to read in my data?"
objectives:
- "Learn difference between read.table and fread"
keypoints:
- fread is much faster and (typically) requires less work.  You may
  benefit from some of the functionalities in the data.table library
  that should be faster than data.frame manipulations

---

# read.data vs fread vs read_csv: which is faster??
In the past I have used the read.data function to read in data, but now there are faster options that work much better if you're reading in huge data: fread (data.table package) and read_csv (readr library).  More information about these can be found [here](http://analyticstraining.com/2015/if-youre-a-data-analyst-you-should-read-this-review-of-hadleys-readr-0-1-0-right-now/). 

```r
#install.packages("data.table") # Only run this if you've never installed it
#install.packages("readr")
library(data.table)
library(readr)
```

```
## Warning: package 'readr' was built under R version 3.3.2
```

```r
# This is simply the demo from the R help for fread, but it shows how much faster fread is!
# Make up a data set (I haven't covered data.table, but it is like data.frame)
n=1e6
DT = data.table( a=sample(1:1000,n,replace=TRUE),
                 b=sample(1:1000,n,replace=TRUE),
                 c=rnorm(n),
                 d=sample(c("foo","bar","baz","qux","quux"),n,replace=TRUE),
                 e=rnorm(n),
                 f=sample(1:1000,n,replace=TRUE) )
# Save it and get the size info
write.table(DT,"test.csv",sep=",",row.names=FALSE,quote=FALSE)
cat("File size (MB):", round(file.info("test.csv")$size/1024^2),"\n")

#Here is the read.table timing.  The bit in the system.time() is what 
# you'd typically use to read it in.
# header=TRUE lets it know there's a header (column names)
# sep = "," is the delimiter
# quote="" disables quoting
# stringsAsFactors=FALSE is really handy, since you often
#     don't want the strings to automatically be made into factors

# note, the "=" notation won't work since the assignment is within another function
# so <- is used instead.
system.time(DF2 <- read.table("test.csv",header=TRUE,sep=",",stringsAsFactors=FALSE))
class(DF2)

# read_csv from readr
system.time(DF3 <- read_csv("test.csv"))
```

```
## Parsed with column specification:
## cols(
##   a = col_integer(),
##   b = col_integer(),
##   c = col_double(),
##   d = col_character(),
##   e = col_double(),
##   f = col_integer()
## )
```

```r
class(DF3)

# fread from data.table
system.time(DT <- fread("test.csv"))
class(DT)
```
It used to be the case the fread was only a data.table format, which made plotting in ggplot2 difficult, since that requires a data.frame.  Guess they've changed it!  I would use either fread or read_csv, although read_csv will only work for comma delimited files. 

One thing you must be careful about is that data.tables behave differently than regular data.frames.  Specifically, data.table uses [pass-by-reference](https://stackoverflow.com/questions/373419/whats-the-difference-between-passing-by-reference-vs-passing-by-value), which improves performance but has odd behavior.  For example, if I create a copy of DT2, it is still linked to DT and if I change a column heading in DT2 it will change it in DT as well!

```r
DT2 = DT
names(DT2)

# change a to a2
names(DT2)[1] = "a2"
names(DT2)

# Now look at DT
names(DT)
#!!

# If I add to DT2, what happens?
DT2$g = DT2$f^2
names(DT2)
names(DT)
# Nope, only in the new one

# What if I manipulate the values in a column of DT2?
# see what we're starting with
DT2$b[1:5]
DT2$b = DT2$b^2
# See the change
DT2$b[1:5]
# Did it alter the original?
DT$b[1:5]

#  What if I change something in DT, is it automatically changed in DT2?
# See what we start with
DT$c[1:10]
DT$c = DT$c^2
# See the change in DT
DT$c[1:10]
# How's DT2?
DT2$c[1:10]
# unchanged
```


Now for some cleanup, since we created a big file that we don't need...

```r
# system() allows us to run a command in the Linux environment
system("rm test.csv")
```

# Summary of functions 

Function Name | What it does
------------------------- | -------------------------
read.table | Older function for reading in data.  Flexible, but slow
fread | Part of data.table library. Fast and simple way to read in data.  Once loaded data is both a data.table and data.frame, which is good for things like ggplot2
read_csv | part of readr library.  Not as fast as fread, but treats as tbl_df, tble and data.frame
system | Allows you to run commands in Linux/Unix via R

