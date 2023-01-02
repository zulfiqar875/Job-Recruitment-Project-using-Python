#import libraries

from flask import Flask, render_template, request, session, redirect, url_for
from flask_mysqldb import MySQL
import MySQLdb.cursors
import mysql.connector
app = Flask(__name__)
app.secret_key = 'jobrecuirment'

#code for connection
app.config['MYSQL_HOST'] = 'localhost'#hostname
app.config['MYSQL_USER'] = 'root'#username
app.config['MYSQL_PASSWORD'] = ''#password
#in my case password is null so i am keeping empty
app.config['MYSQL_DB'] = 'Job'#database name

mysql = MySQL(app)

@app.route("/")
def index():
    return render_template("Index.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/report")
def report():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    cursor.execute('SELECT * FROM Contactus')
    data = cursor.fetchall()
    return render_template("Report.html", report = data)

@app.route('/register',methods=['POST'])
def register():
    msg=''
    # print("testing page")
    #applying empty validation
    if request.method == 'POST':
        #passing HTML form data into python variable
        a = request.form['fname']
        b = request.form['lname']
        c = request.form['cnic']
        d = request.form['gender']
        e = request.form['email']
        f = request.form['phone']
        g = request.form['address']
        h = ""
        i = request.form['password']
        #creating variable for connection
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        #query to check given data is present in database or no
        cursor.execute('SELECT * FROM User WHERE Email = % s', (e,))
        #fetching data from MySQL
        result = cursor.fetchone()
        if result:
            msg = 'User already exists !'
            return render_template('signup.html', msg=msg)
        else:
            #executing query to insert new data into MySQL
            cursor.execute('INSERT INTO User VALUES (NULL, % s, %s, % s, % s, % s, % s, % s, % s, % s, %s)', (a, b, c, d, e,f,g,h,i, '2'))
            mysql.connection.commit()
            #displaying message
            msg = 'Thanks For Joing Us!'
            return render_template('Index.html', msg=msg)

    elif request.method == 'POST':
        msg = 'Please fill out the form !'
        return render_template('signup.html', msg=msg)
    
@app.route('/login',methods=['GET','POST'])
def projectreg():
    msg=''
    #applying empty validation
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        #passing HTML form data into python variable
        a = request.form['username']
        b = request.form['password']
        #creating variable for connection
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        #query to check given data is present in database or no
        cursor.execute('SELECT * FROM User WHERE Email = %s AND Password = %s', (a, b,))
        #fetching data from MySQL
        result = cursor.fetchone()
        print (result)
        if result:
            session['loggedin'] = True
            session['id'] = result['Uid']
            session['username'] = result['Fname']
            session['type'] = result['Type']
            msg = "Logged in successfully!"
            return redirect(url_for('home'))
        else:
            msg = 'Incorrect email/password!'
            return render_template('Index.html', msg=msg)

    elif request.method == 'POST':
        msg = 'Please fill out the form !'
        return render_template('Index.html', msg=msg)

@app.route('/login/home')
def home():
    # Check if user is loggedin
    if 'loggedin' in session:
        if session['type'] == 2:
            msg = "Logged in successfully!"
            return render_template('udashboard.html', msg = msg, username=session['username'], userid = session['id'])
        elif session['type'] == 1:
            msg = "Logged in successfully!"
            return render_template('admin.html', msg = msg, username=session['username'], userid = session['id'])
        elif session['type'] == 3:
            msg = "Logged in successfully!"
            uid = session['id']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT COUNT(*) FROM jobs Where Cid = % s', [uid])
            data = cursor.fetchone()

            cursor.execute('SELECT COUNT(*) FROM applyjob Where Cid = % s', [uid])
            resume = cursor.fetchone()
            
            cursor.execute('SELECT COUNT(*) FROM applyjob Where Cid = % s AND Status = % s', ([uid], 'Approved (Shortlist)'))
            complete = cursor.fetchone()
            
            return render_template('jdashboard.html',job = data, resume = resume, complete = complete, msg = msg, username=session['username'], userid = session['id'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))

@app.route('/login/resume')
def resume():
    # Check if user is loggedin
    if 'loggedin' in session:
        msg = "Logged in successfully!"
        return render_template('resume.html', msg = msg, username=session['username'], userid = session['id'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))

@app.route('/createresume',methods=['POST'])
def createresume():
    msg=''
    print(request.form)
    # print("testing page")
    #applying empty validation
    if request.method == 'POST':
        #creating variable for connection
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        
        print(request.form['degree1'])
        cursor.execute('INSERT INTO resume VALUES (NULL,%s , %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s)', 
                        (request.form['Uid'], request.form['degree1'], request.form['pass1'], request.form['status1'], request.form['degre2'], request.form['pass2'], request.form['status2'],request.form['degree3'], request.form['pass3'], request.form['status3'],request.form['degre4'], request.form['pass4'], request.form['status4'],request.form['degree5'], request.form['pass5'], request.form['status5'],request.form['company1'], request.form['dest1'], request.form['sdate1'], request.form['edate1'],request.form['company2'], request.form['dest2'], request.form['sdate2'], request.form['edate2'],request.form['company3'], request.form['dest3'], request.form['sdate3'], request.form['edate3'], request.form['certificate1'], request.form['title1'], request.form['csdate1'], request.form['cedate1'], request.form['certificate2'], request.form['title2'], request.form['csdate2'], request.form['cedate2'], request.form['certificate3'], request.form['title3'], request.form['csdate3'], request.form['cedate3'], request.form['skill1'], request.form['level1'], request.form['skill2'], request.form['level2'], request.form['skill3'], request.form['level3'],request.form['language1'], request.form['llevel1'], request.form['language2'], request.form['llevel2'], request.form['language3'], request.form['llevel3'], request.form['job']  ))
        mysql.connection.commit()
            #displaying message
        msg = 'Resume Updated!'
        return redirect(url_for('home'))

    elif request.method == 'POST':
        msg = 'Please fill out the form !'
        return render_template('signup.html', msg=msg)

@app.route('/login/newjobs')
def newjobs():
    # Check if user is loggedin
    if 'loggedin' in session:
        msg = "Logged in successfully!"
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM jobs')
        data = cursor.fetchall()
        return render_template('jobs.html', company = data , msg = msg, username=session['username'], userid = session['id'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))

@app.route('/jobview', methods=['POST'])
def jobview():
    # Check if user is loggedin
    if 'loggedin' in session:
        msg = "Logged in successfully!"
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM jobs Where Jid = % s', (request.form['jid']))
        data = cursor.fetchone()
        # print(data)
        cid = request.form['cid']
        id = data['Jid']
        title = data['Title']
        sec  = data['Sector']
        des  = data['Description']
        exp  = data['Experience']
        typ  = data['Type']
        bene = data['Benefit']
        sal  = data['Salary']
        return render_template('jobview.html', a = title, b = sec, c = des, d = exp, e = typ, f = bene, g = sal, i = id, cid = cid , msg = msg, username=session['username'], userid = session['id'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))


@app.route('/applyjob',methods=['POST'])
def applyjob():
    msg=''
    print(request.form)
    #applying empty validation
    if request.method == 'POST':
        #creating variable for connection
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        cursor.execute('INSERT INTO applyjob VALUES (NULL,%s , %s, %s, %s, %s, %s, %s, %s)', 
        (request.form['Uid'], request.form['Jid'], request.form['Cid'],request.form['username'], 'panding',request.form['title'], request.form['sector'], request.form['type'],))
        mysql.connection.commit()
            #displaying message
        msg = 'Resume Updated!'
        return redirect(url_for('home'))

    elif request.method == 'POST':
        msg = 'Please fill out the form !'
        return render_template('signup.html', msg=msg)


@app.route('/login/appliedjob')
def appliedjob():
    # Check if user is loggedin
    if 'loggedin' in session:
        msg = "Logged in successfully!"
        d = session['id']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM applyjob Where Uid = % s', (session['id'],))
        # c = "SELECT jobs.Title, jobs.Sector, applyjob.Status FROM jobs LEFT JOIN applyjob ON jobs.Jid = applyjob.Jid=2"
        # cursor.execute(c)
        data = cursor.fetchall()
        print(data)
        return render_template('appliedjob.html', appliedjob = data , username=session['username'], userid = session['id'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))
# ===============================================================
#                           Admin Routes
@app.route('/login/company')
def company():
    # Check if user is loggedin
    if 'loggedin' in session:
        msg = "Logged in successfully!"
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM User Where Type = % s', ('3',))
        data = cursor.fetchall()
        return render_template('company.html', company = data , msg = msg, username=session['username'], userid = session['id'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))

@app.route('/createcompany',methods=['POST'])
def addcompany():
    msg=''
    #applying empty validation
    if request.method == 'POST':
        #passing HTML form data into python variable
        a = request.form['companyname']
        b = request.form['companyowner']
        c = request.form['companysector']
        d = request.form['companyaddress']
        e = request.form['companycontact']
        f = request.form['companyemail']
        g = request.form['companypassword']
        h = request.form['companystatus']
        #creating variable for connection
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        #query to check given data is present in database or no
        cursor.execute('SELECT * FROM User WHERE Email = % s', (f,))
        #fetching data from MySQL
        result = cursor.fetchone()
        if result:
            msg = 'User already exists!'
            return redirect(url_for('home'))
        else:
            #executing query to insert new data into MySQL
            cursor.execute('INSERT INTO User VALUES (NULL, % s, %s, % s, % s, % s, % s, % s, % s, % s, %s)', (a, b, c,'' ,f,e,d,h,g,'3'))
            mysql.connection.commit()
            #displaying message
            msg = 'Thanks For Joing Us!'
            return redirect(url_for('home'))

    elif request.method == 'POST':
        msg = 'Please fill out the form !'
        return render_template('signup.html', msg=msg)

@app.route('/login/user')
def user():
    # Check if user is loggedin
    if 'loggedin' in session:
        msg = "Logged in successfully!"
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM User Where Type = % s', ('2',))
        data = cursor.fetchall()
        return render_template('user.html', company = data , msg = msg, username=session['username'], userid = session['id'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))


# ===============================================================
#                           Company Routes

@app.route('/login/companyjobs')
def companyjobs():
    # Check if user is loggedin
    if 'loggedin' in session:
        msg = "Logged in successfully!"
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM jobs Where Cid = % s', (session['id'],))
        data = cursor.fetchall()
        return render_template('Companyjob.html', company = data , msg = msg, username=session['username'], userid = session['id'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))

@app.route('/createjobs',methods=['POST'])
def createjobs():
    msg=''
    #applying empty validation
    if request.method == 'POST':
        #passing HTML form data into python variable
        a = request.form['jobsector']
        b = request.form['title']
        c = request.form['description']
        d = request.form['experience']
        e = request.form['type']
        f = request.form['benefit']
        g = request.form['salary']
        h = request.form['jobstatus']
        i = request.form['Cid']
        #creating variable for connection
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        #executing query to insert new data into MySQL
        cursor.execute('INSERT INTO jobs VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (i,a, b, c,d,e,f,g,h))
        mysql.connection.commit()
        #displaying message
        msg = 'Thanks For Joing Us!'
        return redirect(url_for('home'))

    elif request.method == 'POST':
        msg = 'Please fill out the form !'
        return render_template('signup.html', msg=msg)


@app.route('/login/jobrequest')
def jobrequest():
    # Check if user is loggedin
    if 'loggedin' in session:
        msg = "Logged in successfully!"
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM User Where Type = % s', ('3',))
        data = cursor.fetchall()
        return render_template('company.html', company = data , msg = msg, username=session['username'], userid = session['id'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))



@app.route('/login/jobresume')
def jobresume():
    # Check if user is loggedin
    if 'loggedin' in session:
        msg = "Logged in successfully!"
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM applyjob Where Cid = % s', (session['id'],))
        data = cursor.fetchall()
        return render_template('jobresume.html', company = data , msg = msg, username=session['username'], userid = session['id'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))

@app.route('/login/userinfo')
def userinfo():
    # Check if user is loggedin
    if 'loggedin' in session:
        msg = "Logged in successfully!"
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM applyjob Where Cid = % s', (session['id'],))
        data = cursor.fetchaonce()
        return render_template('jobresume.html', company = data , msg = msg, username=session['username'], userid = session['id'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))



@app.route('/jobaction', methods=['POST'])
def jobaction():
    # Check if user is loggedin
    if 'loggedin' in session:
        msg = "Logged in successfully!"
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user Where Uid = % s', (request.form['uid'],))
        data = cursor.fetchone()
        cursor.execute('SELECT * FROM resume Where Uid = % s', (request.form['uid'],))
        res = cursor.fetchone()
        return render_template('userdetail.html', Aid = request.form['aid'], info = data ,resume = res , msg = msg, username=session['username'], userid = session['id'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))


@app.route('/checked',methods=['POST'])
def checked():
    msg=''
    #applying empty validation
    if request.method == 'POST':
        #passing HTML form data into python variable
        a = request.form['status']
        print(a)
        print(request.form['aid'])
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # cursor.execute("UPDATE applyjob SET Status = %s WHERE Aid = %s", 
        #        (a, request.form['aid'],))
        import mysql.connector
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="job"
        )

        mycursor = mydb.cursor()
        sql = "UPDATE applyjob SET Status = %s WHERE Aid = %s"
        val = (a, request.form['aid'])

        mycursor.execute(sql, val)

        mydb.commit()
        # res = cursor.fetchone()


        msg = 'Thanks For Joing Us!'
        return redirect(url_for('home'))
# ===============================================================
#                           All Logout Routes
@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   msg = 'Sucessfully Logout!'
   return redirect(url_for('index'))
    
if __name__ == "__main__":
    app.run(debug=True)
  