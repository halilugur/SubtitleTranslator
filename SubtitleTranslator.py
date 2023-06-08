# Create an instance of the class
from AreaSelectScreen import AreaSelection
from SubtitleCapture import SubtitleTranslator

area_selection = AreaSelection()
x, y, width, height = area_selection.get_selected_area()

# Target language for translation (e.g., 'tr' for Turkish)
target_language = 'tr'

# Adjust the coordinates to match the game area containing subtitles
game_area_coordinates = {'top': x, 'left': y, 'width': width, 'height': height}

# Translation model name
translation_model = 'Helsinki-NLP/opus-mt-tc-big-en-tr'

translator = SubtitleTranslator(target_language, game_area_coordinates, translation_model)
translator.run_translation()
