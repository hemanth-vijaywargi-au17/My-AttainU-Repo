import { Component } from 'react'

class Post extends Component {
    showPost = (e) => {
        this.props.methods.showPost(e.target, this.props.postDetails.title, this.props.postDetails.body)
    }

    render() {
        return (
            <li onClick={this.showPost} className="post-title">{this.props.postDetails.title}</li>
        );
    }
}

export default Post