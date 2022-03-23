from flask import render_template, send_file
from app import app

@app.route('/') 
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

#Returning variables from the results.py file to keep the routes more object oriented
@app.route('/total_sentiment', methods = ['GET', 'POST'] )
def total_sentiment():
    from app.results import language_labels, total_results
    total_labels = language_labels
    total_values = total_results
    return render_template('total_sentiment.html', labels=total_labels, values=total_values)

@app.route('/left_sentiment', methods = ['GET', 'POST'] )
def left_sentiment():
    from app.results import language_labels, left_results
    left_labels = language_labels
    left_values = left_results
    return render_template('left_sentiment.html', labels=left_labels, values=left_values)

@app.route('/right_sentiment', methods = ['GET', 'POST'] )
def right_sentiment():
    from app.results import language_labels, right_results
    right_labels = language_labels
    right_values = right_results
    return render_template('right_sentiment.html', labels=right_labels, values=right_values)

@app.route('/activity', methods = ['GET', 'POST'] )
def activity():
    from app.results import m_time_list, m_count_list 
    activity_labels = m_time_list
    activity_values = m_count_list
    return render_template('activity.html', labels=activity_labels, values=activity_values)

#Sending a compressed JSON to the end user. Use Pandas "pd.read_json('')" to reconvert the file to a readable dataframe
@app.route('/raw_data_collection', methods = ['GET', 'POST'] )
def raw_data():
    p = "downloadable_data.json.zip"
    return send_file(p, as_attachment=True)

#Final two routes are returning text in the body of the .html templates they refer to
@app.route('/methods', methods = ['GET', 'POST'] )
def study_methods():
    return render_template('methods.html', title='Methods')

@app.route('/analysis_conclusion', methods = ['GET', 'POST'] )
def analysis_conclusion():
    return render_template('analysis_conclusion.html', title='Methods')