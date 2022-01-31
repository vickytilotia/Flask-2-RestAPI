from flask import Flask, render_template, request, redirect, jsonify    

app = Flask(__name__)



@app.route('/<int:a>')
def avg(a):
    # return str((a+a)//2)
    result = {
        "Number" : a,
        "Square of Number" : a**2,
        "Cube of a Number" : a**3,
    }
    return jsonify(result)





if __name__=="__main__":
    app.run(debug=True)