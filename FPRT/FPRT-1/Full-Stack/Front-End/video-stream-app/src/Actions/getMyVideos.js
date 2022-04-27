import axios from "axios";

// Action Creator
const getMyVideos = () => {
  return async (dispatch, getState) => {
    let response = await axios.get("/api/getUserVideos", {
      headers: {
        token: getState().user.token,
      },
    });
    let videosObj = {}
    let videos = response.data
    videos.forEach(video=>{
      videosObj[video._id] = video
    })
    dispatch({
      type: "GET_MY_VIDEOS",
      payload: videosObj,
    });
  };
};

export default getMyVideos;
