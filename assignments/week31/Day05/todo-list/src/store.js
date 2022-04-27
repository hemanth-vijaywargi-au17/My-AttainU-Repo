import { createStore } from 'redux'
import TodoItem from './Components/TodoItem';

//  Initial State
const initialState = {
    listItems: []
}

// Reducer
const myReducer = (state = initialState, action) => {
    if (action.type === "CREATE_LIST_ITEM") {
        let newItem = <TodoItem text={action.payload}/>
        return {
            listItems: [...state.listItems, newItem]
        }
    }
    return state
}

// Action Creator
export function createListItem(text) {
    return {
        type: "CREATE_LIST_ITEM",
        payload: text
    }
}

// Creating Store
export const myStore = createStore(myReducer, window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__())