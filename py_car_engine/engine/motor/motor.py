import sys
sys.path.append('../gazolin/')
from gazolin import *

class Motor:
    def __init__(
        self,
        gazolin: gazolin,
        #lgk = limitli güç kaynağı
        #m = maksimum
        #mm = minimum
        m_tasan_hiz_lgk: float = 0.2,
        #dby = dakikada bir yenileme
        #sby = saniyede bir yenileme
        m_dby : float=5000,
    ):
        self.m_tasan_hiz_lgk = m_tasan_hiz_lgk
        self.m_dby =m_dby
        self.gazolin = gazolin
        self.toplamda_alinan_gaz = GazPorsiyon(
            gazolin=gazolin,
            litre_oran=0,
        )
        self.rotasyon: float =0

    @classmethod
    def normal_benzinli_motor_sagla(cls):
        class Benzin(gazolin):
            pass

        benzin95 = Benzin(oktan=95)
        return cls(
            gazolin=benzin95,
        )

    @classmethod
    def normal_dizel_motor_sagla(cls):
        class Dizel(gazolin):
            pass

        dizel170 = Dizel(oktan=95)
        return cls(
            gazolin=dizel170,
        )
    def tedarik(
        self,
        gaz_porsiyon : GazPorsiyon,
        saniye: float,
        ):
            self.motor_sesi = 5

            if gaz_porsiyon.litre_oran <= 0 or saniye <= 0:
                return

            self.toplamda_alinan_gaz += gaz_porsiyon
            tasan_hiz = min(
                gaz_porsiyon.litre_oran / saniye,
                self.m_tasan_hiz_lgk
            )
            goreceli_akis_hizi = tasan_hiz / self.m_tasan_hiz_lgk
            goreceli_oktan = gaz_porsiyon.gazolin.oktan / self.gazolin.oktan
            dby= self.m_dby * goreceli_akis_hizi * goreceli_oktan

            sby = dby / 60

            rotasyon = round(dby * saniye, nsayi=2)
            self.rotasyon += rotasyon
            return rotasyon
