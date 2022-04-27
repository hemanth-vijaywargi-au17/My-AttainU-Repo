import { useEffect, useRef, useState } from "react";

function formatTime(seconds) {
  let mins = String(parseInt(seconds / 60));
  let secs = String(seconds % 60);
  if (mins.length === 1) {
    mins = "0" + mins;
  }
  if (secs.length === 1) {
    secs = "0" + secs;
  }
  return mins + ":" + secs;
}

function useStopWatch(initialTime) {
  const [seconds, setSeconds] = useState(initialTime || 0);
  const [running, setRunning] = useState(false);
  const timerId = useRef();

  useEffect(() => {
    if (running) {
      timerId.current = setInterval(() => {
        setSeconds((prevState) => {
          return prevState + 1;
        });
      }, 1000);
    } else {
      clearInterval(timerId.current);
    }
  }, [running]);

  return {
    formattedTime: formatTime(seconds),
    timeInSeconds: seconds,
    start: () => {
      setRunning(true);
    },
    stop: () => {
      setRunning(false);
    },
    reset: () => {
      setRunning(false);
      setSeconds(0);
    },
  };
}

export default useStopWatch;
