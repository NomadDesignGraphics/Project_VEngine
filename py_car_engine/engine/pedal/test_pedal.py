import sys
sys.path.append('../gazolin/')
sys.path.append('../gazpompasi/')
import pedal
from gazolin import GazPorsiyon, gazolin
from gazpompasi import GazPompalama

class Benzin(gazolin):
    pass

class DenemePedal:
    def deneme_gaz_pompasi(self) -> None:
        gaz_tanki = GazPorsiyon(
            gazolin=Benzin(
                oktan=95,
            ),
            litre_oran = 10,
        )
        gaz_pompasi = GazPompalama(
            baglanan_gaz_pompasi=gaz_tanki,
            baglanan_motor = None,
            m_goreceli_lgk=0.2,
        )
        pedal = Pedal(
            baglanan_gaz_pompasi=gaz_pompasi,
        )
        cikan_gaz = pedal.gazabas(
            ne_kadar_sert=0.5,
            saniye=5,
        )
        assert cikan_gaz.litre_oran==0.5

        cikan_gaz = pedal.gazabas(
            ne_kadar_sert=1,
            saniye=10,
        )
        assert cikan_gaz.litre_oran==2
