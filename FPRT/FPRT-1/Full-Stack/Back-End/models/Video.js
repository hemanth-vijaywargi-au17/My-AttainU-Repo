const { Schema, model } = require("mongoose");

const VideoSchema = new Schema({
  caption: {
    type: String,
    required: true,
  },
  hashtags: {
    type: [String],
    required: true,
  },
  video_url: {
    type: String,
    required: true,
  },
  noOfLikes: {
    type: Number,
  },
  createdAt: {
    type: String,
    required: true,
  },
  uploadedBy: {
    type: Object,
  },
});

const VideoModel = model("video", VideoSchema);

module.exports = VideoModel;
