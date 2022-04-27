import React, { useState } from "react";

function withSearch(PassedComponent) {
  return function (props) {
    const [query, setQuery] = useState("");
    return (
      <div className="search-box">
        <input
          type="text"
          value={query}
          onChange={(e) => {
            setQuery(e.target.value);
          }}
          placeholder={`...Search ${props.name}`}
        />
        <PassedComponent
          {...props}
          list={props.list.filter((item) =>
            item.toLowerCase().includes(query.toLowerCase())
          )}
        />
      </div>
    );
  };
}

export default withSearch;
