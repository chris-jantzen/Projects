
const Twit = require('twit');
const config = require('./config.js');

let Twitter = new Twit(config);

let stream = Twitter.stream('statuses.filter', { track: ['@APICincy']});
stream.on('tweet', (tweet) => {
    console.log(tweet);
});
