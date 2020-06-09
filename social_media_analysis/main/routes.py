from flask import render_template, request, Blueprint, redirect, url_for
from social_media_analysis.twitter.forms import NameForm, BotForm,HashtagForm, TweetForm


main = Blueprint('main', __name__)


@main.route("/twitter", methods=['GET', 'POST'])
def twitter():
	#try:
		botform = BotForm()
		botmodal='close'
		if(botform.validate_on_submit()==False and botform.submit.data):
			botmodal='botdetectionmodel'
		if botform.validate_on_submit() and botform.submit.data:
			bot_account_name = botform.name.data
			return redirect(url_for('twitter.bot_account_detection', name=bot_account_name))

		hashtagform = HashtagForm()
		hashtagmodal='close'
		if(hashtagform.validate_on_submit()==False and hashtagform.hashtagsubmit.data):
			hashtagmodal='hashtagmodel'
		if hashtagform.validate_on_submit() and hashtagform.hashtagsubmit.data:
			hashtag = hashtagform.hashtag.data
			return redirect(url_for('twitter.hashtag_tweets', hashtag=hashtag))

		screennamemodal='close'
		screennameform = NameForm()
		if(screennameform.validate_on_submit()==False and screennameform.search.data):
			screennamemodal='searchforaccount'
		if screennameform.validate_on_submit() and screennameform.search.data:
			screen_name = screennameform.name.data
			return redirect(url_for('twitter.user_details', name=screen_name))
		predtweetmodal='close'
		tweetform = TweetForm()
		if(tweetform.validate_on_submit()==False and tweetform.likespredict.data):
			predtweetmodal='likespredmodal'
		if tweetform.validate_on_submit() and tweetform.likespredict.data:
			screen_name = tweetform.name.data
			tweet = tweetform.tweet.data
			#time = tweetform.time.data
			return redirect(url_for('twitter.user_tweets', name=screen_name, tweet=tweet))

		return render_template('twitter.html', title='Twitter', tweetform=tweetform, screennameform=screennameform, botform=botform, hashtagform=hashtagform, predtweetmodal=predtweetmodal, screennamemodal=screennamemodal, botmodal=botmodal, hashtagmodal=hashtagmodal)
	#except:
		#flash('Something went Wrong. Please check weather enterd details are correct', 'warning')
		#return redirect(url_for('main.home'))
@main.route("/", methods=['GET', 'POST'])
@main.route("/home", methods=['GET', 'POST'])
def home():
	#try:
		botform = BotForm()
		botmodal='close'
		if(botform.validate_on_submit()==False and botform.submit.data):
			botmodal='botdetectionmodel'
		if botform.validate_on_submit() and botform.submit.data:
			bot_account_name = botform.name.data
			return redirect(url_for('twitter.bot_account_detection', name=bot_account_name))

		hashtagform = HashtagForm()
		hashtagmodal='close'
		if(hashtagform.validate_on_submit()==False and hashtagform.hashtagsubmit.data):
			hashtagmodal='hashtagmodel'
		if hashtagform.validate_on_submit() and hashtagform.hashtagsubmit.data:
			hashtag = hashtagform.hashtag.data
			return redirect(url_for('twitter.hashtag_tweets', hashtag=hashtag))

		screennamemodal='close'
		screennameform = NameForm()
		if(screennameform.validate_on_submit()==False and screennameform.search.data):
			screennamemodal='searchforaccount'
		if screennameform.validate_on_submit() and screennameform.search.data:
			screen_name = screennameform.name.data
			return redirect(url_for('twitter.user_details', name=screen_name))
		predtweetmodal='close'
		tweetform = TweetForm()
		if(tweetform.validate_on_submit()==False and tweetform.likespredict.data):
			predtweetmodal='likespredmodal'
		if tweetform.validate_on_submit() and tweetform.likespredict.data:
			screen_name = tweetform.name.data
			tweet = tweetform.tweet.data
			#time = tweetform.time.data
			return redirect(url_for('twitter.user_tweets', name=screen_name, tweet=tweet))

		return render_template('twitter.html', title='Twitter', tweetform=tweetform, screennameform=screennameform, botform=botform, hashtagform=hashtagform, predtweetmodal=predtweetmodal, screennamemodal=screennamemodal, botmodal=botmodal, hashtagmodal=hashtagmodal)
	#except:
		#flash('Something went Wrong. Please check weather enterd details are correct', 'warning')
		#return redirect(url_for('main.home'))