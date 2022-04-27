import { useEffect } from "react";
import useLocalStorage from "../Hooks/useLocalStorage";
import useStopWatch from "../Hooks/useStopWatch";

function StopWatch() {
  const [storageValue, setStorageValue] = useLocalStorage("seconds", 0);
  const { formattedTime, timeInSeconds, start, stop, reset } =
    useStopWatch(storageValue);

  // Tracking timeInSeconds and setting it to localStorage everytime it changes
  useEffect(() => {
    setStorageValue(timeInSeconds);
  }, [timeInSeconds]);

  return (
    <div style={{ textAlign: "center" }}>
      <h1>Stop Watch</h1>
      <h1>{formattedTime}</h1>
      <button onClick={start}>Start</button>
      <button onClick={stop}>Stop</button>
      <button onClick={reset}>Reset</button>
    </div>
  );
}

export default StopWatch;
