import pandas as pd
from twilio.rest import Client

account_sid = 'ACd0ab0b571b578e08a09482346ff84c94'
auth_token = '3d48e428392402c45a1fe5e6fe96a56d'
client = Client(account_sid, auth_token)


lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas']> 55000, 'Vendas'].values[0]
        print(f'No mes {mes} Meta alcançada, congratulation. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages \
            .create(
            body=f'No mes {mes} Meta alcançada, congratulation. Vendedor: {vendedor}, Vendas: {vendas}',
            from_='+15673502686',
            to='+351932800240'
        )
        print(message.sid)






