//TODO: post new tweet, setup EC2 instance with this to host the service permanently.

const Twit = require('twit');
const config = require('./config.js');
const subs = require('./substitutions.js');

let Twitter = new Twit(config);

let stream = Twitter.stream('user');
stream.on('tweet', (eventMsg) => {
  // console.log(eventMsg);
  let tweet = eventMsg.text;
  console.log(eventMsg.user.screen_name + "\n" + tweet + "\n");
  let newTweet = {
    status: textSubstitution(tweet)
  };
  if (newTweet.status !== tweet && newTweet.status.length <= 280) {
    console.log(newTweet.status);
    Twitter.post('status/update', newTweet, (err, data, response) => {
      if (err) {
        console.log(err);
      }
      else {
        console.log('Tweet posted!');
      }
    });
  }
});

function textSubstitution (tweet) {
  for (let i in subs) {
    if (tweet.toLowerCase().includes(i.toLowerCase())) {
      tweet = tweet.substr(0, tweet.indexOf(i)) + subs[i] + tweet.substr(tweet.indexOf(i) + i.length, tweet.length);
    }
  }
  return tweet;
}
