from flask import Flask, request, render_template, flash, redirect, url_for
import pymysql
import os
app = Flask(__name__)
app.secret_key = os.urandom(12)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'HW6'

mysql = pymysql.connect(
    host = app.config['MYSQL_HOST'],
    user = app.config['MYSQL_USER'],
    password = app.config['MYSQL_PASSWORD'],
    db = app.config['MYSQL_DB']
)

# Creates table in MySQL workebench
def create_table():
    try: 
        print('Creating Table Started =====')
        cur = mysql.cursor()
        cur.execute(
            '''
            CREATE TABLE IF NOT EXISTS Supplier (
                Sno CHAR(2),
                Sname VARCHAR(100) NOT NULL,
                Status INT CHECK (Status > 0),
                City VARCHAR(100),
                PRIMARY KEY(Sno)
            );

            ''')
        cur.execute(
            '''
            CREATE TABLE IF NOT EXISTS Part(
                Pno CHAR(2),
                Pname VARCHAR(100) NOT NULL,
                Color VARCHAR(50),
                Weight INT CHECK(Weight BETWEEN 1 AND 100),
                City VARCHAR(100),
                UNIQUE (Pname, Color),
                PRIMARY KEY(Pno)
            );
            ''' )
        cur.execute(
            '''
            CREATE TABLE IF NOT EXISTS Shipment(
                Sno CHAR(2),
                Pno CHAR(2),
                Qty INT DEFAULT 100,
                Price DECIMAL(8,3) CHECK (Price > 0),
                PRIMARY KEY (Sno, Pno),
                FOREIGN KEY (Sno) REFERENCES Supplier(Sno),
                FOREIGN KEY (Pno) REFERENCES Part(pno)
                
            );
            ''')
        
        mysql.commit()
        cur.close()
        print('Tables created!')
    except Exception as e:
        print('Error creating Tables', e)
    
# inserting the data into the tables 
def data_insertion():
    try:
        cur = mysql.cursor()
        #Inserting into suppliers
        cur.execute(
            '''
            INSERT INTO SUPPLIER (Sno, Sname, Status, City) VALUES
                ('s1', 'Smith', 20, 'London'),
                ('s2', 'Jones', 10, 'Paris'),
                ('s3', 'Blake', 30, 'Paris'),
                ('s4', 'Clark', 20, 'London'),
                ('s5', 'Adams', 30, NULL);

            '''
        )
        # Inserting into parts table
        cur.execute(
            '''
             INSERT INTO PART (Pno, Pname, Color, Weight, City) VALUES
                ('p1', 'Nut', 'Red', 12, 'London'),
                ('p2', 'Bolt', 'Green', 17, 'Paris'),
                ('p3', 'Screw', NULL, 17, 'Rome'),
                ('p4', 'Screw', 'Red', 14, 'London'),
                ('p5', 'Cam', 'Blue', 12, 'Paris'),
                ('p6', 'Cog', 'Red', 19, 'London');  
            '''
        )
        #Inserting into shipment table 
        cur.execute(
            '''
            INSERT INTO SHIPMENT (Sno, Pno, Qty, Price) VALUES
                ('s1', 'p1', 300, 0.005),
                ('s1', 'p2', 200, 0.009),
                ('s1', 'p3', 400, 0.004),
                ('s1', 'p4', 200, 0.009),
                ('s1', 'p5', 100, 0.01),
                ('s1', 'p6', 100, 0.01),
                ('s2', 'p1', 300, 0.006),
                ('s2', 'p2', 400, 0.004),
                ('s3', 'p2', 200, 0.009),
                ('s3', 'p3', 200, NULL),
                ('s4', 'p2', 200, 0.008),
                ('s4', 'p3', NULL, NULL),
                ('s4', 'p4', 300, 0.006),
                ('s4', 'p5', 400, 0.003);       
            '''
        )
        mysql.commit()
        cur.close()
        print('Table data inserted!')
    except Exception as e:
        print('Error inserting data', e)


@app.route ("/")
def index():
    return render_template('index.html')


# Routing for question 1 
@app.route('/insert_question_one', methods=["GET", "POST"])
def insert_question_one():

    if request.method == "POST":
        Sno = request.form["question-one-sno"]
        Pno = request.form["question-one-pno"]
        Qty = request.form["question-one-qty"]
        Price = request.form["question-one-price"]

        try:
            cur = mysql.cursor()

            #Query to insert data
            sql = "Insert INTO Shipment (Sno, Pno, Qty, Price) VALUES (%s, %s, %s, %s)"
            cur.execute(sql, (Sno, Pno, Qty, Price))
            mysql.commit()

            cur.close


            #flash messges
            flash('Data Inserted successfully', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error Inserting Data: {e}', 'error')
            return render_template('index.html')
    return render_template('index.html')


#Routing for question 2
@app.route('/insert_question_two', methods=["GET", "POST"])
def insert_question_two():

    if request.method == "POST":
        Sno = request.form["question-two-sno"]
        Pno = request.form["question-two-pno"]
        Qty = request.form["question-two-qty"]
        Price = request.form["question-two-price"]

        try:
            cur = mysql.cursor()
            # Query to insert data
            sql = "Insert INTO Shipment (Sno, Pno, Qty, Price) VALUES (%s, %s, %s, %s)"
            #execute Query to insert
            cur.execute(sql, (Sno, Pno, Qty, Price))
            mysql.commit()
            cur.close()
            # Flash messages
            flash('Shipment sucessfully inserted', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error Inserting Data: {e}', 'error')
            return render_template('index.html')
    return render_template('index.html')

    
#Routing for question 3
@app.route('/increase_by_10', methods=["GET", "POST"])
def increase_by_10():
    
    if request.method == "POST":
        try:
            cur = mysql.cursor()
            # Query to update status
            sql = "Update Supplier Set Status = status * 1.1"
            cur.execute(sql)
            mysql.commit()

            cur.close()
            # flash messages
            flash('Status Sucessfully Increased!', 'success')
            return render_template('index.html')
        except Exception as e:
            flash(f'Error Inserting Data: {e}', 'error')
            return render_template('index.html')
    return render_template('index.html')

#Routing for question 4
@app.route('/display_supplier_info', methods=["POST"])
def display_supplier_info():
    if request.method == "POST":
        try:
            cur = mysql.cursor()
            # Query to select info
            sql = "SELECT * FROM Supplier"
            cur.execute(sql)
            suppliers = cur.fetchall()
            cur.close()

            #Flash message
            if suppliers:
                flash('Data Displayed Successfully', 'success')
            
            return render_template('index.html', suppliers=suppliers)
        except Exception as e:
            flash('Error Inserting Data: {e}', 'error')
            return render_template('index.html')
    return render_template('index.html')

#Routing for question 5
@app.route('/display_part_info', methods = ["POST", "GET"])
def display_part_info():
    if request.method == "POST":
        Pno = request.form["question-five-pno"]
        try:
            cur = mysql.cursor()
            # Query to select data
            sql = '''
            SELECT * FROM Supplier 
            WHERE Sno IN (
                SELECT Sno FROM Shipment WHERE Pno = %s     
            )
            '''
            # Execute query
            cur.execute(sql, (Pno,))
            supplier_for_parts = cur.fetchall()
            cur.close()

            #Flash messages
            if supplier_for_parts:
                flash('Data Displayed Successfully', 'success')
           
           
            return render_template('index.html', supplier_for_parts=supplier_for_parts)
        
        except Exception as e:
            flash('Error Inserting Data: {e}', 'error')
            return render_template('index.html')
    return render_template("index.html")

#Reseting the database  
@app.route('/reset_database', methods=["GET", "POST"])
def reset_database():
    if request.method == "POST":
        try:
            cur = mysql.cursor()
            cur.execute('DROP TABLE Shipment;')  
            cur.execute('DROP TABLE Part;')      
            cur.execute('DROP TABLE Supplier;') 
            mysql.commit()

            cur.close()
            create_table()
            data_insertion()

            flash('Database reset!', 'success')
            return render_template('index.html')
        except Exception as e:
            flash(f'Error Reseting Database: {e}', 'error')
            return render_template('index.html')
    return render_template('index.html')



if __name__ == '__main__':
    create_table()
    data_insertion()
    app.run(debug=True)