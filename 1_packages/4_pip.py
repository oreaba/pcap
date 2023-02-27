# did NOT came 
# -------------------------------------
# PIP (Python Package Installer.)

# The repository (or repo for short) we mentioned before is named PyPI (it's short for Python Package Index) 
# and it's maintained by a workgroup named the Packaging Working Group, a part of the Python Software Foundation
# -------------------------------------
# The PyPI repo is sometimes referred to as the Cheese Shop. Really.
# -------------------------------------
# Some Python installations come with pip, some don't.
# What’s more, it doesn’t only depend on the OS you use, although this is a very important factor.

# -------------------------------------
# By the way, there are a few other very famous recursive acronyms. 
# One of them is Linux, which can be interpreted as “Linux is Not Unix”.
# -------------------------------------
# pip --version
# pip3 --version
# -------------------------------------
# Unfortunately, some Linux distributions don't have pip preinstalled, 
# even if Python itself is installed by default
# -------------------------------------
# install pip as a system package using a dedicated package manager (e.g., apt in Debian-like systems)
# -------------------------------------
# dependency is a phenomenon that appears every time you're going to use a piece of software that relies on other software. 
# -------------------------------------
# Does this mean that a potential nyse package user is obliged to trace all dependencies 
# and manually install all the needed packages? That would be horrible, wouldn't it?

# Yes, it's definitely horrible, so you shouldn't be surprised that the process of arduously 
# fulfilling all the subsequent requirements has its own name, and it's called dependency hell.
# -------------------------------------
# Fortunately not - pip can do all of this for you. Really. 
# It can discover, identify, and resolve all dependencies. 
# Moreover, it can do it in the cleverest way, avoiding any unnecessary downloads and reinstalls.


# -------------------------------------
# pip help

# -------------------------------------
# pip help install
# will show you detailed information about using and parameterizing the install command.

# -------------------------------------

# If you want to know what Python packages have been installed so far, you can use the list operation – just like this:

# pip list
# -------------------------------------
# there’s a command that can tell you more about any of the installed packages
# pip show package_name


# -------------------------------------
# In effect, pip uses the Internet to query PyPI and to download the required data. 
# This means that you have to have a network connection working whenever you’re going to ask pip 
# for anything that may involve direct interactions with the PyPI infrastructure.
# -------------------------------------
# pip search anystring

# the search is case insensitive.
# One of these cases occurs when you want to search through PyPI in order to find a desired package. This kind of search is initiated by the following command:
# The anystring provided by you will be searched in:

# the names of all the packages;
# the summary strings of all the packages.

# -------------------------------------
# install the package pygame for you only
# pip install --user pygame

# -------------------------------------
# pip show pygame
# -------------------------------------
# pip list

# -------------------------------------
# import pygame

# run = True
# width = 400
# height = 100
# pygame.init()
# screen = pygame.display.set_mode((width, height))
# font = pygame.font.SysFont(None, 48)
# text = font.render("Welcome to pygame", True, (255, 255, 255))
# screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
# pygame.display.flip()
# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT\
#         or event.type == pygame.MOUSEBUTTONUP\
#         or event.type == pygame.KEYUP:
#             run = False

# -------------------------------------

# it is able to update a locally installed package
# where -U means update. 
# Note: this form of the command makes use of the --user option for the same purpose as presented previously;

# pip install -U package_name
# -------------------------------------
# it is able to install a user-selected version of a package 
# (pip installs the newest available version by default); 
# to achieve this goal you should use the following syntax: 

# pip install pygame==1.9.2
# -------------------------------------
# If any of the currently installed packages are no longer needed and you want to get rid of them, pip will be useful, too. 
# Its uninstall command will execute all the needed steps.
# pip uninstall package_name


# -------------------------------------
# pip help operation - shows brief pip's description;
# pip list - shows list of currently installed packages;
# pip show package_name - shows package_name info including package's dependencies;
# pip search anystring - searches through PyPI directories in order to find packages which name contains anystring;
# pip install name - installs name system-wide (expect problems when you don't have administrative rights);
# pip install --user name - install name for you only; no other your platform's user will be able to use it;
# pip install -U name - updates previously installed package;
# pip uninstall name - uninstalls previously installed package;
# -------------------------------------
# Why should I ensure which one of pip and pip3 works for me?
# When Python 2 and Python 3 coexist in your OS, it's likely that pip identifies the instance of pip working with Python 2 packages only.
