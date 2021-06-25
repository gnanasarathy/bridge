from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'

r=0

@app.route('/api',methods=['GET'])
def api():
    global r
    d = {}
    d['Query'] = str(request.args['Query'])
    flag=int(d['Query'])
    if flag==1:
        r=1
    else:
        r=0
    return jsonify(d)

@app.route('/ans')
def ans():
    return jsonify(r)


if __name__ == '__main__':
    app.run()
