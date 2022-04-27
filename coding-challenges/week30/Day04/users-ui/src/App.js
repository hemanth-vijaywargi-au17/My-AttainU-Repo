import './App.css';
import { useState, useEffect } from 'react'
import User from './Components/User'
import Comment from './Components/Comment'
import { BrowserRouter, Route, Link } from 'react-router-dom'

function App() {
  const [userComponents, setUserComponents] = useState(null)
  const [commentComponents, setCommentComponents] = useState(null)

  useEffect(() => {
    getData()
  }, [])

  async function getData() {
    let responseObj1 = await fetch('https://jsonplaceholder.typicode.com/users')
    let usersData = await responseObj1.json()
    setUserComponents(usersData.map(item => {
      return <User userData={item} key={item.id} />
    }))

    let responseObj2 = await fetch('https://jsonplaceholder.typicode.com/comments')
    let commentsData = await responseObj2.json()
    setCommentComponents(commentsData.map(item => {
      return <Comment commentData={item} key={item.id} />
    }))
  }

  return (
    <div>
      <BrowserRouter>
        <ul>
          <li><Link to="/users">Users</Link></li>
          <li><Link to="/comments">Comments</Link></li>
        </ul>
        <Route path="/users">
          <h1>All Users</h1>
          <div className="users">
            {userComponents}
          </div>
        </Route>
        <Route path="/comments">
          <div className="comments">
            <h1>Comments</h1>
            <ul className="list-group list-group-flush">
              {commentComponents}
            </ul>
          </div>
        </Route>
      </BrowserRouter>
    </div>
  );
}

export default App;
