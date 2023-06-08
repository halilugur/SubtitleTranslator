import cv2
import mss.tools
import numpy as np
import pytesseract
from transformers import MarianMTModel, MarianTokenizer

pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'


class SubtitleTranslator:
    def __init__(self, target_language, game_area_coordinates, translation_model):
        self.target_language = target_language
        self.game_area_coordinates = game_area_coordinates

        # Set up the translation model
        self.translator = MarianMTModel.from_pretrained(translation_model)
        self.tokenizer = MarianTokenizer.from_pretrained(translation_model)

    def detect_and_translate_subtitles(self, roi):
        subtitle_text = pytesseract.image_to_string(roi, lang="eng")
        translated_text = self.translate_text(subtitle_text)
        return translated_text

    def translate_text(self, text):
        # Tokenize the input text
        input_ids = self.tokenizer.encode(text, return_tensors='pt')

        # Translate the text
        translated_ids = self.translator.generate(input_ids, num_beams=4, max_length=100, early_stopping=True)

        # Decode and return the translated text
        translated_text = self.tokenizer.decode(translated_ids[0], skip_special_tokens=True)

        return translated_text

    def process_subtitles(self, translated_subtitles):
        # Process the translated subtitles as desired
        # For example, you can perform additional text processing or send the translated text to another system

        # Print the translated subtitles
        print(translated_subtitles)

    def run_translation(self, process_subtitles=True):
        with mss.mss() as sct:
            while True:
                # Capture the game window screenshot
                game_window = np.array(sct.grab(sct.monitors[1]))  # Adjust the monitor index as needed

                # Get the screen dimensions
                screen_height, screen_width, _ = game_window.shape

                # Adjust game area coordinates if it exceeds screen dimensions
                game_area_height = min(self.game_area_coordinates['height'],
                                       screen_height - self.game_area_coordinates['left'])
                game_area_width = min(self.game_area_coordinates['width'],
                                      screen_width - self.game_area_coordinates['top'])

                # Extract the game area containing subtitles
                game_area = game_window[
                            self.game_area_coordinates['left']:self.game_area_coordinates['left'] + game_area_height,
                            self.game_area_coordinates['top']:self.game_area_coordinates['top'] + game_area_width]

                # Detect and translate subtitles in the game area
                translated_subtitles = self.detect_and_translate_subtitles(game_area)

                # Process the translated subtitles
                if process_subtitles:
                    self.process_subtitles(translated_subtitles)

                # Break the loop if 'q' key is pressed
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
