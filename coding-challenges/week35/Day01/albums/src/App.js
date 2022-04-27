import Users from "./Components/Users";
import Albums from "./Components/Albums";
import Photos from "./Components/Photos";
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Link to="/users">All Users</Link>} />
        <Route path="/users" element={<Users />} />
        <Route path="/albums" element={<Albums />} />
        <Route path="/photos/*" element={<Photos />} />
      </Routes>
    </BrowserRouter>
  );
}
