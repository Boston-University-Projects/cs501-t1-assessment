from project.server import app  # Why this code work? ==> Because, app variable has been created firstly by ./market/__init__.py


#Checks if the run.py file has executed directly and not imported
if __name__ == '__main__':
    app.run()     # Turn on the debug mode. (But, the purpose here, just to verify/show you, the app is created in __init__.py before run.py)
     # run app in debug mode on port 5001
    # app.run(debug=True, port=5001)