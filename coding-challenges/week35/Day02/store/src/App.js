import { useEffect, useState } from "react";
import Product from "./Product";

function App() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch("https://fakestoreapi.com/products")
      .then((response) => response.json())
      .then((data) => setProducts(data))
      .catch(console.log);
  }, []);

  return (
    <div>
      <h1 style={{ textAlign: "center" }}>Products</h1>
      {products.map((product) => {
        return <Product {...product} key={product.id} />;
      })}
    </div>
  );
}

export default App;
