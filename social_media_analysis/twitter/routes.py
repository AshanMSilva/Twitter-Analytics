from flask import render_template, url_for, flash, redirect, request, Blueprint
from social_media_analysis.twitter.codes.sentiment_analysis_twitter_data import TwitterClient, TweetAnalyzer
from social_media_analysis.twitter.codes.Bot_account_detection.bot_account_prediction_methods import Prediction
import numpy as np
import pickle
from social_media_analysis.twitter.codes.Tweet_Likes_Prediction.tweet_likes_prediction import TweetLikesPrediction
from social_media_analysis.twitter.codes.Hashtags_Analyze.hashtag_analyze import HashtagAnalyzer
from collections import Counter

twitter = Blueprint('twitter', __name__)


@twitter.route("/twitter/<string:name>")
def user_details(name):
    try:
        twitter_client = TwitterClient()
        tweet_analyzer = TweetAnalyzer()
        user = twitter_client.get_user(name)
        tweets = twitter_client.get_tweets_of_a_user(name, 100)
        replies = 0
        mentions =0
        hashtags =0
        retweets=0
        links =0
        medias=0
        zero=0
        one =0
        two=0
        three=0
        four=0
        five=0
        six=0
        seven=0
        eight=0
        nine=0
        ten=0
        eleven=0
        twelve=0
        thirteen=0
        fourteen=0
        fifteen=0
        sixteen=0
        seventeen=0
        eighteen=0
        nineteen=0
        twenty=0
        twentyone=0
        twentytwo=0
        twentythree=0
        ids=[]
        favourites=[]
        retweetscount=[]
        for tweet in tweets:
            if(len(tweet.entities['hashtags'])>0):
                hashtags+=1
            if(len(tweet.entities['user_mentions'])>0):
                mentions+=1
            if(len(tweet.entities['urls'])>0):
                links+=1
            if('media' in tweet.entities):
                if(len(tweet.entities['media'])>0):
                    medias+=1
            if(hasattr(tweet, 'retweeted_status')):
                retweets+=1
            if(tweet.in_reply_to_status_id !=None):
                replies+=1
            if(tweet.created_at.hour == 0):
                zero+=1
            if(tweet.created_at.hour == 1):
                one+=1
            if(tweet.created_at.hour == 2):
                two+=1
            if(tweet.created_at.hour == 3):
                three+=1
            if(tweet.created_at.hour == 4):
                four+=1
            if(tweet.created_at.hour == 5):
                five+=1
            if(tweet.created_at.hour == 6):
                six+=1
            if(tweet.created_at.hour == 7):
                seven+=1
            if(tweet.created_at.hour == 8):
                eight+=1
            if(tweet.created_at.hour == 9):
                nine+=1
            if(tweet.created_at.hour == 10):
                ten+=1
            if(tweet.created_at.hour == 11):
                eleven+=1
            if(tweet.created_at.hour == 12):
                twelve+=1
            if(tweet.created_at.hour == 13):
                thirteen+=1
            if(tweet.created_at.hour == 14):
                fourteen+=1
            if(tweet.created_at.hour == 15):
                fifteen+=1
            if(tweet.created_at.hour == 16):
                sixteen+=1
            if(tweet.created_at.hour == 17):
                seventeen+=1
            if(tweet.created_at.hour == 18):
                eighteen+=1
            if(tweet.created_at.hour == 19):
                nineteen+=1
            if(tweet.created_at.hour == 20):
                twenty+=1
            if(tweet.created_at.hour == 21):
                twentyone+=1
            if(tweet.created_at.hour == 22):
                twentytwo+=1
            if(tweet.created_at.hour == 23):
                twentythree+=1
            ids.append(tweet.id)
            favourites.append(tweet.favorite_count)
            retweetscount.append(tweet.retweet_count)
        tweetsdata ={
            "hashtags": hashtags,
            "mentions": mentions,
            "links": links,
            "medias":medias,
            "retweets":retweets,
            "replies":replies
        }
        graphdata ={
            "0":zero,
            "1":one,
            "2":two,
            "3":three,
            "4":four,
            "5":five,
            "6":six,
            "7":seven,
            "8":eight,
            "9":nine,
            "10":ten,
            "11":eleven,
            "12":twelve,
            "13":thirteen,
            "14":fourteen,
            "15":fifteen,
            "16":sixteen,
            "17":seventeen,
            "18":eighteen,
            "19":nineteen,
            "20":twenty,
            "21":twentyone,
            "22":twentytwo,
            "23":twentythree   
        }
        verified='NOTVERIFIED'
        badge='badge-danger'
        if(user.verified):
            verified='VERIFIED'
            badge='badge-success'
        
        return render_template('user_details.html', user=user, tweetsdata=tweetsdata, verified=verified, badge=badge, graphdata=graphdata, ids=ids, favourites=favourites, retweetscount=retweetscount)
    except:
        flash('Something went Wrong. Please check whether enterd details are correct','warning')
        return redirect(url_for('main.twitter'))


@twitter.route("/twitter/hashtag/<string:hashtag>")
def hashtag_tweets(hashtag):
    hasht = '#'+hashtag
    twitter_client = TwitterClient()
    tweets = twitter_client.get_hashtag_tweets(hasht, 'mixed', 100)
    count = len(tweets)
    hashtag_analyzer = HashtagAnalyzer()
    hourdata = hashtag_analyzer.divide_tweets_according_to_hours(tweets)
    monthdata = hashtag_analyzer.divide_tweets_according_to_months(tweets)
    sentimentdata = hashtag_analyzer.divide_tweets_according_to_sentiment(tweets)
    user_mentions = hashtag_analyzer.get_user_mentions(tweets)
    hashtagslist = hashtag_analyzer.get_user_hashtags(tweets)
    userslist = hashtag_analyzer.get_users(tweets)
    mentionslength = len(user_mentions)
    hashtagslength = len(hashtagslist)
    userslength = len(userslist)
    while True:
        if(len(userslist)<15):
            userslist.append(['',0])
        if(len(userslist)>=15):
            break
    while True:
        if(len(hashtagslist)<15):
            hashtagslist.append(['',0])
        if(len(hashtagslist)>=15):
            break
    while True:
        if(len(user_mentions)<15):
            user_mentions.append(['',0])
        if(len(user_mentions)>=15):
            break
    return render_template('hashtag.html',hashtag=hashtag, count=count, mentionslength=mentionslength, userslength=userslength, hashtagslength=hashtagslength, hourdata=hourdata, monthdata=monthdata, sentimentdata=sentimentdata, user_mentions=user_mentions, hashtagslist=hashtagslist, userslist=userslist)

@twitter.route("/twitter/botaccount/<string:name>")
def bot_account_detection(name):
    try:
        twitter_client = TwitterClient()
        user = twitter_client.get_user(name)
        prediction = Prediction()
        created_at = user.created_at
        year = created_at.year
        month = created_at.month
        day = created_at.day
        duration = prediction.get_time_period(year,month,day)
        id = user.id
        description = prediction.sentiment_description(user.description)
        followers_count = user.followers_count
        friends_count = user.friends_count
        listed_count = user.listed_count
        favourites_count = user.favourites_count
        verified = prediction.encode_verified(user.verified)
        statuses_count = user.statuses_count
        default_profile = prediction.encode_default_profile(user.default_profile)
        default_profile_image = prediction.encode_default_profile_image(user.default_profile_image)
        has_extended_profile = prediction.encode_has_extended_profile(user.has_extended_profile)
        pred_list = [description, followers_count, friends_count, listed_count, favourites_count, verified, statuses_count, default_profile, default_profile_image, has_extended_profile, year, month, day, duration]
        pred_list = np.array(pred_list)
        #import model and predict
        pred_result = prediction.predict([pred_list])
        verified='NOTVERIFIED'
        badge='badge-danger'
        if(user.verified):
            verified='VERIFIED'
            badge='badge-success'
        
        return render_template('bot_detection.html', user=user, pred_result = pred_result, verified=verified, badge=badge)
    except:
        flash('Something went Wrong. Please check whether enterd details are correct','warning')
        return redirect(url_for('main.twitter'))
@twitter.route("/twitter/likesprediction/<string:name>")
def user_tweets(name):
    try:
        pred_text = request.args.get('tweet')
        #time = request.args.get('time')
        #hour = int(time[0:2])
        #minute = int(time[3:5])
        if(pred_text==None):
            flash('prdiction tweet text cannot be null','warning')
            return redirect(url_for('main.twitter'))
        twitter_client = TwitterClient()
        user = twitter_client.get_user(name)
        tweet_analyzer = TweetAnalyzer()
        tweets = twitter_client.get_tweets_of_a_user(name, 1000)
        tweets_likes_prediction =TweetLikesPrediction()
        texts=[]
        likes=[]
        retweetscount=[]
        hours =[]
        minutes =[]
        for tweet in tweets:
            minutes.append(tweet.created_at.minute)
            hours.append(tweet.created_at.hour)
            #print(minutes)
            if(hasattr(tweet, 'retweeted_status')):
                texts.append(tweet.retweeted_status.full_text)
            else:
                texts.append(tweet.full_text)
            likes.append(tweet.favorite_count)
            retweetscount.append(tweet.retweet_count)
        #texts = np.array(texts)
        tokenizer = tweets_likes_prediction.set_tokenizer(texts)
        sequences = tweets_likes_prediction.texts_to_sequences(texts, tokenizer)
        padded_sequences = tweets_likes_prediction.get_padded_sequeces(sequences)
        # features=[]
        # for i in range(0,len(likes)):
        #     feature = np.append(padded_sequences[i],likes[i])
        #     features.append(feature)
        # features = np.array(features)
        nplikes = np.array(likes)
        #nphours = np.array(hours)
        #npminutes = np.array(minutes)
        npretweetscount = np.array(retweetscount)
        # features =[]
        # for i in range(0, len(hours)):
        #     l = np.append(padded_sequences[i], hours[i])
        #     l2 = np.append(l, minutes[i])
        #     features.append(l2)
        # npfeatures = np.array(features)
        #print(npfeatures[0])
        #print(padded_sequences[0])
        retweetmodel = tweets_likes_prediction.train_model(padded_sequences, npretweetscount)
        model = tweets_likes_prediction.train_model( padded_sequences, nplikes)
        tweetcount=[]
        for i in range(0, len(likes)):
            tweetcount.append(i)
        pred_text =[pred_text]
        pred_sequence = tweets_likes_prediction.texts_to_sequences(pred_text, tokenizer)
        maxlength = padded_sequences[0].size
        pred_padded_sequence = tweets_likes_prediction.get_padded_sequeces_with_maxlength(pred_sequence, maxlength)
        #result = pred_padded_sequence
        #pred_padded_sequence_with_hour = np.append(pred_padded_sequence[0],hour)
        #pred_padded_sequence_with_minute = np.append(pred_padded_sequence_with_hour,minute)
        #pred_padded_sequence_with_time = np.array([pred_padded_sequence_with_minute])
        result = model.predict(pred_padded_sequence)
        retweet_result= retweetmodel.predict(pred_padded_sequence)
        intResult = abs(int(result))
        intRetweetResult =abs(int(retweet_result))
        return render_template('user_tweets.html',result=intResult, retweet_result=intRetweetResult, retweetscount=retweetscount, likes=likes, tweetcount=tweetcount, user=user, pred_text=pred_text)
    except:
        flash('Something went Wrong. Please check whether enterd details are correct','warning')
        return redirect(url_for('main.twitter'))
