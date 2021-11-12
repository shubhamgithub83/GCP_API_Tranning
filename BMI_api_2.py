from flask import Flask, request, jsonify
import json, requests

app =  Flask(__name__)

def BMI(weight,heights):
    result = {}
    bmi = weight/(heights ** 2)
    result['bmi'] = bmi
    return(result)

@app.route('/bmi', methods=['POST'])
def bmiCalculation():
    input = request.get_json()
    weight = input['weight']
    height = input['height']
    BMIResult = BMI(weight,height)
    url = "http://0.0.0.0:"
    port1 = 5002
    payload = json.dumps({
        "bmi": BMIResult["bmi"]
    })
    print(payload)
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url+str(port1)+"/score", headers=headers, data=payload)
    next_response = json.loads(response.text)
    return(jsonify({"category":next_response["category"]}))

if __name__ == '__main__':
    app.run(host= '0.0.0.0',port = 5001, debug= True)