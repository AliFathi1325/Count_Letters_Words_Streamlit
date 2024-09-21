import streamlit as st

def count_words_and_letters(text):
    # Count words
    words = text.split()
    word_count = len(words)

    # count letters (alphabetic only)
    letter_count = len([char for char in text if char.isalpha()])

    return word_count, letter_count

st.title('Program to count letters and words in the text')
st.write('''
        This app helps you count the number of words and letters (alphabet only) in the text you enter.
        Please enter your text in the box below and click the "counting" button.
''')
text = st.text_area('Please write your text', height=200)

if st.button('counting'):
    if text.split():
        word_count, letter_count = count_words_and_letters(text)
        st.success(f'Your word count: {word_count} and your letter count: {letter_count} in the text.')
    else:
        st.error('Please enter some text to analyze.')
