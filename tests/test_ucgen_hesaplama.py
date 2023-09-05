import  pytest
import sys
def cevre_hesaplama(a,b,c):
    return a+b+c

@pytest.mark.skipif(sys.version_info < (3, 6), reason="Python sürümü 3.6'dan düşük") # skipif koşul gerçekleşirse alttaki testi çalıştırmaz
def alan_hesaplama(taban,yukseklik):
    return (taban*yukseklik)/2

@pytest.mark.xfail # bir testin bilerek başarısız olmasını beklediğimiz durumları işaretlemek
def test_ucgen_cevresi_hesaplama():
    assert cevre_hesaplama(2,3,3) == 9

@pytest.mark.skip(reason = "form css değişti")  # alttaki testin çalıştırılmasını durdurur
def test_ucgen_alan_hesaplam():
    assert alan_hesaplama(4,3) == 6

