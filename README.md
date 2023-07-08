# Chat GPT with Voice and Speech Recognition
🤖 This repository contains a Python program that implements a chatbot using the GPT-3.5 model. The chatbot has a graphical user interface (GUI) and supports voice input and speech recognition.

## Features

- Chat with the AI-powered chatbot using both text and voice input.
- The chatbot uses OpenAI's GPT-3.5 model to generate responses.
- Speech recognition is implemented using the `speech_recognition` library.
- Text-to-speech functionality is provided using the `pyttsx3` library.
- Conversations are stored in a SQLite database for future reference.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/pablosierrafernandez/Chat-GPT-with-Voice-and-Speech-Recognition.git
   ```

2. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Set up the OpenAI API key:
   
   - Sign up for an OpenAI account and obtain an API key.
   - Replace the `api_key` variable in both `chat.py` and `gui.py` files with your API key.

## Usage

### Command-line Interface (chat.py)

Run the `chat.py` file to start the chatbot in the command-line interface.

```
python chat.py
```

You can interact with the chatbot by typing your messages or speaking to it. The chatbot will respond using text and speech.

### Graphical User Interface (gui.py)

Run the `gui.py` file to start the chatbot with a graphical user interface.

```
python gui.py
```

The GUI provides a more user-friendly way to chat with the bot. You can enter text messages in the input field or click the microphone button to speak your message. The chatbot's responses will be displayed in the chat area.

## Configuration

Before running the chatbot, make sure to configure the API key and language settings.

- To configure the API key, open the `gui.py` file and modify the `api_key` variable with your OpenAI API key.

- To change the language, open the `gui.py` file and modify the `new_lang` variable. Supported language options are `'es-Es'` for Spanish and `'en-US'` for English.


## Acknowledgements

- This project utilizes the OpenAI GPT-3.5 model. Visit the [OpenAI website](https://openai.com) for more information.
- The speech recognition functionality is powered by the `speech_recognition` library. Visit the [GitHub repository](https://github.com/Uberi/speech_recognition) for more details.
- The text-to-speech functionality is provided by the `pyttsx3` library. Visit the [GitHub repository](https://github.com/nateshmbhat/pyttsx3) for more details.


## Disclaimer

This chatbot is an experimental project and may not always provide accurate or appropriate responses. Use it at your own risk. The developers are not responsible for any consequences resulting from the use of this chatbot.

