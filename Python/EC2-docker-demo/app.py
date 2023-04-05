import os

import json
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Docker hosted on AWS test for AI Lab'

@app.route('/', methods=['POST'])
def regex_phone_numbers():
    record = json.loads(request.data)
    content = record["data"]
    result = re.finditer(r"\(?\d{3}\)?[- .]\d{3}[- .]\d{4}", content, re.MULTILINE)
    ret, prevend = '', 0
    for match in result:
        sStart, sEnd = match.span()
        pNumber = content[sStart:sEnd]
                                                # replace with commented out if format/length dont need to be censored
        ret += content[prevend:sStart] + "*"*10 #''.join("*" if c.isdigit() else c for c in pNumber)
        prevend = sEnd
    ret += content[prevend:]
    return ret


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
