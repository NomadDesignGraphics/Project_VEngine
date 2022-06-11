import pytest

from gazolin import (
    gazolin,
    GazPorsiyon,
    istenmeyenGazolinKarisim,
)

class Benzin(gazolin):
    pass

class Dizel(gazolin):
    pass

class DenemeBenzinYarat(object):
    def deneme_benzin_yarat(self) -> None:
        benzin = Benzin(oktan=95)
        dizel = Dizel(oktan=70)
        assert isinstance(benzin, gazolin)
        assert isinstance(benzin, benzin)
        assert isinstance(dizel, gazolin)
        assert isinstance(dizel, Dizel)

    def deneme_porsiyon_yarat(self) -> None:
        benzin95 =Benzin(oktan=95)
        benzin98 = Benzin(oktan=98)

        porsiyon1 = GazPorsiyon(
            gazolin = benzin95,
            litre_oran =2.5,
        )
        assert isinstance(porsiyon1, GazPorsiyon)

        porsiyon2 = GazPorsiyon(
            gazolin = benzin98,
            litre_oran =3.5,
        )
        assert isinstance(porsiyon1, GazPorsiyon)
        karisim = porsiyon1+porsiyon2

        assert karisim.gazolin.oktan == 96.75

        dizel = GazPorsiyon(
            gazolin = Dizel(oktan=70),
            litre_oran =100,
        )

        with pytest.raises(istenmeyenGazolinKarisim):
            porsiyon1+dizel

        with pytest.raises(istenmeyenGazolinKarisim):
            dizel+porsiyon1
