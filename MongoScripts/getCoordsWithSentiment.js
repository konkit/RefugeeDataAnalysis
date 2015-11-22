db.refugee_tweets.find().forEach(function(tweet) {
  if( tweet.coordinates != null ) {
    var coordinates = tweet.coordinates.coordinates

    var sentiment_num = 0;
    if( tweet.sentiment === 'positive') {
      sentiment_num = 1;
    } else if( tweet.sentiment === 'negative' ) {
      sentiment_num = -1;
    }

    print(tweet._id.valueOf() + "    " + (new Date(tweet.created_at)).getTime() + "    " + coordinates[0] + "    " + coordinates[1] + "    " + sentiment_num );
  }
});
