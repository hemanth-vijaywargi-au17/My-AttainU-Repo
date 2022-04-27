import './App.css';
import { useState, useEffect } from 'react'
import Post from './Components/Post.js'

function App() {

  const [postComponents, setPostComponents] = useState(null);
  const [currentPost, setCurrentPost] = useState({title : null, body : null});

  async function getData() {
    const response = await fetch('https://jsonplaceholder.typicode.com/posts')
    const postsData = await response.json()
    const postComponents = postsData.map(item => {
      return <Post postDetails={item} showPost={showPost}/>
    })
    setPostComponents(postComponents)
  }

  // ComponentDidMount
  useEffect(() => {
      getData()
  }, [])

  function showPost(id,t,b){
    setCurrentPost({title : t, body : b})
  }

  return (
    <div>

      <h1>Post Book</h1>

      <div className="container">

        <div className="list-box">
          <h2>Post List</h2>
          <ul className="post-list">
            {postComponents}
          </ul>
        </div>

        <div className="details-box">
          <h2>Post Details</h2>
          <div className="post-details">
            <div className="title">{currentPost.title || "Click any Post to see it's Contents"}</div>
            <p className="body">{currentPost.body}</p>
          </div>
        </div>

      </div>
    </div>
  );
}

export default App;
