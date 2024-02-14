from flask import Flask, render_template, jsonify

app=Flask("__name__")

JOBS=[
    {'ID':1,'title':'Junior Engineer1', 'Location':'Seoul','salary':'10000'},
    {'ID':2,'title':'Junior Engineer2', 'Location':'Seoul','salary':'10000'},
    {'ID':3,'title':'Junior Engineer3', 'Location':'Seoul','salary':'10000'},
    {'ID':4,'title':'Junior Engineer4', 'Location':'Seoul','salary':'10000'},
]

@app.route("/")
def hello_world():
    #return "Hello you mother fucker!"
    return render_template("index.html",job=JOBS)

@app.route("/api/jobs")
def databank():
    return jsonify(JOBS)

@app.route("/main")
def main():
    Result=plus(2,3)
    return "you fuck ass hole "+str(Result)

def plus(a,b):
    return a+b

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)