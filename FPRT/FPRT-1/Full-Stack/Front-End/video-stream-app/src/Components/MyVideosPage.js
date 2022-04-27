import React, { useEffect, useState } from "react";
import { useSelector } from "react-redux";
import VideoCard from "./VideoCard";

function MyVideosPage() {
  const myVideos = useSelector((state) => state.user.my_videos);
  const [videos, setVideos] = useState([]);

  useEffect(() => {
    let videos = [];
    for (const [key, value] of Object.entries(myVideos)) {
      let inMyVideos = value._id in myVideos;
      videos.push(
        <VideoCard {...value} key={value._id} inMyVideos={inMyVideos} />
      );
    }
    setVideos(videos);
  }, [myVideos]);

  return (
    <>
      <h1 className="text-center text-4xl mt-4 text-bold text-white">
        My Videos
      </h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 px-28 gap-4 py-8 ">
        {videos}
      </div>
    </>
  );
}

export default MyVideosPage;
