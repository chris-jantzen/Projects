let Twit = require('twit');
let config = require('./config.js');

let T = new Twit(config);

let stream = T.stream('user');

stream.on('follow', followed);

function followed(eventMsg) {
  console.log("Followed!");
  let name = eventMsg.source.name;
  let screenName = eventMsg.source.screen_name;
  postTweet('@' + screenName + ' thanks for following, ' + name + "!");
}

function postTweet(txt) {
  let tweet = {
    status: txt
  };

  T.post('statuses/update', tweet, (err, data, response) => {
    if (err) {
      console.log("Error has occured");
    }
    else {
      console.log("Tweet Posted");
    }
  });
}
