print("id,retweets")
db.refugee_tweets.find().forEach(function(tweet) {
    print(tweet._id.valueOf() + "," + tweet.retweet_count);
});
