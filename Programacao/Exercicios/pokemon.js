// const counterPokemonKanto = 151
const counterPokemonJohto = 251 // For vai de 152 ate 251

const fetchPokemons = async () => {
    for ( let index = 152; index <= counterPokemonJohto; index++ ) {
        await getPokemons(index)
    }
}

// const translateTypePokemon = () => {}

const getPokemons = async (id) => {
    const url = `https://pokeapi.co/api/v2/pokemon/${id}`
    const response = await fetch(url)
    const data = await response.json()
    
    console.log(`${data.id}. ${data.name} => type: ${data.types.map(element => element.type.name)}`)
}

// const createCardPokemon = () => { Obs.: Pensando em fazer 10 pokemons por fileira}

// const searchPokemon = () => {}

fetchPokemons()