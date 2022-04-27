import { useDispatch } from "react-redux";

export default function TodoListInput(props) {
    let input = ''
    const dispatcher = useDispatch()
    function handleClick() {
        const createListItem = {
            type: "CREATE_LIST_ITEM",
            payload: input
        }
        dispatcher(createListItem)
    }
    return (
        <div>
            <input type="text" onChange={(e) => { input = e.target.value }} />
            <button onClick={handleClick}>Add Item</button>
        </div>
    );
}