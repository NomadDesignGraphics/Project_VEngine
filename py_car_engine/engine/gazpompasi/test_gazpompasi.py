import sys
sys.path.append('../gazolin/')

from gazolin import GazPorsiyon,gazolin
from gazpompasi import GazPompalama

class Benzin(gazolin):
    pass

class DenemeGazPompalama:
    def deneme_gaz_pompalama(self) -> None:
        gaz_tanki = GazPorsiyon(
            gazolin = Benzin(
                oktan=95,
            ),
            litre_oran=10,
        )
        gaz_pompasi = GazPompalama(
            baglanan_gaz_tanki = gaz_tanki,
            baglanan_motor = None,
            m_goreceli_lgk=0.2,
        )
        DisaVerim_gaz = gaz_pompasi.apply(
            voltaj =6,
            saniye=5,
        )

        assert DisaVerim_gaz.litre_oran == 0.5
