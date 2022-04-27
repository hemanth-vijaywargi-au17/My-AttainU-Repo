import axios from "axios";
import actions from ".";

// Action Creator
const deleteVideo = (video_id) => {
  return async (dispatch, getState) => {
    let data = {
      videoId: video_id,
    };
    let options = {
      headers: {
        token: getState().user.token,
      },
    };
    await axios.post("/api/deleteVideo", data, options);
    dispatch({ type: "DELETE_VIDEO", payload: video_id });
  };
};

export default deleteVideo;
