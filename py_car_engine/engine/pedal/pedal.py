import sys
sys.path.append('../gazolin/')
sys.path.append('../gazpompasi/')

from gazolin import GazPorsiyon
from gazpompasi import GazPompalama
from dataclasses import dataclass

class Pedal:
    baglanan_gaz_pompasi: GazPompalama

    def gazabas(
        self,
        ne_kadar_sert:float,
        saniye:float,
        )-> GazPorsiyon:
        if saniye < 0:
            raise ValueError("Negatif zaman dilimi kabul edilmiyor")

        ne_kadar_sert = max(0, ne_kadar_sert)
        ne_kadar_sert = min(1, ne_kadar_sert)
        return self.baglanan_gaz_pompasi.apply(
            voltaj=12*ne_kadar_sert,
            saniye=saniye,
        )
