from dataclasses import dataclass
from typing import Optional
from unittest.case import TestCase

from app.structs import ColunaXLSXConfig
from app.xlsx import obter_valores_da_coluna


@dataclass
class ValorColunaFake:
    value: Optional[str]


class ObterValoresDaColunaTests(TestCase):
    def test_retorna_valores_da_coluna_da_pagina(self):
        pagina = {
            'A1': ValorColunaFake(None),
            'A2': ValorColunaFake('a'),
            'A3': ValorColunaFake('b'),
            'A4': ValorColunaFake(None)
        }
        coluna_config = ColunaXLSXConfig(coluna='A', linhas=[2, 3])

        valores = obter_valores_da_coluna(pagina, coluna_config)

        self.assertEqual(2, len(valores))
        self.assertEqual('a', valores[0])
        self.assertEqual('b', valores[1])
