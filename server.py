from flask import Flask , render_template, request, redirect, session

app = Flask(__name__)
app.secret_key='159487263'

@app.route('/')
def index():
    if 'count' not in session:
        session['count']=0
    session['count']+=1
    return render_template("index.html", count= session['count'])

@app.route('/add_two')
def addtwo():
    session['count']+=1
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)