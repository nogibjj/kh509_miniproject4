# Pandas Descriptive Statistics Script
Mini-Project2
Katelyn Hucker (kh509)

My mini-project imports the iris.csv dataset and then calculates the average petal length of the iris flowers in the dataset using the python pandas library. 

# Changes 
_______________________________

### Requirements.txt:
The requirements file added pandas 2.0.0 to its list of required libraries. This allows pandas to be installed as a package. 

### Makefile:
The Makefile has been uncommented to actually run properly on the statistics script. The Makefile installs the libraries in the requirements.txt, tests the code with the test_main.py file, then formats and lints with python black and pylint. 

# New 
_______________________________

### stat1.py:
stat1.py is a statistics script that takes advantage of the pandas library. The script imports a csv file of the developers choosing, in this case it is the iris.csv dataset. The dataset contains varying numeric information about iris flowers. The whole dataset is imported with the read_csv method. The script contains a function that imports a dataframe's column, calculates and returns the mean of the column. The function is then called on the petal length coloumn of the data frame and printed out. 

### test_main.py:
The test_main.py file is file used to to test the stat1.py script. It tests that the calculate_mean function from the stat1.py script. The test function takes a local small dataframe column, "Height,' and asserts that the mean is what should be outputted from the function. 

# Running the project
_______________________________
The project builds through the github worflows folder, cicd.yml file. It installs, lints, tests, formats, and the python script. 
