import { useState } from "react";
import { Link, Navigate } from "react-router-dom";
import actions from "../Actions";
import { connect } from "react-redux";
import { signupSchema } from "../utils/JoiValidation";

const SignUp = (props) => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmpassword, setConfirmpassword] = useState("");
  const [image, setImage] = useState(null);
  const [validationError, setValidationError] = useState("");

  if (props.error_message === "Sign Up SuccessFull!") {
    props.clear_message();
    return <Navigate to="/login" />;
  }

  const handleSubmitForm = (e) => {
    e.preventDefault();
    const result = signupSchema.validate({
      username: username,
      email: email,
      pass: password,
      repeat_password: confirmpassword,
    });

    if (result.error) {
      setValidationError(result.error);
    } else {
      setValidationError("");
      props.signup(username, email, password, image);
    }
  };

  return (
    <div className="form-parent">
      <form
        method="POST"
        className="form"
        onSubmit={handleSubmitForm}
        noValidate
      >
        <h2 className="form-heading">Sign Up</h2>
        <input
          type="username"
          className="form-input"
          name="username"
          placeholder="Username"
          onChange={(e) => setUsername(e.target.value)}
          value={username}
          onClick={() => {
            props.clear_message();
            setValidationError("");
          }}
        />
        <input
          type="email"
          className="form-input"
          name="email"
          placeholder="Email"
          onChange={(e) => setEmail(e.target.value)}
          value={email}
          onClick={() => {
            props.clear_message();
            setValidationError("");
          }}
        />

        <input
          type="password"
          className="form-input"
          name="password"
          placeholder="Password"
          onChange={(e) => setPassword(e.target.value)}
          value={password}
          onClick={() => {
            props.clear_message();
            setValidationError("");
          }}
        />

        <input
          type="password"
          className="form-input"
          name="confirm-password"
          placeholder="Confirm Password"
          onChange={(e) => setConfirmpassword(e.target.value)}
          value={confirmpassword}
          onClick={() => {
            props.clear_message();
            setValidationError("");
          }}
        />
        <div className="form-small-text">
          Upload your profile picture (optional)
        </div>

        <input
          type="file"
          className=""
          name="userImage"
          onChange={(e) => {
            setImage(e.target.files[0]);
          }}
          onClick={() => {
            props.clear_message();
            setValidationError("");
          }}
        />

        <div className="form-error-message">
          {validationError.message || props.error_message}
        </div>

        <button className="form-submit-btn">Register</button>

        <div>
          <span className="">Already a Member ?</span>
          <Link to="/login" className="form-secondary-btn">
            Log In
          </Link>
        </div>
      </form>
    </div>
  );
};

const mapStateToProps = (state) => {
  return {
    error_message: state.user.signup_error_message,
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    clear_message: () => {
      dispatch({
        type: "CLEAR_ERROR_MESSAGE",
      });
    },
    signup: (username, email, password, userImage) => {
      dispatch(actions.userSignUp(username, email, password, userImage));
    },
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(SignUp);
