# Programmering med Python (2021)
This is a fundamental Python course with focus of learning important programming concepts in order to solve various problems by writing Python programs. All lecture codes can be found in the course [Github repo][ghr].

[ghr]: https://github.com/yuna-liu/python-programming-Yuna-Liu



## Schedule

The schedule of this course is:

|     Week     | Content                                                       |
| :----------: | ------------------------------------------------------------- |
| [week1] | installation, git, vscode, variables, I/O, if, while, lab 1   |
| [week2] | for, lists, random, matplotlib, pipenv                        |
| [week3] | strings, functions, lab 2                                     |
| [week4] | exception handling, file handling, dictionary, lab 2          |
| [week5] | OOP: class, object, attributes, properties, decorators, lab 3 |
| [week6] | OOP: inheritance, polymorphism, docstring, lab 3              |
| [week7] | repetition                                                    |
| [week8] | written exam                                                      |



## Resources
Many exercises and lecture materials are in form of Jupyter notebooks with **.ipynb** extensions. Sometimes GitHub may not load them correctly for preview, then you can use [Open in Colab][colab_addon], which is an addon in Chrome to open the notebook in Colab. Alternatively, you can go to [jupyter nbviewer][nbviewer], and paste the link to the notebook for previewing. 

[nbviewer]: https://nbviewer.jupyter.org/
[colab_addon]: https://chrome.google.com/webstore/detail/open-in-colab/iogfkhleblhcpcekbiedikdehleodpjo?hl=sv






## How to set up working enviroment


## 1. git, github and vs code

1.1 Download Python (add a path), Visual studio code(add a path), git och github desktop

1.2 Go to github and register an account.

1.3 Build a repository/repo in github.

1.4 Open this repo in github desktop.

1.5 Choose a right folder place to clone.


## 2. How to edit, commit and push new changes

2.1 Add file, add folder or edit file in Visual studio code.

2.2 Ctrl+S for saving the changes

2.3 Write message and commit changes 

2.4 Push to github

## 3. How to set up matplotlib

3.1 Through open folder to go to a repo in Visual studio code 

3.2 Open terminal: input "pip install pipenv", to install pip enviroment. 

In pipenv we are going to install external packages. We are going to have one pipenv for one course. 

If we are going to work in a big project, then everyone should have the same version of Python. This is the reason why we are using pipenv.

3.3 Write "pipenv install shell" n terminal, to get Pipfile and Pipfile.lock

If Pipfile.lock is not seen, then one should fix add path through setting in system environment.


3.4 Input the following codes:

"pipenv install matplotlib", to install package.

"pipenv install ipykernel", to fix jupyter.

3.5 Open a jupyter file that you are going to work with. Choose the pipenv under your repo that stated in 3.1 as terminal.

3.6 import matplotlib.pyplot as plt