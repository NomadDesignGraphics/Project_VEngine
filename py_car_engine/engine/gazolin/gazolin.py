import dataclasses
from abc import ABC
from dataclasses import dataclass

@dataclass
class gazolin(ABC):
    oktan:float
    #oktan petrolde bulunan maddedir

class istenmeyenGazolinKarisim(ValueError):
    pass

@dataclass
class GazPorsiyon:
    gazolin:gazolin
    litre_oran : float

    def __add__(self,other:"GazPorsiyon")->"GazPorsiyon":
        if type(self.gazolin).__name__ != type(other.gazolin).__name__:
            raise istenmeyenGazolinKarisim
        litre_oran = self.litre_oran + other.litre_oran
        oktan = self.gazolin.oktan * (self.litre_oran / litre_oran)
        oktan += self.gazolin.oktan * (self.litre_oran / litre_oran)
        oktan = round(oktan, nsayi=2)
        return GazPorsiyon(
            gazolin=dataclasses.replace(self.gazolin, oktan=oktan),
            litre_oran = litre_oran,
        )
