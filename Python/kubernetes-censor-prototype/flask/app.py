from flask import Flask, render_template, url_for, request
import sys
import datetime
sys.path.append('../censor-code')
from censorText import censor_text
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    time_start = datetime.datetime.now()
    content = ''
    output = ''
    if request.method == 'POST':
        content = request.form['content']
        output = censor_text(content)
        time_end = datetime.datetime.now()
        timetocompute = str((time_end - time_start).microseconds // 1000)
        return render_template('index.html', output=output, content=content, timetocompute=timetocompute)
    else:
        return render_template('index.html', output=output, content=content)

if __name__ == "__main__":
    app.run(debug=True)