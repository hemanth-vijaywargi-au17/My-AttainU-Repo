import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";

export default function Users() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/users")
      .then((response) => response.json())
      .then((data) => setUsers(data))
      .catch(console.log);
  }, []);

  return (
    <ul style={{ fontSize: "24px" }}>
      <h1>Users</h1>
      {users.map((user) => {
        return (
          <li key={user.id}>
            <Link to={`/albums?userId=${user.id}`}>{user.name}</Link>
          </li>
        );
      })}
    </ul>
  );
}
