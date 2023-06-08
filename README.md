# Game Subtitle Recognition and Translation

This repository contains a Python project for recognizing subtitles in games and displaying them in the desired language. The project utilizes computer vision, natural language processing, and user interface development techniques.

## Features

- Extracts subtitles from game screens using computer vision techniques.
- Performs optical character recognition (OCR) on the extracted subtitle text.
- Detects the language of the subtitles.
- Translates the subtitles into the desired language using pre-trained models.
- Displays the translated subtitles in real-time on the game screen.

## Requirements

- Python 3.7 or higher
- OpenCV (`cv2`) - Install using `pip install opencv-python`
- Tkinter - Included with Python (no additional installation required)
- MSS (`mss`) - Install using `pip install mss`
- NumPy - Install using `pip install numpy`
- PyTesseract - Install using `pip install pytesseract`
- Transformers - Install using `pip install transformers`

## Usage

1. Clone the repository:
``` git clone https://github.com/your-username/game-subtitle-recognition.git ```
2. Install the required libraries (if not installed already):
``` pip install -r requirements.txt ```
3. Run the main script:
``` python SubtitleTranslator.py ```
4. Follow the on-screen instructions to configure the desired language and view the translated subtitles.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [OpenCV](https://opencv.org/)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [Hugging Face Transformers](https://huggingface.co/transformers)

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
