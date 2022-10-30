#!/usr/bin/env python
# coding: utf-8

# In[7]:


a = int(input("Bir Sayı Giriniz: "))
b = int(input("Bir Sayı Giriniz: "))
c = int(input("Bir Sayı Giriniz: "))
carpım = a*b*c
z = "İşlemin sonucu {}"
print(z.format(carpım))


# kilo = int(input("Kilo Giriniz: "))
# boy = int(input("Boy Giriniz: "))
# islem = (kilo/boy)**boy
# print(islem)

# In[10]:


kilo = int(input("Kilo Giriniz: "))
boy = float(input("Boy Giriniz: "))
islem = (kilo/boy)*boy
print(islem)


# In[21]:


benzinFİYAT = int(20)
benzinMİKTARI = int(input("Araçta bulunan benzin miktarını giriniz: "))
kaçKilometre = int(input("Gidilen Yolu kioletre cinsinden giriniz: "))
harcananBenzin = int(input("Harcanan Benzin Miktarı: "))

kBenzin = benzinMİKTARI - harcananBenzin
kHarcama = (kaçKilometre/harcananBenzin)*benzinFİYAT
kalanyolFiyat = kBenzin*benzinFİYAT

print(kBenzin, kHarcama, kalanyolFiyat)


# In[19]:


adSoyad = input("Ad Soyad giriniz: ")
telNo= int(input("Telefon Numarası Giriniz: "))
print(adSoyad,telNo,sep = "\n")


# In[24]:


x = int(input("bir sayı giriniz: "))
y = int(input("Bir sayı giriniz"))
işlem = "{}numaralı sayı ile {} sayı değişti"
    print(.format(1=y,0=x)


# In[26]:


uçgeninAkenarı = int(input("Uzun Kenar: "))
uçgeninBkenarı = int(input("Kısa Kenar: "))
hipo = uçgeninAkenarı^2+uçgeninBkenarı^2
sonuc = hipo^2
print(sonuc)


# In[ ]:




