#!/usr/bin/env python
# coding: utf-8

# In[2]:


a = 2

if (a == 2):
    print(a)
print("Hello, World!")


# In[27]:


işlem = int(input("Bir İşlem Numarası Giriniz: "))

if (işlem == 1):
    print("1. İşlem Seçildi")
elif (işlem == 2):
    print("2. İşlem Seçildi")
elif (işlem == 3):
    print("3. İşlem Seçildi")
else :
    print("Yanlış İşlem Girildi")


# In[21]:


sayı1 = int(input("Bir İşlem Numarası Giriniz: "))
sayı2 = int(input("Bir İşlem Numarası Giriniz: "))
sayı3 = int(input("Bir İşlem Numarası Giriniz: "))

if (sayı1 > sayı2 and sayı1>sayı3):
    print("Sayı 1 en Büyüktür")
elif(sayı2 > sayı3 and sayı2 > sayı1):
    print("Sayı2, en büyük")
elif(sayı3> sayı1 and sayı3 > sayı2): 
    print("Sayı 3 en büyüktür")
else:
    print("Bir sayı değeri girin!")
          


# In[26]:


kilo = int(input("Kilo Giriniz: "))
boy = float(input("Boy Giriniz: "))

bki = kilo/(boy*boy)
print (bki)

if (bki<18.5):
    print("Zayıftır")
elif(18.5<=bki<25):
    print("Normal")
elif(25<=bki<30):
    print("Fazla kilolu")
elif(30<=bki):
    print("Yemişte yemiş Obez!")
else:
    print("Değer bulunamadı")
    

