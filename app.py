import os
from flask import Flask, render_template, request
    # import libraries
app=Flask(__name__)

@app.route('/')
def index():
    return(render_template('index.html'))

@app.route('/',methods=['POST'])
def getvalue():
    symbol=request.form['search']

    f=open('history.csv',"a")
    line = str(symbol)+"\n"
    f.write(line)
    f.close()
    return(render_template('index.html', sym=symbol))

if __name__=='__main__':
    app.run(debug=True)
    os.system('python my_file.py')
