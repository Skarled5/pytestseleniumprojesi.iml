import pytest
import softest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import Anasayfa
import UrunDetaySayfasi

class TestHomepage(softest.TestCase):

    def class_setup(self):
        self.anasayfa = Anasayfa(self.driver)

    @pytest.mark.smoke
    def test_ust_menu_linklerini_dogrula(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://www.trendyol.com/")

        expected_menu = ["Grocery","Mobiles","Fashion","Electronics","Home And Furmite","Appliances","Travel"
                         ,"Beaty","Two"]

        elements = self.driver.find_elements("")

        actual_menu_items = []

        for i in elements:
            actual_menu_items.append(i.text)
        for i in range(len(expected_menu)):
            assert  expected_menu[i] == actual_menu_items[i]

        driver.quit()

    @pytest.mark.smoke
    def test_urun_ismine_tiklayinca_urun_detaylari_sayfasi_acilir_isim_kontrolu(self):
        self.driver.get("")
        anasayfa = Anasayfa(self.driver)
        urun_detay_sayfasi =  UrunDetaySayfasi(self.driver)
        urun_ismi = self.anasayfa.ilk_urun_ismini_ver()
        print("Anasayfa ürün ismi ",urun_ismi)
        anasayfa.ilk_urun_ismine_tikla()
        urun_ismi_detay_sayfasi = urun_detay_sayfasi.urun_ismini_ver()
        assert urun_ismi == urun_ismi_detay_sayfasi

    # bir assert ifadesi başarısız olsa bile, geri kalan assert ifadeleri yine de çalışır

    @pytest.mark.smoke
    def test_urun_fiyatina_tiklayinca_urun_detaylari_sayfasi_acilir_fiyat_kotrolu(self):
        self.driver.get("")
        anasayfa = Anasayfa(self.driver)
        urun_detay_sayfasi = UrunDetaySayfasi(self.driver)
        urun_fiyati = anasayfa.ilk_urun_fiyatini_ver()
        print("Anasayfa ürün fiyatı ",urun_fiyati)
        anasayfa.ilk_urun_fiyatina_tikla()
        urun_fiyat_detay_sayfasi = urun_detay_sayfasi.urun_fiyatini_ver()
        assert urun_fiyati == urun_fiyat_detay_sayfasi









