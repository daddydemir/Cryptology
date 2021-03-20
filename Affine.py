# Affine - Doğrusal şifreleme

# dersteki metin/şifreli :=> hot AXG

# Bu algoritmada 2 tane anahta kullanılır ve birinci anahtarla karakter setindeki eleman sayısı aralrında asal olmalıdır . 
# Başka bir deyişle EBOB(a,n) = 1 | n : karakter setindeki eleman sayısı 
# denklem ax + b şeklindedir . Anahtarlar belirlendikten sonra şifrelenecek metnin sayısal kaşılıkları elde edilir ve x yerine yazılır 
# ax + b işelminin ardından çıkan sonucun 26 ya göre modu alınır , bu her karakter için tekrarlanır ve sayıya karşılık gelen karakter yazılır 

def clearSpace(message): # metindeki boşlukları temizler 
	d = ""
	for i in range(len(message)):
		if(message[i] != " "):
			d += message[i] 
	return d

def checkMsg(message): # karakter setimizde tanımlı olmayan karakterlrin kontrolü
	sayac = 0
	for i in range(len(message)):
		for k in range(len(alphabet0)):
			if(message[i] == alphabet0[k]):
				sayac += 1

	if( sayac == len(message)):
		print("Girilen metin uygundur .")
		return True
	else:
		print("Bu metin şifrelenemez .")
		return False

def checkKey(anahtar): # Birici anahtala 26 nın asallığının konrolü
	bolen1 = [] # anahtarın tam bölenlerini burda tut
	bolen2 = [] # karakter setinin tam bölenlerini burda tut
	ret = True  
	for i in range(2,anahtar+1): # anahtar değerine 1 ekleme sebebim range() fonksiyonun 1 eksiğini almasından kaynaklı 
		deger = anahtar % i
		if(deger == 0):
			bolen1.append(i)
	for i in range(2, len(alphabet0)+1):
		deger = len(alphabet0) % i
		if (deger == 0):
			bolen2.append(i)
	for i in bolen1:
		for k in bolen2:
			if(i == k): # ortak bölenleri varsa 
				ret = False
				break

	return ret

def encode(message , a1 ,a2):
	letterNumber = [] # her harfe karşılık gelen sayıyı burada tut
	hash0 = "" # metnin şifrelenmiş hali

	for i in range(len(message)):
		for k in range(len(alphabet0)):
			if( message[i] == alphabet0[k] ):
				letterNumber.append(k)

	for i in letterNumber: # ( ax + b ) mod26
		deger = ((a1*i) + a2 )%26
		hash0 += alphabet0[deger]
	print("Şifrelendi : " ,hash0.upper())
	return hash0

def decode(message , a1 , a2):
	letterNumber = [] 
	msg = "" # metnin orijinal hali

	for i in range(len(message)):
		for k in range(len(alphabet0)):
			if( message[i] == alphabet0[k]):
				letterNumber.append(k) # her harfe karşılık gelen sayıyı listeye ekle

	for i in letterNumber:
		sayi = (i-a2)/a1  # işlemleri tersten yapıyor . bu kısmı anlamadıysanız affine.md ye bakabilirsiniz . 
		if(sayi != int(sayi)): # tam sayı olup olmadığını kontol ediyor
			while(True):
				i = i+26
				sayi = (i-a2)/a1
				if(sayi == int(sayi)):
					sayi = int(sayi)
					sayi = sayi%26
					msg += alphabet0[sayi]
					break
		else:
			sayi = int(sayi)
			sayi = sayi%26
			msg += alphabet0[sayi]
	print("Orijinali  : " , msg)

alphabet0 = "abcdefghijklmnopqrstuvwxyz" 
word = ""
key0 = 0; key1 = 0
while True:

	print("Program türkçe karakter desteklememektedir !")
	msg = input("Şifrelemek istediğiniz metni girin : ")
	msg = msg.lower() # karakterleri küçük harf yapar
	msg = clearSpace(msg) 
	if(checkMsg(msg)):
		word = msg
		break

while True:
	key0 = int(input("Birinci şifreleme anahtarını [1-25] giriniz : ")) # karakter setinin uzunluğu ile aralarında asal olmalı 
	if( key0 < 1 or key0 > 25):
		print("Birinci şifreleme anahtarı [1-25] aralığında olmalıdır .")
		continue
	if(checkKey(key0)):
		print("girilen değer uygundur")
	else:
		print("26 ile aralarında asal olmalıdır .")
		continue
	key1 = int(input("İkinci şifreleme anahtarını [1,25] giriniz : ")) # mod26 ya göre işlem yaptığımız için 1-25 aralığını kullandık
	if( key1 >= 1 and key1 <= 25):
		break
	else:
		print("İkinci şifreleme anahtarı [1-25] aralığında olmalıdır .")
 
word = encode(word , key0 , key1)

decode(word , key0 , key1)
