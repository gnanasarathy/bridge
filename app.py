from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/api',methods=['GET'])
def api():
    d = {}
    d['Query'] = str(request.args['Query'])
    flag=int(d['Query'])
    if flag==1:
        f = open("file.txt", "w")
        f.write("yes")
        f.close()
    else:
        f = open("file.txt", "w")
        f.write("no")
        f.close()
    return jsonify(d)

@app.route('/ans')
def ans():
    f = open("file.txt", "r")
    t=f.read()
    return jsonify(t)


if __name__ == '__main__':
    app.run()
