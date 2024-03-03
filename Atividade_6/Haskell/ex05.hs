import Text.Printf (printf)

main :: IO ()
main = do
    putStrLn "Digite o mês e ano (Ex: 01/2021) e IPCA:"
    loop "" (1/0) "" (-1/0) 0 0
  where
    loop menorMesAno menorIpca maiorMesAno maiorIpca somaIpca totalMeses = do
        entrada <- getLine
        if entrada == "*"
            then do
                let mediaIpca = if totalMeses == 0 then 0 else somaIpca / fromIntegral totalMeses
                printf "Menor IPCA: %.2f no mês/ano %s\n" menorIpca menorMesAno
                printf "Maior IPCA: %.2f no mês/ano %s\n" maiorIpca maiorMesAno
                printf "Média do IPCA: %.2f\n" mediaIpca
            else do
                let (mesAno, rest) = break (== ' ') entrada
                    ipcaStr = drop 1 rest
                    ipca = read ipcaStr :: Double
                loop (if ipca < menorIpca then mesAno else menorMesAno)
                     (min menorIpca ipca)
                     (if ipca > maiorIpca then mesAno else maiorMesAno)
                     (max maiorIpca ipca)
                     (somaIpca + ipca)
                     (totalMeses + 1)
