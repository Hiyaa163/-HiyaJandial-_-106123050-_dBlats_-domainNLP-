import nltk
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
video_id = input("Enter the YouTube video ID: ").strip()
x= YouTubeTranscriptApi.get_transcript(video_id)
transcript=TextFormatter().format_transcript(x)
transcript = transcript.replace('\n', '. ')  
transcript = transcript.strip()

sentences=sent_tokenize(transcript)
i=0
for i in range(len(sentences[i])):
    words=word_tokenize(sentences[i])
    words=[WordNetLemmatizer().lemmatize(word.lower(),pos='v') for word in words if word not in set(stopwords.words('english'))]
    sentences[i]=' '.join(words)   
filler_words=["uh","um","like","well","ah","actually","you see","you know","subscribe","click the link","thanks for watching","so"]
j=0
for i in range(len(sentences[j])):
    words=word_tokenize(sentences[j])
    words=[word.lower() for word in words if word.lower() not in filler_words]
    sentences[j]=' '.join(words)

tfidf=TfidfVectorizer(max_features=100)
y=tfidf.fit_transform(sentences).toarray()
sent_score=y.sum(axis=1)
scored_sentences = [(sentences[i], sent_score[i]) for i in range(len(sentences))]
sorted_sentences = sorted(scored_sentences, key=lambda x: x[1], reverse=True)
summary = "\n".join([sentence for sentence , score in sorted_sentences[:50]])
print("Summary:")
print(summary)