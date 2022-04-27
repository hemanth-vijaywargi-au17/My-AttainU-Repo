import { useDispatch, useSelector } from "react-redux";
import { Link } from "react-router-dom";
import actions from "../Actions";

function NavBar() {
  const isLoggedIn = useSelector((state) => state.user.isLoggedIn);
  const name = useSelector((state) => state.user.name);
  const profile_pic_url = useSelector((state) => state.user.profile_pic_url);
  const dispatch = useDispatch();
  const logOut = () => {
    dispatch(actions.userLogOut());
  };

  return (
    <div className="navbar">
      {/*Nav Brand */}
      <Link to="/" className="navbrand">
        <svg
          className="navbrand-icon"
          fill="currentColor"
          viewBox="0 0 20 20"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path d="M2 6a2 2 0 012-2h6a2 2 0 012 2v8a2 2 0 01-2 2H4a2 2 0 01-2-2V6zM14.553 7.106A1 1 0 0014 8v4a1 1 0 00.553.894l2 1A1 1 0 0018 13V7a1 1 0 00-1.447-.894l-2 1z"></path>
        </svg>
        <h1 className="navbrand-name">Video Stream App</h1>
      </Link>

      {/*Navigation*/}
      <nav className="navigation">
        {/*Links*/}
        {isLoggedIn ? (
          <>
            <Link to="/upload" className="nav-link">
              <div className="flex space-x-1 justify-center items-center">
                <svg
                  className="w-6 h-6"
                  fill="currentColor"
                  viewBox="0 0 20 20"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    fillRule="evenodd"
                    d="M3 17a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM6.293 6.707a1 1 0 010-1.414l3-3a1 1 0 011.414 0l3 3a1 1 0 01-1.414 1.414L11 5.414V13a1 1 0 11-2 0V5.414L7.707 6.707a1 1 0 01-1.414 0z"
                    clipRule="evenodd"
                  ></path>
                </svg>
                <span>Upload</span>
              </div>
            </Link>
            <div className="nav-link" onClick={logOut}>
              Log out
            </div>
            <Link to="/myvideos" className="nav-link">
              <div className="flex space-x-3 justify-center items-center">
                <img
                  src={profile_pic_url}
                  style={{objectFit: "cover"}}
                  alt=""
                  className="w-14 h-14 rounded-full"
                />
                <span>{name}</span>
              </div>
            </Link>
          </>
        ) : (
          <>
            <Link className="nav-link" to="/login">
              Login
            </Link>

            <Link className="nav-link" to="/signup">
              Sign Up
            </Link>
          </>
        )}
      </nav>
    </div>
  );
}

export default NavBar;
