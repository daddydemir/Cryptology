# Affine Şifre çözme 

![WhatsApp Image 2021-03-20 at 14 20 57](https://user-images.githubusercontent.com/42716195/111867815-8f23a400-8987-11eb-93f2-42dd789afc07.jpeg)

---
Burada kullanılan fonsksiyon (7x+3)mod(26)' dır . Bunun tersini alma işlemini kolaylaştırmak için karakter setindeki herhangi bir karaktere denkgelen bir sayıyı alalım 
ben 23 (X)' ü aldım . <br>
* (7x+3)mod(26) = 23 şeklinde bir denklen elde ederiz . 
* Burada ilk düşünmemiz gereken `hangi sayının modu 23 yapar` : { 23 , 49 , 75 , 101 , ... }
* işlemden de farkedildiği üzre bir den çok sayının 26 ile modu 23 yapabiliyor 
* Fakat bunlar tam sayı değiller bizim aradığımız tam sayı olmalı 
* 26 ile modu 23 yapan sayılara baktığımızda bir örüntü farkederiz 
* ilk elemandan sonraki elemanlara 26 eklenerek gidiyor : { 23 , 23+26 , 23 +2(26) , 23+3(26) , ... }
* geriye sadece tam sayı elde ettiğimiz değeri bulmak kalıyor 
