import { useEffect } from 'react'

function Alarm(props) {
    useEffect(() => {
        var date1 = new Date(); // current date
        var date2 = new Date(props.alarmTime);
        var timeOut = Math.abs(date2.getTime() - date1.getTime()); // in miliseconds
        setTimeout(() => {
            alert("WAKEEEEE UPPPPPPP")
        }, timeOut)
    }, [])

    return (
        <li className="alarm">{props.alarmTime.slice(11) + "  (" + (props.alarmTime.slice(0, 10)) + ")"}</li>
    );
}

export default Alarm