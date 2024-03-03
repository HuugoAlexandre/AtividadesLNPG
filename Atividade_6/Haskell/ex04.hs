import Data.List (sortOn, minimumBy, maximumBy)
import Data.Ord (comparing)

data Participante = Participante { nome :: String, respostas :: [Int], acertos :: Int } deriving (Show)

qtdQuests :: Int
qtdQuests = 10

lerGabarito :: IO [Int]
lerGabarito = do
    putStrLn "Digite o gabarito, cada resposta separada por espaço:"
    fmap (map read . words) getLine

lerParticipantes :: [Int] -> IO [Participante]
lerParticipantes gabarito = do
    putStrLn "Digite o nome do participante (ou * para encerrar):"
    nome <- getLine
    if nome == "*"
        then return []
        else do
            putStrLn $ "Digite as respostas de " ++ nome ++ ", cada resposta separada por espaço:"
            respostasStr <- getLine
            let respostas = map read $ words respostasStr
            let acertos = length $ filter (\(r, g) -> r == g) $ zip respostas gabarito
            participantes <- lerParticipantes gabarito
            return (Participante nome respostas acertos : participantes)

main :: IO ()
main = do
    gabarito <- lerGabarito
    participantes <- lerParticipantes gabarito
    let participantesOrdenados = sortOn nome participantes
        menorNota = minimumBy (comparing acertos) participantesOrdenados
        maiorNota = maximumBy (comparing acertos) participantesOrdenados
        qtdAcimaMetade = length $ filter (\p -> acertos p > qtdQuests `div` 2) participantesOrdenados
    putStrLn "Lista dos participantes com suas respectivas notas:"
    mapM_ (\p -> putStrLn $ nome p ++ " " ++ show (acertos p)) participantesOrdenados
    putStrLn $ "Menor nota: " ++ show (acertos menorNota) ++ ", do participante: " ++ nome menorNota
    putStrLn $ "Maior nota: " ++ show (acertos maiorNota) ++ ", do participante: " ++ nome maiorNota
    putStrLn $ "Percentual de participantes com mais da metade de acertos: " ++ show (fromIntegral qtdAcimaMetade / fromIntegral (length participantesOrdenados) * 100) ++ "%"
