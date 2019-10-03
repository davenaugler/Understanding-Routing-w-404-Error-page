from flask import Flask, abort, render_template

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def sayName(name):
    print(name)
    return "Hi " + name + "!"

@app.route('/repeat/<int:num>/<word>')
def repeat(num, word):
    print(num,",",word)
    # num = int(num)
    stringWords = ''
    for x in range(0, num, 1):
        stringWords = stringWords + word + ' '
    print(num)
    return stringWords

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")
    # return 'This is a 404 Error! Please check the URL and try again.'


if __name__=="__main__":
    app.run(debug=True)