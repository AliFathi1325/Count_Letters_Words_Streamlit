<!-- @format -->

# Word and Letter Counting App whit Streamlit

This project is a simple Streamlit web application that allows users to count the number of words and letters in a given block of text.

## Features

- **Word Count**: Counts the total number of words in the input text.
- **Letter Count**: Counts the total number of alphabetic characters in the text.
- Provides user-friendly feedback for both successful counts and error handling if no text is entered.

## How to Run the App

### Prerequisites

- Python 3.x
- Streamlit must be installed. If not installed, you can do so with the following command:

  pip install streamlit

### Running the Application

To run the application locally, follow these steps:

1. Clone or download this repository.
2. Navigate to the directory containing the `main.py` file.
3. Run the following command in your terminal:

   streamlit run main.py

4. This will launch the app in your default browser.

## Usage

1. After running the app, you will see a title and a text area where you can input any text.
2. Enter your text in the provided text box.
3. Click the **"counting"** button.
4. The app will display the word count and letter count (alphabetical characters only) based on your input.

## Example

- Input: "Hello World!"
- Output:
  - Word Count: 2
  - Letter Count: 10

## Technologies Used

- **Python**: Core programming language.
- **Streamlit**: Framework for building interactive web applications.
