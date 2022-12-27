# SPAM-message-Classifier
`M.Sc. Sem 4 project`

“SPAM Message Classifier” can be used by the users to check if the message they received is a SPAM message or a normal message.

# Dataset
The datasets are the collection of data. 
The dataset which is used in this project was downloaded from the UCI repository. 
This dataset contained 5572 rows with five columns which was imported into the system for the pre-processing, extracting features, and classification.

# Data Cleaning
After getting the data the next step is to pre-process it. All the unwanted columns were removed. The columns were renamed in a more understandable way. All the duplicate values and all the null value items were removed. We renamed ham and spam as 0 and 1.  Data was transformed to lower case. Data was tokenized and all special characters were removed along with stopwords and punctuations.


# EDA
Here we tried to understand the data. We analyzed data using various plots and charts. We compared data by creating new columns for number of characters, number of sentences and number of words.
From the analysis we came to know that SPAM messages have higher tendency to be longer and also found about the most common and highly used words in SPAM messages  and normal messages.

# Model building
![imageedit_2_3652100704](https://user-images.githubusercontent.com/32393519/209702339-91556cd1-1829-4ae5-9d88-8a6f56962c2d.png)

We tested the data with various algorithms and after testing with various algorithms we came into the conclusion that the Naïve bayes algorithm is the most suited for this project because it obtained the highest accuracy and precession in the test.

# Streamlit
Streamlit is an open-source app framework for Machine Learning and Data Science teams.
Streamlit turns data scripts into shareable web apps in minutes. All in pure Python. No front‑end experience required.

We used Streamlit framework to create the GUI of this project.
`StreamLit` 

# Requirement
`streamlit`
`nltk`
`sklearn`

# Run the command
```streamlit run app.py ```

# Screenshots
![image](https://user-images.githubusercontent.com/32393519/209701908-76c8427e-8aef-467e-8e0a-1d5bf9ac5248.png)
![image](https://user-images.githubusercontent.com/32393519/209701924-bc6a1a7a-e7b1-4ccc-8bed-d7d21e382202.png)
![image](https://user-images.githubusercontent.com/32393519/209701930-9b35d414-4c88-4d36-8938-133f2ab43143.png)
