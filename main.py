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
    # __name__ is interpereter variable store name of file
    # __main__ is interpreter variable store name of file that has to be run 
    # like python manage.py, here manage.py is __main__
    # basically it prevent executing this function when this file is imported in another file
    
    app.run(debug=True)