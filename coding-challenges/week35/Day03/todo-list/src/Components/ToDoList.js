import React, { useContext, useState } from "react";
import { myAppContext } from "../App";
import ToDoListItem from "../Components/ToDoListItem";

function ToDoList() {
  const [input, setInput] = useState("");
  let contextValue = useContext(myAppContext);
  let toDoList = contextValue.toDoList;
  let setToDoList = contextValue.setToDoList;

  const handleAdd = () => {
    setToDoList([input, ...toDoList]);
  };

  let ToDoItems = toDoList.map((item, index) => {
    return <ToDoListItem text={item} key={`list-item-${index}`} />;
  });

  return (
    // To-Do List Container
    <div className="todo-list-container">
      {/* Heading */}
      <h1 className="heading">To-do List</h1>
      {/* To-Do List Input */}
      <div className="input-section">
        <input
          type="text"
          placeholder="Enter an Item"
          value={input}
          onChange={(e) => {
            setInput(e.target.value);
          }}
        />
        <button onClick={handleAdd}>Add To-do</button>
      </div>
      {/* To-Do List */}
      <div className="list">
        {ToDoItems.length !== 0 ? ToDoItems : "List Empty!"}
      </div>
    </div>
  );
}

export default ToDoList;
