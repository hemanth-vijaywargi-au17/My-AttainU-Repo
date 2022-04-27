const { Router } = require("express");
const routes = Router();
const UserModel = require("../models/User");
const cloudinary = require("cloudinary").v2;
const streamifier = require("streamifier");

// Cloudinary Configuration
cloudinary.config({
  cloud_name: process.env.CLOUD_NAME,
  api_key: process.env.API_KEY,
  api_secret: process.env.API_SECRET,
});

routes.get("/", async (req, res) => {
  let allUsers = await UserModel.find();
  res.render("AllUsers", { allUsers });
});

routes.get("/upload", (req, res) => {
  res.render("Form");
});

routes.post("/upload", async (req, res) => {
  let cld_upload_stream = cloudinary.uploader.upload_stream(
    { folder: "User Pics" },
    async (error, result) => {
      if (error) {
        res.send("Error Happened!");
        return;
      }
      await UserModel.create({
        name: req.body.userName,
        imageURL: result.secure_url,
      });
      res.send("User Added!");
    }
  );

  streamifier
    .createReadStream(req.files.userImage.data)
    .pipe(cld_upload_stream);
});

module.exports = routes;
