import { combineReducers } from "redux";
import appReducer from "./appReducer";
import userReducer from "./userReducer";

const initialState = {
  user: userReducer,
  app: appReducer,
};
const rootReducer = combineReducers(initialState);

export default rootReducer;
