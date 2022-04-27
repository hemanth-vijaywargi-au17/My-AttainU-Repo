import { useNavigate } from "react-router-dom";

function VideoCard(props) {
  const { video_url, caption, uploadedBy, createdAt, _id, inMyVideos } = props;
  const navigate = useNavigate();
  return (
    <div
      onClick={() => {
        navigate(`/video/${_id}`);
      }}
      className="w-80 cursor-pointer"
    >
      <video src={video_url} preload="metadata" className="w-full h-44"></video>
      <div className="h-20 flex mt-4">
        <div className="mr-5 ml-1">
          <img
            src={uploadedBy.profile_pic_url}
            style={{objectFit: "cover"}}
            alt=""
            className="w-10 h-10 rounded-full"
          />
        </div>
        <div className="text-white space-y-1">
          <div className="text-lg line-clamp-1">{caption}</div>
          <div className="text-sm text-gray-300">{uploadedBy.username}</div>
          <div className="text-sm text-gray-300">
            {new Date(createdAt).toLocaleDateString()}
          </div>
        </div>
      </div>
    </div>
  );
}

export default VideoCard;
