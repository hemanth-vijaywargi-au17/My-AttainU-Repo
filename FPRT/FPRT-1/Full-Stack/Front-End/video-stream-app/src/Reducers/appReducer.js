import actions from "../Actions";

// Initial State
const initialState = {
  allVideos: {},
};

// Reducer
const appReducer = (state = initialState, action) => {
  if (action.type === "GET_ALL_VIDEOS") {
    return {
      ...state,
      allVideos: action.payload,
    };
  }

  if(action.type === 'DELETE_VIDEO'){
    let oldObj = state.allVideos
    let newObj ={}
    Object.assign(newObj,oldObj)
    delete newObj[action.payload]
    return{
      ...state,
      allVideos : newObj
    }
  }

  return state;
};

export default appReducer;
