from dominio import Leilao, Usuario
import time

gui = Usuario('Gui', 500.0)
yuri = Usuario('Yuri', 500.0)

leilao = Leilao('Celular')

gui.propoe_lance(leilao, 100.0)
yuri.propoe_lance(leilao, 150.0)

for lance in leilao.lances:
    print(f'o usuario {lance.usuario.nome} fez o lance de R$ {lance.valor}')


print(f'o menor lance foi de {leilao.menor_lance} e o maior lance foi de {leilao.maior_lance}')
