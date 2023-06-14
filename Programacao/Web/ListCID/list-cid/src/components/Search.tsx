export default function Search() {
    const handleSearch = () => {
        // Pegar o valor digitado no campo

        // Pegar o card com as informações do CID

        // Após ter um valor digitado, button dispara um evento com a função Filtrar

        // Função Filtrar
            // Se o campo não está vazio [há algo digitado]
                // Para cada card
                    // Pegar as informações do CID (numero ou nome)

                    // Se o valor digitado não tiver dado incluido no card
                        // Esconder os demais cards

                    // senão
                        // Exibir os cards referente à pesquisa

            // senão
                // exiba todos os cards
    }

    return (
        <>
            <button onClick={handleSearch}></button>   
        </>
    )
}