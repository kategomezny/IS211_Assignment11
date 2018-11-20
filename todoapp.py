#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""delivers a Flask app that provides a simple

To Do List app"""


from flask import Flask, render_template, request, redirect

from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, SelectField

from wtforms.validators import DataRequired, Email


task = []


class InputTask(FlaskForm):

    TaskName = StringField('Task', validators =[DataRequired()])

    Priority = SelectField('Priority level', choices = [('low','Low'),('medium','Medium'),('high','High') ])

    Email = StringField('Email', validators =[DataRequired(), Email()])

    Submit = SubmitField('Submit')
    

app = Flask(__name__)

app.config['SECRET_KEY']= '2851479a9def3bf88beedf53fdb26f71'


@app.route('/', methods = ['POST','GET'])

def index():

    Myform =  InputTask()

    return render_template('index.html', totallist=len(task), form=Myform)


@app.route('/submit',methods = ['POST', 'GET'])

def Submit():

    if request.method == 'POST':

       results = request.form.to_dict()

       task.append(results)

       return render_template("submit.html",mydata=task)
   

@app.route('/clear', methods = ['POST'])

def clear_list():

    del task[:]

    return redirect('/')


if __name__ == '__main__':

    app.run(debug=True)


