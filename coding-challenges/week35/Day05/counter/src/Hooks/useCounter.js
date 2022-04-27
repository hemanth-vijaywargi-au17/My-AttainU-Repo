import { useReducer } from "react";
import counterReducer from '../Reducers/counterReducer'

function useCounter(initialCount=0) {
  const [state, dispatch] = useReducer(counterReducer, initialCount);
  
  const increment = () => {
    dispatch({ type: "INCREMENT_COUNT" });
  };

  const decrement = () => {
    dispatch({ type: "DECREMENT_COUNT" });
  };

  return {
    count: state,
    increment,
    decrement,
  };
}

export default useCounter;
