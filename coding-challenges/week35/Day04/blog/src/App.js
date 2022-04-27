import "./App.css";
import { Routes, Route, Link } from "react-router-dom";
import Blogs from "./Blogs";
import Blog from "./Blog";

function App() {
  return (
    <Routes>
      <Route path="/" element={<h1>Home</h1>}></Route>
      <Route path="/blogs/*" element={<Blogs />}></Route>
    </Routes>
  );
}

export default App;
