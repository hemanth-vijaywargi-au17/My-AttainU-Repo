import { useState } from 'react'
import './Clock.css'
import Alarm from './Alarm'

function Clock(props) {
    const [alarmsList, setalarmsList] = useState([])
    const [alarmComponents, setalarmComponents] = useState([])
    const [newAlarm, setNewAlarm] = useState(null)

    function addAlarm() {
        if (newAlarm) {
            if (!(alarmsList.includes(newAlarm))) {
                setalarmsList([...alarmsList, newAlarm])
                setalarmComponents([...alarmComponents, <Alarm key={newAlarm} alarmTime={newAlarm} />])
            }
        }
    }

    return (
        <div className="container">
            <h1>Digital Clock</h1>
            <div className="clock">
                <div className="time">
                    <div>{props.currentTime.slice(0, props.currentTime.length - 3)}</div>
                    <div>{props.currentTime.slice(props.currentTime.length - 3, props.currentTime.length)}</div>
                </div>
                <div className="date">{props.date}</div>
            </div>
            <div className="alarm">
                <input type="datetime-local" onChange={(e) => { setNewAlarm(e.target.value) }} required />
                <button onClick={addAlarm}>Set Alarm</button>
            </div>

            <h2>Alarms List</h2>
            <ul className="alarm-list">
                {alarmComponents}
            </ul>
        </div>
    )
}

export default Clock