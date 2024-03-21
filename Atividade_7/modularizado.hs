import Data.List

type Evento = String
type Agenda = [Evento]

main :: IO ()
main = do
    putStrLn "Bem-vindo ao Gerenciador de Agenda!"
    loop []

loop :: Agenda -> IO ()
loop agenda = do
    putStrLn "\nSelecione uma opção:"
    putStrLn "1. Adicionar evento"
    putStrLn "2. Remover evento"
    putStrLn "3. Visualizar agenda"
    putStrLn "4. Sair"
    opcao <- getLine
    processarOpcao opcao agenda

processarOpcao :: String -> Agenda -> IO ()
processarOpcao "1" agenda = adicionarEvento agenda
processarOpcao "2" agenda = removerEvento agenda
processarOpcao "3" agenda = visualizarAgenda agenda
processarOpcao "4" _      = putStrLn "Saindo do programa..."
processarOpcao _   agenda = do
    putStrLn "Opção inválida. Tente novamente."
    loop agenda

adicionarEvento :: Agenda -> IO ()
adicionarEvento agenda = do
    putStrLn "Digite o evento a ser adicionado:"
    evento <- getLine
    let novaAgenda = agenda ++ [evento]
    loop novaAgenda

removerEvento :: Agenda -> IO ()
removerEvento agenda = do
    putStrLn "Digite o índice do evento a ser removido:"
    indiceStr <- getLine
    let indice = read indiceStr
        novaAgenda = delete (agenda !! indice) agenda
    loop novaAgenda

visualizarAgenda :: Agenda -> IO ()
visualizarAgenda agenda = do
    putStrLn "Eventos na Agenda:"
    mapM_ putStrLn agenda
    loop agenda
