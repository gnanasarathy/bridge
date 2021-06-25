from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'

r = {}
r['state'] = 0

@app.route('/api',methods=['GET'])
def api():
    d = {}
    d['Query'] = str(request.args['Query'])
    if d['Query'] == '1':
        r['state']= 1
    else:
        r['state']= 0
    return jsonify(d)

@app.route('/ans')
def ans():
    return jsonify(r)


if __name__ == '__main__':
    app.run()
