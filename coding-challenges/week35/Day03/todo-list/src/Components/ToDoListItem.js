import React from 'react'

function ToDoListItem(props) {
    return (
        <div className="list-item">
            {props.text}
        </div>
    )
}

export default ToDoListItem
