---
title: "Plotting"
teaching: 10
exercises: 5
questions:
- "How can I make a quick and easy plot?"
- "How can I make a beautiful plot?"
objectives:
- "Learn plot() and ggplot() basics"
keypoints:
- 

---

# Simple plot command
When it comes to plotting, ggplot makes the most beautiful plots (IMHO).  That said, I almost always use simple plotting functions if I'm just quickly running through some analyses.  This could be because ggplot didn't exist when I first learned R, because folks I know who only learn ggplot seem to do okay.  There is a pretty steep learning curve, but once you get the hang of it, it isn't too bad.  Here I'll just show two simple examples of making a plot with two lines using plot and ggplot

```r
x = seq(1, 10, 0.1)
cosx = cos(x)
sinx = sin(x)

# simple function.  Default is points, so I change to line
plot(x, cosx, type = 'l', col = 'red')
# Add using lines function
lines(x, sinx, col = 'cyan')
# Add a legend, 'topleft' autoplaces in topleft corner, bty = 'n'
# suspends the formation of a black box around the legend
# lty = c(1,1) tells it to use two solid lines
legend('topleft',c("sin(x)", "cos(x)"), lty = c(1, 1), col = c("red", "cyan"), bty = 'n')
```
 Two things with the above: lty tells legend you want solid lines.
 Without that it won't add lines to the legend.  Also, you can see R
 is a big lacidasical about single vs double quotes.  I'm not
 consistent and it doesn't (typically) matter.

# Prettier plot using ggplot2
Although there's a steeper learning curve, the plots are much nicer
with ggplot.  For one, the x and y range will automatically rescale so
all the data will appear in the plot.  With the above, if the original
plot created with plot() doesn't have a range wide enough for the
second line added using lines(), you must manually fix it.  There are
plenty of other reasons to dedicate some time to making ggplot work
and it eventually starts to make sense.  The plot is built by adding
features to it.
```r
# Load the ggplot2 library
library(ggplot2)
# ggplot wants a data frame in long format
# Stack the values
values = c(cosx, sinx)
# Create a variable that indicates what is being plotted
function.type = rep(c("cos(x)", "sin(x)"), each = length(x))
xval = c(x, x)
plot.dat = data.frame(values, xval, function.type)

ggplot(plot.dat, 
       aes(x = xval, y = values, colour = function.type))+
  geom_line()
```

```r
# If you want cos(x) second in the legend, make function type a factor and relevel
plot.dat$function.type = factor(plot.dat$function.type, c("sin(x)", "cos(x)"))
ggplot(plot.dat, 
       aes(x = xval, y = values, colour = function.type))+
  geom_line()
```
There's much, much more you can do with ggplot.  Here's a good [starting point](http://tutorials.iq.harvard.edu/R/Rgraphics/Rgraphics.html) if you want to learn more.
# On your own
Using ggplot, add a third line to the plot: sin(x)+cos(x).

# Summary of functions

Function Name | What it does
------------------------- | -------------------------
plot | makes basic plots
lines | adds a line to a plot started with plot()
ggplot | the start of the ggplot plotting function.  Other layers must be added to generate the plot
geom_line | Tells ggplot that you want a line plot
