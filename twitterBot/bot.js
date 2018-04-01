const Twit = require('twit');
const config = require('./config.js');
const subs = require('./substitutions.js');

let Twitter = new Twit(config);

let params = {screen_name: 'CNN'};
let userDetails = {
  description: '',
  screen_name: '',
  id: 0,
  count: 1,
  exclude_replies: true,
  include_rts: false
};

Twitter.get('users/lookup', params, (error, users, response) => {
  if(error) throw error;

  userDetails.description = users[0].name;
  userDetails.screen_name = users[0].screen_name;
  userDetails.id = users[0].id;

  Twitter.get('statuses/user_timeline', userDetails, (error, tweets, response) => {
    if(!error) {
      console.log(tweets);
    }
    else {
      console.log('error');
    }
  });
});

//TODO: Figure out stream, make modifications to text if possible and post new tweet, setup EC2 instance with this to host the service permanently.






// stream.on('tweet', (tweet) => {
//   console.log(tweet);
// });
//
// let stream = Twitter.stream('statuses/sample');




// function followed(eventMsg) {
//   console.log("Followed!");
//   let name = eventMsg.source.name;
//   let screenName = eventMsg.source.screen_name;
//   postTweet('@' + screenName + ' thanks for following, ' + name + "!");
// }
//
// function postTweet(txt) {
//   let tweet = {
//     status: txt
//   };
//
//   T.post('statuses/update', tweet, (err, data, response) => {
//     if (err) {
//       console.log("Error has occured");
//     }
//     else {
//       console.log("Tweet Posted");
//     }
//   });
// }
