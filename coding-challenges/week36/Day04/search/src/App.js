import "./App.css";
import List from "./Components/List";
import useFetch from "./Components/useFetch";

function App() {
  const products = useFetch(`https://fakestoreapi.com/products`);
  const users = useFetch(`https://fakestoreapi.com/users`);

  return (
    <div className="parent">
      <List list={products.map((obj) => obj.title)} name="Products" />
      <List
        list={users.map((obj) => obj.name.firstname + " " + obj.name.lastname)}
        name="Users"
      />
    </div>
  );
}

export default App;
