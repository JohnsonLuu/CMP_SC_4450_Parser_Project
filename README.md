# 4450 Parser Project

In this project, our team will be implementing a parser for the Python language by using Backus-Naur Forms (BNFs) in ANTLR. The team will work together to complete sprints, or deliverables, by the due date. For each of these sprints, the team will meet or communicate though discord to assign each member a task to complete by the end of the sprint. After completing each sprint, the team's project should be able to parse Python code for each of the required tasks.

## Team Members

Logan Alcaraz (@logan-alcaraz)\
Sarah Duong (@sarahduong)\
Darian Hu (@dhu2001)\
Kermit Kreder (@kermitkreder)\
Johnson Luu (@johnsonluu1)

## Project Requirements

To be able to run this project, users will need to have the following installed:\
\
ANTLR, Java 11+, and Python\
\
Users will be running this project in the Python Runtime Environment.

## How to Use/Run the Parser

To setup the environments listed above, users will need to run the following commands:

ANTLR:\
\
Run the following in the console to install ANTLR:   

```
$pip install antlr4-tools
```
Consult https://github.com/antlr/antlr4/blob/master/doc/getting-started.md for any issues that may arise when installing ANTLR.  

Next, run the command below to download the antlr JAR file. This can also be downloaded directly from https://www.antlr.org/download.html. 
```
pip install antlr4-python3-runtime
```
Java:

Head to the link below and install the latest version of Java
https://www.oracle.com/java/technologies/downloads/

Once installed, use the following command to run the jar file:
\
```java -jar .\antlr-4.11.1-complete.jar -Dlanguage=Python3 .\pythonparser.g4```

Python:

Head to the link below and install the latest version of Python
https://www.python.org/downloads/

Once installed, run the following command to test Python files:
\
```python main.py test.py```

## Visualization of Grammar (VS Code)
To begin, install "ANTLR4 grammar syntax support" extension for Visual Studio Code.  
\
This can be done through the Extension Marketplace in VS Code or directly at   
https://marketplace.visualstudio.com/items?itemName=mike-lischke.vscode-antlr4. 

Open the .g4 file.  

Click on Run and then Add Configuration  
When prompted, choose "Node.js"  

Now, this should auto-generate a configuration file for debugging.  

Change the configuration file to below:
```json
{
    "version": "2.0.0",
    "configurations": [
        {
            "name": "Debug ANTLR4 grammar",
            "type": "antlr-debug",
            "request": "launch",
            "input": "test.py",
            "grammar": "pythonparser.g4",
            "startRule": "start",
            "printParseTree": true,
            "visualParseTree": true
        }
    ]
}
```
When you run the debugger, the extension will automatically generate the parse tree.

## Demo

https://youtu.be/cLoJI3GhsWQ 
