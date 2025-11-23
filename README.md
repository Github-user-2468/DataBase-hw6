# DataBase-hw6

This project updates the database and queries the data using flask, pymysql, HTML5, and CSS3

## To Prepare computer
1. **Have Python, MySQL workbench and, VS Code installed**
2. **Have the required Python extensions installed in VS Code** 
    * Pylance
    * Python
    * Python Debugger
     * Python Environments

3. **Set up a database in MySQL Workbench**
    * Set up a database connection
    * run the Query Create database HW6;
    * Use the database by running the query use HW6

## To run code
1. **Before running you need to create a virtual enviroment to do so follow listed steps**
    1. Hit Control Shift P (command shift p for mac users)
    2. Select create virtual environment
    3. Select venv environment and your python addition
    4. Click the checkbox to download dependences OR run pip -install -r requirements.txt to install dependences in your terminal
    5. create environment

2. **To run the code open a new terminal and run the following command** 
```bash
python app.py  <= WINDOWS
python3 app.py  <= MAC
```
3. **This will start a development server and click the port it is running on**
#### EXAMPLE OUTPUT 
```
karig@Karigan_Laptop MINGW64 ~/Downloads/DataBase-hw6-main
$ python app.py
Creating Table Started =====
Tables created!
Table data inserted!
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000   <== THIS IS THE PORT COPY THE HTTP ADDRESS INTO YOUR PREFERRED BROWSER =====================
Press CTRL+C to quit
 * Restarting with stat
Creating Table Started =====
Tables created!
```
4. **ENJOY THE PROGRAM!**