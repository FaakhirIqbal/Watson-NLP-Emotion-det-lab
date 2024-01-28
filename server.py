from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector, emotion_predictor

# Initialize Flask app
app = Flask(__name__)

@app.route("/emotionDetector")
def sent_detector():
    """
    Endpoint to analyze text for emotions.

    Returns:
    str: A string describing the detected emotions and the dominant emotion.
    """
    # Retrieving text from the request's query parameter
    text_to_detect = request.args.get('textToAnalyze', '')

    # Ensure text is provided
    if not text_to_detect:
        return "No text provided. Please input text for analysis."

    # Call the emotion detection and prediction functions
    response = emotion_detector(text_to_detect)
    formatted_response = emotion_predictor(response)

    # Check for valid response
    if formatted_response['dominant_emotion'] is None:
        return "Error in emotion detection. Please try again."

    # Formatting the response string
    response_str = ", ".join([f"'{emotion}': {score}" for emotion, score in formatted_response.items() if emotion != 'dominant_emotion'])
    return f"For the given statement, the system response is {response_str}. The dominant emotion is {formatted_response['dominant_emotion']}."

@app.route("/")
def render_index_page():
    """ Render the main index page of the application. """
    return render_template('index.html')

if __name__ == "__main__":
    # Run the Flask application
    app.run(host="0.0.0.0", port=5000)
