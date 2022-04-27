import React, { useEffect, useState } from "react";
import { useSearchParams } from "react-router-dom";

export default function Photos() {
  const [photos, setPhotos] = useState([]);
  let [searchParams] = useSearchParams();
  const id = searchParams.get("albumId");

  useEffect(() => {
    fetch(`https://jsonplaceholder.typicode.com/photos?albumId=${id}`)
      .then((response) => response.json())
      .then((data) => setPhotos(data))
      .catch(console.log);
  }, [id]);

  return (
    <div>
      <h1>Photos</h1>
      {photos.map((photo) => {
        return (
          <div
            style={{
              width: "100px",
              border: "1px solid black",
              margin: "10px",
              display: "inline-block",
            }}
            key={photo.id}
          >
            <img
              src={photo.thumbnailUrl}
              alt="Not Found"
              style={{ width: "100%" }}
            />
            <p>{photo.title}</p>
          </div>
        );
      })}
    </div>
  );
}
