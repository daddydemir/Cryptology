# The Shift Cipher - Kaydırma şifrelemesi 

# dersteki metin/şifreli :=> wewillmeetatmidnight HPHTWWXPPELEXTOYTRSE

# Bu algoritma alfabedeki her harfe 0 dan başlayarak bir sayı ataması yapar 
# elde edilen her sayıyı anahtar değeriyle toplar , çıkan sonucun 26 ile modunu alır 
# son olarak oluşan sayıya karşılık gelen harleri birleştirir ve şifreleme bitti , 

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

def encode(message , key0):
	letterNumber = [] # her harfe karşılık gelen sayıyı burada tut
	hash0 = "" # metnin şifrelenmiş hali 
	for i in range(len(message)):
		for k in range(len(alphabet0)):
			if( message[i] == alphabet0[k] ):
				letterNumber.append(k)

	for i in letterNumber:
		sayi = i+key0 # her harfe karşılık gelen sayıya anahtar değerini ekle 
		sayi = sayi%26 # çıkan sayının 26 ya göre modunu al 
		hash0 += alphabet0[sayi] # elde eilen sayıya karşılık gelen harfi ekle 
	print("Şifrelendi : " ,hash0.upper()) # upper() karakterleri büyük yapar
	return hash0

def decode(message="HPHTWWXPPELEXTOYTRSE" , key0=11): # paramtre vermeden çağırdığında bu metin ve 11 sayısı üzerinden işlem yapar
	message = message.lower()
	letterNumber = []
	msg = "" # metnin orijinal hali
	for i in range(len(message)):
		for k in range(len(alphabet0)):
			if( message[i] == alphabet0[k]):
				letterNumber.append(k) # her harfe karşılık gelen sayıyı listeye ekle

	for i in letterNumber:
		sayi = i-key0
		if (sayi < 0):
			sayi = 26+sayi
		sayi = sayi%26
		msg += alphabet0[sayi]
	print("Orijinali  : " , msg)
	

alphabet0 = "abcdefghijklmnopqrstuvwxyz"
word = ""
key  = 0
while True:

	print("Program türkçe karakter desteklememektedir !")
	msg = input("Şifrelemek istediğiniz metni girin : ")
	msg = msg.lower() # karakterleri küçük harf yapar
	msg = clearSpace(msg) 
	if(checkMsg(msg)):
		word = msg
		break
while True:
	a = int(input("Kodlama anahtarını belirleyin [1,25] : ")) # 0 ve 26 kullanılırsa herhangi bir değişiklik olmaz 
	if(a >= 1 and a <= 25):
		key = a
		break
	else:
		print("[1,25] aralığında olmalı !")

sifreliMetin = encode(word , key)
decode(sifreliMetin , key)
