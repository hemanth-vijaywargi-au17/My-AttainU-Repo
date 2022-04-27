import {Provider} from 'react-redux'
import TodoList from './Components/TodoList.js';
import TodoListInput from './Components/TodoListInput.js';
import {myStore} from './store.js'

function App() {
  return (
    <Provider store={myStore}>
      <div>
        <TodoListInput/>
        <TodoList/>
      </div>
    </Provider>
  );
}

export default App;
