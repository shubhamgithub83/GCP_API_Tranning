import requests

response = requests.post(url='http://127.0.0.1:5001/addage', json={"age":50,"random_no":90})


print("Sum of ages is : ",response.json())

response1 = requests.post(url='http://127.0.0.1:5002/sumby2', json={"sum":response.json()})

print("Age Divided by 2 is : ",response1.json())