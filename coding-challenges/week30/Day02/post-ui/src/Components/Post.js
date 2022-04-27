function Post(props) {

    function show() {
        props.showPost(props.postDetails.id,props.postDetails.title, props.postDetails.body)
    }

    return (
        <li className="post-title" onClick={show}>{props.postDetails.title}</li>
    );
}

export default Post