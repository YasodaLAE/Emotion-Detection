import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    if response.status_code == 400:
        return {'anger': None, 'disgust': None,'fear': None,'joy': None,'sadness': None,'dominant_emotion': None }
    elif response.status_code == 200:
        emotionDict = {}
        proba = 0
        label = formatted_response['emotionPredictions'][0]['emotion']
        for key, value in label.items():
            emotionDict[key] = value
            if value > proba:
                proba = value
                emotion = key 
        return {'anger': emotionDict['anger'], 'disgust': emotionDict['disgust'],'fear': emotionDict["fear"],
                'joy': emotionDict['joy'],
                'sadness': emotionDict['sadness'],
                'dominant_emotion': emotion }
