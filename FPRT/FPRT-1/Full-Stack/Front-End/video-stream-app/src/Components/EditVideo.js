import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import actions from "../Actions";

function EditVideo() {
  const params = useParams();
  const myVideos = useSelector((state) => state.user.my_videos);
  let video = myVideos[params.id];
  const [caption, setCaption] = useState(video.caption);
  const [tags, setTags] = useState(video.hashtags.join(' '));
  const [message, setMessage] = useState("");

  const dispatch = useDispatch();

  const handleEdit = (e) => {
    e.preventDefault();
    dispatch(actions.editVideo(params.id, caption, tags));
    setMessage("Your Video has been Edited!");
  };

  return (
    <div className="form-parent">
      <form className="form" onSubmit={handleEdit}>
        <h2 className="form-heading">Edit Video</h2>

        <div>
          <label htmlFor="">Caption (Video Title)</label>
          <input
            className="form-input mt-1"
            type="text"
            name="caption"
            placeholder="my video title"
            autoComplete="off"
            onChange={(e) => setCaption(e.target.value)}
            value={caption}
            required
          />
        </div>

        <div>
          <label htmlFor="">HashTags (space seperated)</label>
          <input
            className="form-input mt-1"
            type="text"
            name="hashtags"
            placeholder="example1 example2"
            autoComplete="off"
            onChange={(e) => setTags(e.target.value)}
            value={tags}
          />
        </div>
        <div className="form-error-message form-small-text">{message}</div>
        <button className="form-submit-btn" type="submit">
          Edit
        </button>
      </form>
    </div>
  );
}

export default EditVideo;
