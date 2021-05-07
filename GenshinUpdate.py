#This program is used to see what words are mentioned within Genshin Impact's 1.4 update.
from wordcloud import WordCloud, STOPWORDS
from PIL import Image

#import numpy
import numpy as npy

#Create the dataset for the wordcloud, set encoding to utf8 so no errors occur.
dataset = open("genshinUpdate.txt", "r" , encoding="utf8").read()

def create_word_cloud (string):
   maskArray = npy.array(Image.open("cloudimage.png"))
   cloud = WordCloud(background_color = "white", max_words = 200, mask = maskArray, stopwords = set(STOPWORDS))
   cloud.generate(string)
   cloud.to_file("wordCloud.png")
dataset = dataset.lower()
create_word_cloud(dataset)