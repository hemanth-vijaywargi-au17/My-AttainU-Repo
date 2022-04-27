import axios from "axios";

// Action Creator
const userLogin = (userEmail, userPassword) => {
  return async (dispatch, getState) => {
    let userCred = {
      email: userEmail,
      password: userPassword,
    };
    let response = await axios.post("/api/login", userCred);
    if (response.data.error) {
      dispatch({
        type: "USER_LOGIN_FAILED",
        payload: response.data.message,
      });
    } else {
      let data = response.data;
      localStorage.setItem("userLoggedIn", true);
      localStorage.setItem("userToken", data.token);
      localStorage.setItem("userName", data.name);
      localStorage.setItem("profile_pic_url", data.profile_pic_url);

      dispatch({
        type: "USER_LOGIN_SUCCESS",
        payload: {
          token: data.token,
          name: data.name,
          profile_pic_url: data.profile_pic_url,
        },
      });
    }
  };
};

export default userLogin;
