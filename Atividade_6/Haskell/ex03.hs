-- Importando o módulo Text.Printf para formatar a saída
import Text.Printf (printf)

-- Função principal
main :: IO ()
main = do
    putStrLn "Informe a quantidade de brinquedos vendidos: "
    n <- readLn :: IO Int
    let precoBrinquedo = 19.9 :: Double
        totalVendas = fromIntegral n * precoBrinquedo
        bonusQuant = n `div` 15
        valorBonus = fromIntegral bonusQuant * (totalVendas * 0.08)
        salario = (totalVendas / 2) + valorBonus :: Double

    printf "Valor arrecadado com as vendas: R$%.2f\n" totalVendas
    printf "Valor arrecadado com bônus: R$%.2f\n" valorBonus
    printf "Salário total: R$%.2f\n" salario
