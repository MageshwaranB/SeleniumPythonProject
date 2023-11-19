To install the required modules, navigate to the
src/requirements.txt, then hit
pip install -r requirements.txt on the terminal

selenium - selenium libraries
pytest - python test framework
pytest-html - pytest html reports
pytest-xdist - to run test parallely 
openpyxl - MS excel support
allure-pytest - to generate allure reports


Project Structure:
1. src
    - Configuration Folder - it holds the config.ini file used for storing the common set of values like url
    - Logs - it will hold the log files
    - page_objects - This package holds page classes
    - Screenshots - This folder holds the screenshots of test failures
    - TestData
    - utilities - Utilities package has the utility functions
2. test
    This holds the testcases and also the confttest.py where we specify the common actions like setting up the browser, launching the url 
   