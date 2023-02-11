# Wattsapp-chat-analyser
EDA of WhatsApp personal chat or group chat deployed through streamlit library of python. 




https://user-images.githubusercontent.com/102272183/215309181-18507e7c-0572-4d53-a6d7-78d9518585c9.mp4

## About Preprocessor.py and Helper.py

## Preprocessor.py
This python file contains the code for preprocessing the chat data. It is used to extract the relevant information from the chat and store it in a pandas dataframe. The information that is stored in the dataframe includes date and time of the message, name of the user who sent the message, the message, the day of the week, the hour, and the period of the day when the message was sent.

The preprocess function in the Preprocessor.py takes the raw chat data as input and returns the preprocessed data in the form of a pandas dataframe.

## The following libraries are imported in Preprocessor.py:
re (for regular expression operations)

pandas (for data processing and manipulation)

## Helper.py
This python file contains helper functions that are used to fetch various statistics and insights from the chat data. It uses the data that is obtained from the Preprocessor.py.

### The following libraries are imported in Helper.py:

urlextract (for extracting URLs from text)

wordcloud (for creating word clouds)

pandas (for data processing and manipulation)

collections (for counting elements in a list)

emoji (for emoji processing)

### The functions in Helper.py include:


fetch_stats: This function takes two arguments, the selected user and the preprocessed data obtained from Preprocessor.py. It returns the number of messages sent by the selected user, the number of words in those messages, the number of media messages sent by the selected user, and the number of links shared by the selected user.

most_busy_users: This function takes the preprocessed data as input and returns the top most active users and their contribution in the form of a percentage.
create_wordcloud: This function takes the selected user and the preprocessed data as input. It returns a word cloud representing the most common words used by the selected user.

most_common_words: This function takes the selected user and the preprocessed data as input. It returns the most common words used by the selected user.

## Note: For the wordcloud and most_common_words functions, a text file named 'stop_Hinglish.txt' is used to remove stop words.

