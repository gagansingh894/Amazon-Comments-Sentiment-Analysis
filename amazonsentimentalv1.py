import requests
from bs4 import BeautifulSoup
import pandas as pd 
from textblob import TextBlob 

startURL = r'https://www.amazon.com/PlayStation-Slim-1TB-Console-Bundle-4/product-reviews/B07YLDNTKB/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'

def getComments(startURL):
	sauce = requests.get(startURL)
	soup = BeautifulSoup(sauce.text, 'lxml')
	reviewList = soup.find_all('span', attrs = {'class': 'a-size-base review-text review-text-content'})
	rList = []
	polarityList = []
	subjectList = []

	for review in reviewList:
		rList.append(review.text)
		polarityList.append(TextBlob(review.text).sentiment.polarity)
		subjectList.append(TextBlob(review.text).sentiment.subjectivity)
	amazon_df = pd.DataFrame({'Review': rList, 'Polarity': polarityList, 'Subjectivity': subjectList})
	return amazon_df
	amazon_df.to_excel('data.xlsx')





# startURL = r'https://www.amazon.in/All-new-Echo-Plus-2nd-built/product-reviews/B0794JD9JS/ref=dpx_acr_txt?showViewpoints=1'
#print(soup.prettify())
#usernameList = soup.find_all('span', attrs = {'class': 'a-profile-name'})
#reviewheadingList = soup.find_all('span', attrs = {'class': 'a-size-base review-title a-text-bold'})
#uList = []
#rhList = []
