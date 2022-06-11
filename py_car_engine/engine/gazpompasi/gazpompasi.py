import dataclasses
from dataclasses import dataclass
from typing import Optional
import sys
sys.path.append('../motor/')
sys.path.append('../gazolin/')
from motor import Motor
from gazolin import GazPorsiyon

class NegatifVoltaj(ValueError):
    pass

class CokYuksekVoltaj(ValueError):
    pass

@dataclass

class GazPompalama:
    baglanan_gaz_tanki:GazPorsiyon
    baglanan_motor: Optional[Motor]
    #lgk = limitli güç kaynağı
    #m = maximum
    m_goreceli_lgk: float

    def apply(
        self,
        voltaj:float,
        saniye:float,
    )-> GazPorsiyon:
        if voltaj < 0:
            raise NegatifVoltaj

        elif voltaj > 14:
            raise CokYuksekVoltaj

        goreceli_lgk = self.m_goreceli_lgk * voltaj /12
        oran = round(min(self.baglanan_gaz_tanki.litre_oran,
                goreceli_lgk * saniye),
                nsayi=2
                )
        self.baglanan_gaz_tanki.litre_oran -= oran
        gaz_porsiyon = dataclasses.replace(
            self.baglanan_gaz_tanki,
            litre_oran=oran
        )

        if self.baglanan_motor is not None:
            self.baglanan_motor.tedarik(
                gaz_porsiyon=gaz_porsiyon,
                saniye=saniye,
            )
        return gaz_porsiyon
