import withSearch from "./withSearch";

function List({ list, name }) {
  return (
    <div className="list">
      <h1>{name}</h1>
      {list.length!==0?list.map((item) => (
        <div className="list-item" key={item}>
          {item}
        </div>
      )):`...No Results`}
    </div>
  );
}

export default withSearch(List);
