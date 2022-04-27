const { Router } = require("express");
const jwt = require("jsonwebtoken");
const UserModel = require("../models/User");
const { compare } = require("bcrypt");
const VideoModel = require("../models/Video");

const UserRoutes = Router();

// Authentication MiddleWare
function Authenticate(req, res, next) {
  try {
    let token = req.header("token");
    let secret = process.env.SECRET;
    let decodedData = jwt.verify(token, secret);
    req.email = decodedData.currentUser;
    next();
  } catch (err) {
    res.json({
      error: true,
      errorObj: err,
    });
  }
}

UserRoutes.post("/signup", async (req, res) => {
  try {
    let data = req.body;

    // Checking if user already exists
    let response = await UserModel.find({ email: data.email });

    if (response.length != 0) {
      res.json({
        error: true,
        message: "User Already Exists",
      });
      return;
    }

    if (req.files) {
      // File Data (any type of file)
      const fileData = req.files.userImage; // userImage is the "name" of our file input field.

      // Making a unique Filename using md5 and actual name of the file when uploaded.
      const fileName = `${fileData.md5}-${fileData.name}`;

      // Path where the file is to be stored on the server.
      const filePath = `${__dirname}/../public/userImages/${fileName}`;

      // Saving the path/url of our file in text data
      data.profile_pic_url = `/userImages/${fileName}`;

      // Moving the uploded file to the specified filePath
      fileData.mv(filePath);
    } else {
      data.profile_pic_url = `/userImages/default.png`;
    }
    data.uploaded_videos = [];

    // Inserting the Textual data in our mongodb Model
    const insertedData = await UserModel.create(data);

    // Sending Textual data as a response to successful submission of data
    res.status(201).send(insertedData);
  } catch (err) {
    res.json({
      error: true,
      errorObj: err,
    });
  }
});

UserRoutes.post("/login", async (req, res) => {
  try {
    let data = req.body;

    // Check if data is empty
    if (!data.email || !data.password) {
      res.json({
        error: true,
        message: "Empty data",
      });
      return;
    }

    // Check if User Exists
    let db_response = await UserModel.find({ email: data.email });
    if (db_response.length == 0) {
      res.json({
        error: true,
        message: "User Does Not Exist, Please signup First!",
      });
      return;
    }

    // Check if Password is Correct
    let passwordIsCorrect = await compare(
      data.password,
      db_response[0].password
    );

    if (passwordIsCorrect) {
      // Generate a token
      const secret = process.env.SECRET;
      const jwtToken = jwt.sign({ currentUser: data.email }, secret, {
        expiresIn: "10d",
      });
      
      res.json({
        error: false,
        message: "User Logged in Successfully!",
        token: jwtToken,
        name: db_response[0].name,
        profile_pic_url: db_response[0].profile_pic_url,
      });
      return;
    }

    res.json({
      error: true,
      message: "Incorrect Password!",
    });
  } catch (err) {
    res.json({
      error: true,
      errorObj: err,
    });
  }
});

UserRoutes.get("/getUserVideos", Authenticate, async (req, res) => {
  let db_response = await UserModel.find({ email: req.email }).populate(
    "uploaded_videos"
  );
  res.json(db_response[0].uploaded_videos);
});

UserRoutes.post("/upload", Authenticate, async (req, res) => {
  let data = req.body;
  let fileData = req.files.video;

  // Making a unique Filename using md5 and actual name of the file when uploaded.
  const fileName = `${fileData.md5}-${fileData.name}`;

  // Path where the file is to be stored on the server.
  const filePath = `${__dirname}/../public/userVideos/${fileName}`;

  // Saving the path/url of our file in text data
  data.video_url = `/userVideos/${fileName}`;

  // Moving the uploded file to the specified filePath
  fileData.mv(filePath);

  data.noOfLikes = 0;
  data.createdAt = new Date();
  data.hashtags = data.hashtags.split(" ");
  let user = await UserModel.find({ email: req.email });
  data.uploadedBy = {
    username: user[0].name,
    profile_pic_url: user[0].profile_pic_url,
  };

  let response = await VideoModel.create(data);

  let db_response = await UserModel.updateOne(
    { email: req.email },
    { $addToSet: { uploaded_videos: [response._id] } }
  );
  res.json(db_response);
});

UserRoutes.get("/allVideos", async (req, res) => {
  let response = await VideoModel.find({}).populate("uploadedBy");
  res.json(response);
});

UserRoutes.post("/deleteVideo", Authenticate, async (req, res) => {
  let videoId = req.body.videoId;
  let user = await UserModel.find({ email: req.email });
  let userId = user[0]._id;
  await VideoModel.deleteOne({ _id: videoId });
  await UserModel.updateOne(
    { _id: userId },
    { $pull: { uploaded_videos: videoId } }
  );
  res.json("Deleted!");
});

UserRoutes.post("/editVideo", Authenticate, async (req, res) => {
  let videoId = req.body.videoId;
  await VideoModel.updateOne(
    { _id: videoId },
    { caption: req.body.caption, hashtags: req.body.hashtags.split(" ") }
  );
  res.json("Updated!");
});

module.exports = { UserRoutes };
