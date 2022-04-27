import React, { useEffect, useState } from "react";
import { Link, useSearchParams } from "react-router-dom";

export default function Albums() {
  const [albums, setAlbums] = useState([]);
  let [searchParams] = useSearchParams();
  const id = searchParams.get("userId");

  useEffect(() => {
    fetch(`https://jsonplaceholder.typicode.com/albums?userId=${id}`)
      .then((response) => response.json())
      .then((data) => setAlbums(data))
      .catch(console.log);
  }, [id]);

  return (
    <ul style={{ fontSize: "24px" }}>
      <h1>Albums</h1>
      {albums.map((album) => {
        return (
          <li key={album.id}>
            <Link to={`/photos?albumId=${album.id}`}>{album.title}</Link>
          </li>
        );
      })}
    </ul>
  );
}
