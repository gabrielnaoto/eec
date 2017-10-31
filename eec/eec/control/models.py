import math
from django.db import models

# Create your models here.

class FluxoCaixa(object):

    def get_valor_futuro(self, *args, **kwargs):
        pmt = kwargs['pmt']
        i = kwargs['i'] / 100
        n = kwargs['n']
        return pmt * (math.pow((1 + i), n) - 1)

    def get_valor_principal(self, *args, **kwargs):
        pass

    def get_pagamento(self, *args, **kwargs):
        pass

    def get_quantidade_parcelas(self, *args, **kwargs):
        pass

    def get_taxa_juros(self, *args, **kwargs):
        pass
