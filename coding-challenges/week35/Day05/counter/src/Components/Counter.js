import useCounter from "../Hooks/useCounter";

function Counter() {
  // Custom Hook useCounter() , takes initialCount as a param
  const { count, increment, decrement } = useCounter(0);

  return (
    <div>
      <h1>Count : {count}</h1>
      <button onClick={increment}>Increment Count</button>
      <button onClick={decrement}>Decrement Count</button>
    </div>
  );
}

export default Counter;
