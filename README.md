# Github Actions Matrix Build
Mini-Project4
Katelyn Hucker (kh509)

My miniproject 4 uses previous code files from miniproject 2. My project now can be built on windows and linux (ubuntu) operating systems. It also works with Python versions: 3.7,3.8,3.9.

[![matrix build python 3.7-3.9 windows ubuntu](https://github.com/nogibjj/kh509_miniproject4/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/kh509_miniproject4/actions/workflows/cicd.yml)


# Github Actions
_______________________________
The cicd.yml demonstrates the workflow of github actions. The matrix build installs, tests, lints, formats, and runs the function for 6 builds. Python 3.7 ubuntu and windows, Python 3.8 ubuntu and windows, Python 3.9 ubuntu and windows. It passes all workflows for each build making it a well tested and developed project. It can work on different systems and versions for more broad usage. 
# Descriptions of the files
_______________________________

### Requirements.txt:
In addition to the needed dependencies for linting, formating, and testing, the requirements file added pandas 2.0.0 to its list of required libraries. I also added matplotlibb.pyplot 3.7.0. This allows pandas and matplotlib.pyplot to be installed as packages. 

### Makefile:
The Makefile has been uncommented to actually run properly on the statistics script. The Makefile installs the libraries in the requirements.txt, tests the code with the test_main.py file, then formats and lints with python black and pylint. 

### stat1.py:
stat1.py is a statistics script that takes advantage of the pandas library. The script imports a csv file as a dataframe, of the developers choosing, in this case it is the iris.csv dataset. The dataset contains varying numeric information about iris flowers. The whole dataset is imported with the read_csv method. The script contains a function that imports a dataframe's column, calculates and returns the descriptive stats of the column. The function is then called on the petal length coloumn of the iris data frame and printed out. The script also produces a boxplot of this user selected column of interest. The developer can change which dataframe and column they are looking as the function allows new inputs. The figure is saved as a boxplot.png for that column of interest.The boxplot is a visualization that includes most of the descriptive statistics output, including median, max, min, and quantiles. The visualization for the petal length column is below.

![image](https://github.com/nogibjj/kh509miniproject2/assets/143521756/01b5b0f3-55b6-4847-8386-4685c22450af)


### test_main.py:
The test_main.py file is file used to to test the stat1.py script. It tests that the calculate descriptive stats function from the stat1.py script. The test function takes a local small dataframe column, "Height,' and asserts that the mean, min, and max is what should be outputted from the function. There is also a test case to confrim that a boxplot graph is formed and saved in the workflow.

# Running the project
_______________________________
The project uses the python template as a base. It was then edited and added on for this week's specific needs. The project builds through the github worflows folder, cicd.yml file. It installs, lints, tests, formats, and runs the python script. 
