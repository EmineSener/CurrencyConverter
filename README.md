# Döviz Çevirici

Döviz Çevirici uygulaması Türk Lirası , Dolar ve Euro arasında dönüşüm yapan bir uygulamadır. 

Uygulama Python ile geliştirilmiştir ve Python'un Tkinter paketi aracılığıyla uygulamanın arayüzü tasarlanmıştır. 

Uygulamada henüz mevcut olmayan resimlerle arayüz güçlendirilebilir.

Uygulama kur değerlerini sabit almaktadır,kur değerleri anlık olarak güncellenebilir.



## Kurulum

* Programın kurulumuna başlamadan önce programda gerekli Python kütüphanelerinin yerel bilgisayarınızda yüklü olduğundan emin olmalısınız. Ardından aşağıdaki adımları takip etmelisiniz.


1.Deponun sağ üst kısmında `Code`  yazan yeşil butona tıkladıktan sonra `ZIP İndir` sekmesine tıklayıp yerel bilgisayara proje kaynak kodları indirilir.

2.Kaynak kod `Thonny` IDE'si aracılığıyla çalıştırılır. 



## Kullanım

Program çalıştırıldığında karşınıza ilk olarak aşağıda görüldüğü gibi bilgilendirme ekranı çıkacaktır.

Bilgilendirmeyi okuduğunuzda `Back` butonuna tıklayarak bir sonraki aşamaya geçebilirsiniz.

![alt text](https://github.com/EmineSener/CurrencyConverter/blob/main/images/window1.png)



Bir sonraki aşamada karşınıza çıkacak ekran aracılığıyla hangi para birimini dönüştürmek istediğinizi seçebilirsiniz.

Seçiminizi tamamladıktan sonra `Next` butonuyla diğer aşamaya geçilir. 

Program yönergesini tekrar okumak istediğiniz takdirde `Back` butonu ile bilgilendirme ekranına geri dönebilirsiniz.

![alt text](https://github.com/EmineSener/CurrencyConverter/blob/main/images/window2.png)



3.aşamada dönüştürmek istediğiniz miktarı girmeniz ardından da onu kaydetmeniz gerekiyor.

Yine `Back` ve  `Next` butonlarıyla ekranlar arası geçiş yapabilirsiniz.

`Back` butonuyla seçtiğiniz para birimini değiştirebilirsiniz.

![alt text](https://github.com/EmineSener/CurrencyConverter/blob/main/images/window3.png)



4.aşamada ise dönüştürülmek istenilen para birimi seçilir.

![alt text](https://github.com/EmineSener/CurrencyConverter/blob/main/images/window4%20-%20Kopya.png)



Son aşamada ise sonuç kullanıcıya bildirilir.

![alt text](https://github.com/EmineSener/CurrencyConverter/blob/main/images/window5.png)




##### Back ve Next Butonları

`Next` butonu sayesinde seçimlerinizi ve girdilerinizi sabitleyip bir sonraki aşamaya geçebilirsiniz.

`Next` butonuna son defa basılmasıyla sonuca ulaşılır.

`Back` butonuyla seçimlerinizi ve miktar girdinizi değiştirebilirsiniz.

Bu özellikle eldeki para her üç birime de tek seferde dönüştürülebilir.



## Proje Detayı

Programda kullanıcı kaynaklı hatalar mesaj kutuları aracılığıyla kullanıcıya bilgilendirilerek engellenmiştir.

Eğer kullanıcı hesaplatmak istediği miktarı rakam harici değer ile girerse program takip eden uyarı mesajını verecektir.

![alt text](https://github.com/EmineSener/CurrencyConverter/blob/main/images_warn/warn1.png)



Kullanıcı hangi para birimini dönüştürmek istediğini ve hangi para birimine dönüştüreceğini aynı seçerse aşağıdaki uyarı mesajı verilecektir.

![alt text](https://github.com/EmineSener/CurrencyConverter/blob/main/images_warn/warn2.png)



Son olarak, kullanıcı her iki birimi de seçmeden hesaplama yapmak isterse takip eden uyarı mesajı verilip programın sonlanması önlenecektir.

![alt text](https://github.com/EmineSener/CurrencyConverter/blob/main/images_warn/warn3.png)
