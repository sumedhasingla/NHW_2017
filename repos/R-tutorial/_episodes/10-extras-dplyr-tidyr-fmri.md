---
title: "Extra bits we probably won't have time to cover"
teaching: 0
exercises: 0
questions:
- "What is the fastest way to read in my data?"
objectives:
- "Learn difference between read.table and fread"
keypoints:
- fread is much faster and (typically) requires less work.  You may
  benefit from some of the functionalities in the data.table library
  that should be faster than data.frame manipulations

---


##9 Other useful things I probably won't have time to cover
I'm guessing we will have run out of town by this point, but I wanted to mention the extremely useful tidyr and dplyr libraries.  Together these two libraries provide really great functions for manipulating data frames.  Here's a [cheatsheet](https://www.rstudio.com/wp-content/uploads/2015/02/data-wrangling-cheatsheet.pdf) and you can read more about it [here](https://rpubs.com/bradleyboehmke/data_wrangling).  A couple of quick examples are in the following.  Typically I use it to convert between wide and long data formats. 

```r
# install.packages("dplyr")
# install.packages("tidyr")
# install.packages("Lahman")
library(dplyr)
library(tidyr)
library(Lahman)  #I'm using a data set from this library
```

```r
# Use this Batting data (this is in the Lahman library)
dim(Batting)
names(Batting)

players = group_by(Batting, playerID)
#players looks the same, but has more info, as the grouping has been defined
dim(players)
dim(Batting)
head(players)
head(Batting)
# Now I can create easy summaries, over players...
games = summarise(players, total = sum(G))

# dplyr adds the %>% function, which serves as a "pipe", piping the output from one
#  command into the input of the next.  Really cleans up code.  This does what the above code did
games.using.dplyr = Batting %>%
  group_by(playerID) %>%
  summarise(total = sum(G))
```

There are more and more libraries for dealing with fMRI data, or simulating fMRI data, but I typically use the fmri library to read in NIfTI data.  The only snag is the nifti file needs to be unzipped first.

```r
library(fmri)
# First load in the structure
# This file is already unzipped
dat.struct = read.NIFTI("~/Dropbox/NeuroHackWeek/bold.nii")
dat = extract.data(dat.struct)
dim(dat)
```
### Summary of functions

Function Name | What it does
------------------------- | -------------------------
tidy (library)  | really useful library of functions
dplry (library) | Another really useful library
groupby | Function that adds grouping to data frame
summarise | Once data are grouped (using groupby) allows summaries within group
%>%  | The piping function from dplyr.  Once you get the hang of this,
it is a fantastic tool
read.NIFTI | In fmri library.  Reads in header info
extract.data | in fmri library, extracts data from NIfTI file.
