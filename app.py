import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
import base64

st.set_page_config(
    page_title="SPAM message checker",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.markdown('__About this project__')
st.sidebar.info("SPAM Message Classifier can be used by the users to check the message they received is whether a SPAM message or normal message.")

st.sidebar.markdown('__What is a SPAM message?__')
st.sidebar.info("SPAM is not only annoying but also dangerous to users. Spam messages can be defined as any message that was not requested by a user but was sent to that user and many others, typically with malicious intent.The message includes promotional, personal, or fake messages that may trick you into giving out information and also fraudulent messages for hacking accounts.There is a very high chance for the users to undergo financial loss due to these SPAM messages.")




ps = PorterStemmer()



def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("SPAM Message Classifier")

input_sms = st.text_area("Enter the message",value='', height=350)

if st.button('Predict'):

    # 1. preprocess
    transformed_sms = transform_text(input_sms)
    # 2. vectorize
    vector_input = tfidf.transform([transformed_sms])
    # 3. predict
    result = model.predict(vector_input)[0]
    # 4. Display
    if result == 1:
        st.info("Spam")
    else:
        st.info("Not Spam")





