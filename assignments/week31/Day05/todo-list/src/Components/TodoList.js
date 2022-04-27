import {useSelector} from 'react-redux'

function TodoList() {
    let listItems = useSelector(state=>state.listItems)
    return (
        <div className="bg-gray-200 p-4 rounded space-y-3">
          {listItems}
        </div>
    )
}

export default TodoList
