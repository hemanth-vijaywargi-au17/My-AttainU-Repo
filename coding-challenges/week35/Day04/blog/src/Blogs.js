import React from "react";
import { Routes, Route } from "react-router-dom";
import Blog from "./Blog";

function Blogs() {
  return (
    <>
      <h1>Blogs Page (Enter blog id in path param to view a specific blog)</h1>
      <Routes>
        <Route path="/:id" element={<Blog />}></Route>
      </Routes>
    </>
  );
}

export default Blogs;
