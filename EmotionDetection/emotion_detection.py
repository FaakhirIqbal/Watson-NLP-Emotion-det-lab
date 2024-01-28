import requests

def emotion_detector(text_to_analyze):
    """
    Detect emotions in the given text by making a POST request to an external API.

    Args:
    text_to_analyze (str): The text for emotion analysis.

    Returns:
    dict: A dictionary with emotions and their values or None if an error occurs.
    """
    # URL of the external emotion detection API
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Headers required by the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # The input data in JSON format
    input_json = { "raw_document": { "text": text_to_analyze } }

    # Making a POST request to the API
    response = requests.post(URL, json=input_json, headers=header)

    # Checking if the request was successful
    if response.status_code == 200:
        # Parsing the JSON response
        return response.json()
    else:
        # Returning None for each emotion in case of an error
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}

def emotion_predictor(detected_text):
    """
    Predicts the dominant emotion from the detected emotions.

    Args:
    detected_text (dict): A dictionary containing detected emotions.

    Returns:
    dict: A dictionary with the dominant emotion and its value.
    """
    # Check if all values are None (indicating an error in detection)
    if all(value is None for value in detected_text.values()):
        return detected_text

    # Processing the detected emotions to find the dominant one
    if 'emotionPredictions' in detected_text and detected_text['emotionPredictions']:
        emotions = detected_text['emotionPredictions'][0]['emotion']
        max_emotion = max(emotions, key=emotions.get)
        emotions['dominant_emotion'] = max_emotion
        return emotions

    # Return None if emotion predictions are not available
    return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
