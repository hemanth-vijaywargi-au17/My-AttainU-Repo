// Initial State
const initialState = {
  isLoggedIn: Boolean(localStorage.getItem("userLoggedIn")) || false,
  token: localStorage.getItem("userToken") || null,
  name: localStorage.getItem("userName") || "",
  profile_pic_url: localStorage.getItem("profile_pic_url") || "",
  error_message: "",
  signup_error_message: "",
  my_videos: {},
};

// Reducer
const userReducer = (state = initialState, action) => {
  if (action.type === "DELETE_VIDEO") {
    let oldObj = state.my_videos;
    let newObj = {};
    Object.assign(newObj, oldObj);
    delete newObj[action.payload];
    return {
      ...state,
      my_videos: newObj,
    };
  }

  if (action.type === "GET_MY_VIDEOS") {
    return {
      ...state,
      my_videos: action.payload,
    };
  }

  if (action.type === "USER_LOGIN_FAILED") {
    return {
      ...state,
      error_message: action.payload,
    };
  }

  if (action.type === "USER_LOGIN_SUCCESS") {
    let payload = action.payload;
    return {
      ...state,
      isLoggedIn: true,
      token: payload.token,
      error_message: "",
      username: payload.username,
      profile_pic_url: payload.profile_pic_url,
    };
  }

  if (action.type === "USER_LOG_OUT") {
    return {
      ...state,
      isLoggedIn: false,
      token: null,
      error_message: "",
    };
  }

  if (action.type === "CLEAR_ERROR_MESSAGE") {
    return {
      ...state,
      error_message: "",
      signup_error_message: "",
    };
  }

  if (action.type === "SIGNUP_FAILED") {
    return {
      ...state,
      signup_error_message: action.payload,
    };
  }

  if (action.type === "SIGNUP_SUCCESS") {
    return {
      ...state,
      signup_error_message: action.payload,
    };
  }

  return state;
};

export default userReducer;
