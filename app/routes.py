from flask import render_template, send_file
from app import app


@app.route('/') 
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/total_sentiment', methods = ['GET', 'POST'] )
def total_sentiment():
    total_labels = ['Hostile Language', 'Defensive Language', 'Overlapping Language', 'Unrelated Discussion']
    total_values = [15664, 47475, 52296, 719]
    return render_template('total_sentiment.html', labels=total_labels, values=total_values)

@app.route('/left_sentiment', methods = ['GET', 'POST'] )
def left_sentiment():
    left_labels = ['Hostile Language', 'Defensive Language', 'Overlapping Language', 'Unrelated Discussion']
    left_values = [126, 246, 192, 5]
    return render_template('left_sentiment.html', labels=left_labels, values=left_values)

@app.route('/right_sentiment', methods = ['GET', 'POST'] )
def right_sentiment():
    right_labels = ['Hostile Language', 'Defensive Language', 'Overlapping Language', 'Unrelated Discussion']
    right_values = [169, 249, 212, 0]
    return render_template('right_sentiment.html', labels=right_labels, values=right_values)

@app.route('/activity', methods = ['GET', 'POST'] )
def activity():
    return render_template('activity.html', title='Activity')

@app.route('/raw_data_collection', methods = ['GET', 'POST'] )
def raw_data():
    p = "downloadable_data.json"
    return send_file(p, as_attachment=True)


@app.route('/methods', methods = ['GET', 'POST'] )
def study_methods():
    return render_template('methods.html', title='Methods')

@app.route('/analysis_conclusion', methods = ['GET', 'POST'] )
def analysis_conclusion():
    return render_template('analysis_conclusion.html', title='Methods')