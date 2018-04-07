//TODO: make it not post 20 times, setup EC2 instance with this to host the service permanently.

const Twit = require('twit');
const config = require('./config.js');
const subs = require('./substitutions.js');

let Twitter = new Twit(config);

let stream = Twitter.stream('user');
stream.on('tweet', (eventMsg) => {
  let tweet = eventMsg.text;
  console.log(eventMsg.user.screen_name + "\n" + tweet + "\n");
  let newTweet = textSubstitution(tweet)
  if (newTweet !== tweet && newTweet.length <= 280) {
    console.log(newTweet.status);
    Twitter.post('statuses/update', { status: newTweet }, (err, data, response) => {
      if (err) {
        console.log(err);
        return;
      }
      console.log('Tweet posted!');
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
