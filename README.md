# Health_Monitoring_System_using_ML(Logistic Regression)_Using Flask

*Install Flask in VSCode
1.Install the Python extension.

2.Install a version of Python 3 Options include:
  a.(All operating systems) A download from python.org; typically use the Download button that appears first on the page.
  b.(Linux) The built-in Python 3 installation works well, but to install other Python packages you must run sudo apt install python3-pip in the terminal.
  c.(macOS) An installation through Homebrew on macOS using brew install python3.
  d.(All operating systems) A download from Anaconda (for data science purposes).
3.On Windows, make sure the location of your Python interpreter is included in your PATH environment variable. You can check the location by running path at the command prompt. If the Python interpreter's folder isn't included, open Windows Settings, search for "environment", select Edit environment variables for your account, then edit the Path variable to include that folder.

*Create a project environment for the Flask
you will create a virtual environment in which Flask is installed. Using a virtual environment avoids installing Flask into a global Python environment and gives you exact control over the libraries used in an application.
On your file system, create a folder for this tutorial, such as hello_flask.
Open this folder in VS Code by navigating to the folder in a terminal and running code ., or by running VS Code and using the File > Open Folder command.

In VS Code, open the Command Palette (View > Command Palette or (Ctrl+Shift+P)). Then select the Python: Create Environment command to create a virtual environment in your workspace. Select venv and then the Python environment you want to use to create it.

Install Flask in the virtual environment by running the following command in the VS Code Terminal:
    **python -m pip install flask**
You now have a self-contained environment ready for writing Flask code. VS Code activates the environment automatically when you use Terminal: Create New Terminal. If you open a separate command prompt or terminal, activate the environment by running source .venv/bin/activate (Linux/macOS) or .venv\Scripts\Activate.ps1 (Windows). You know the environment is activated when the command prompt shows (.venv) at the beginning.


To implement the proposed real-time health monitoring system, a cloud network model was developed using the ThingSpeak platform, which offers a convenient infrastructure for data collection, storage, and analysis. 
The system leverages machine learning algorithms, including K-Nearest Neighbors (KNN), Decision Tree, Support Vector Machine (SVM), and Logistic Regression, to train the model on the dataset that shows the prediction of taking consultation of Doctor based on the values of parameters of collected data .
In the subsequent sections, we will discuss the  dataset used, parameter tuning for the machine learning algorithms, and the evaluation results of the cloud network model. 
These findings will shed light on the performance and effectiveness of the system in accurately predicting the necessity of medical consultation based on vital sign analysis.
