import Clock from "./Components/Clock";
import { useState, useEffect } from 'react'

function App() {
  const [date, setDate] = useState(new Date())
  useEffect(() => {
    setInterval(() => { setDate(new Date()) }, 1000)
  }, [])

  return (
    <div>
      <Clock currentTime={date.toLocaleTimeString()} date={date.toDateString()} />
    </div>
  );
}

export default App;
