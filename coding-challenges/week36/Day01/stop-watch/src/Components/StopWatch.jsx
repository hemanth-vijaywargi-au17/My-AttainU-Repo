import useStopWatch from "./useStopWatch";

function StopWatch() {
  const { time, start, stop, reset } = useStopWatch();

  return (
    <>
      <h1>Stop Watch</h1>
      <h1>{time}</h1>
      <button onClick={start}>Start</button>
      <button onClick={stop}>Stop</button>
      <button onClick={reset}>Reset</button>
    </>
  );
}

export default StopWatch;
