import './App.css';
import { Component } from 'react'
import Post from './Components/Post.js'

class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
      currentPost: {
        title: null,
        body: null
      }
    }
  }

  async componentDidMount() {
    const response = await fetch('https://jsonplaceholder.typicode.com/posts')
    const posts = await response.json()
    const postComponents = posts.map(item => {
      return <Post methods={{ showPost: this.show }} postDetails={item} />
    })
    this.setState({ components: postComponents, currentPost: { element: null, title: null, body: null } })
  }

  show = (target, t, b) => {
    let prev = this.state.currentPost.element
    if (prev) {
      prev.style.removeProperty('background-color')
    }

    target.style.backgroundColor = "rgba(0,0,0,0.3)"
    this.setState({ currentPost: { ...this.state, element: target, title: t, body: b } })
  }

  render() {

    return (
      <div>

        <h1>Post Book</h1>

        <div className="container">

          <div className="list-box">
            <h2>Post List</h2>
            <ul className="post-list">
              {this.state.components}
            </ul>
          </div>

          <div className="details-box">
            <h2>Post Details</h2>
            <div className="post-details">
              <div className="title">{this.state.currentPost.title || "Click on any Post to see it's Details"}</div>
              <p className="body">{this.state.currentPost.body}</p>
            </div>
          </div>

        </div>
      </div>
    );
  }


}

export default App;
