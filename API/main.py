from crypt import methods
from flask import Flask,jsonify,request
app=Flask(__name__)
@app.route('/celsiustofahrenheit',methods=['POST'])
def ctof():
    data=request.get_json()
    temperature=data["temperature"]
    c=(1.8*temperature)+32
    output=str(temperature)+"degree celsius is"+str(c)+"degree fahrenheit"
    return(jsonify({"output":output}))
if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)