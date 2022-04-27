import './PokeCard.css'
import { useState, useEffect } from 'react'

function PokeCard(props) {
    const [pokemonData, setPokemonData] = useState({
        imgURL: null,
        poke_name: null,
        poke_id: null,
        poke_type: null
    })
    const [bg, setBg] = useState("white")

    useEffect(() => {
        getData()
    }, [])

    async function getData() {
        const responseObj = await fetch(`https://pokeapi.co/api/v2/pokemon/${props.name}`)
        const responseJson = await responseObj.json()
        setPokemonData({
            imgURL: responseJson.sprites.front_default,
            poke_name: responseJson.name.replace(/(^|\s)\S/g, letter => letter.toUpperCase()),
            poke_id: responseJson.id,
            poke_type: responseJson.types[0].type.name
        })
        const bgData = {
            grass: "hsl(123,88%,93%)",
            fire: "hsl(355,82%,93%)",
            water: "hsl(197,83%,92%)",
            poison: "hsl(134,40%,72%)",
            normal: "hsl(0,0%,96%)",
            fairy: "pink",
        }

        setBg(bgData[responseJson.types[0].type.name])
    }
    return (
        <div className="poke-card" style={{ backgroundColor: bg }}>
            <div className="imgBox">
                <img src={pokemonData.imgURL} alt="" />
            </div>
            <div className="poke-id">#{pokemonData.poke_id}</div>
            <div className="poke-name">{pokemonData.poke_name}</div>
            <div className="poke-type">Type : {pokemonData.poke_type}</div>
        </div>
    );
}

export default PokeCard