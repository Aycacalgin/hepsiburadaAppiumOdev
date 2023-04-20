hepsiburada  ---AYÇA ÇALGIN
=====================

hepsiburada uye olma
-------------------------
* hepsiburada  uygulamasi acilir,uygulamanin acildigi kontrol edilir
* "uyeolmayadaoturumacmaıkonu" xpath'li elemente tikla
* "2" saniye bekle
* "uyeolbtn" xpath'li elemente tikla
* "2" saniye sayfanın yüklenmesini bekle
* Eposta alanına "ayca.calgin@testinium.com" bilgisini gir
* "dogrulamaMailiText" xpath'li element gorunur olana kadar bekle

  Basarılı giris yapma
----------------------
*"girisyapbtn" xpath'li elemente tikla
*"txtUserName" id'li elemente <ayca.calgin@testinium.com> text degerini gonder
*"devametbtn" id'li elemente tikla

Anasayfada bulunan markadan urun aratma
----
* "marksSpencer" id'li elemente tikla
* marks&spencer   urunlerine   <dericeket> degerini gonderme

-----Favorilere ekleme
-------------
 * "favorıeklemebtn" xpath'li elemente tikla
 * "favorıeklemebtn "xpath'li element gorunur olana kadar bekle


--Sepete ekleme
-----------
 *"sepeteeklemebtn" xpath'li elemente tiklanır
 *"sepeteeklemebtn" xpath'li element kayıp olana kadar bekle


 -----Sepet ekleme onaylanması ve kontrolu
-----------
*"sepeteeklemebtn2" id'li elemente tiklanır
*"sepeteeklemekontrol" li elementin oldugu kontrol edilir

------Odeme sayfasına gitme
---------------
*"alısverisitamamlabtn" id'li elemente tiklanır
*string listenin iki elementinin esit oldugunu kontrol et


