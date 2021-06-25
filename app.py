from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'Hello World'

@app.route('/api',methods=['GET'])
def api():
    d = {}
    d['Query'] = str(request.args['Query'])
    return jsonify(d)


if __name__ == '__main__':
    app.run()
