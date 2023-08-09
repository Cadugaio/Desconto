print('Bem Vindo a loja do Carlos Eduardo Gaio')
valor_produto = float(input('entre com o valor desejado: '))
qtd_produto = int(input('entre com a quantidade desejada: '))
desconto_produto = 0
if qtd_produto <= 9:
    desconto_produto = 0.00
elif 10 <= qtd_produto < 100:
    desconto_produto = 0.05
elif 100 <= qtd_produto < 1000:
    desconto_produto = 00.10
else:
    desconto_produto = 0.15

total_sem_desconto = valor_produto * qtd_produto
print('o valor total sem desconto é: R$ {:.2f}'.format(total_sem_desconto))
total_com_desconto = total_sem_desconto - total_sem_desconto * desconto_produto
print('o valor total com desconto é: R$ {:.2f}'.format(total_com_desconto))

