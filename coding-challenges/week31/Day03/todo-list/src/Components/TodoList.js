import {useSelector} from 'react-redux'
import {useEffect} from 'react'
import TodoItem  from './TodoItem';

export default function TodoList(props){

    let list = useSelector(state=>state.ListItems)
    useEffect(()=>{

    },[])
    
    return(
        <ul>
            <TodoItem text={list[0].text||null}/>
        </ul>
    );
}