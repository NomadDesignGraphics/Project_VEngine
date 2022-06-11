import sys
sys.path.append('../motor/')
sys.path.append('../pedal/')
sys.path.append('../gazolin/')
sys.path.append('../gazpompasi/')
from motor import Motor
from gazolin import gazolin
from gazpompasi import GazPompalama
from pedal import Pedal

class HerseyiTesteTabiTut:
    def Her_test_okeymi(self) -> None:
        icerikler= [
            'Benzin türü Gazolin oluştur',
            `95 ve 98'lik 2 farklı gaz tankı oluştur `,
            `98'lik Benzin le çalışan motor yarat `,
            `Gaz pompası yarat ve onu gaz tankıyla motor a bağla`,
            `pedal yarat ve pompaya bağla`,
            `Pedala bas ve rotasyonların arttığını gör`,
            `:return:`,]
        print("Motor Test Sistemi")
        for i in range(7):
            for icerik in icerikler:
                print("{0}.{1} \n".format(i,icerik))
        
