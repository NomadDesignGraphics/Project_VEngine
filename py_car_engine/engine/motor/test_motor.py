import pytest
import motor
import sys
sys.path.append('../gazolin/')
from gazolin import *
class Benzin(gazolin):
    pass

class DenemeMotor:
    def deneme_motor(self) -> None:
        benzin100 = Benzin(oktan=100)
        motor = Motor(
            gazolin=benzin100,
            m_dby = 1000*60,
            m_tasan_hiz_lgk=1,
        )
        motor.tedarik(
            gaz_porsiyon = GazPorsiyon(
                gazolin=benzin100,
                litre_oran=1,
            ),
            saniye = 1,
        )
        assert motor.rotasyon ==1000

    def test_normal_motor(self) -> None:
        benzin95 = Benzin(octan=95)
        motor = Motor.normal_benzinli_motor_sagla()
        assert isinstance(motor, Motor)
        rotasyon = motor.tedarik(
            gaz_porsiyon = GazPorsiyon(
                gazolin=benzin95,
                litre_oran=1,
            ),
            saniye=5,
        )
        assert rotasyon == 416.67

        rotasyon = motor.tedarik(
            gaz_porsiyon=GazPorsiyon(
                gazolin = benzin95,
                litre_oran=2,
            ),
            saniye = 5,
        )
        assert rotasyon ==416.67

        rotasyon = motor.tedarik(
            gaz_porsiyon=GazPorsiyon(
                gazolin=benzin95,
                litre_oran=2,
            ),
            saniye =60,
        ),
        assert rotasyon == 833.33
