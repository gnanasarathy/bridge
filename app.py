from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/api',methods=['GET'])
def api():
    d = {}
    r = {}
    r['state'] = 0
    d['Query'] = str(request.args['Query'])
    if d['Query'] == '1':
        r['state']= 1
    return jsonify(r)


if __name__ == '__main__':
    app.run()
