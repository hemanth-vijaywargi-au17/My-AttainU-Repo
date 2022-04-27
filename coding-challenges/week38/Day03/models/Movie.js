const { Schema, model } = require("mongoose");
const fs = require('fs')

const MovieSchema = new Schema({
  title: Schema.Types.String,
  year: Schema.Types.Number,
  runtime: Schema.Types.Number,
  released: Schema.Types.Date,
  poster: Schema.Types.String,
  plot: Schema.Types.String,
  fullplot: Schema.Types.String,
  lastupdated: Schema.Types.String,
  type: Schema.Types.String,
  directors: [Schema.Types.String],
  imdb: {
    rating: Schema.Types.Number,
    votes: Schema.Types.Number,
    id: Schema.Types.Number,
  },
  cast: [Schema.Types.String],
  countries: [Schema.Types.String],
  genres: [Schema.Types.String],
  tomatoes: {
    viewer: {
      rating: Schema.Types.Number,
      numReviews: Schema.Types.Number,
    },
    lastUpdated: Schema.Types.Date,
  },
  num_mflix_comments: Schema.Types.Number,
});

MovieSchema.pre("aggregate", function () {
  this._startTime = Date.now(); // Get Time in MilliSeconds
});

MovieSchema.post("aggregate", function () {
    let file = 'queryTime.txt'
    let data = `Query : ${JSON.stringify(this._pipeline)}, Time taken: ${Date.now() - this._startTime} ms\n`
    let options = {flag: 'a'}
    let callback = ()=>{console.log(data)}
    fs.writeFile( file, data, options, callback )
});

const MovieModel = model("movie", MovieSchema);

module.exports = { MovieModel };
