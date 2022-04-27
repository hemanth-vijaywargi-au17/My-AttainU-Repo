import { createContext, useState } from "react";
import "./App.css";
import TodoList from "./Components/ToDoList";

export const myAppContext = createContext();

function App() {
  const [toDoList, setToDoList] = useState([]);
  let contextValue = { toDoList, setToDoList };

  return (
    <myAppContext.Provider value={contextValue}>
      <TodoList />
    </myAppContext.Provider>
  );
}

export default App;
