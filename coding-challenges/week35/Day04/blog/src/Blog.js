import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router'

function Blog() {
    let pathParams = useParams()
    let id = pathParams.id
    const [blog, setBlog] = useState([]);

    useEffect(() => {
      fetch(`https://jsonplaceholder.typicode.com/posts/${id}`)
        .then((response) => response.json())
        .then((data) => setBlog(data))
        .catch(console.log);
    }, [id]);

    return (
        <div>
            <h1>BlogId - {id} : {blog.title}</h1>
            <p>{blog.body}</p>
        </div>
    )
}

export default Blog
