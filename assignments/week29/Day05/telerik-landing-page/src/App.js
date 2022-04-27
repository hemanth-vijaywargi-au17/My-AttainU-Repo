import Product from "./Components/product";
import productsInfo from "./Components/productsInfo";
import './App.css'

const productComponents = productsInfo.map(item => {
  return <Product productsInfo={item} />
})

function App() {
  return (
    <div>
      <header>
        <nav>
          Wasn't Able to Make the Navbar, Completed the rest of the UI.
        </nav>
      </header>

      <main>
        <section id="landing">
          <div>
            <h1>Develop Experiences</h1>
            <p>UI frameworks and app developments tools that 1.9 million developers love</p>
          </div>
        </section>

        <section id="products">
          {productComponents}
        </section>
      </main>

    </div>
  );
}

export default App;
