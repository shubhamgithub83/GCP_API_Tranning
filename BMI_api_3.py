from flask import Flask, request, jsonify
import json

app =  Flask(__name__)

def category(bmi):
    result = {}
    if bmi < 18.5:
        result['category'] = "Under Weight"
    elif bmi >= 18.5 and bmi <= 24.9:
        result['category'] = "Normal"
    elif bmi >= 25 and bmi <= 29.9:
        result['category'] = "Over Weight"
    elif bmi >= 30 and bmi <= 34.9:
        result['category'] = "Obese"
    else:
        result['category'] = "Extreme Obese"
    return(result)

@app.route('/score', methods=['POST'])
def bmiCategory():
    input = request.get_json()
    bmi = input['bmi']
    CategoryResult = category(bmi)
    dump = CategoryResult["category"]
    return(jsonify({"category":dump}))

if __name__ == '__main__':
    app.run(debug= True,host= '0.0.0.0',port = 5002)