// Action Creator
const userLogOut = () => {
    localStorage.removeItem('userLoggedIn')
    localStorage.removeItem('userToken')
    localStorage.removeItem("userName");
    localStorage.removeItem("profile_pic_url");
  return {
      type:"USER_LOG_OUT"
  }
}

export default userLogOut;
