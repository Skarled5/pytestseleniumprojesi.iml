from pages.arama_sayfasi import AramaSayfasi


class TestArama():

    def test_arama_uyarisi_iki_harfli(self):
        self.driver.get("https://demowebshop.tricentis.com/")
        arama = AramaSayfasi(self.driver) # miras alma (inheritance)
        arama.arama_yap("ab")
        mesaj = arama.arama_uyari_mesajini_ver()
        assert mesaj == "Search term minimum length is 3 characters"
        assert mesaj == "No products were found that matched your criteria."

    def test_arama_uyarisi_ilgili_sonuc_cıkmayinca(self):
        self.driver.get("https://demowebshop.tricentis.com/")
        arama = AramaSayfasi(self.driver)
        arama.arama_yap("xyz")
        mesaj = arama.arama_uyari_mesajini_ver()
        assert mesaj == "No products were found that matched your criteria."



    # arama = AramaSayfasi(self.driver) gibi), TestArama sınıfı ve AramaSayfasi sınıfı arasında bir ilişki kurulur. Bu ilişki sayesinde TestArama sınıfı, AramaSayfasi sınıfının özelliklerine ve metotlarına erişebilir.
    # Yani, TestArama sınıfı AramaSayfasi sınıfını kullanarak belirli test senaryolarını test edebilir ve AramaSayfasi sınıfının metotlarını çağırabilir. Bu ilişki, miras alma ile değil,
    # TestArama sınıfının AramaSayfasi sınıfını kullanarak bir nesne oluşturmasıyla gerçekleşir. Bu nesne aracılığıyla AramaSayfasi sınıfının özelliklerine ve metotlarına erişebilirsiniz.




















