# Vigenere şifreleme 

# dersteki metin/şifreli :=> thiscryptosystemisnotsecure VPXZGIAXIVWPUBTTMJPWIZITWZT

# Bu algotirmada string bir anahtar kullanılır , şifreleyeceğimiz metni anahatar uzunluğunda kümelere ayırırız 
# metni ve anahtarı numerik olarak yazar ve bunları toplarız , çıkan sayı 26 dan büyükse modu alınır , küçükse direkt alınır
# elde edilen sayılara karşılık gelen karakterler birleştirilerek şifreleme tamamlanır 

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

def encode(message , anahtar):
	letterNumber = [] # her harfe karşılık gelen sayıyı burada tut
	keyNumber = []    # anahtardaki harflere karşılık gelen sayıları burda tut 
	hash0 = "" 		  # metnin şifrelenmiş hali
	tutSayi = 0
	for i in range(len(message)):
		for k in range(len(alphabet0)):
			if(message[i] == alphabet0[k]):
				letterNumber.append(k)

	for i in range(len(anahtar)):
		for k in range(len(alphabet0)):
			if(anahtar[i] == alphabet0[k]):
				keyNumber.append(k)

	for i in letterNumber:
		if(tutSayi == len(anahtar)):
			tutSayi = 0
		tut = i+keyNumber[tutSayi]
		tut = tut%26
		hash0 += alphabet0[tut]
		tutSayi += 1

	print("Şifrelendi : " ,hash0.upper())
	return hash0
 

def decode(message , anahtar):
	letterNumber = [] # her harfe karşılık gelen sayıyı burada tut
	keyNumber = []    # anahtardaki harflere karşılık gelen sayıları burda tut 
	msg = "" 		  # metnin orijinal hali
	tutSayi = 0

	for i in range(len(message)):
		for k in range(len(alphabet0)):
			if(message[i] == alphabet0[k]):
				letterNumber.append(k)

	for i in range(len(anahtar)):
		for k in range(len(alphabet0)):
			if(anahtar[i] == alphabet0[k]):
				keyNumber.append(k)

	for i in letterNumber:
		if(tutSayi == len(anahtar)):
			tutSayi = 0

		tut = i - keyNumber[tutSayi]
		if (tut < 0):
			tut = tut+26
		tut = tut%26
		msg += alphabet0[tut]
		tutSayi += 1
	print("Orijinali  : " , msg)




alphabet0 = "abcdefghijklmnopqrstuvwxyz" 
word = ""
key0 = ""

while True:

	print("Program türkçe karakter desteklememektedir !")
	msg = input("Şifrelemek istediğiniz metni girin : ")
	msg = msg.lower() # karakterleri küçük harf yapar
	msg = clearSpace(msg) 
	if(checkMsg(msg)):
		word = msg
		break

while True:
	msg = input("Şifreleme anahtarını girin (String) : ")
	msg = msg.lower()
	msg = clearSpace(msg)
	if(checkMsg(msg)):
		key0= msg
		break

word = encode(word , key0)
decode(word , key0)


