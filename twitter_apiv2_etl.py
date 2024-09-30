import tweepy
import datetime as dt
import s3fs
import json
import zipfile
import pandas as pd

"""
Twitter is not providing tweets data through free API anymore. Hence I got to use Kaggle data from here. 
https://www.kaggle.com/datasets/mmmarchetti/tweets-dataset"""


def extract_tweets():
    #Extract
    df_zip = zipfile.ZipFile('tweets dataset.zip')
    df = pd.read_csv(df_zip.open('tweets.csv'))

    # # Print number of rows with no country details.
    # print(df['country'].isnull().sum())
    # # print the rows with country data.
    # print(df['country'].notna().sum())
    # # print(df['country'].notnull()) #This will print True and False for each row.
    # country_df = df[df['country'].notna()]
    # print(country_df)

    #Transform
    #Remove the tweets with less than 5K likes OR  tweets with less than 2K shares.
    df = df[ (df['number_of_likes'] < 5000) | (df['number_of_shares'] < 2000) ]

    #Load
    df.to_csv("/Processed_Output_Data/cleaned_tweets_data.csv")

    # Save the data to s3 bucket after processing.
    # df.to_csv("s3://")

    # consumer_key="VapojCQtfGdfdggwKioZDkThisIsDummyWTrkjesdz"
    # consumer_secret="TyftltWNUydggfDC2wBSveThisIsDummyI2VW15JabAYJnvFEAxWdyCA1MQlsLabn"
    #
    # access_token = "767385476ThisIsDummy8sfgh31469568-i35qKuZhghghSIDV1AmUCfxzSxgzBZnGoUeQ"
    # access_token_secret = "WXYuSXtxxlmmi04mu24ghghgh6yhThisIsDummy6y69Gq6niyLpbfsycVUH8ex"
    #
    # bearer_token = "AAAAAAAAAAAAAAAAAAAAAETdvwEAAAAThisIsDummyAK0GWJ7lz0HxaghghftezdlVCDgBPRDSS0TY%3D4Ln2mD4WqBEhW8XHz9xNk5gC5yvty5qVCNmvfeMwsrsPQnkRh3"
    #
    # client = tweepy.Client(bearer_token=bearer_token,
    #               consumer_key=consumer_key,
    #               consumer_secret=consumer_secret,
    #               access_token=access_token,
    #               access_token_secret=access_token_secret,
    #               return_type=dict,
    #               wait_on_rate_limit=False)
    #
    # query = "covid -is:retweet"
    # tweets = client.search_recent_tweets(query=query)
    #
    # print(tweets)

