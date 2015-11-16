var locationsHash = {};

db.refugee_tweets.find().forEach(function(tweet) {

    if( typeof( tweet.user ) !== 'undefined' && tweet.user.location != null ) {
        var locationVal = tweet.user.location.replace(new RegExp(',', 'g'), '.');

        if( typeof( locationsHash[locationVal] ) == 'undefined' ) {
            locationsHash[locationVal] = 0;
        }
        locationsHash[locationVal]++;
    }

});

print("Total: " + Object.keys(locationsHash).length);

for (var i = 0, keys = Object.keys(locationsHash), ii = keys.length; i < ii; i++) {
      print(keys[i] + ',' + locationsHash[keys[i]]);
}
