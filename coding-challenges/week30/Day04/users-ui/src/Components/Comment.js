function Comment(props) {
    return (
        <li className="list-group-item">
            <div className="small text-muted">{props.commentData.name} - ({props.commentData.email})</div>
            <div>{props.commentData.body}</div>
        </li>
    );
}
export default Comment