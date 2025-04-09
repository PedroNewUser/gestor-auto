import unittest
from src.app import soma, eh_par, fatorial_numero, cadastro_usuario

class TestApp(unittest.TestCase):
        
    def test_soma_positivos(self):
        result = soma(2,5)
        self.assertEqual(result,7)
        
    def test_soma_negativos(self):
        result = soma(-5,-5)
        self.assertEqual(result, -10)
        
    def test_soma_zeros(self):
        result = soma(-5, 5) 
        self.assertEqual(result, 0)
        
    def test_eh_par_true(self):
        result = eh_par(2)
        self.assertEqual(result, True)
        
    def test_eh_par_impar(self):
        result = eh_par(3)
        self.assertEqual(result, False)
        
    def test_fatorial_numero(self):
        result = fatorial_numero(5)
        self.assertEqual(result, 120)
        
    def test_cadastro_usuario_sucesso(self):
        result = cadastro_usuario("Tiago", "tiaguinho123@gmail.com")
        self.assertEqual(result, "Sucesso")
        
    def test_cadastro_usuario_falha(self):
        cadastro_usuario("Tiago", "pedro@gmail.com")
        result = cadastro_usuario("Tiago", "pedro@gmail.com")
        self.assertEqual(result, "Email já existe")
        
if __name__ == '__main__':
    unittest.main        