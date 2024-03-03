-- Função para calcular pi com base no número de termos
calculaPi :: Int -> Double
calculaPi n = (somaPi 0 n 1 1) * 32

-- Função auxiliar para somar os termos para calcular pi
somaPi :: Double -> Int -> Int -> Int -> Double
somaPi soma 0 _ _ = soma
somaPi soma n denominador sinal
    | sinal == 1 = somaPi (soma + (1.0 / fromIntegral (denominador * denominador * denominador))) (n - 1) (denominador + 2) (-sinal)
    | otherwise  = somaPi (soma - (1.0 / fromIntegral (denominador * denominador * denominador))) (n - 1) (denominador + 2) (-sinal)

-- Função principal
main :: IO ()
main = do
    putStrLn "Informe o número de termos para calcular pi: "
    n <- readLn :: IO Int
    let piAproximado = (calculaPi n) ** (1.0/3.0)
    putStrLn $ "O valor aproximado de pi com " ++ show n ++ " termos é: " ++ show piAproximado
