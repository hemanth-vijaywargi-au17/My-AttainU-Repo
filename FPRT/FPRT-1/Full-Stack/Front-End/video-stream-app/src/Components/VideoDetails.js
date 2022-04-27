import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate, useParams } from "react-router-dom";
import actions from "../Actions";

function VideoDetails() {
  const params = useParams();
  const allVideos = useSelector((state) => state.app.allVideos);
  const myVideos = useSelector((state) => state.user.my_videos);
  const {
    video_url,
    caption,
    uploadedBy,
    createdAt,
    hashtags,
    noOfLikes,
    _id,
  } = allVideos[params.id];

  const [controls, setControls] = useState(true);
  const dispatch = useDispatch();
  const navigate = useNavigate();

  function deleteVideo() {
    console.log("delete video called");
    dispatch(actions.deleteVideo(_id));
    navigate("/");
  }

  return (
    <div className="flex justify-center">
      <div className="w-1/2 m-6 " onClick={() => setControls(true)}>
        {/* Video */}
        <video
          src={video_url}
          preload="metadata"
          className="w-full"
          controls={controls}
        ></video>

        {/* Meta Data */}
        <div className=" flex justify-between items-center mt-4">
          <div className="flex">
            <div className="mr-5 ml-1">
              <img
                src={uploadedBy.profile_pic_url}
                style={{ objectFit: "cover" }}
                alt=""
                className="w-10 h-10 rounded-full"
              />
            </div>
            <div className="text-white space-y-1">
              <div className="text-xl font-semibold">{caption}</div>
              <div className="text-sm text-gray-300">{uploadedBy.username}</div>
              <div className="text-sm text-gray-300">
                {new Date(createdAt).toLocaleDateString()}
              </div>
            </div>
          </div>
          <div className="flex gap-2 justify-center items-center">
            <svg
              className="w-10 h-10 text-white hover:text-blue-500 cursor-pointer"
              fill="currentColor"
              viewBox="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path d="M2 10.5a1.5 1.5 0 113 0v6a1.5 1.5 0 01-3 0v-6zM6 10.333v5.43a2 2 0 001.106 1.79l.05.025A4 4 0 008.943 18h5.416a2 2 0 001.962-1.608l1.2-6A2 2 0 0015.56 8H12V4a2 2 0 00-2-2 1 1 0 00-1 1v.667a4 4 0 01-.8 2.4L6.8 7.933a4 4 0 00-.8 2.4z"></path>
            </svg>
            <div className="text-white text-lg">{noOfLikes}</div>
          </div>
          {_id in myVideos ? (
            <div className="flex gap-3 items-center">
              <svg
                onClick={() => {
                  navigate(`/editVideo/${_id}`);
                }}
                className="w-10 h-10 text-blue-700 hover:text-blue-500 cursor-pointer"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z"></path>
              </svg>
              <svg
                onClick={deleteVideo}
                className="w-10 h-10  text-red-700 hover:text-red-500 cursor-pointer"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  fillRule="evenodd"
                  d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z"
                  clipRule="evenodd"
                ></path>
              </svg>
            </div>
          ) : null}
        </div>
        
        <div className="text-white">
          <div className="text-lg">Tags</div>
          <div className="flex gap-2">
            {hashtags.map((tag) => {
              return <span key={tag}>{" #" + tag}</span>;
            })}
          </div>
        </div>
      </div>
    </div>
  );
}

export default VideoDetails;
