#importing required libraries
from flask import Flask
from flask import render_template,jsonify,request
import requests
import wolframalpha
import wikipedia
from engine import *
import random
import json

app = Flask(__name__)

#route('/') decorator will help in binding home.html anytime application runs, it will upload home.html
@app.route('/')
def hello_world():
    return render_template('chatcontainer.html')

get_random_response = lambda intent:random.choice(intent_response_dict[intent])

@app.route('/chat',methods=["POST"])
def chat():
    try:
        user_message = request.form["text"]
        response = requests.get("http://localhost:5000/parse",params={"q":user_message})
        response = response.json()
        entities = response.get("entities")
        topresponse = response["topScoringIntent"]
        intent = topresponse.get("intent")
        if(len(entities)==0 and intent == "gsu-info"):
           clientwolfram = wolframalpha.Client('E2HAQT-YL96RHPLKR')
           res = clientwolfram.query(user_message)
           if user_message.find("where") != -1:
              for key,val in next(res.results).items():
                  if(key == 'infos'):
                      for key,value in val.items():
                          if(key == 'info'):
                              response_text = json.dumps(value)
                              print(response_text)
           else:
              for key,value in next(res.results).items():
                  if(key == 'subpod'):
                     for key,value in value.items():
                         if(key == 'img'):
                             for key,value in value.items():
                                 if(key == '@alt'):
                                     response_text = json.dumps(value)
                                     print(response_text)
        else:
            if intent == "gsu-info":
                response_text = gsu_info(entities)
            else:
                response_text = get_random_response(intent)
        return jsonify({"status":"success","response":response_text})
    except Exception as e:
        wikipedia_res = wikipedia.summary(user_message)
        print(wikipedia_res)
        if wikipedia_res:
            return jsonify({"status":"success","response":wikipedia_res})
        else:
            return jsonify({"status":"success","response":"Sorry I will give back to you on this next time..."})

app.config["DEBUG"] = True
if __name__ == "__main__":
    app.run(port=8080)
