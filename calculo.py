entrada = input("Entre com o valor do consumo dado em KWH: ")

tarifaSI = 0.5572
print(tarifaSI)
consumo = 188
print(consumo)
pis = (0.92 / 100)
print(pis)
cofins = (4.23 / 100)
print(cofins)
icms = 0.12
print(icms)

pis = '1,65%'
cofins = '7,6%'

tabela_icms = {'0 a 90': 'isento', '91 a 200': '0.12', 'acima de 200': '0.25'}

tabela_cosip_2019 = {'0 - 80': '0,00', '81 - 100': '2,96', '101 - 180': '7,87',
                    '181 - 220': '9,49', '221 - 300': '15,83', '301 - 400':'22,16',
                    '401 - 500': '27,68', '501 - 600': '34,94', '601 - 700':'40,78',
                    '701 - 800': '46,61', '801 - 900': '52,40', '901 - 1.000':'58,21',
                    '1.001 - 2.000': '103,84', '2.001 - 3.000': '162,78', '3.001- 4.000':
                    '186,79', '4.001 - 5.000': '236,55', '5.001 - 7.000':'333,89',
                    '7.001 - 10.000': '472,93', 'Acima de 10.000': '547,03'}

tabela_cosip_2020 = {'0 - 80': '0,00', '81 - 100': '3,06', '101 - 180': '8,14',
                    '181 - 220': '9,81', '221 - 300': '16,36', '301 - 400': '22,91',
                    '401 - 500': '28,61', '501 - 600': '36,12', '601 - 700': '42,15',
                    '701 - 800': '48,18', '801 - 900': '54,17', '901 - 1.000': '60,17',
                    '1.001 - 2.000': '107,34', '2.001 - 3.000': '168,27', '3.001- 4.000':
                    '193,08', '4.001 - 5.000': '244,52', '5.001 - 7.000':'345,14',
                    '7.001 - 10.000': '488,87', 'Acima de 10.000': '565,46'}

tarifaCI = tarifaSI / (1 - (pis + cofins + icms))
valor_pago_sem_cosip = tarifaCI * 188 
print("Tarifa sem imposto ", tarifaSI)
print("Tarifa com imposto ", tarifaCI)
print("Valor a ser pago sem CIP/COSIP: ", valor_pago_sem_cosip)
print("COSIP: ", tabela_cosip_2019['181 - 220']) 
