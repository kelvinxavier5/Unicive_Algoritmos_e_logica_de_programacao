from calculadora import *
import pytest 

def test_somar_valores_10_e_20():
    assert somar(10, 20) == 35
    
def test_subtrair_valores_negativos():
    assert subtrair(-1, -1) == 0
    
def test_cumprimentar_aluno_com_boas_vindas():
    assert dar_boas_vindas_ao_aluno("kelvin") \
            == "Olá, kelvin!"
            
def test_dividir_valor_por_zero():
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)