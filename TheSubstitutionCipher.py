# The Substitution Cipher - Değiştirme şifrelemesi 

# dersteki metin/şifreli :=> thisciphertextcannotbedecrypted MGZVYZLGHCMHJMYXSSFMNHAHYCDLMHA

# Bu algoritmada alfabedeki harflerin yerini karıştırarak yeni bir karakter seti oluşturuyoruz 
# 'a' harfi yerine yeni karakter setinin ilk elemanı geliyor , bu mantıkla alfabedeki her harfe bir karşılık buluyoruz 
# Dersteki örnekleri yapabilmek adına derste kullanılan karakter setini kullandım 

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

def encode(message):
	tut = "" 
	for i in range(len(message)):
		for k in range(len(alphabet0)):
			if(message[i] == alphabet0[k]):
				tut += alphabet1[k]
	print("Şifrelendi : " , tut.upper())
	return tut.upper()

def decode(message):
	message = message.lower()
	tut = ""
	for i in range(len(message)):
		for k in range(len(alphabet1)):
			if(message[i] == alphabet1[k]):
				tut += alphabet0[k]
	print("Orijinali  : " , tut)
	return tut 

alphabet0 = "abcdefghijklmnopqrstuvwxyz" 
alphabet1 = "xnyahpogzqwbtsflrcvmuekjdi" # şifrelemede kullanılacak karakter seti 
word = ""

while True:

	print("Program türkçe karakter desteklememektedir !")
	msg = input("Şifrelemek istediğiniz metni girin : ")
	msg = msg.lower() # karakterleri küçük harf yapar
	msg = clearSpace(msg) 
	if(checkMsg(msg)):
		word = msg
		break

word = encode(word)
word = decode(word)

