import axios from "axios";

// Action Creator
const getAllVideos = () => {
  return async (dispatch, getState) => {
    let response = await axios.get("/api/allvideos");
    let videosObj = {}
    let videos = response.data
    videos.forEach(video=>{
      videosObj[video._id] = video
    })
    dispatch({
      type: "GET_ALL_VIDEOS",
      payload: videosObj,
    });
  };
};

export default getAllVideos;
