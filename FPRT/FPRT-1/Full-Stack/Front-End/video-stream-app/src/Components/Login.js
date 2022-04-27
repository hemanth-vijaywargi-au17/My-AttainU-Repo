import { useState } from "react";
import { Link, Navigate } from "react-router-dom";
import { connect } from "react-redux";
import actions from "../Actions";
import { loginSchema } from "../utils/JoiValidation";

const Login = (props) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [validationError, setValidationError] = useState("");

  if (props.isLoggedIn) {
    return <Navigate to="/" />;
  }

  const handleSubmitForm = (e) => {
    e.preventDefault();
    const result = loginSchema.validate({ email: email, pass: password });

    if (result.error) {
      setValidationError(result.error);
    } else {
      setValidationError("");
      props.login(email, password);
    }
  };

  return (
    <div className="form-parent">
      <form
        className="form"
        method="POST"
        onSubmit={handleSubmitForm}
        noValidate
      >
        <h2 className="form-heading">Login</h2>

        <input
          className="form-input"
          type="email"
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
          className="form-input"
          type="password"
          name="password"
          placeholder="Password"
          onChange={(e) => setPassword(e.target.value)}
          value={password}
          onClick={() => {
            props.clear_message();
            setValidationError("");
          }}
        />

        <div className="form-error-message">{validationError.message || props.error_message}</div>

        <button type="submit" className="form-submit-btn">Submit</button>

        <div>
          <span>Not a member ?</span>
          <Link to="/signup" className="form-secondary-btn">
            Sign Up
          </Link>
        </div>
      </form>
    </div>
  );
};

const mapStateToProps = (state) => {
  return {
    isLoggedIn: state.user.isLoggedIn,
    error_message: state.user.error_message,
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    clear_message: () => {
      dispatch({
        type: "CLEAR_ERROR_MESSAGE",
      });
    },
    login: (email, password) => {
      dispatch(actions.userLogin(email, password));
    },
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(Login);
