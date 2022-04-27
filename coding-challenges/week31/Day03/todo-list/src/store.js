import { createStore } from 'redux'

//  Initial State
const initialState = {
    listItems: []
}

// Reducer
const myReducer = (state = initialState, action) => {
    if (action.type === "CREATE_LIST_ITEM") {
        let newItem = action.payload
        return {
            listItems:[...state.listItems,newItem],
        }

    }
    return state
}

// Creating Store
export const myStore = createStore(myReducer,window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__())