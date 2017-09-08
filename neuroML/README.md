# neuroML
A set of notebooks to introduce neuroscientists to concepts in machine learning.

To use:

1. Clone or download this repository
2. cd into the repository
3. Call docker:

```
docker run -it --rm  -v $PWD:/home/neuro/test -p 8888:8888 satra/ibro-workshop-2017

```

4. start jupyter:

```
$ jupyter-notebook --ip=*
```

5. open the url in a local browser.


Main resources:
 - [scikit-learn user guide](http://scikit-learn.org/stable/user_guide.html)
 - [Monte Lunacek tutorial](https://github.com/mlunacek/meetup_data_science_2016)
 - [Jake Vanderplas tutorial](https://github.com/jakevdp/sklearn_tutorial)
