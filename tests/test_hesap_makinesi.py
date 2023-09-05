import  pytest

def toplama(a,b):
    return a+b

def cıkarma(a,b):
    return a-b


def bolme(a,b):
    return a/b

def carpma(a,b):
    return a*b

def test_toplama(): # python bunu test algılar çünkü test yazısı var üstekileri algılamaz
    assert 4 == toplama(2,2)

def test_cıkarma():
    assert 2 == cıkarma(5,3)

@pytest.mark.smoke # smoke biz uydurduk istediğimizi diğebiliriz
@pytest.mark.islem
def test_bolme():
    assert 2 == bolme(10,5)

def test_carpma():
    assert carpma(3,3) == 9
