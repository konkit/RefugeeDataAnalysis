print("id,lat,lng")
db.refugee_tweets.find().forEach(function(tweet) {
  if( tweet.coordinates != null ) {
    var coordinates = tweet.coordinates.coordinates
    print(tweet._id.valueOf() + "," + tweet.created_at + "," + coordinates[0] + "," + coordinates[1] );
  }
});
