from unittest import TestCase

from leilao.dominio import Leilao, Lance, Usuario
from leilao.excecoes import LanceInvalido


class TestLeilao(TestCase):

    def setUp(self) -> None:
        self.gui = Usuario('Gui', 500.0)
        self.yuri = Usuario('Yuri', 500.0)
        self.rodrigo = Usuario('Rodrigo', 500.0)

        self.lance_do_yuri = Lance(self.yuri, 100.0)
        self.lance_do_gui = Lance(self.gui, 150.0)
        self.lance_do_rodrigo = Lance(self.rodrigo, 250.0)

        self.leilao = Leilao('Celular')

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adcionados_em_ordem_crescente(self):
        self.leilao.propoe(self.lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_um_lance_quando_adcionados_em_ordem_decrescente(self):
        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_do_gui)
            self.leilao.propoe(self.lance_do_yuri)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):
        self.leilao.propoe(self.lance_do_gui)

        valor_esperado = 150.0

        self.assertEqual(valor_esperado, self.leilao.menor_lance)
        self.assertEqual(valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_3_lances(self):
        self.leilao.propoe(self.lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(self.lance_do_rodrigo)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 250.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_do_gui)

        quantidade_de_lances_recebido = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances_recebido)

    def test_deve_permitir_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        self.leilao.propoe(self.lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)

        quantidades_de_lances = len(self.leilao.lances)

        self.assertEqual(2, quantidades_de_lances)

    def test_nao_deve_permitir_propor_um_lance_caso_o_ultimo_lance_seja_do_mesmo_usuario(self):
        lance_do_gui200 = Lance(self.gui, 200)

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_do_gui)
            self.leilao.propoe(lance_do_gui200)
