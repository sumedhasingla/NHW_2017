
# coding: utf-8

# # Basics
# 
# We'll fly through this, but if you forget any of the basic notebook functionality, you can come back here to find it.
# 
# 
# ## Notebook navigation
# 
# You'll notice that when you select a "cell" of the notebook, there is a colored bar on the left. If that bar is blue you are in command mode and you can use the command mode shortcuts to manipulate cells and move quickly through the notebook. If you press `enter` on a selected cell, you'll enter edit mode and a cursor will appear inside the cell. Once you've finished editing the cell, you can press `esc` to return to command mode.
# 
# ## Running Cells
# 
# `shit+enter`: run a cell and advance the active cell to the following cell  
# `ctrl+enter`: run a cell and keep this cell as the active cell
# 
# ## Help Menu
# 
# The help menu has links to documentation for notebooks, markdown, extensions (if installed), and lots of frequently used modules. Most importantly though, you can see all of the keyboard shortcuts there.
# 
# ## Displaying variables
# 
# By default the notebook will display the value of variables or statements when they're alone on a line.

# In[1]:


foo = "Having fun"
foo


# The notebook will pretty print some types of outputs, such as pandas dataframes.

# In[2]:


import seaborn as sns
iris = sns.load_dataset('iris')
iris.head()


# With a settings change, you can also make the notebook print out any variable or statement on it's own line.

# In[3]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


# In[4]:


foo
iris.head()


# ## Function help
# 
# It's easy to get function documentation when you're in the jupyter notebook. Pressing `shift+tab` when your cursor is inside the parentheses of of a function will bring up the call signature of the function, and you can expand this to get the full documetation.

# In[5]:


# Press shift+tab inside the parentheses to get print's call signature and docstring 
print()


# Prepending or appending a question mark on a library, method, or variable will also bring up it's docstring.

# In[6]:


get_ipython().magic('pinfo range')


# In[7]:


get_ipython().magic('pinfo iris.head')


# ## Executing shell commands with !
# If you need to run a shell command you can do so right from the notebook by prepending the line with an exclamation mark.

# In[8]:


get_ipython().system('pwd')


# ## Multicursor and alt-select
# You can drop a cursor at multiple points inside the same cell with `ctrl(cmd on mac)+click` or by clicking and dragging while holding alt.

# In[9]:


###Exercise###
# Use multicursor to add Bear to each item in the following list
# You'll see the plus sign in the corner throughout the rest 
# of this notebook. You can expand it to see the solution
bears = ["Yogi"
        ,"Pooh"
        ,"Fuzz"
        ,"Tall"]


# In[10]:


bears = ["Yogi Bear"
        ,"Pooh Bear"
        ,"Fuzz Bear"
        ,"Tall Bear"]


# # Jupyter notebook extensions
# Jupyter notebook extensions give notebooks various additional functionality, but they're not all garaunteed to be stable. You can find instructions for installing them here: https://github.com/ipython-contrib/jupyter_contrib_nbextensions
# 
# 

# # IPython Magic
# If you are running your notebook with an python kernel, there are some special built in funcitonality that you can access with "magic" functions. There are line magics that are preceded by a single `%` and affect only that line and cell magics preceded by `%%` that you place at the beginning of a cell to modify the behavior of that cell. There are [lots of magics](http://ipython.readthedocs.io/en/stable/interactive/magics.htm), but here are some handy ones.

# ## Environtment variables: %env
# If you need to modify the environment variables that apply to a running notebook and don't want to restart your notebook server, `%env` allows you to check and set them from within the notebook

# In[10]:


get_ipython().magic('env')


# In[11]:


get_ipython().magic('env FOO="Warming up"')


# In[12]:


get_ipython().magic('env FOO')


# ## Manipulating files with magic

# ### Load a file: %load
# With the `%load` magic you can load the contents of a file into a cell

# In[ ]:


# %load boring.py
print("Not much going on here")


# In[15]:


# %load boring.py
print("Not much going on here")


# ### Writing files: %%writefile
# With `%%writefile` you can write the contents of a cell to a file. Let's create a simple python script that sets a python variable equal to the value of the environment variable we just created.

# In[13]:


get_ipython().run_cell_magic('writefile', './grab_foo.py', "import os\nbar = os.environ['FOO']")


# ### Running files: %run
# `%run` is a line magic that executes the file or ipython notebook passed to it.

# In[14]:


get_ipython().magic('run ./grab_foo.py')
print(bar)


# ## Debugging: %pdb, %debug
# `%pdb` toggles automatic calling of [The Python Debugger (pdb)](https://docs.python.org/3.6/library/pdb.html#debugger-commands) so you can figure out what is breaking whenever an error is thrown.  
# 
# [`%debug`](http://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-debug) lets you drop into pdb after an error has been thrown even if automatic calling was off. You can also activate the debugger before executing code which allows you to set break points.

# In[15]:


def is_moving(alive, location="south"):
    """determine if a creature is moving"""
    
    if (not alive) and (location=="north"):
        moving = True
    elif not alive:
        moving = 1/0
    else:
        moving = True
    return moving
        


# In[16]:


get_ipython().magic('pdb')
is_moving(False)


# In[18]:


# Turn autopdb back off
get_ipython().magic('pdb')


# In[19]:


get_ipython().magic('debug')


# ## Why's my code so slow: timing and profiling
# `%%time` gives you the execution time of a single run of a cell.
# 
# 
# `%%timeit` runs a statment 100,000 times and gives you the total execution time, it repeats this 3 times and returns the quickest result, this gives you an idea of the best case for execution of this code on your machine. The mean isn't used because slower execution times are often the result of other processes interfering with python.
# 
# `%prun` runs the statement you give it and returns the number of times each internal function was called within the statement.
# 
# 

# In[20]:


def slow_reverse(x):
    y = []
    for xi in x:
        y.insert(0,xi)
    return y
def something_slow(n):
    b = []
    for i in range(0,n):
        b.append(i)
        b = slow_reverse(b)
        
def fast_reverse(x):
    return x[::-1]
def something_fast(n):
    b = []
    for i in range(0,n):
        b.append(i)
        b = fast_reverse(b)


# In[21]:


get_ipython().run_cell_magic('timeit', '', 'something_slow(100)')


# In[22]:


get_ipython().run_cell_magic('timeit', '', 'something_fast(100)')


# In[23]:


pres = get_ipython().magic('prun -r something_slow(100)')
pres.print_stats()


# In[24]:


pres = get_ipython().magic('prun -r something_fast(100)')
pres.print_stats()


# ## Pretty pictures: %matplotlib inline
# 
# One of the really nice parts of notebooks is that you have markdown, code, and figures all in one document. the `%matplotlib inline` magic turns on plotting in the notebook.

# In[25]:


from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
get_ipython().magic('matplotlib inline')


# In[26]:


for s in pd.unique(iris.species):
    x = iris.loc[iris.species == s,"sepal_length"]
    y = iris.loc[iris.species == s,"sepal_width"]
    plt.plot(x,y,'o', label =s);
    plt.legend(loc='best');


# ## Bonus: Speaking of plotting, seaborn makes things easier and prettier
# You can see the [seaborn documentation](https://seaborn.pydata.org/index.html) for more examples of pretty plots made easy

# In[27]:


import seaborn as sns
sns.set()
sns.pairplot(iris,hue="species");


# # Widgets
# 
# [Ipython widgets](http://ipywidgets.readthedocs.io/en/stable/index.html) are python objects represented in the browser than you can use to create interactive GUIs. This can be particularly useful for exploring your data. We'll use the `interact` function to create some interactive widgets.
# 
# ## interact
# `interact` creates UI elements that let you control the input parameters to a function. So first we'll need a function.

# In[28]:


from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets


# In[29]:


def f(x):
    print(x)


# In[30]:


#now we'll create an interactive ui
interact(f,x=2.);


# In[31]:


#interact will create a checkbox if you pass it a bool
interact(f,x=True);


# In[32]:


#interact will create a text area if you pass it a string
interact(f,x="Your text here");


# In[33]:


#interact will create a dropdown if you pass it a list or dict
interact(f,x=["Option 1", "Option 2"]);
interact(f,x={"Option 1":1, "Option 2":2});


# Now these examples are fine, but they don't do much. We've already seen that jupyter cand do inline plotting, so now we'll make an inline interactive plot. We turned on inline plotting earlier, so now we just need a function that accepts a parameter and draws a plot.

# In[34]:


def plotpower(a):
    x = np.linspace(1,10,100)
    y = x**a
    plt.plot(x,y)


# In[35]:


interact(plotpower, a = 2.);


# ## interactive
# What if we want to get the value of a? `interact` is a shortcut that makes and displays the widget object for you based on your inputs, `interactive` just creates and returns the widget object. You'll need to use `Ipython.display.display` to view the widget.

# In[36]:


widg_obj = interactive(plotpower, a = 2.);


# In[37]:


from IPython.display import display
display(widg_obj)


# Now that you've got a widget object the `.kwargs` property holds the interactively defined value of your inputs.

# In[38]:


widg_obj.kwargs


# ### widget exercise
# 
# Below you can find a simple function to plot a trigonometric function that takes three input parameters. Create a widget that allows the three input parameters to be manipulated interactively. You might need to debug trig_plot.

# In[39]:


def trig_plot(frequency, amplitude, fx_name= 'sin'):
    """Plot a trigonometric function for values of x between 0 and 2pi.
    Function plotted will be fx(x*frequency)*amplitude.
    
    Parameters
    ----------
    frequency: float or int indicated frequency
    amplitude: float or int indicated amplitude
    fx_name: string indicated the trigonmetric function to plot, should be one of sin, cos, or tan
    """
    if fx_name == 'cos ':
        fx = np.cos
    elif fx_name == 'tan ':
        fx = np.tan
    elif fx_name == 'sin ':
        fx = np.sin
    else:
        raise NotImplementedError("The function %s has not been implemented"%fx_name)
    x = np.linspace(0,2*np.pi,100)
    y = fx(frequency * x)*amplitude
    plt.plot(x,y)
    
    return y


# In[ ]:





# In[58]:


tp_widget = interactive(trig_plot,
            frequency = (0.1,10.0),
            amplitude = (0.1,10.0),
            fx_name=['sin','cos','tan'])
display(tp_widget)


# Now assign the result of your interactive plot to a variable `tp_res` and the arguments to `tp_args`.

# In[ ]:





# In[61]:


tp_res = tp_widget.result
tp_args= tp_widget.args


# ## Niwidgets
# [Niwidgets](https://github.com/janfreyberg/niwidgets) lets you interactively explore neuroimaging data in yor notebook.

# In[40]:


get_ipython().system('pip install niwidgets')


# In[41]:


from niwidgets import NiftiWidget

from niwidgets import examplet1

test_widget = NiftiWidget(examplet1)
test_widget.nifti_plotter()


# In[42]:


from niwidgets import examplezmap
import nilearn.plotting as nip

test = NiftiWidget(examplezmap)
test.nifti_plotter(plotting_func=nip.plot_glass_brain, threshold=(0.0, 10.0, 0.01),
                   display_mode=['ortho','xz'])


# # Beyond Python
# Jupyter notebooks aren't just for Python. Jupyter actually referst to JUlia PYThon and R. It's easy to install other kernels with anaconda.

# ## Julia
# From [Julia's docs](https://docs.julialang.org/en/stable/manual/introduction/): "The Julia programming language... is a flexible dynamic language, appropriate for scientific and numerical computing, with performance comparable to traditional statically-typed languages."
# 
# To run julia in Jupyter note books, you'll first need to install julia. You can download the package for your machine from [here](https://julialang.org/downloads/). 

# In[43]:


# This will print out what you need to put ininstall_ijulia.jl
jupyter_path = get_ipython().getoutput('which jupyter')
print('ENV["JUPYTER"]="%s"'%jupyter_path[0])
print('Pkg.add("IJulia")')
print('Pkg.build("IJulia")')


# Use a writefile magic to write the output of the above cell to a file called install_ijulia.jl

# In[ ]:





# In[16]:


get_ipython().run_cell_magic('writefile', 'install_ijulia.jl', 'ENV["JUPYTER"]="/Users/nielsond/miniconda3/envs/nhw_ipynb/bin/jupyter"\nPkg.add("IJulia")\nPkg.build("IJulia")')


# In[17]:


get_ipython().system('/Applications/Julia-0.6.app/Contents/Resources/julia/bin/julia ./install_ijulia.jl')


# Now unfortunately you'll need to restart your jupyter server for it to find the new kernels. If you're following along on jupyter hub, you won't be able to do this.

# ## R

# In[56]:


get_ipython().system('conda install -y -c r r-essentials')
#rpy2 lets python and R interact with each other.
get_ipython().system('conda install -y rpy2')


# In[2]:


get_ipython().magic('load_ext rpy2.ipython')


# In[3]:


get_ipython().magic('R require(ggplot2)')


# In[4]:


iris


# You can use the `%%R` cell magic to indicate that a cell will contain R code. the magic accpets arguments, including `-i` for data passed from Python to R. Let's use ggplot to plot the iris dataset that we loaded from python

# In[11]:


get_ipython().run_cell_magic('R', '-i iris', 'ggplot(iris, aes(x = sepal_length, y = petal_width, color = species)) + geom_point() + \n    geom_smooth(method = "lm", se = F)')


# # Making notebooks play nice with git
# Instructions from: https://svds.com/jupyter-notebook-best-practices-for-data-science/
# git diffs on jupyter notebooks can be a mess. If you automatically save out the .py and .html versions and track those with git as well, then you can look at the .py to evaluate changes to the code and look at the .html to evaluate changes to the outputs.

# In[4]:


import os
from subprocess import check_output
if os.path.exists(os.path.expanduser('~/.jupyter/jupyter_notebook_config.py')):
    print("Good to go")
else:
    get_ipython().system('jupyter notebook --generate-config')
    # could also use the subprocess library
    # check_output("jupyter notebook --generate-config")


# In[ ]:


get_ipython().magic('load /Users/nielsond/.jupyter/jupyter_notebook_config.py')


# In[6]:


get_ipython().run_cell_magic('writefile', '/home/shotgunosine/.jupyter/jupyter_notebook_config.py', '# Configuration file for jupyter-notebook.\n\nc = get_config()\n### If you want to auto-save .html and .py versions of your notebook:\n# modified from: https://github.com/ipython/ipython/issues/8009\nimport os\nfrom subprocess import check_call\n\ndef post_save(model, os_path, contents_manager):\n    """post-save hook for converting notebooks to .py scripts"""\n    if model[\'type\'] != \'notebook\':\n        return # only do this for notebooks\n    d, fname = os.path.split(os_path)\n    check_call([\'jupyter\', \'nbconvert\', \'--to\', \'script\', fname], cwd=d)\n    check_call([\'jupyter\', \'nbconvert\', \'--to\', \'html\', fname], cwd=d)\n\nc.FileContentsManager.post_save_hook = post_save\n\n\n#------------------------------------------------------------------------------\n# Application(SingletonConfigurable) configuration\n#------------------------------------------------------------------------------\n\n## This is an application.\n\n## The date format used by logging formatters for %(asctime)s\n#c.Application.log_datefmt = \'%Y-%m-%d %H:%M:%S\'\n\n## The Logging format template\n#c.Application.log_format = \'[%(name)s]%(highlevel)s %(message)s\'\n\n## Set the log level by value or name.\n#c.Application.log_level = 30\n\n#------------------------------------------------------------------------------\n# JupyterApp(Application) configuration\n#------------------------------------------------------------------------------\n\n## Base class for Jupyter applications\n\n## Answer yes to any prompts.\n#c.JupyterApp.answer_yes = False\n\n## Full path of a config file.\n#c.JupyterApp.config_file = \'\'\n\n## Specify a config file to load.\n#c.JupyterApp.config_file_name = \'\'\n\n## Generate default config file.\n#c.JupyterApp.generate_config = False\n\n#------------------------------------------------------------------------------\n# NotebookApp(JupyterApp) configuration\n#------------------------------------------------------------------------------\n\n## Set the Access-Control-Allow-Credentials: true header\n#c.NotebookApp.allow_credentials = False\n\n## Set the Access-Control-Allow-Origin header\n#  \n#  Use \'*\' to allow any origin to access your server.\n#  \n#  Takes precedence over allow_origin_pat.\n#c.NotebookApp.allow_origin = \'\'\n\n## Use a regular expression for the Access-Control-Allow-Origin header\n#  \n#  Requests from an origin matching the expression will get replies with:\n#  \n#      Access-Control-Allow-Origin: origin\n#  \n#  where `origin` is the origin of the request.\n#  \n#  Ignored if allow_origin is set.\n#c.NotebookApp.allow_origin_pat = \'\'\n\n## Whether to allow the user to run the notebook as root.\n#c.NotebookApp.allow_root = False\n\n## DEPRECATED use base_url\n#c.NotebookApp.base_project_url = \'/\'\n\n## The base URL for the notebook server.\n#  \n#  Leading and trailing slashes can be omitted, and will automatically be added.\n#c.NotebookApp.base_url = \'/\'\n\n## Specify what command to use to invoke a web browser when opening the notebook.\n#  If not specified, the default browser will be determined by the `webbrowser`\n#  standard library module, which allows setting of the BROWSER environment\n#  variable to override it.\n#c.NotebookApp.browser = \'\'\n\n## The full path to an SSL/TLS certificate file.\n#c.NotebookApp.certfile = \'\'\n\n## The full path to a certificate authority certificate for SSL/TLS client\n#  authentication.\n#c.NotebookApp.client_ca = \'\'\n\n## The config manager class to use\n#c.NotebookApp.config_manager_class = \'notebook.services.config.manager.ConfigManager\'\n\n## The notebook manager class to use.\n#c.NotebookApp.contents_manager_class = \'notebook.services.contents.largefilemanager.LargeFileManager\'\n\n## Extra keyword arguments to pass to `set_secure_cookie`. See tornado\'s\n#  set_secure_cookie docs for details.\n#c.NotebookApp.cookie_options = {}\n\n## The random bytes used to secure cookies. By default this is a new random\n#  number every time you start the Notebook. Set it to a value in a config file\n#  to enable logins to persist across server sessions.\n#  \n#  Note: Cookie secrets should be kept private, do not share config files with\n#  cookie_secret stored in plaintext (you can read the value from a file).\n#c.NotebookApp.cookie_secret = b\'\'\n\n## The file where the cookie secret is stored.\n#c.NotebookApp.cookie_secret_file = \'\'\n\n## The default URL to redirect to from `/`\n#c.NotebookApp.default_url = \'/tree\'\n\n## Disable cross-site-request-forgery protection\n#  \n#  Jupyter notebook 4.3.1 introduces protection from cross-site request\n#  forgeries, requiring API requests to either:\n#  \n#  - originate from pages served by this server (validated with XSRF cookie and\n#  token), or - authenticate with a token\n#  \n#  Some anonymous compute resources still desire the ability to run code,\n#  completely without authentication. These services can disable all\n#  authentication and security checks, with the full knowledge of what that\n#  implies.\n#c.NotebookApp.disable_check_xsrf = False\n\n## Whether to enable MathJax for typesetting math/TeX\n#  \n#  MathJax is the javascript library Jupyter uses to render math/LaTeX. It is\n#  very large, so you may want to disable it if you have a slow internet\n#  connection, or for offline use of the notebook.\n#  \n#  When disabled, equations etc. will appear as their untransformed TeX source.\n#c.NotebookApp.enable_mathjax = True\n\n## extra paths to look for Javascript notebook extensions\n#c.NotebookApp.extra_nbextensions_path = []\n\n## Extra paths to search for serving static files.\n#  \n#  This allows adding javascript/css to be available from the notebook server\n#  machine, or overriding individual files in the IPython\n#c.NotebookApp.extra_static_paths = []\n\n## Extra paths to search for serving jinja templates.\n#  \n#  Can be used to override templates from notebook.templates.\n#c.NotebookApp.extra_template_paths = []\n\n## \n#c.NotebookApp.file_to_run = \'\'\n\n## Deprecated: Use minified JS file or not, mainly use during dev to avoid JS\n#  recompilation\n#c.NotebookApp.ignore_minified_js = False\n\n## (bytes/sec) Maximum rate at which messages can be sent on iopub before they\n#  are limited.\n#c.NotebookApp.iopub_data_rate_limit = 1000000\n\n## (msgs/sec) Maximum rate at which messages can be sent on iopub before they are\n#  limited.\n#c.NotebookApp.iopub_msg_rate_limit = 1000\n\n## The IP address the notebook server will listen on.\n#c.NotebookApp.ip = \'localhost\'\n\n## Supply extra arguments that will be passed to Jinja environment.\n#c.NotebookApp.jinja_environment_options = {}\n\n## Extra variables to supply to jinja templates when rendering.\n#c.NotebookApp.jinja_template_vars = {}\n\n## The kernel manager class to use.\n#c.NotebookApp.kernel_manager_class = \'notebook.services.kernels.kernelmanager.MappingKernelManager\'\n\n## The kernel spec manager class to use. Should be a subclass of\n#  `jupyter_client.kernelspec.KernelSpecManager`.\n#  \n#  The Api of KernelSpecManager is provisional and might change without warning\n#  between this version of Jupyter and the next stable one.\n#c.NotebookApp.kernel_spec_manager_class = \'jupyter_client.kernelspec.KernelSpecManager\'\n\n## The full path to a private key file for usage with SSL/TLS.\n#c.NotebookApp.keyfile = \'\'\n\n## The login handler class to use.\n#c.NotebookApp.login_handler_class = \'notebook.auth.login.LoginHandler\'\n\n## The logout handler class to use.\n#c.NotebookApp.logout_handler_class = \'notebook.auth.logout.LogoutHandler\'\n\n## The MathJax.js configuration file that is to be used.\n#c.NotebookApp.mathjax_config = \'TeX-AMS-MML_HTMLorMML-full,Safe\'\n\n## A custom url for MathJax.js. Should be in the form of a case-sensitive url to\n#  MathJax, for example:  /static/components/MathJax/MathJax.js\n#c.NotebookApp.mathjax_url = \'\'\n\n## Dict of Python modules to load as notebook server extensions.Entry values can\n#  be used to enable and disable the loading ofthe extensions. The extensions\n#  will be loaded in alphabetical order.\n#c.NotebookApp.nbserver_extensions = {}\n\n## The directory to use for notebooks and kernels.\n#c.NotebookApp.notebook_dir = \'\'\n\n## Whether to open in a browser after starting. The specific browser used is\n#  platform dependent and determined by the python standard library `webbrowser`\n#  module, unless it is overridden using the --browser (NotebookApp.browser)\n#  configuration option.\n#c.NotebookApp.open_browser = True\n\n## Hashed password to use for web authentication.\n#  \n#  To generate, type in a python/IPython shell:\n#  \n#    from notebook.auth import passwd; passwd()\n#  \n#  The string should be of the form type:salt:hashed-password.\n#c.NotebookApp.password = \'\'\n\n## Forces users to use a password for the Notebook server. This is useful in a\n#  multi user environment, for instance when everybody in the LAN can access each\n#  other\'s machine though ssh.\n#  \n#  In such a case, server the notebook server on localhost is not secure since\n#  any user can connect to the notebook server via ssh.\n#c.NotebookApp.password_required = False\n\n## The port the notebook server will listen on.\n#c.NotebookApp.port = 8888\n\n## The number of additional ports to try if the specified port is not available.\n#c.NotebookApp.port_retries = 50\n\n## DISABLED: use %pylab or %matplotlib in the notebook to enable matplotlib.\n#c.NotebookApp.pylab = \'disabled\'\n\n## (sec) Time window used to  check the message and data rate limits.\n#c.NotebookApp.rate_limit_window = 3\n\n## Reraise exceptions encountered loading server extensions?\n#c.NotebookApp.reraise_server_extension_failures = False\n\n## DEPRECATED use the nbserver_extensions dict instead\n#c.NotebookApp.server_extensions = []\n\n## The session manager class to use.\n#c.NotebookApp.session_manager_class = \'notebook.services.sessions.sessionmanager.SessionManager\'\n\n## Supply SSL options for the tornado HTTPServer. See the tornado docs for\n#  details.\n#c.NotebookApp.ssl_options = {}\n\n## Supply overrides for terminado. Currently only supports "shell_command".\n#c.NotebookApp.terminado_settings = {}\n\n## Token used for authenticating first-time connections to the server.\n#  \n#  When no password is enabled, the default is to generate a new, random token.\n#  \n#  Setting to an empty string disables authentication altogether, which is NOT\n#  RECOMMENDED.\n#c.NotebookApp.token = \'<generated>\'\n\n## Supply overrides for the tornado.web.Application that the Jupyter notebook\n#  uses.\n#c.NotebookApp.tornado_settings = {}\n\n## Whether to trust or not X-Scheme/X-Forwarded-Proto and X-Real-Ip/X-Forwarded-\n#  For headerssent by the upstream reverse proxy. Necessary if the proxy handles\n#  SSL\n#c.NotebookApp.trust_xheaders = False\n\n## DEPRECATED, use tornado_settings\n#c.NotebookApp.webapp_settings = {}\n\n## The base URL for websockets, if it differs from the HTTP server (hint: it\n#  almost certainly doesn\'t).\n#  \n#  Should be in the form of an HTTP origin: ws[s]://hostname[:port]\n#c.NotebookApp.websocket_url = \'\'\n\n#------------------------------------------------------------------------------\n# ConnectionFileMixin(LoggingConfigurable) configuration\n#------------------------------------------------------------------------------\n\n## Mixin for configurable classes that work with connection files\n\n## JSON file in which to store connection info [default: kernel-<pid>.json]\n#  \n#  This file will contain the IP, ports, and authentication key needed to connect\n#  clients to this kernel. By default, this file will be created in the security\n#  dir of the current profile, but can be specified by absolute path.\n#c.ConnectionFileMixin.connection_file = \'\'\n\n## set the control (ROUTER) port [default: random]\n#c.ConnectionFileMixin.control_port = 0\n\n## set the heartbeat port [default: random]\n#c.ConnectionFileMixin.hb_port = 0\n\n## set the iopub (PUB) port [default: random]\n#c.ConnectionFileMixin.iopub_port = 0\n\n## Set the kernel\'s IP address [default localhost]. If the IP address is\n#  something other than localhost, then Consoles on other machines will be able\n#  to connect to the Kernel, so be careful!\n#c.ConnectionFileMixin.ip = \'\'\n\n## set the shell (ROUTER) port [default: random]\n#c.ConnectionFileMixin.shell_port = 0\n\n## set the stdin (ROUTER) port [default: random]\n#c.ConnectionFileMixin.stdin_port = 0\n\n## \n#c.ConnectionFileMixin.transport = \'tcp\'\n\n#------------------------------------------------------------------------------\n# KernelManager(ConnectionFileMixin) configuration\n#------------------------------------------------------------------------------\n\n## Manages a single kernel in a subprocess on this host.\n#  \n#  This version starts kernels with Popen.\n\n## Should we autorestart the kernel if it dies.\n#c.KernelManager.autorestart = True\n\n## DEPRECATED: Use kernel_name instead.\n#  \n#  The Popen Command to launch the kernel. Override this if you have a custom\n#  kernel. If kernel_cmd is specified in a configuration file, Jupyter does not\n#  pass any arguments to the kernel, because it cannot make any assumptions about\n#  the arguments that the kernel understands. In particular, this means that the\n#  kernel does not receive the option --debug if it given on the Jupyter command\n#  line.\n#c.KernelManager.kernel_cmd = []\n\n## Time to wait for a kernel to terminate before killing it, in seconds.\n#c.KernelManager.shutdown_wait_time = 5.0\n\n#------------------------------------------------------------------------------\n# Session(Configurable) configuration\n#------------------------------------------------------------------------------\n\n## Object for handling serialization and sending of messages.\n#  \n#  The Session object handles building messages and sending them with ZMQ sockets\n#  or ZMQStream objects.  Objects can communicate with each other over the\n#  network via Session objects, and only need to work with the dict-based IPython\n#  message spec. The Session will handle serialization/deserialization, security,\n#  and metadata.\n#  \n#  Sessions support configurable serialization via packer/unpacker traits, and\n#  signing with HMAC digests via the key/keyfile traits.\n#  \n#  Parameters ----------\n#  \n#  debug : bool\n#      whether to trigger extra debugging statements\n#  packer/unpacker : str : \'json\', \'pickle\' or import_string\n#      importstrings for methods to serialize message parts.  If just\n#      \'json\' or \'pickle\', predefined JSON and pickle packers will be used.\n#      Otherwise, the entire importstring must be used.\n#  \n#      The functions must accept at least valid JSON input, and output *bytes*.\n#  \n#      For example, to use msgpack:\n#      packer = \'msgpack.packb\', unpacker=\'msgpack.unpackb\'\n#  pack/unpack : callables\n#      You can also set the pack/unpack callables for serialization directly.\n#  session : bytes\n#      the ID of this Session object.  The default is to generate a new UUID.\n#  username : unicode\n#      username added to message headers.  The default is to ask the OS.\n#  key : bytes\n#      The key used to initialize an HMAC signature.  If unset, messages\n#      will not be signed or checked.\n#  keyfile : filepath\n#      The file containing a key.  If this is set, `key` will be initialized\n#      to the contents of the file.\n\n## Threshold (in bytes) beyond which an object\'s buffer should be extracted to\n#  avoid pickling.\n#c.Session.buffer_threshold = 1024\n\n## Whether to check PID to protect against calls after fork.\n#  \n#  This check can be disabled if fork-safety is handled elsewhere.\n#c.Session.check_pid = True\n\n## Threshold (in bytes) beyond which a buffer should be sent without copying.\n#c.Session.copy_threshold = 65536\n\n## Debug output in the Session\n#c.Session.debug = False\n\n## The maximum number of digests to remember.\n#  \n#  The digest history will be culled when it exceeds this value.\n#c.Session.digest_history_size = 65536\n\n## The maximum number of items for a container to be introspected for custom\n#  serialization. Containers larger than this are pickled outright.\n#c.Session.item_threshold = 64\n\n## execution key, for signing messages.\n#c.Session.key = b\'\'\n\n## path to file containing execution key.\n#c.Session.keyfile = \'\'\n\n## Metadata dictionary, which serves as the default top-level metadata dict for\n#  each message.\n#c.Session.metadata = {}\n\n## The name of the packer for serializing messages. Should be one of \'json\',\n#  \'pickle\', or an import name for a custom callable serializer.\n#c.Session.packer = \'json\'\n\n## The UUID identifying this session.\n#c.Session.session = \'\'\n\n## The digest scheme used to construct the message signatures. Must have the form\n#  \'hmac-HASH\'.\n#c.Session.signature_scheme = \'hmac-sha256\'\n\n## The name of the unpacker for unserializing messages. Only used with custom\n#  functions for `packer`.\n#c.Session.unpacker = \'json\'\n\n## Username for the Session. Default is your system username.\n#c.Session.username = \'nielsond\'\n\n#------------------------------------------------------------------------------\n# MultiKernelManager(LoggingConfigurable) configuration\n#------------------------------------------------------------------------------\n\n## A class for managing multiple kernels.\n\n## The name of the default kernel to start\n#c.MultiKernelManager.default_kernel_name = \'python3\'\n\n## The kernel manager class.  This is configurable to allow subclassing of the\n#  KernelManager for customized behavior.\n#c.MultiKernelManager.kernel_manager_class = \'jupyter_client.ioloop.IOLoopKernelManager\'\n\n#------------------------------------------------------------------------------\n# MappingKernelManager(MultiKernelManager) configuration\n#------------------------------------------------------------------------------\n\n## A KernelManager that handles notebook mapping and HTTP error handling\n\n## \n#c.MappingKernelManager.root_dir = \'\'\n\n#------------------------------------------------------------------------------\n# ContentsManager(LoggingConfigurable) configuration\n#------------------------------------------------------------------------------\n\n## Base class for serving files and directories.\n#  \n#  This serves any text or binary file, as well as directories, with special\n#  handling for JSON notebook documents.\n#  \n#  Most APIs take a path argument, which is always an API-style unicode path, and\n#  always refers to a directory.\n#  \n#  - unicode, not url-escaped\n#  - \'/\'-separated\n#  - leading and trailing \'/\' will be stripped\n#  - if unspecified, path defaults to \'\',\n#    indicating the root path.\n\n## \n#c.ContentsManager.checkpoints = None\n\n## \n#c.ContentsManager.checkpoints_class = \'notebook.services.contents.checkpoints.Checkpoints\'\n\n## \n#c.ContentsManager.checkpoints_kwargs = {}\n\n## Glob patterns to hide in file and directory listings.\n#c.ContentsManager.hide_globs = [\'__pycache__\', \'*.pyc\', \'*.pyo\', \'.DS_Store\', \'*.so\', \'*.dylib\', \'*~\']\n\n## Python callable or importstring thereof\n#  \n#  To be called on a contents model prior to save.\n#  \n#  This can be used to process the structure, such as removing notebook outputs\n#  or other side effects that should not be saved.\n#  \n#  It will be called as (all arguments passed by keyword)::\n#  \n#      hook(path=path, model=model, contents_manager=self)\n#  \n#  - model: the model to be saved. Includes file contents.\n#    Modifying this dict will affect the file that is stored.\n#  - path: the API path of the save destination\n#  - contents_manager: this ContentsManager instance\n#c.ContentsManager.pre_save_hook = None\n\n## \n#c.ContentsManager.root_dir = \'/\'\n\n## The base name used when creating untitled directories.\n#c.ContentsManager.untitled_directory = \'Untitled Folder\'\n\n## The base name used when creating untitled files.\n#c.ContentsManager.untitled_file = \'untitled\'\n\n## The base name used when creating untitled notebooks.\n#c.ContentsManager.untitled_notebook = \'Untitled\'\n\n#------------------------------------------------------------------------------\n# FileManagerMixin(Configurable) configuration\n#------------------------------------------------------------------------------\n\n## Mixin for ContentsAPI classes that interact with the filesystem.\n#  \n#  Provides facilities for reading, writing, and copying both notebooks and\n#  generic files.\n#  \n#  Shared by FileContentsManager and FileCheckpoints.\n#  \n#  Note ---- Classes using this mixin must provide the following attributes:\n#  \n#  root_dir : unicode\n#      A directory against against which API-style paths are to be resolved.\n#  \n#  log : logging.Logger\n\n## By default notebooks are saved on disk on a temporary file and then if\n#  succefully written, it replaces the old ones. This procedure, namely\n#  \'atomic_writing\', causes some bugs on file system whitout operation order\n#  enforcement (like some networked fs). If set to False, the new notebook is\n#  written directly on the old one which could fail (eg: full filesystem or quota\n#  )\n#c.FileManagerMixin.use_atomic_writing = True\n\n#------------------------------------------------------------------------------\n# FileContentsManager(FileManagerMixin,ContentsManager) configuration\n#------------------------------------------------------------------------------\n\n## Python callable or importstring thereof\n#  \n#  to be called on the path of a file just saved.\n#  \n#  This can be used to process the file on disk, such as converting the notebook\n#  to a script or HTML via nbconvert.\n#  \n#  It will be called as (all arguments passed by keyword)::\n#  \n#      hook(os_path=os_path, model=model, contents_manager=instance)\n#  \n#  - path: the filesystem path to the file just written - model: the model\n#  representing the file - contents_manager: this ContentsManager instance\n#c.FileContentsManager.post_save_hook = None\n\n## \n#c.FileContentsManager.root_dir = \'\'\n\n## DEPRECATED, use post_save_hook. Will be removed in Notebook 5.0\n#c.FileContentsManager.save_script = False\n\n#------------------------------------------------------------------------------\n# NotebookNotary(LoggingConfigurable) configuration\n#------------------------------------------------------------------------------\n\n## A class for computing and verifying notebook signatures.\n\n## The hashing algorithm used to sign notebooks.\n#c.NotebookNotary.algorithm = \'sha256\'\n\n## The sqlite file in which to store notebook signatures. By default, this will\n#  be in your Jupyter data directory. You can set it to \':memory:\' to disable\n#  sqlite writing to the filesystem.\n#c.NotebookNotary.db_file = \'\'\n\n## The secret key with which notebooks are signed.\n#c.NotebookNotary.secret = b\'\'\n\n## The file where the secret key is stored.\n#c.NotebookNotary.secret_file = \'\'\n\n## A callable returning the storage backend for notebook signatures. The default\n#  uses an SQLite database.\n#c.NotebookNotary.store_factory = traitlets.Undefined\n\n#------------------------------------------------------------------------------\n# KernelSpecManager(LoggingConfigurable) configuration\n#------------------------------------------------------------------------------\n\n## If there is no Python kernelspec registered and the IPython kernel is\n#  available, ensure it is added to the spec list.\n#c.KernelSpecManager.ensure_native_kernel = True\n\n## The kernel spec class.  This is configurable to allow subclassing of the\n#  KernelSpecManager for customized behavior.\n#c.KernelSpecManager.kernel_spec_class = \'jupyter_client.kernelspec.KernelSpec\'\n\n## Whitelist of allowed kernel names.\n#  \n#  By default, all installed kernels are allowed.\n#c.KernelSpecManager.whitelist = set()')


# In[ ]:




get_ipython().run_cell_magic('writefile', '/Users/nielsond/.jupyter/jupyter_notebook_config.py', '# Configuration file for jupyter-notebook.\n\n#------------------------------------------------------------------------------\n# Application(SingletonConfigurable) configuration\n#------------------------------------------------------------------------------\n\n## This is an application.\n\n## The date format used by logging formatters for %(asctime)s\n#c.Application.log_datefmt = \'%Y-%m-%d %H:%M:%S\'\n\n## The Logging format template\n#c.Application.log_format = \'[%(name)s]%(highlevel)s %(message)s\'\n\n## Set the log level by value or name.\n#c.Application.log_level = 30\n\n#------------------------------------------------------------------------------\n# JupyterApp(Application) configuration\n#------------------------------------------------------------------------------\n\n## Base class for Jupyter applications\n\n## Answer yes to any prompts.\n#c.JupyterApp.answer_yes = False\n\n## Full path of a config file.\n#c.JupyterApp.config_file = \'\'\n\n## Specify a config file to load.\n#c.JupyterApp.config_file_name = \'\'\n\n## Generate default config file.\n#c.JupyterApp.generate_config = False\n\n#------------------------------------------------------------------------------\n# NotebookApp(JupyterApp) configuration\n#------------------------------------------------------------------------------\n\n## Set the Access-Control-Allow-Credentials: true header\n#c.NotebookApp.allow_credentials = False\n\n## Set the Access-Control-Allow-Origin header\n#  \n#  Use \'*\' to allow any origin to access your server.\n#  \n#  Takes precedence over allow_origin_pat.\n#c.NotebookApp.allow_origin = \'\'\n\n## Use a regular expression for the Access-Control-Allow-Origin header\n#  \n#  Requests from an origin matching the expression will get replies with:\n#  \n#      Access-Control-Allow-Origin: origin\n#  \n#  where `origin` is the origin of the request.\n#  \n#  Ignored if allow_origin is set.\n#c.NotebookApp.allow_origin_pat = \'\'\n\n## Whether to allow the user to run the notebook as root.\n#c.NotebookApp.allow_root = False\n\n## DEPRECATED use base_url\n#c.NotebookApp.base_project_url = \'/\'\n\n## The base URL for the notebook server.\n#  \n#  Leading and trailing slashes can be omitted, and will automatically be added.\n#c.NotebookApp.base_url = \'/\'\n\n## Specify what command to use to invoke a web browser when opening the notebook.\n#  If not specified, the default browser will be determined by the `webbrowser`\n#  standard library module, which allows setting of the BROWSER environment\n#  variable to override it.\n#c.NotebookApp.browser = \'\'\n\n## The full path to an SSL/TLS certificate file.\n#c.NotebookApp.certfile = \'\'\n\n## The full path to a certificate authority certificate for SSL/TLS client\n#  authentication.\n#c.NotebookApp.client_ca = \'\'\n\n## The config manager class to use\n#c.NotebookApp.config_manager_class = \'notebook.services.config.manager.ConfigManager\'\n\n## The notebook manager class to use.\n#c.NotebookApp.contents_manager_class = \'notebook.services.contents.largefilemanager.LargeFileManager\'\n\n## Extra keyword arguments to pass to `set_secure_cookie`. See tornado\'s\n#  set_secure_cookie docs for details.\n#c.NotebookApp.cookie_options = {}\n\n## The random bytes used to secure cookies. By default this is a new random\n#  number every time you start the Notebook. Set it to a value in a config file\n#  to enable logins to persist across server sessions.\n#  \n#  Note: Cookie secrets should be kept private, do not share config files with\n#  cookie_secret stored in plaintext (you can read the value from a file).\n#c.NotebookApp.cookie_secret = b\'\'\n\n## The file where the cookie secret is stored.\n#c.NotebookApp.cookie_secret_file = \'\'\n\n## The default URL to redirect to from `/`\n#c.NotebookApp.default_url = \'/tree\'\n\n## Disable cross-site-request-forgery protection\n#  \n#  Jupyter notebook 4.3.1 introduces protection from cross-site request\n#  forgeries, requiring API requests to either:\n#  \n#  - originate from pages served by this server (validated with XSRF cookie and\n#  token), or - authenticate with a token\n#  \n#  Some anonymous compute resources still desire the ability to run code,\n#  completely without authentication. These services can disable all\n#  authentication and security checks, with the full knowledge of what that\n#  implies.\n#c.NotebookApp.disable_check_xsrf = False\n\n## Whether to enable MathJax for typesetting math/TeX\n#  \n#  MathJax is the javascript library Jupyter uses to render math/LaTeX. It is\n#  very large, so you may want to disable it if you have a slow internet\n#  connection, or for offline use of the notebook.\n#  \n#  When disabled, equations etc. will appear as their untransformed TeX source.\n#c.NotebookApp.enable_mathjax = True\n\n## extra paths to look for Javascript notebook extensions\n#c.NotebookApp.extra_nbextensions_path = []\n\n## Extra paths to search for serving static files.\n#  \n#  This allows adding javascript/css to be available from the notebook server\n#  machine, or overriding individual files in the IPython\n#c.NotebookApp.extra_static_paths = []\n\n## Extra paths to search for serving jinja templates.\n#  \n#  Can be used to override templates from notebook.templates.\n#c.NotebookApp.extra_template_paths = []\n\n## \n#c.NotebookApp.file_to_run = \'\'\n\n## Deprecated: Use minified JS file or not, mainly use during dev to avoid JS\n#  recompilation\n#c.NotebookApp.ignore_minified_js = False\n\n## (bytes/sec) Maximum rate at which messages can be sent on iopub before they\n#  are limited.\n#c.NotebookApp.iopub_data_rate_limit = 1000000\n\n## (msgs/sec) Maximum rate at which messages can be sent on iopub before they are\n#  limited.\n#c.NotebookApp.iopub_msg_rate_limit = 1000\n\n## The IP address the notebook server will listen on.\n#c.NotebookApp.ip = \'localhost\'\n\n## Supply extra arguments that will be passed to Jinja environment.\n#c.NotebookApp.jinja_environment_options = {}\n\n## Extra variables to supply to jinja templates when rendering.\n#c.NotebookApp.jinja_template_vars = {}\n\n## The kernel manager class to use.\n#c.NotebookApp.kernel_manager_class = \'notebook.services.kernels.kernelmanager.MappingKernelManager\'\n\n## The kernel spec manager class to use. Should be a subclass of\n#  `jupyter_client.kernelspec.KernelSpecManager`.\n#  \n#  The Api of KernelSpecManager is provisional and might change without warning\n#  between this version of Jupyter and the next stable one.\n#c.NotebookApp.kernel_spec_manager_class = \'jupyter_client.kernelspec.KernelSpecManager\'\n\n## The full path to a private key file for usage with SSL/TLS.\n#c.NotebookApp.keyfile = \'\'\n\n## The login handler class to use.\n#c.NotebookApp.login_handler_class = \'notebook.auth.login.LoginHandler\'\n\n## The logout handler class to use.\n#c.NotebookApp.logout_handler_class = \'notebook.auth.logout.LogoutHandler\'\n\n## The MathJax.js configuration file that is to be used.\n#c.NotebookApp.mathjax_config = \'TeX-AMS-MML_HTMLorMML-full,Safe\'\n\n## A custom url for MathJax.js. Should be in the form of a case-sensitive url to\n#  MathJax, for example:  /static/components/MathJax/MathJax.js\n#c.NotebookApp.mathjax_url = \'\'\n\n## Dict of Python modules to load as notebook server extensions.Entry values can\n#  be used to enable and disable the loading ofthe extensions. The extensions\n#  will be loaded in alphabetical order.\n#c.NotebookApp.nbserver_extensions = {}\n\n## The directory to use for notebooks and kernels.\n#c.NotebookApp.notebook_dir = \'\'\n\n## Whether to open in a browser after starting. The specific browser used is\n#  platform dependent and determined by the python standard library `webbrowser`\n#  module, unless it is overridden using the --browser (NotebookApp.browser)\n#  configuration option.\n#c.NotebookApp.open_browser = True\n\n## Hashed password to use for web authentication.\n#  \n#  To generate, type in a python/IPython shell:\n#  \n#    from notebook.auth import passwd; passwd()\n#  \n#  The string should be of the form type:salt:hashed-password.\n#c.NotebookApp.password = \'\'\n\n## Forces users to use a password for the Notebook server. This is useful in a\n#  multi user environment, for instance when everybody in the LAN can access each\n#  other\'s machine though ssh.\n#  \n#  In such a case, server the notebook server on localhost is not secure since\n#  any user can connect to the notebook server via ssh.\n#c.NotebookApp.password_required = False\n\n## The port the notebook server will listen on.\n#c.NotebookApp.port = 8888\n\n## The number of additional ports to try if the specified port is not available.\n#c.NotebookApp.port_retries = 50\n\n## DISABLED: use %pylab or %matplotlib in the notebook to enable matplotlib.\n#c.NotebookApp.pylab = \'disabled\'\n\n## (sec) Time window used to  check the message and data rate limits.\n#c.NotebookApp.rate_limit_window = 3\n\n## Reraise exceptions encountered loading server extensions?\n#c.NotebookApp.reraise_server_extension_failures = False\n\n## DEPRECATED use the nbserver_extensions dict instead\n#c.NotebookApp.server_extensions = []\n\n## The session manager class to use.\n#c.NotebookApp.session_manager_class = \'notebook.services.sessions.sessionmanager.SessionManager\'\n\n## Supply SSL options for the tornado HTTPServer. See the tornado docs for\n#  details.\n#c.NotebookApp.ssl_options = {}\n\n## Supply overrides for terminado. Currently only supports "shell_command".\n#c.NotebookApp.terminado_settings = {}\n\n## Token used for authenticating first-time connections to the server.\n#  \n#  When no password is enabled, the default is to generate a new, random token.\n#  \n#  Setting to an empty string disables authentication altogether, which is NOT\n#  RECOMMENDED.\n#c.NotebookApp.token = \'<generated>\'\n\n## Supply overrides for the tornado.web.Application that the Jupyter notebook\n#  uses.\n#c.NotebookApp.tornado_settings = {}\n\n## Whether to trust or not X-Scheme/X-Forwarded-Proto and X-Real-Ip/X-Forwarded-\n#  For headerssent by the upstream reverse proxy. Necessary if the proxy handles\n#  SSL\n#c.NotebookApp.trust_xheaders = False\n\n## DEPRECATED, use tornado_settings\n#c.NotebookApp.webapp_settings = {}\n\n## The base URL for websockets, if it differs from the HTTP server (hint: it\n#  almost certainly doesn\'t).\n#  \n#  Should be in the form of an HTTP origin: ws[s]://hostname[:port]\n#c.NotebookApp.websocket_url = \'\'\n\n#------------------------------------------------------------------------------\n# ConnectionFileMixin(LoggingConfigurable) configuration\n#------------------------------------------------------------------------------\n\n## Mixin for configurable classes that work with connection files\n\n## JSON file in which to store connection info [default: kernel-<pid>.json]\n#  \n#  This file will contain the IP, ports, and authentication key needed to connect\n#  clients to this kernel. By default, this file will be created in the security\n#  dir of the current profile, but can be specified by absolute path.\n#c.ConnectionFileMixin.connection_file = \'\'\n\n## set the control (ROUTER) port [default: random]\n#c.ConnectionFileMixin.control_port = 0\n\n## set the heartbeat port [default: random]\n#c.ConnectionFileMixin.hb_port = 0\n\n## set the iopub (PUB) port [default: random]\n#c.ConnectionFileMixin.iopub_port = 0\n\n## Set the kernel\'s IP address [default localhost]. If the IP address is\n#  something other than localhost, then Consoles on other machines will be able\n#  to connect to the Kernel, so be careful!\n#c.ConnectionFileMixin.ip = \'\'\n\n## set the shell (ROUTER) port [default: random]\n#c.ConnectionFileMixin.shell_port = 0\n\n## set the stdin (ROUTER) port [default: random]\n#c.ConnectionFileMixin.stdin_port = 0\n\n## \n#c.ConnectionFileMixin.transport = \'tcp\'\n\n#------------------------------------------------------------------------------\n# KernelManager(ConnectionFileMixin) configuration\n#------------------------------------------------------------------------------\n\n## Manages a single kernel in a subprocess on this host.\n#  \n#  This version starts kernels with Popen.\n\n## Should we autorestart the kernel if it dies.\n#c.KernelManager.autorestart = True\n\n## DEPRECATED: Use kernel_name instead.\n#  \n#  The Popen Command to launch the kernel. Override this if you have a custom\n#  kernel. If kernel_cmd is specified in a configuration file, Jupyter does not\n#  pass any arguments to the kernel, because it cannot make any assumptions about\n#  the arguments that the kernel understands. In particular, this means that the\n#  kernel does not receive the option --debug if it given on the Jupyter command\n#  line.\n#c.KernelManager.kernel_cmd = []\n\n## Time to wait for a kernel to terminate before killing it, in seconds.\n#c.KernelManager.shutdown_wait_time = 5.0\n\n#------------------------------------------------------------------------------\n# Session(Configurable) configuration\n#------------------------------------------------------------------------------\n\n## Object for handling serialization and sending of messages.\n#  \n#  The Session object handles building messages and sending them with ZMQ sockets\n#  or ZMQStream objects.  Objects can communicate with each other over the\n#  network via Session objects, and only need to work with the dict-based IPython\n#  message spec. The Session will handle serialization/deserialization, security,\n#  and metadata.\n#  \n#  Sessions support configurable serialization via packer/unpacker traits, and\n#  signing with HMAC digests via the key/keyfile traits.\n#  \n#  Parameters ----------\n#  \n#  debug : bool\n#      whether to trigger extra debugging statements\n#  packer/unpacker : str : \'json\', \'pickle\' or import_string\n#      importstrings for methods to serialize message parts.  If just\n#      \'json\' or \'pickle\', predefined JSON and pickle packers will be used.\n#      Otherwise, the entire importstring must be used.\n#  \n#      The functions must accept at least valid JSON input, and output *bytes*.\n#  \n#      For example, to use msgpack:\n#      packer = \'msgpack.packb\', unpacker=\'msgpack.unpackb\'\n#  pack/unpack : callables\n#      You can also set the pack/unpack callables for serialization directly.\n#  session : bytes\n#      the ID of this Session object.  The default is to generate a new UUID.\n#  username : unicode\n#      username added to message headers.  The default is to ask the OS.\n#  key : bytes\n#      The key used to initialize an HMAC signature.  If unset, messages\n#      will not be signed or checked.\n#  keyfile : filepath\n#      The file containing a key.  If this is set, `key` will be initialized\n#      to the contents of the file.\n\n## Threshold (in bytes) beyond which an object\'s buffer should be extracted to\n#  avoid pickling.\n#c.Session.buffer_threshold = 1024\n\n## Whether to check PID to protect against calls after fork.\n#  \n#  This check can be disabled if fork-safety is handled elsewhere.\n#c.Session.check_pid = True\n\n## Threshold (in bytes) beyond which a buffer should be sent without copying.\n#c.Session.copy_threshold = 65536\n\n## Debug output in the Session\n#c.Session.debug = False\n\n## The maximum number of digests to remember.\n#  \n#  The digest history will be culled when it exceeds this value.\n#c.Session.digest_history_size = 65536\n\n## The maximum number of items for a container to be introspected for custom\n#  serialization. Containers larger than this are pickled outright.\n#c.Session.item_threshold = 64\n\n## execution key, for signing messages.\n#c.Session.key = b\'\'\n\n## path to file containing execution key.\n#c.Session.keyfile = \'\'\n\n## Metadata dictionary, which serves as the default top-level metadata dict for\n#  each message.\n#c.Session.metadata = {}\n\n## The name of the packer for serializing messages. Should be one of \'json\',\n#  \'pickle\', or an import name for a custom callable serializer.\n#c.Session.packer = \'json\'\n\n## The UUID identifying this session.\n#c.Session.session = \'\'\n\n## The digest scheme used to construct the message signatures. Must have the form\n#  \'hmac-HASH\'.\n#c.Session.signature_scheme = \'hmac-sha256\'\n\n## The name of the unpacker for unserializing messages. Only used with custom\n#  functions for `packer`.\n#c.Session.unpacker = \'json\'\n\n## Username for the Session. Default is your system username.\n#c.Session.username = \'nielsond\'\n\n#------------------------------------------------------------------------------\n# MultiKernelManager(LoggingConfigurable) configuration\n#------------------------------------------------------------------------------\n\n## A class for managing multiple kernels.\n\n## The name of the default kernel to start\n#c.MultiKernelManager.default_kernel_name = \'python3\'\n\n## The kernel manager class.  This is configurable to allow subclassing of the\n#  KernelManager for customized behavior.\n#c.MultiKernelManager.kernel_manager_class = \'jupyter_client.ioloop.IOLoopKernelManager\'\n\n#------------------------------------------------------------------------------\n# MappingKernelManager(MultiKernelManager) configuration\n#------------------------------------------------------------------------------\n\n## A KernelManager that handles notebook mapping and HTTP error handling\n\n## \n#c.MappingKernelManager.root_dir = \'\'\n\n#------------------------------------------------------------------------------\n# ContentsManager(LoggingConfigurable) configuration\n#------------------------------------------------------------------------------\n\n## Base class for serving files and directories.\n#  \n#  This serves any text or binary file, as well as directories, with special\n#  handling for JSON notebook documents.\n#  \n#  Most APIs take a path argument, which is always an API-style unicode path, and\n#  always refers to a directory.\n#  \n#  - unicode, not url-escaped\n#  - \'/\'-separated\n#  - leading and trailing \'/\' will be stripped\n#  - if unspecified, path defaults to \'\',\n#    indicating the root path.\n\n## \n#c.ContentsManager.checkpoints = None\n\n## \n#c.ContentsManager.checkpoints_class = \'notebook.services.contents.checkpoints.Checkpoints\'\n\n## \n#c.ContentsManager.checkpoints_kwargs = {}\n\n## Glob patterns to hide in file and directory listings.\n#c.ContentsManager.hide_globs = [\'__pycache__\', \'*.pyc\', \'*.pyo\', \'.DS_Store\', \'*.so\', \'*.dylib\', \'*~\']\n\n## Python callable or importstring thereof\n#  \n#  To be called on a contents model prior to save.\n#  \n#  This can be used to process the structure, such as removing notebook outputs\n#  or other side effects that should not be saved.\n#  \n#  It will be called as (all arguments passed by keyword)::\n#  \n#      hook(path=path, model=model, contents_manager=self)\n#  \n#  - model: the model to be saved. Includes file contents.\n#    Modifying this dict will affect the file that is stored.\n#  - path: the API path of the save destination\n#  - contents_manager: this ContentsManager instance\n#c.ContentsManager.pre_save_hook = None\n\n## \n#c.ContentsManager.root_dir = \'/\'\n\n## The base name used when creating untitled directories.\n#c.ContentsManager.untitled_directory = \'Untitled Folder\'\n\n## The base name used when creating untitled files.\n#c.ContentsManager.untitled_file = \'untitled\'\n\n## The base name used when creating untitled notebooks.\n#c.ContentsManager.untitled_notebook = \'Untitled\'\n\n#------------------------------------------------------------------------------\n# FileManagerMixin(Configurable) configuration\n#------------------------------------------------------------------------------\n\n## Mixin for ContentsAPI classes that interact with the filesystem.\n#  \n#  Provides facilities for reading, writing, and copying both notebooks and\n#  generic files.\n#  \n#  Shared by FileContentsManager and FileCheckpoints.\n#  \n#  Note ---- Classes using this mixin must provide the following attributes:\n#  \n#  root_dir : unicode\n#      A directory against against which API-style paths are to be resolved.\n#  \n#  log : logging.Logger\n\n## By default notebooks are saved on disk on a temporary file and then if\n#  succefully written, it replaces the old ones. This procedure, namely\n#  \'atomic_writing\', causes some bugs on file system whitout operation order\n#  enforcement (like some networked fs). If set to False, the new notebook is\n#  written directly on the old one which could fail (eg: full filesystem or quota\n#  )\n#c.FileManagerMixin.use_atomic_writing = True\n\n#------------------------------------------------------------------------------\n# FileContentsManager(FileManagerMixin,ContentsManager) configuration\n#------------------------------------------------------------------------------\n\n## Python callable or importstring thereof\n#  \n#  to be called on the path of a file just saved.\n#  \n#  This can be used to process the file on disk, such as converting the notebook\n#  to a script or HTML via nbconvert.\n#  \n#  It will be called as (all arguments passed by keyword)::\n#  \n#      hook(os_path=os_path, model=model, contents_manager=instance)\n#  \n#  - path: the filesystem path to the file just written - model: the model\n#  representing the file - contents_manager: this ContentsManager instance\n#c.FileContentsManager.post_save_hook = None\n\n## \n#c.FileContentsManager.root_dir = \'\'\n\n## DEPRECATED, use post_save_hook. Will be removed in Notebook 5.0\n#c.FileContentsManager.save_script = False\n\n#------------------------------------------------------------------------------\n# NotebookNotary(LoggingConfigurable) configuration\n#------------------------------------------------------------------------------\n\n## A class for computing and verifying notebook signatures.\n\n## The hashing algorithm used to sign notebooks.\n#c.NotebookNotary.algorithm = \'sha256\'\n\n## The sqlite file in which to store notebook signatures. By default, this will\n#  be in your Jupyter data directory. You can set it to \':memory:\' to disable\n#  sqlite writing to the filesystem.\n#c.NotebookNotary.db_file = \'\'\n\n## The secret key with which notebooks are signed.\n#c.NotebookNotary.secret = b\'\'\n\n## The file where the secret key is stored.\n#c.NotebookNotary.secret_file = \'\'\n\n## A callable returning the storage backend for notebook signatures. The default\n#  uses an SQLite database.\n#c.NotebookNotary.store_factory = traitlets.Undefined\n\n#------------------------------------------------------------------------------\n# KernelSpecManager(LoggingConfigurable) configuration\n#------------------------------------------------------------------------------\n\n## If there is no Python kernelspec registered and the IPython kernel is\n#  available, ensure it is added to the spec list.\n#c.KernelSpecManager.ensure_native_kernel = True\n\n## The kernel spec class.  This is configurable to allow subclassing of the\n#  KernelSpecManager for customized behavior.\n#c.KernelSpecManager.kernel_spec_class = \'jupyter_client.kernelspec.KernelSpec\'\n\n## Whitelist of allowed kernel names.\n#  \n#  By default, all installed kernels are allowed.\n#c.KernelSpecManager.whitelist = set()')


# In[ ]:





# 
# 
# 
# ### Widgets
# 
# ### Sharing notebooks
#   - github, Jupyter config changes
#   - binder
#   
# ### Javascript slickness
#   - RISE
#   - 
# 
# ### Extensions
