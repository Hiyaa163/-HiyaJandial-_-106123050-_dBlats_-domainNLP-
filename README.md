# -HiyaJandial-_-106123050-_dBlats_-domainNLP-
Youtube Transcript Summarizer
This code extracts the transcript of a given YouTube video, processes the text by removing unnecessary words, and generates a summary after scoring the sentences using TF-IDF.
It fetches the transcript of a YouTube video using the **YouTube Transcript API**.
Then the transcript is preprocessed by:
  - Tokenizing sentences and words.
  - Lemmatizing words to their base form and then removing stopwords.
  - Removing filler words.
Sentences are scored using **TF-IDF** (Term Frequency-Inverse Document Frequency) to determine the importance of each sentence.
Based on the scores, a summary of the top 50 sentences is created.
References:
   -Udemy Course:- Complete Data Science,Machine Learning,DL,NLP Bootcamp
   -https://thegrenze.com/pages/servej.php?fn=14_1.pdf&name=YouTube%20Video%20Transcript%20Summarizer%20using%20NLP&id=1795&association=GRENZE&journal=GIJET&year=2023&volume=9&issue=2
