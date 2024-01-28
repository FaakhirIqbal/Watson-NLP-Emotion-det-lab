import unittest
from EmotionDetection.emotion_detection import emotion_detector, emotion_predictor

class TestEmotionDetection(unittest.TestCase):
    """
    Test suite for emotion detection functionality.
    """

    def test_emotion_predictor(self):
        """
        Test cases for emotion_predictor function.
        """
        test_cases = [
            ("I am glad this happened", 'joy'),
            ("I am really mad about this", 'anger'),
            ("I feel disgusted just hearing about this", 'disgust'),
            ("I am so sad about this", 'sadness'),
            ("I am really afraid that this will happen", 'fear')
        ]

        for text, expected_emotion in test_cases:
            with self.subTest(text=text):
                result = emotion_predictor(emotion_detector(text))
                self.assertEqual(result['dominant_emotion'], expected_emotion, f"Failed for text: {text}")

if __name__ == '__main__':
    unittest.main()
