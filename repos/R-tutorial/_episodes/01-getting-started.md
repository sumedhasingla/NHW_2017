---
title: "Installing R and getting started"
teaching: 10
exercises: 5
questions:
- "How should I begin?"
objectives:
- "Learn how to install R"
- "Basic commands"
- "Assigning something to a variable"
keypoints:
- R installation is easy
- Library installation is simple (if library is in CRAN)
- There are multiple ways of assigning data to a variable

---

# Installing R and R libraries


[R](https://www.r-project.org/) is free and I highly recommend using R through the IDE, [RStudio](https://www.rstudio.com/), which offers a lot of helpful functionality like generating R markdown files easily and integrating with github.  A common confusion is that updating RStudio is also updating R, but this is not the case.  RStudio uses R, but they are updated and installed independently.

To install R and RStudio, start by installing R and then install RStudio second.  RStudio should automatically find R when it installs.

Like Python, R requires installing libraries for more advanced tools, but  the installation is typically very easy.  Most libraries you will want to use are located in the [CRAN](https://cran.r-project.org/) (Comprehensive R Archive Network), which can be accessed through R, directly.  The following illustrates how you'd install and load a package.



```r
# <-  The comment in R is the hash symbol

# To grab libraries for installation, R will ask you to
# select a CRAN "mirror".  The following line will set the
# mirror permanently so R doesn't ask you over and over again.
#  All the mirrors are listed here: https://cran.r-project.org/mirrors.html

# You only need to run this once ever (not once per session)
options(repos=structure(c(CRAN="http://cran.us.r-project.org")))


# To install a library use the following, note double quotes are used.
# A "newer" feature is dependencies (libraries the library of 
# interest needs) will automatically be installed.

# You only need to run this once ever (not once per session)
install.packages("ggplot2")

# To load the library so you can access the functions 

# Run once per session if you'd like to use it
library("ggplot2")
```
Now open a new editor (in RStudio click the white page icon in the upper left and select, "R Script", and we'll write a quick "hello world".  Enter the following in the file and save it in a file called "first_script.R".

```r
print("Hello world")
```

I feel it is poor coding form to change working directories, so I always recommend typing out the full paths to files.  So edit the following to reflect where you just stored your file.  This will run your script.

```r
source("/Users/jeanettemumford/Documents/Research/Teaching/neurohackweek2017/first_script.R")
```

If you want to run the script from the LINUX prompt you would use "Rscript first_script.R".  

In RStudio, you can simply hit cmd+return (on a Mac) to run the current line that the cursor is on, or you can copy and paste into the R terminal window.  Give that a shot with your single line in first_script.R and add these following simple commands and run them.

# Assigning data to a variable

```r
a <- 4
b <- 10
a*b
a-b
```

Now, you will notice I use the "<-" symbol to assign a value to a variable.  You can also use "=" and the result is the same.  Why didn't the developers use the equal sign?  The short answer is it originally was used to set function values, for example in the command, rnorm(10, mean = 5), it is setting the mean value to 5 within the rnorm function.  Back in the day there was a single button that made the "<-" and, in fact, in some editors a shortcut still exists (e.g. Aquamacs).  I prefer fewer keystrokes and don't find it to be confusing, so I will be using the "=" in this tutorial.  You can read a longer answer [here](http://blog.revolutionanalytics.com/2008/12/use-equals-or-arrow-for-assignment.html).

There's one last way to assign a number to a variable and this can be very useful if you're creating variables in a loop and, for example, you would like the loop number to be included in the variable name.  

```r
assign("a", 5)
a
```
To insert a variable name, you can combine assign() with another function in R that allows you to combine strings and variables.  The paste0() function and sprintf() allow for this.  

```r
x = 10
# paste0 simply connects everything
paste0("variable", x)

# Alternatively, sprintf can work and has some additional flexibilities

# On your own, look at the help for sprintf.  By the way simply type "?" followed
#  by your command name to open the help page
?sprintf
sprintf("variable%s", x)
# the %s acts as a fill in the blank for strings.  You'd need to change this for number input
```

# On your own
Play around with the paste or sprintf commands.  Try to create a variable called "variable10" that has a value of 4 using the following:

```r
a = "variable"
b = 10
c = 4
```

# Summary of functions
For more information about any of these functions, simply type ?function.name at the R prompt to open the help.  Eg, ?options will tell you more about options().

Function Name | What it does
------------------------- | -------------------------
options | Let's you set various global options in R
install.packages | Used to install packages.  Only install once.
library | Load a library.  Needed each session 
print | Print strings to screen
source | Run all code contained in a file
<- | Older, but still commonly used, symbol for assigning values to a variable
assign | more flexible function for assigning values to a variable name
