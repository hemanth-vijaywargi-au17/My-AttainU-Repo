import {useDispatch} from 'react-redux'
import {useState} from 'react'
import {createListItem} from './store'
import TodoList from './Components/TodoList';

function App() {
  const [input,setInput] = useState("")
  let dispatcher = useDispatch()
  function add(){
    let newAction = createListItem(input)
    dispatcher(newAction)
  }
  return (
    
      <div className="sm:w-5/6 md:3/6 m-4 lg:w-2/6 mx-auto">
        {/*Add Item UI*/}
        <div className="flex items-center p-2">
          <input type="text" placeholder="Enter New ToDo" className="p-2 border-2 border-gray-300 rounded w-full focus:outline-none" 
          onChange={(e)=>{setInput(e.target.value)}}/>
          <button className="p-2 border-2 border-gray-300 text-green-400 rounded group hover:bg-green-400"
          onClick={add}>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 mx-3 group-hover:text-white " viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M10 3a1 1 0 011 1v5h5a1 1 0 110 2h-5v5a1 1 0 11-2 0v-5H4a1 1 0 110-2h5V4a1 1 0 011-1z" clip-rule="evenodd" />
            </svg>
          </button>
        </div>
        {/*ToDo List*/}
        <TodoList/>
      </div>
  );
}

export default App;
