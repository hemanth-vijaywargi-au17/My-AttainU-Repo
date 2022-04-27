import axios from "axios";
import actions from ".";

// Action Creator
const editVideo = (video_id,caption,hashtags) => {
  return async (dispatch, getState) => {
    let data = {
      videoId: video_id,
      caption,
      hashtags
    };
    let options = {
      headers: {
        token: getState().user.token,
      },
    };
    await axios.post("/api/editVideo", data, options);
    dispatch({ type: "EDIT_VIDEO", payload: video_id });
    dispatch(actions.getAllVideos())
    dispatch(actions.getMyVideos())
  };
};

export default editVideo;
