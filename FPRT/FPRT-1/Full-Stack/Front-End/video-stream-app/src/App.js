import { BrowserRouter, Route, Routes } from "react-router-dom";
import "./App.css";
import NavBar from "./Components/NavBar";
import Login from "./Components/Login";
import SignUp from "./Components/SignUp";
import Home from "./Components/Home";
import UploadPage from "./Components/UploadPage";
import MyVideosPage from "./Components/MyVideosPage";
import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import actions from "./Actions";
import VideoDetails from "./Components/VideoDetails";
import EditVideo from "./Components/EditVideo";

function App() {
  const dispatch = useDispatch();
  const isLoggedIn = useSelector(state=>state.user.isLoggedIn)

  useEffect(() => {
    dispatch(actions.getAllVideos());
  }, []);

  useEffect(() => {
    if(isLoggedIn){
      dispatch(actions.getMyVideos())
    }
  }, [isLoggedIn])

  return (
    <BrowserRouter>
      <NavBar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<SignUp />} />
        <Route path="/upload" element={<UploadPage />} />
        <Route path="/myvideos" element={<MyVideosPage />} />
        <Route path="/video/:id" element={<VideoDetails />} />
        <Route path="/editVideo/:id" element={<EditVideo />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
