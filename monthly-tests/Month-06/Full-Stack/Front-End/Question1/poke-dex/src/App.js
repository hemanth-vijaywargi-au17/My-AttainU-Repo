import './App.css';
import { useState, useEffect } from 'react'
import PokeCard from './Components/PokeCard'

function App() {
  const [pokeComponents, setPokeComponents] = useState(null)

  useEffect(() => {
    getData(1000)
  }, [])

  async function getData(n) {
    const responseObj = await fetch(`https://pokeapi.co/api/v2/pokemon?limit=${n}`)
    const responseJson = await responseObj.json()
    let components = responseJson.results.map(item => {
      return <PokeCard name={item.name} url={item.url} key={item.name} />
    })
    setPokeComponents(components)
  }

  return (
    <div className="parent">
      <h1>Poke Dex</h1>
      <div className="poke-dex">
        {pokeComponents}
      </div>
    </div>
  );
}

export default App;
