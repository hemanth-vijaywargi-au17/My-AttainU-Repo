const { Schema, model } = require("mongoose");
const { hash } = require("bcrypt");

const UserSchema = new Schema({
  name: {
    type: String,
    required: true,
  },
  email: {
    type: String,
    required: true,
  },
  password: {
    type: String,
    required: true,
  },
  profile_pic_url: {
    type: String,
  },
  uploaded_videos: {
    type: [Schema.Types.ObjectId],
    ref: 'video'
  },
});

// Hashing Password before saving to DB (Mongoose MiddleWare)
UserSchema.pre("save", async function (next) { 
  let hashedPassword = await hash(this.password, 10);
  this.password = hashedPassword;
  next();
});

const UserModel = model("user", UserSchema);

module.exports = UserModel;
