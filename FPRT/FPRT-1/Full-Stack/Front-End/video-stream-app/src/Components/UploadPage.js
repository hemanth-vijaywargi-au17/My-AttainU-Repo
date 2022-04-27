import axios from "axios";
import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import getVideoDuration from "../utils/getVideoDuration";
import actions from "../Actions";

function UploadPage() {
  const [caption, setCaption] = useState("");
  const [tags, setTags] = useState("");
  const [video, setVideo] = useState(null);
  const [progress, setProgress] = useState(null);
  const [error, setError] = useState("");

  const dispatch = useDispatch();
  const token = useSelector((state) => state.user.token);

  const handleUpload = async (e) => {
    e.preventDefault();

    // Check Video Size (100 MB limit)
    if (video.size > 104857600) {
      setError("Video cannot be greater than 100 MB in Size");
      return;
    }

    // Calculate Video Duration
    // let videoDuration = await getVideoDuration(video);

    // Check Video Dration
    // if(videoDuration>10){
    //     setError("Video cannot be more than 10 seconds Long")
    //     return
    // }

    const url = `/api/upload`;
    const formData = new FormData();
    formData.append("caption", caption);
    formData.append("hashtags", tags);
    formData.append("video", video);
    const options = {
      headers: {
        "content-type": "multipart/form-data",
        token: token,
      },
      onUploadProgress: (data) => {
        //Set the progress value to show the progress bar
        setProgress(Math.round((100 * data.loaded) / data.total));
      },
    };
    await axios.post(url, formData, options);
    dispatch(actions.getAllVideos());
    dispatch(actions.getMyVideos());
  };

  return (
    <div className="form-parent">
      <form className="form" onSubmit={handleUpload}>
        <h2 className="form-heading">Upload</h2>

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

        <div>
          <label htmlFor="">Your Video</label>
          <input
            className="mt-1"
            type="file"
            name="hashtags"
            placeholder="example1 example2"
            autoComplete="off"
            onChange={(e) => {
              setVideo(e.target.files[0]);
            }}
            onClick={() => {
              setError("");
              setProgress(null);
            }}
            required
            accept=".mp4" // Only Allow .mp4 video format
          />
        </div>
        <div className="form-error-message form-small-text">
          {error || progress
            ? progress === 100
              ? "Upload Complete"
              : `Upload Progress... ${progress}`
            : null}
        </div>
        <button className="form-submit-btn" type="submit">
          Upload
        </button>
      </form>
    </div>
  );
}

export default UploadPage;
