-- Definição do tipo de dados para representar um passageiro, desnecessário nesse exercício, mas deixei para lembrar algo semelhante a struct em C
data Passenger = Passenger { rg :: String
                           , passagem :: String
                           , dataNascimentoRG :: String
                           , dataNascimentoPassagem :: String
                           , assento :: String
                           } deriving (Show)

-- Função para processar a entrada do usuário para um único passageiro
processarPassageiro :: Int -> IO ()
processarPassageiro n = do
    putStrLn $ "Passageiro " ++ show n ++ ", tem RG? (rg ou nao possui): "
    rgInput <- getLine
    if rgInput == "nao possui"
        then putStrLn "A saída é nessa direção."
        else do
            putStrLn "Tem passagem? (passagem ou nao possui): "
            passagemInput <- getLine
            if passagemInput == "nao possui"
                then putStrLn "A recepção é nessa direção."
                else do
                    putStrLn "Digite a data de nascimento que consta no RG: "
                    dataNascimentoRGInput <- getLine
                    putStrLn "Digite a data de nascimento que consta na passagem: "
                    dataNascimentoPassagemInput <- getLine
                    if dataNascimentoRGInput /= dataNascimentoPassagemInput
                        then putStrLn "190"
                        else do
                            putStrLn "Informe seu assento: "
                            assentoInput <- getLine
                            putStrLn $ "O seu assento é o " ++ assentoInput ++ ", tenha um ótimo dia."

-- Função principal para processar os passageiros
main :: IO ()
main = do
    putStrLn "Digite a quantidade de passageiros: "
    qtdPassageiros <- readLn :: IO Int
    mapM_ processarPassageiro [1..qtdPassageiros]
