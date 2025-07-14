# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 21:46:58 2025

@author: gzb
"""

# import streamlit as st

# st.title("Basit Streamlit Uygulaması")

# # Kullanıcıdan sayı al
# sayi = st.number_input("Bir sayı girin:", value=1, step=1)

# # Sayıyı ikiyle çarp
# sonuc = sayi * 2

# # Sonucu göster
# st.write(f"Girdiğiniz sayının iki katı: {sonuc}")

#########################################################

# import streamlit as st

# st.title("Merhaba, Streamlit!")
# st.write("Bu, ilk basit uygulaman.")

# isim = st.text_input("Adını yaz:")
# if isim:
#     st.write(f"Hoş geldin, {isim}!")

##########################################################

# import streamlit as st

# st.title("💧 Basit Su Ayak İzi Hesaplayıcı")

# # Girdi al
# st.header("Günlük Su Tüketiminiz")
# su_tuketimi = st.number_input("Günde kaç litre su harcıyorsunuz?", min_value=0.0, step=0.1)

# # Hesapla
# if st.button("Yıllık Su Ayak İzini Hesapla"):
#     yillik_su = su_tuketimi * 365
#     st.success(f"Yıllık su ayak izin: {yillik_su:.1f} litre 💧")
    
###############################################################

# app.py

# import streamlit as st

# st.set_page_config(page_title="Su Ayak İzi Hesaplayıcı", page_icon="💧", layout="centered")

# st.title("💧 Su Ayak İzi Hesaplayıcı")
# st.markdown("Bu uygulama yıllık su ayak izinizi tahmini olarak hesaplar.")

# # Kullanıcıdan veri girişi
# st.header("Alışkanlıklarınıza dair birkaç soru:")

# et_tuketimi = st.slider("Haftalık kırmızı et tüketiminiz (porsiyon)", 0, 14, 3)
# su_tuketimi = st.slider("Günlük içme suyu tüketiminiz (litre)", 0, 10, 2)
# dus_suresi = st.slider("Günlük duş süreniz (dakika)", 0, 30, 10)

# # Hesaplama
# if st.button("Su Ayak İzimi Hesapla"):
#     su_iz = (
#         et_tuketimi * 7000 * 52 +  # et: 1 porsiyon ≈ 7000 litre/yıl
#         su_tuketimi * 365 +       # içme suyu
#         dus_suresi * 9 * 365      # duş: 9 litre/dk
#     )
#     st.success(f"Yıllık su ayak izin: {su_iz:.0f} litre 💧")

####################################################################

# # app.py

# import streamlit as st

# st.set_page_config(page_title="Su Ayak İzi Hesaplayıcı", page_icon="💧", layout="centered")
# st.title("💧 Su Ayak İzi Hesaplayıcı")

# st.markdown("Aşağıdaki soruları yanıtlayarak yıllık su ayak izinizi öğrenin.")

# with st.form("su_formu"):
#     st.header("🍖 Beslenme")
#     et = st.number_input("Haftada kaç öğün et yiyorsunuz?", min_value=0, step=1)
#     sut = st.number_input("Günde kaç bardak süt/süt ürünü tüketiyorsunuz?", min_value=0, step=1)
#     sebze = st.number_input("Günde kaç porsiyon sebze/meyve tüketiyorsunuz?", min_value=0, step=1)

#     st.header("🚿 Kişisel Temizlik")
#     dus = st.number_input("Günde kaç dakika duş alıyorsunuz?", min_value=0, step=1)
#     camasir = st.number_input("Haftada kaç kez çamaşır yıkıyorsunuz?", min_value=0, step=1)

#     st.header("👕 Tüketim Alışkanlıkları")
#     kiyafet = st.number_input("Ayda kaç yeni kıyafet alıyorsunuz?", min_value=0, step=1)

#     st.header("🚗 Ulaşım")
#     araba_km = st.number_input("Haftalık ortalama kaç km araba kullanıyorsunuz?", min_value=0, step=1)

#     submit = st.form_submit_button("Hesapla")

# if submit:
#     # Su katsayıları (litre)
#     katsayi = {
#         "et": 1500,            # litre / öğün
#         "sut": 200,            # litre / bardak
#         "sebze": 50,           # litre / porsiyon
#         "dus": 9,              # litre / dakika
#         "camasir": 150,        # litre / yıkama
#         "kiyafet": 2500,       # litre / kıyafet
#         "araba": 0.3           # litre / km
#     }

#     # Yıllık hesaplama
#     et_yillik = et * 52 * katsayi["et"]
#     sut_yillik = sut * 365 * katsayi["sut"]
#     sebze_yillik = sebze * 365 * katsayi["sebze"]
#     dus_yillik = dus * 365 * katsayi["dus"]
#     camasir_yillik = camasir * 52 * katsayi["camasir"]
#     kiyafet_yillik = kiyafet * 12 * katsayi["kiyafet"]
#     araba_yillik = araba_km * 52 * katsayi["araba"]

#     toplam = sum([et_yillik, sut_yillik, sebze_yillik, dus_yillik, camasir_yillik, kiyafet_yillik, araba_yillik])

#     st.success(f"Toplam yıllık su ayak izin: {round(toplam):,} litre 💧")

#     # Detaylı sonuçlar
#     st.subheader("Kategori Bazlı Sonuçlar")
#     st.write(f"• Et tüketimi: {round(et_yillik):,} litre")
#     st.write(f"• Süt ürünleri: {round(sut_yillik):,} litre")
#     st.write(f"• Sebze/meyve: {round(sebze_yillik):,} litre")
#     st.write(f"• Duş: {round(dus_yillik):,} litre")
#     st.write(f"• Çamaşır: {round(camasir_yillik):,} litre")
#     st.write(f"• Kıyafet: {round(kiyafet_yillik):,} litre")
#     st.write(f"• Araba kullanımı: {round(araba_yillik):,} litre")

#################################################################################################

# import streamlit as st

# st.title("Su Ayak İzi Hesaplayıcı 💧")

# st.write("Günlük su tüketiminizi litre cinsinden giriniz:")

# gunluk_tuketim = st.number_input("Günlük su tüketimi (litre)", min_value=0.0, value=100.0)

# yillik_su_ayak_izi = gunluk_tuketim * 365

# st.write(f"Yıllık su ayak iziniz: {yillik_su_ayak_izi:,.0f} litre 💧")

#############################################################################################

# import streamlit as st

# st.title("Su Ayak İzi Hesaplayıcı")

# st.header("Günlük Su Kullanımı Bilgileri")

# # Kullanıcıdan girdileri alıyoruz
# dus_suresi = st.number_input("Günlük duş süresi (dakika)", min_value=0, max_value=60, value=10)
# camasir_sayisi = st.number_input("Günlük çamaşır makinesi kullanımı (adet)", min_value=0, max_value=10, value=1)
# bulasik_sayisi = st.number_input("Günlük bulaşık makinesi kullanımı (adet)", min_value=0, max_value=10, value=1)

# st.write("---")

######################################################################################################

# import streamlit as st

# st.title("Su Ayak İzi Hesaplayıcı")

# st.header("Günlük Su Kullanımı Bilgileri")

# dus_suresi = st.number_input("Günlük duş süresi (dakika)", min_value=0, max_value=60, value=10)
# camasir_sayisi = st.number_input("Günlük çamaşır makinesi kullanımı (adet)", min_value=0, max_value=10, value=1)
# bulasik_sayisi = st.number_input("Günlük bulaşık makinesi kullanımı (adet)", min_value=0, max_value=10, value=1)

# if st.button("Hesapla"):
#     # Ortalama su tüketimleri (litre)
#     su_dus = dus_suresi * 12      # dakikada 12 litre duş suyu
#     su_camasir = camasir_sayisi * 50  # bir çamaşır makinesi kullanımı yaklaşık 50 litre
#     su_bulasik = bulasik_sayisi * 15  # bir bulaşık makinesi kullanımı yaklaşık 15 litre

#     toplam_su = su_dus + su_camasir + su_bulasik

#     st.success(f"Günlük tahmini su tüketiminiz: {toplam_su:.2f} litre")

#####################################################################################################

# import streamlit as st
# import matplotlib.pyplot as plt

# st.set_page_config(page_title="Su Ayak İzi Hesaplayıcı", page_icon="💧", layout="centered")

# st.title("🌊 Su Ayak İzi Hesaplayıcı")
# st.write("""
# Bu uygulama, günlük su kullanımınızı farklı kalemler bazında hesaplayarak, aylık ve yıllık su ayak izinizi tahmini olarak verir.
# """)

# # Girdi alanları
# st.header("Su Tüketimi Girdileri (litre)")

# ev_su = st.number_input("Ev kullanımı (içme, yemek, banyo vb.)", min_value=0.0, value=150.0, step=0.1)
# bahce_su = st.number_input("Bahçe sulama", min_value=0.0, value=20.0, step=0.1)
# arac_yikama_su = st.number_input("Araç yıkama", min_value=0.0, value=15.0, step=0.1)
# diger_su = st.number_input("Diğer kullanımlar", min_value=0.0, value=10.0, step=0.1)

# st.write("-----")

# if st.button("Hesapla"):
#     # Toplam günlük su tüketimi
#     toplam_gunluk = ev_su + bahce_su + arac_yikama_su + diger_su
#     toplam_aylik = toplam_gunluk * 30
#     toplam_yillik = toplam_gunluk * 365

#     # Sonuçları göster
#     st.subheader("Sonuçlar:")
#     st.write(f"**Günlük tahmini su tüketiminiz:** {toplam_gunluk:,.2f} litre 💧")
#     st.write(f"**Aylık tahmini su tüketiminiz:** {toplam_aylik:,.2f} litre 💧")
#     st.write(f"**Yıllık tahmini su tüketiminiz:** {toplam_yillik:,.2f} litre 💧")

#     # Grafik çizimi
#     kalemler = ['Ev', 'Bahçe Sulama', 'Araç Yıkama', 'Diğer']
#     degerler = [ev_su, bahce_su, arac_yikama_su, diger_su]

#     fig, ax = plt.subplots()
#     ax.bar(kalemler, degerler, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
#     ax.set_ylabel("Günlük Su Tüketimi (litre)")
#     ax.set_title("Günlük Su Tüketimi Dağılımı")
#     st.pyplot(fig)

#     # Buy Me a Coffee butonu
#     st.markdown("---")
#     st.markdown("""
#     **Beğendiyseniz destek olmak için:**

#     [![Buy Me a Coffee](https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png)](https://www.buymeacoffee.com/kullaniciadiniz)
#     """, unsafe_allow_html=True)

# st.write("© 2025 Su Ayak İzi Hesaplayıcı - Geliştirici: GoeKoe")

#############################################

# import streamlit as st
# import matplotlib.pyplot as plt

# # Sayfa başlığı ve açıklama
# st.set_page_config(page_title="Kurumsal Su Ayak İzi Hesaplayıcı", page_icon="💧", layout="centered")

# st.markdown(
#     "<h1 style='color:#003366;'>Su Ayak İzi Hesaplayıcı</h1>",
#     unsafe_allow_html=True
# )
# st.markdown(
#     "<p style='color:#555555;'>Kişisel ve kurumsal su tüketiminizi hesaplayın, su ayak izinizi yönetin.</p>",
#     unsafe_allow_html=True
# )

# # Girdi alanları
# st.subheader("Su Tüketim Bilgileri")
# kisi_sayisi = st.number_input("Kişi Sayısı", min_value=1, value=1)
# gunluk_tuketim = st.number_input("Kişi Başına Günlük Su Tüketimi (litre)", min_value=0.0, value=150.0)

# # Hesapla butonu
# if st.button("Hesapla"):
#     yillik_tuketim = kisi_sayisi * gunluk_tuketim * 365
#     st.markdown(f"<h3 style='color:#007acc;'>Yıllık Su Tüketiminiz: {yillik_tuketim:,.0f} litre 💧</h3>", unsafe_allow_html=True)

#     # Grafik çizimi
#     fig, ax = plt.subplots()
#     ax.bar(["Yıllık Su Tüketimi"], [yillik_tuketim], color="#007acc")
#     ax.set_ylabel("Litre")
#     ax.set_ylim(0, yillik_tuketim * 1.2)
#     st.pyplot(fig)

#     # İpucu kutusu
#     st.info(
#         "Su tasarrufu yaparak hem doğayı koruyabilir hem de su faturalarınızı azaltabilirsiniz. "
#         "Basit alışkanlık değişiklikleri büyük fark yaratır."
#     )

##########################################################################

# import streamlit as st
# import matplotlib.pyplot as plt
# import numpy as np

# st.title("Su Ayak İzi Hesaplama ve Analizi")

# # Girdi alanları
# kisi_sayisi = st.number_input("Evde yaşayan kişi sayısı:", min_value=1, step=1)
# gunluk_tuketim = st.number_input("Kişi başı günlük ortalama su tüketimi (litre):", min_value=0.0, step=0.1, format="%.1f")

# if st.button("Hesapla"):
#     # Yıllık toplam su tüketimi
#     yillik_tuketim = kisi_sayisi * gunluk_tuketim * 365
#     st.write(f"Yıllık toplam su ayak iziniz: {yillik_tuketim:,.0f} litre 💧")

#     # Aylık tahmini tüketim (basit 12 aya bölme)
#     aylik_tuketim = yillik_tuketim / 12
#     aylik_tuketim_kisi_basi = aylik_tuketim / kisi_sayisi

#     st.write(f"Aylık ortalama toplam su tüketimi: {aylik_tuketim:,.0f} litre")
#     st.write(f"Aylık kişi başı su tüketimi: {aylik_tuketim_kisi_basi:,.1f} litre")

#     # Grafik çizimi
#     aylar = ["Oca", "Şub", "Mar", "Nis", "May", "Haz", "Tem", "Ağu", "Eyl", "Eki", "Kas", "Ara"]
#     aylik_tuketimler = np.full(12, aylik_tuketim)
#     aylik_kisi_basi = np.full(12, aylik_tuketim_kisi_basi)

#     fig, ax = plt.subplots(figsize=(10,5))
#     ax.bar(aylar, aylik_tuketimler, alpha=0.6, label="Toplam Aylık Su Tüketimi (Litre)")
#     ax.plot(aylar, aylik_kisi_basi, color='orange', marker='o', label="Aylık Kişi Başı Su Tüketimi (Litre)")
#     ax.set_ylabel("Litre")
#     ax.set_title("Aylık Su Tüketimi Analizi")
#     ax.legend()
#     ax.grid(True)

#     st.pyplot(fig)

# st.header("Detaylı Su Tüketim Alanları")

# # Günlük litre bazında farklı kullanım alanları
# dus = st.number_input("Günlük duş su tüketimi (litre):", min_value=0.0, step=0.1, format="%.1f")
# camasir = st.number_input("Günlük çamaşır su tüketimi (litre):", min_value=0.0, step=0.1, format="%.1f")
# tuvalet = st.number_input("Günlük tuvalet su tüketimi (litre):", min_value=0.0, step=0.1, format="%.1f")
# mutfak = st.number_input("Günlük mutfak su tüketimi (litre):", min_value=0.0, step=0.1, format="%.1f")
# diger = st.number_input("Günlük diğer su tüketimi (litre):", min_value=0.0, step=0.1, format="%.1f")

# if st.button("Detaylı Tüketimi Hesapla"):
#     toplam_gunluk = dus + camasir + tuvalet + mutfak + diger
#     yillik_toplam = toplam_gunluk * kisi_sayisi * 365
#     st.write(f"Detaylı toplam günlük su tüketimi (kişi başı): {toplam_gunluk:.1f} litre")
#     st.write(f"Yıllık toplam su tüketimi: {yillik_toplam:,.0f} litre 💧")

#     # Grafik
#     kullanımlar = ["Duş", "Çamaşır", "Tuvalet", "Mutfak", "Diğer"]
#     gunluk_miktarlar = [dus, camasir, tuvalet, mutfak, diger]

#     fig2, ax2 = plt.subplots()
#     ax2.pie(gunluk_miktarlar, labels=kullanımlar, autopct='%1.1f%%', startangle=90)
#     ax2.set_title("Günlük Su Tüketimi Dağılımı")
#     st.pyplot(fig2)    
#######################################

# import streamlit as st
# import matplotlib.pyplot as plt

# st.title("Yıllık Su Ayak İzi Hesaplama ve Tasarruf Önerileri")

# # 1. Girdi alanları
# ev_kişi = st.number_input("Evde yaşayan kişi sayısı:", min_value=1, value=3)
# günlük_su_tuketimi = st.number_input("Kişi başı günlük su tüketimi (litre):", min_value=1, value=150)
# camasir_miktari = st.number_input("Günlük çamaşır yıkama sayısı:", min_value=0, value=2)
# bulaşık_miktari = st.number_input("Günlük bulaşık makinesi kullanımı:", min_value=0, value=1)

# if st.button("Hesapla"):
#     # 2. Hesaplama
#     yıllık_tüketim = ev_kişi * günlük_su_tuketimi * 365
#     çamaşır_su = camasir_miktari * 50 * 365  # ortalama 50 litre
#     bulaşık_su = bulaşık_miktari * 15 * 365  # ortalama 15 litre
#     toplam_su = yıllık_tüketim + çamaşır_su + bulaşık_su
    
#     st.write(f"**Toplam yıllık su tüketiminiz:** {toplam_su:,.0f} litre 💧")
    
#     # 3. Grafikler
#     fig1, ax1 = plt.subplots()
#     kategoriler = ['Kişisel Tüketim', 'Çamaşır', 'Bulaşık']
#     miktarlar = [yıllık_tüketim, çamaşır_su, bulaşık_su]
#     ax1.pie(miktarlar, labels=kategoriler, autopct='%1.1f%%', startangle=90)
#     ax1.set_title("Yıllık Su Tüketimi Dağılımı")
#     st.pyplot(fig1)
    
#     fig2, ax2 = plt.subplots()
#     ax2.bar(kategoriler, miktarlar, color=['blue', 'green', 'orange'])
#     ax2.set_ylabel("Su Tüketimi (litre)")
#     ax2.set_title("Yıllık Su Tüketimi (Litres)")
#     st.pyplot(fig2)
    
#     # 4. Tasarruf önerileri
#     st.markdown("### Su Tasarrufu Önerileri")
#     st.markdown("""
#     - **Kişisel Tüketim:** Duş süresini kısaltın, muslukları kapalı tutun.  
#     - **Çamaşır:** Çamaşır makinesini tam doluyken çalıştırın.  
#     - **Bulaşık:** Bulaşık makinesini tam doluyken ve ekonomik modda çalıştırın.
#     """)
    
#     # 5. Genel bilinçlendirme metni
#     st.markdown("---")
#     st.markdown("""
#     💧 **Su tasarrufu önemlidir!**  
#     Dünyada su kaynakları sınırlıdır ve bilinçsiz kullanım geleceğimizi tehdit eder.  
#     Küçük alışkanlık değişiklikleriyle büyük fark yaratabilirsiniz.
#     """)


################################################################

# # app.py
# import streamlit as st
# import matplotlib.pyplot as plt
# import pandas as pd

# st.set_page_config(page_title="Su Ayak İzi Hesaplayıcı", layout="wide")
# st.title("💧 Su Ayak İzi Hesaplayıcı")

# st.markdown("""
# ### Bu uygulama ile günlük su tüketiminizi hesaplayabilir,
# su tasarrufu konusunda farkındalık kazanabilirsiniz.
# *Veriler genel ortalamalara dayalıdır.*
# """)

# st.sidebar.header("Kullanıcı Bilgileri")
# isim = st.sidebar.text_input("Adınız:")
# ulke = st.sidebar.selectbox("Ülkeniz:", ["Türkiye", "Almanya", "ABD", "Diğer"])

# st.sidebar.markdown("---")
# st.sidebar.header("Günlük Alışkanlıklar")

# dus = st.sidebar.slider("Günde kaç dakika duş alıyorsunuz?", 0, 30, 10)
# bulasik = st.sidebar.slider("Bulaşık yıkama süresi (dakika)?", 0, 60, 15)
# tuvalet = st.sidebar.slider("Günlük sifon çekme sayısı?", 0, 15, 5)

# st.sidebar.markdown("---")
# st.sidebar.header("Aylık Alışkanlıklar")
# bahce = st.sidebar.slider("Bahçe sulama (haftalık kez)", 0, 14, 2)
# arac = st.sidebar.slider("Araç yıkama (ayda kez)", 0, 8, 2)

# st.sidebar.markdown("---")
# st.sidebar.header("Beslenme ve Tüketim")
# et = st.sidebar.slider("Haftada kaç gün et tüketiyorsunuz?", 0, 7, 3)
# kıyafet = st.sidebar.slider("Ayda kaç kıyafet alıyorsunuz?", 0, 20, 2)

# st.sidebar.markdown("---")
# if st.sidebar.button("Hesapla"):
#     # Su ayak izi katsayıları (litre bazında)
#     katsayilar = {
#         "dus": dus * 9,  # 9 litre/dk
#         "bulasik": bulasik * 6,  # 6 litre/dk
#         "tuvalet": tuvalet * 9,  # 9 litre/sifon
#         "bahce": bahce * 100 * 4,  # haftalık 4 hafta x 100 litre
#         "arac": arac * 150,  # 150 litre/yıkama
#         "et": et * 700 * 4,  # 700 litre/gün, 4 hafta
#         "kıyafet": kıyafet * 2500,  # ortalama kıyafet başı
#     }

#     toplam_gunluk = katsayilar["dus"] + katsayilar["bulasik"] + katsayilar["tuvalet"]
#     toplam_aylik = katsayilar["bahce"] + katsayilar["arac"] + katsayilar["et"] + katsayilar["kıyafet"]

#     toplam_yillik = (toplam_gunluk * 365) + (toplam_aylik * 12)

#     st.subheader(f"\n\n👤 {isim if isim else 'Kullanıcı'}, yıllık toplam su ayak izin: **{toplam_yillik:,.0f} litre** 💧")

#     # Pie chart veri
#     kategoriler = ["Duş", "Bulaşık", "Tuvalet", "Bahçe Sulama", "Araç Yıkama", "Et Tüketimi", "Kıyafet"]
#     degerler = [
#         katsayilar["dus"] * 365,
#         katsayilar["bulasik"] * 365,
#         katsayilar["tuvalet"] * 365,
#         katsayilar["bahce"] * 12,
#         katsayilar["arac"] * 12,
#         katsayilar["et"] * 12,
#         katsayilar["kıyafet"] * 12,
#     ]

#     fig, ax = plt.subplots()
#     ax.pie(degerler, labels=kategoriler, autopct="%1.1f%%", startangle=90)
#     ax.axis("equal")
#     st.pyplot(fig)

#     st.markdown("---")
#     st.subheader("💡 Tasarruf Önerileri")
#     st.info("🚿 Duş süresini 2 dakika kısaltmak yılda yaklaşık 6.500 litre su tasarrufu sağlar.")
#     st.info("🚽 Çift kademeli sifon kullanımı yılda 10.000 litreye kadar su tasarrufu sağlayabilir.")
#     st.info("🥩 Et tüketimini haftada 1 gün azaltmak yılda 14.000 litre su tasarrufu sağlar.")
#     st.info("👕 Her ay 1 kıyafet daha az satın almak 30.000 litre su tasarrufu demektir.")

#     st.markdown("---")
#     st.markdown("### 🌍 Neden Önemlidir?")
#     st.write("Tatlı su kaynakları sınırlıdır ve hızla tükenmektedir. Bireysel olarak su ayak izimizi azaltmak, iklim değişikliğiyle mücadelede önemli bir adımdır.")
#     st.write("Bu araç ile hem kendi tüketiminizi ölçebilir hem de çevrenizle paylaşarak farkındalığı artırabilirsiniz.")

#     st.markdown("""
# ---
# 💖 Bu uygulamayı faydalı bulduysanız destek olabilirsiniz. 

# [Buy Me a Coffee](https://www.buymeacoffee.com/GoeKoe)

# Feedback: goe.koe@gmail.com
# """)

# ##############################################################
# import streamlit as st
# import matplotlib.pyplot as plt

# st.set_page_config(page_title="Su Ayak İzi Hesaplayıcı", layout="centered")

# st.title("💧 Su Ayak İzi Hesaplayıcı")
# st.markdown("Günlük su tüketiminizi tahmin etmek için aşağıdaki bilgileri girin.")

# st.subheader("🚿 Günlük Kullanım Verileri")

# # Elle girilebilir alanlar
# daily_shower = st.number_input("Günde duşta harcadığınız su (litre)", min_value=0, max_value=500, value=60)
# toilet_flush = st.number_input("Günde sifon kullanımından kaynaklı su (litre)", min_value=0, max_value=200, value=30)
# brushing_teeth = st.number_input("Günde diş fırçalarken harcanan su (litre)", min_value=0, max_value=50, value=5)
# laundry_per_week = st.number_input("Haftada kaç makine çamaşır yıkıyorsunuz?", min_value=0, max_value=14, value=3)
# dishwashing_per_week = st.number_input("Haftada kaç makine bulaşık yıkıyorsunuz?", min_value=0, max_value=14, value=4)

# st.subheader("🍽️ Yıllık Beslenme Verileri")

# meat_per_week = st.number_input("Haftada kaç öğün et tüketiyorsunuz?", min_value=0, max_value=21, value=4)
# dairy_per_week = st.number_input("Haftada kaç öğün süt/süt ürünleri tüketiyorsunuz?", min_value=0, max_value=21, value=7)
# vegetables_per_week = st.number_input("Haftada kaç öğün sebze/taze ürün tüketiyorsunuz?", min_value=0, max_value=21, value=10)

# # Hesaplama
# if st.button("Hesapla 💧"):
#     # Günlük kullanım
#     daily_water_use = daily_shower + toilet_flush + brushing_teeth
#     weekly_laundry = laundry_per_week * 50
#     weekly_dishwashing = dishwashing_per_week * 30
#     weekly_domestic = (daily_water_use * 7) + weekly_laundry + weekly_dishwashing
#     annual_domestic = weekly_domestic * 52

#     # Beslenme su ayak izi
#     meat_water = meat_per_week * 700  # litre/öğün
#     dairy_water = dairy_per_week * 250
#     veg_water = vegetables_per_week * 100
#     weekly_food = meat_water + dairy_water + veg_water
#     annual_food = weekly_food * 52

#     # Toplam su ayak izi
#     total_annual = annual_domestic + annual_food

#     # Sonuç
#     st.success(f"🔎 Günlük tahmini su tüketiminiz: {daily_water_use:.2f} litre")
#     st.success(f"💧 Yıllık su ayak izin: {total_annual:,.0f} litre")

#     # Grafik: Aylık dağılım
#     labels = ['Evsel Kullanım', 'Beslenme']
#     values = [annual_domestic, annual_food]
#     fig, ax = plt.subplots()
#     ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#00BFFF', '#90EE90'])
#     ax.axis('equal')
#     st.pyplot(fig)

#     # Bilinçlendirme
#     st.markdown("---")
#     st.info("💡 *Tasarruf İpucu:* Günde 1 dakika daha kısa duş almak yılda binlerce litre su tasarrufu sağlayabilir!")
    
##########################################

# import streamlit as st
# import matplotlib.pyplot as plt

# st.set_page_config(page_title="Su Ayak İzi Hesaplayıcı", layout="centered")

# st.title("💧 Su Ayak İzi Hesaplayıcı")
# st.markdown("Günlük alışkanlıklarınızı analiz ederek **yıllık su tüketiminizi** öğrenin ve **tasarruf yollarını** keşfedin.")

# st.subheader("🚿 Günlük Kullanım Verileri")

# daily_shower = st.number_input("Günde duşta harcadığınız su (litre)", min_value=0, max_value=500, value=60)
# toilet_flush = st.number_input("Günde sifon kullanımından kaynaklı su (litre)", min_value=0, max_value=200, value=30)
# brushing_teeth = st.number_input("Günde diş fırçalarken harcanan su (litre)", min_value=0, max_value=50, value=5)
# laundry_per_week = st.number_input("Haftada kaç makine çamaşır yıkıyorsunuz?", min_value=0, max_value=14, value=3)
# dishwashing_per_week = st.number_input("Haftada kaç makine bulaşık yıkıyorsunuz?", min_value=0, max_value=14, value=4)

# st.subheader("🍽️ Yıllık Beslenme Verileri")

# meat_per_week = st.number_input("Haftada kaç öğün et tüketiyorsunuz?", min_value=0, max_value=21, value=4)
# dairy_per_week = st.number_input("Haftada kaç öğün süt/süt ürünleri tüketiyorsunuz?", min_value=0, max_value=21, value=7)
# vegetables_per_week = st.number_input("Haftada kaç öğün sebze/taze ürün tüketiyorsunuz?", min_value=0, max_value=21, value=10)

# # Hesapla
# if st.button("Hesapla 💧"):
#     daily_water_use = daily_shower + toilet_flush + brushing_teeth
#     weekly_laundry = laundry_per_week * 50
#     weekly_dishwashing = dishwashing_per_week * 30
#     weekly_domestic = (daily_water_use * 7) + weekly_laundry + weekly_dishwashing
#     annual_domestic = weekly_domestic * 52

#     meat_water = meat_per_week * 700
#     dairy_water = dairy_per_week * 250
#     veg_water = vegetables_per_week * 100
#     weekly_food = meat_water + dairy_water + veg_water
#     annual_food = weekly_food * 52

#     total_annual = annual_domestic + annual_food

#     st.success(f"🔎 Günlük tahmini su tüketiminiz: {daily_water_use:.2f} litre")
#     st.success(f"💧 Yıllık su ayak izin: {total_annual:,.0f} litre")

#     # Grafik
#     labels = ['Evsel Kullanım', 'Beslenme']
#     values = [annual_domestic, annual_food]
#     fig, ax = plt.subplots()
#     ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#00BFFF', '#90EE90'])
#     ax.axis('equal')
#     st.pyplot(fig)

#     st.markdown("---")
#     st.subheader("💡 Tasarruf ve Bilinçlendirme")

#     st.info("🚿 **Duş süresini 1 dakika azaltmak**, yılda ortalama **10.000 litre su** tasarrufu sağlar.")
#     st.info("🧺 **Çamaşır ve bulaşık makinelerini tam dolu çalıştırmak**, haftada 200 litreye kadar tasarruf sağlar.")
#     st.info("🍔 **Haftada 1 öğün et azaltmak**, yılda yaklaşık **36.000 litre su** kazandırır.")
#     st.info("💧 **Sızıntı tespiti ve onarımı**, yılda binlerce litre suyun boşa gitmesini önler.")

#     st.markdown("---")
#     st.subheader("🌍 Uygulamayı Paylaş ve Destekle")

#     st.markdown(
#         """
#         🔗 **Bağlantılar:**

#         - [📬 Bana e-posta gönder](mailto:seninemailin@example.com)
#         - [🔗 LinkedIn Profilim](https://www.linkedin.com/in/seninprofilin)
#         - [☕ Buy Me a Coffee](https://www.buymeacoffee.com/seninlinkin)

#         > Bu uygulamayı beğendiysen, paylaşarak veya destek olarak daha fazla kişiye ulaşmasına yardımcı olabilirsin 💙
#         """,
#         unsafe_allow_html=True
#     )

##############################################


# import streamlit as st
# import matplotlib.pyplot as plt
# import pandas as pd
# from fpdf import FPDF
# import smtplib
# from email.message import EmailMessage

# # 📚 Sayfa ayarları
# st.set_page_config(page_title="Su Ayak İzi Hesaplayıcısı", layout="centered")
# st.title("🚰 Su Ayak İzi Hesaplayıcısı")
# st.markdown("""
# Su tüketiminizi daha iyi anlamanız için günlük alışkanlıklarınıza dayalı bir hesaplama sunuyoruz.

# ---
# """)

# st.subheader("🛁 Günlük Alışkanlıklar")

# # Kullanıcıdan alınan sayılar
# showers_per_day = st.number_input("Günde kaç kez duşa giriyorsunuz?", min_value=0, max_value=5, value=1)
# shower_duration = st.slider("Bir duş ortalama kaç dakika sürüyor?", min_value=1, max_value=30, value=10)
# toilet_uses = st.number_input("Günde kaç kez sifon çekiyorsunuz?", min_value=0, max_value=20, value=4)
# brushing_times = st.number_input("Günde kaç kez diş fırçalıyorsunuz?", min_value=0, max_value=10, value=2)
# laundry_per_week = st.number_input("Haftada kaç kez çamaşır yıkıyorsunuz?", min_value=0, max_value=14, value=3)
# dishwashing_per_week = st.number_input("Haftada kaç kez bulaşık yıkıyorsunuz?", min_value=0, max_value=14, value=4)

# st.caption("""
# - 🌊 Ortalama 1 dakikalık duş: **10 litre**
# - 🚰 1 sifon: **9 litre**
# - 🪪 1 diş fırçalama: **2 litre**
# - ✉️ 1 çamaşır makinesi: **120 litre**
# - 🧼 1 bulaşık makinesi: **60 litre**
# """)

# # 📊 Hesaplamalar
# daily_shower = showers_per_day * shower_duration * 10  # 10 litre/dk
# daily_toilet = toilet_uses * 9
# daily_brushing = brushing_times * 2
# daily_laundry = (laundry_per_week * 120) / 7
# daily_dishwashing = (dishwashing_per_week * 60) / 7

# total_daily = daily_shower + daily_toilet + daily_brushing + daily_laundry + daily_dishwashing
# total_yearly = total_daily * 365

# # 📊 Grafik veri hazırlığı
# data = pd.DataFrame({
#     "Kategori": ["Duş", "Sifon", "D. Fırçalama", "Çamaşır", "Bulaşık"],
#     "Günlük Su Tüketimi (L)": [daily_shower, daily_toilet, daily_brushing, daily_laundry, daily_dishwashing]
# })

# # 📊 Grafik gösterimi
# st.subheader("📊 Su Tüketimi Grafiği")
# graph_type = st.selectbox("Grafik tipi seçin", ["Bar Chart", "Line Chart"])

# fig, ax = plt.subplots()
# if graph_type == "Bar Chart":
#     ax.bar(data["Kategori"], data["Günlük Su Tüketimi (L)"], color="skyblue")
# else:
#     ax.plot(data["Kategori"], data["Günlük Su Tüketimi (L)"], marker="o", color="green")
# ax.set_ylabel("Litre")
# ax.set_title("Günlük Su Tüketimi")
# st.pyplot(fig)

# # 🌊 Sonuç
# st.success(f"Toplam günlük su tüketiminiz: {total_daily:.2f} litre")
# st.info(f"Yıllık tahmini su ayak izin: {total_yearly:,.0f} litre 💧")

# # 📶 Bilinçlendirme
# with st.expander("🔹 Tasarruf ve Bilinçlendirme Önerileri"):
#     st.markdown("""
#     - Duş sürelerini 5 dakikanın altında tutmaya çalışın.
#     - Sifon kullanımında yeni nesil az su tüketen sistemleri tercih edin.
#     - Diş fırçalarken musluğu kapatmayı unutmayın.
#     - Çamaşır ve bulaşık makinelerini tam dolmadan çalıştırmayın.
#     """)

# # 📄 PDF Çıktısı
# if st.button("PDF Olarak İndir"):
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", size=12)
#     pdf.cell(200, 10, txt="Su Ayak İzi Raporu", ln=True, align="C")
#     pdf.cell(200, 10, txt=f"Günlük Su Tüketimi: {total_daily:.2f} litre", ln=True)
#     pdf.cell(200, 10, txt=f"Yıllık Su Ayak İzi: {total_yearly:.0f} litre", ln=True)
#     pdf.output("su_ayak_izi_raporu.pdf")
#     st.success("PDF indirildi!")

# # 📧 Email gönderimi
# with st.expander("📧 Raporu mail olarak gönder"):
#     email = st.text_input("E-posta adresinizi girin")
#     if st.button("Gönder") and email:
#         msg = EmailMessage()
#         msg.set_content(f"Günlük su tüketiminiz: {total_daily:.2f} L, Yıllık: {total_yearly:.0f} L")
#         msg["Subject"] = "Su Ayak İzi Raporunuz"
#         msg["From"] = "your_email@example.com"
#         msg["To"] = email
#         try:
#             with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
#                 smtp.starttls()
#                 smtp.login("your_email@example.com", "your_password")
#                 smtp.send_message(msg)
#             st.success("E-posta gönderildi!")
#         except:
#             st.error("E-posta gönderilemedi. Lütfen ayarları kontrol edin.")

# # 🌐 Sosyal ve destek bilgisi
# st.markdown("""
# ---
# **Destek olmak isterseniz:** [Buy Me a Coffee](https://www.buymeacoffee.com/yourprofile) ☕

# LinkedIn: [linkedin.com/in/yourname](https://linkedin.com/in/yourname)  
# Email: your_email@example.com
# """)

##########################

# import streamlit as st
# import matplotlib.pyplot as plt
# from fpdf import FPDF
# import base64
# import io

# # Sabitler - Ortalama litre değerleri
# FLUSH_PER_USE = 6          # 1 sifonda giden litre
# HANDWASH_PER_USE = 2       # El yıkamada litre
# SHOWER_PER_MIN = 9         # Dakikada litre
# TOOTHBRUSH_PER_USE = 1     # Diş fırçalarken litre
# LAUNDRY_PER_USE = 50       # Çamaşır makinesi litre
# DISHWASHER_PER_USE = 15    # Bulaşık makinesi litre

# # Başlık
# st.title("💧 Personal Water Footprint Calculator")

# st.markdown("""
# Welcome! This app estimates your daily and annual water footprint based on your habits.
# Please enter the following information:
# """)

# # Kullanıcı girdileri
# toilet_visits = st.number_input("How many times do you go to the toilet per day?", min_value=0, step=1, value=4)
# st.caption("Each toilet flush uses about 6 liters of water.")
# st.write("Hope you wash your hands afterwards! We'll add water for that too.")

# handwash_count = st.number_input("How many times do you wash your hands daily?", min_value=0, step=1, value=5)
# shower_minutes = st.number_input("How many minutes do you spend showering daily?", min_value=0.0, step=0.5, value=7.0)
# toothbrush_count = st.number_input("How many times do you brush your teeth daily?", min_value=0, step=1, value=2)

# laundry_uses = st.number_input("How many times a day do you run your washing machine?", min_value=0, step=1, value=1)
# dishwasher_uses = st.number_input("How many times a day do you run your dishwasher?", min_value=0, step=1, value=1)

# # Grafik tipi seçimi
# chart_type = st.selectbox("Select chart type for visualization:", ["Bar Chart", "Line Chart", "Pie Chart"])

# if st.button("Calculate Water Footprint"):
#     # Hesaplamalar
#     flush_water = toilet_visits * FLUSH_PER_USE
#     handwash_water = handwash_count * HANDWASH_PER_USE
#     shower_water = shower_minutes * SHOWER_PER_MIN
#     toothbrush_water = toothbrush_count * TOOTHBRUSH_PER_USE
#     laundry_water = laundry_uses * LAUNDRY_PER_USE
#     dishwasher_water = dishwasher_uses * DISHWASHER_PER_USE

#     total_daily = flush_water + handwash_water + shower_water + toothbrush_water + laundry_water + dishwasher_water
#     total_annual = total_daily * 365

#     # Sonuçları göster
#     st.subheader("Your Water Footprint Results")
#     st.write(f"**Daily water consumption:** {total_daily:,.2f} liters")
#     st.write(f"**Annual water consumption:** {total_annual:,.2f} liters")

#     # Detaylı liste
#     st.markdown("### Breakdown (daily liters):")
#     st.write(f"- Toilet flushes: {flush_water:,.2f}")
#     st.write(f"- Hand washing: {handwash_water:,.2f}")
#     st.write(f"- Shower: {shower_water:,.2f}")
#     st.write(f"- Tooth brushing: {toothbrush_water:,.2f}")
#     st.write(f"- Laundry machine: {laundry_water:,.2f}")
#     st.write(f"- Dishwasher: {dishwasher_water:,.2f}")

#     # Grafik için veriler
#     labels = ['Toilet flush', 'Hand washing', 'Shower', 'Tooth brushing', 'Laundry machine', 'Dishwasher']
#     values = [flush_water, handwash_water, shower_water, toothbrush_water, laundry_water, dishwasher_water]

#     fig, ax = plt.subplots()

#     if chart_type == "Bar Chart":
#         ax.bar(labels, values, color='skyblue')
#         ax.set_ylabel('Liters per day')
#         ax.set_title('Daily Water Consumption by Activity')
#     elif chart_type == "Line Chart":
#         ax.plot(labels, values, marker='o', linestyle='-', color='green')
#         ax.set_ylabel('Liters per day')
#         ax.set_title('Daily Water Consumption by Activity')
#     else:  # Pie Chart
#         ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
#         ax.set_title('Daily Water Consumption Distribution')

#     st.pyplot(fig)

#     # Bilinçlendirme metni
#     st.markdown("""
#     ---
#     ### Water Conservation Tips 💡
#     - Fix leaking faucets promptly to save thousands of liters per year.
#     - Take shorter showers; reducing 1 minute can save up to 9 liters.
#     - Use washing machines and dishwashers with full loads to maximize efficiency.
#     - Turn off the tap while brushing your teeth.
#     - Reuse water when possible, such as for gardening.
#     """)

#     # PDF raporu oluşturma
#     def create_pdf():
#         pdf = FPDF()
#         pdf.add_page()
#         pdf.set_font("Arial", size=12)

#         pdf.cell(0, 10, "Personal Water Footprint Report", ln=1, align='C')
#         pdf.ln(10)

#         pdf.cell(0, 10, f"Daily water consumption: {total_daily:,.2f} liters", ln=1)
#         pdf.cell(0, 10, f"Annual water consumption: {total_annual:,.2f} liters", ln=1)
#         pdf.ln(5)

#         pdf.cell(0, 10, "Breakdown (daily liters):", ln=1)
#         pdf.cell(0, 10, f" - Toilet flushes: {flush_water:,.2f}", ln=1)
#         pdf.cell(0, 10, f" - Hand washing: {handwash_water:,.2f}", ln=1)
#         pdf.cell(0, 10, f" - Shower: {shower_water:,.2f}", ln=1)
#         pdf.cell(0, 10, f" - Tooth brushing: {toothbrush_water:,.2f}", ln=1)
#         pdf.cell(0, 10, f" - Laundry machine: {laundry_water:,.2f}", ln=1)
#         pdf.cell(0, 10, f" - Dishwasher: {dishwasher_water:,.2f}", ln=1)
#         pdf.ln(10)

#         pdf.cell(0, 10, "Water Conservation Tips:", ln=1)
#         pdf.multi_cell(0, 10, """- Fix leaking faucets promptly to save thousands of liters per year.
# - Take shorter showers; reducing 1 minute can save up to 9 liters.
# - Use washing machines and dishwashers with full loads to maximize efficiency.
# - Turn off the tap while brushing your teeth.
# - Reuse water when possible, such as for gardening.""")

#         # Footer with social/contact links
#         pdf.ln(10)
#         pdf.set_font("Arial", size=10)
#         pdf.cell(0, 10, "Connect with me:", ln=1)
#         pdf.cell(0, 10, "LinkedIn: https://www.linkedin.com/in/yourprofile", ln=1)
#         pdf.cell(0, 10, "Email: your.email@example.com", ln=1)
#         pdf.cell(0, 10, "Buy Me a Coffee: https://www.buymeacoffee.com/yourprofile", ln=1)

#         return pdf.output(dest='S').encode('latin1')

#     pdf_bytes = create_pdf()
#     b64 = base64.b64encode(pdf_bytes).decode()

#     st.markdown(f"[📄 Download PDF report](data:application/octet-stream;base64,{b64})")

#     # Sosyal linkler altı
#     st.markdown("---")
#     st.markdown("""
#     ### Connect with me:
#     [LinkedIn](https://www.linkedin.com/in/yourprofile) | [Email](mailto:your.email@example.com) | [Buy Me a Coffee](https://www.buymeacoffee.com/yourprofile)
#     """)

# # Tema ve renkler Streamlit'in kendi ayarlarından da yapılabilir, ama 
# # istersen bunu da özelleştirebiliriz (CSS, özel komponent vb.)

######################
# import streamlit as st
# import matplotlib.pyplot as plt
# from fpdf import FPDF
# import base64

# # Ortalama litre değerleri
# FLUSH_PER_USE = 6          # 1 sifon suyu litre
# HANDWASH_PER_USE = 2       # el yıkama litre
# SHOWER_PER_MIN = 9         # duş litre/dakika
# TOOTHBRUSH_PER_USE = 1     # diş fırçalama litre
# LAUNDRY_PER_USE = 50       # çamaşır makinesi litre/kullanım
# DISHWASHER_PER_USE = 15    # bulaşık makinesi litre/kullanım

# st.title("💧 Personal Water Footprint Calculator")

# # 3. Ülke seçimi
# country = st.selectbox("Select your country:", ["Turkey", "Germany", "USA", "Other"])

# st.markdown("""
# Welcome! This app estimates your daily and annual water footprint based on your habits.
# Please fill in your daily and weekly water use habits below.
# """)

# toilet_visits = st.number_input("How many times do you go to the toilet per day?", min_value=0, step=1, value=4)
# st.caption("Each toilet flush uses about 6 liters of water.")
# st.write("Hope you wash your hands afterwards! We'll add water for that too.")

# handwash_count = st.number_input("How many times do you wash your hands daily?", min_value=0, step=1, value=5)

# # 1. Duş için haftalık soru
# shower_days = st.number_input("How many days per week do you take a shower?", min_value=0, max_value=7, step=1, value=7)
# shower_minutes_per_day = st.number_input("Average shower duration (minutes) on shower days?", min_value=0.0, step=0.5, value=7.0)
# shower_total_minutes_weekly = shower_days * shower_minutes_per_day
# shower_avg_daily = shower_total_minutes_weekly / 7

# toothbrush_count = st.number_input("How many times do you brush your teeth daily?", min_value=0, step=1, value=2)

# # 2. Çamaşır ve bulaşık makineleri haftalık
# laundry_uses_weekly = st.number_input("How many times do you run your washing machine per week?", min_value=0, step=1, value=2)
# dishwasher_uses_weekly = st.number_input("How many times do you run your dishwasher per week?", min_value=0, step=1, value=3)

# chart_type = st.selectbox("Select chart type for visualization:", ["Bar Chart", "Line Chart", "Pie Chart"])

# if st.button("Calculate Water Footprint"):
#     flush_water = toilet_visits * FLUSH_PER_USE
#     handwash_water = handwash_count * HANDWASH_PER_USE
#     shower_water = shower_avg_daily * SHOWER_PER_MIN
#     toothbrush_water = toothbrush_count * TOOTHBRUSH_PER_USE
#     laundry_water = (laundry_uses_weekly / 7) * LAUNDRY_PER_USE
#     dishwasher_water = (dishwasher_uses_weekly / 7) * DISHWASHER_PER_USE

#     total_daily = flush_water + handwash_water + shower_water + toothbrush_water + laundry_water + dishwasher_water
#     total_annual = total_daily * 365

#     st.subheader(f"Your Water Footprint Results ({country})")
#     st.write(f"**Daily water consumption:** {total_daily:,.2f} liters")
#     st.write(f"**Annual water consumption:** {total_annual:,.2f} liters")

#     st.markdown("### Breakdown (daily liters):")
#     st.write(f"- Toilet flushes: {flush_water:,.2f}")
#     st.write(f"- Hand washing: {handwash_water:,.2f}")
#     st.write(f"- Shower: {shower_water:,.2f}")
#     st.write(f"- Tooth brushing: {toothbrush_water:,.2f}")
#     st.write(f"- Laundry machine: {laundry_water:,.2f}")
#     st.write(f"- Dishwasher: {dishwasher_water:,.2f}")

#     labels = ['Toilet flush', 'Hand washing', 'Shower', 'Tooth brushing', 'Laundry machine', 'Dishwasher']
#     values = [flush_water, handwash_water, shower_water, toothbrush_water, laundry_water, dishwasher_water]

#     fig, ax = plt.subplots()

#     if chart_type == "Bar Chart":
#         ax.bar(labels, values, color='skyblue')
#         ax.set_ylabel('Liters per day')
#         ax.set_title('Daily Water Consumption by Activity')
#     elif chart_type == "Line Chart":
#         ax.plot(labels, values, marker='o', linestyle='-', color='green')
#         ax.set_ylabel('Liters per day')
#         ax.set_title('Daily Water Consumption by Activity')
#     else:
#         ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
#         ax.set_title('Daily Water Consumption Distribution')

#     st.pyplot(fig)

#     st.markdown("""
#     ---
#     ### Water Conservation Tips 💡
#     - Fix leaking faucets promptly to save thousands of liters per year.
#     - Take shorter showers; reducing 1 minute can save up to 9 liters.
#     - Use washing machines and dishwashers with full loads to maximize efficiency.
#     - Turn off the tap while brushing your teeth.
#     - Reuse water when possible, such as for gardening.
#     """)

#     # PDF raporu
#     def create_pdf():
#         pdf = FPDF()
#         pdf.add_page()
#         pdf.set_font("Arial", "B", 16)
#         pdf.cell(0, 10, "Personal Water Footprint Report", ln=1, align="C")
#         pdf.set_font("Arial", size=12)
#         pdf.cell(0, 10, f"Country: {country}", ln=1)
#         pdf.cell(0, 10, f"Daily water consumption: {total_daily:,.2f} liters", ln=1)
#         pdf.cell(0, 10, f"Annual water consumption: {total_annual:,.2f} liters", ln=1)
#         pdf.ln(5)
#         pdf.cell(0, 10, "Breakdown (daily liters):", ln=1)
#         pdf.cell(0, 10, f" - Toilet flushes: {flush_water:,.2f}", ln=1)
#         pdf.cell(0, 10, f" - Hand washing: {handwash_water:,.2f}", ln=1)
#         pdf.cell(0, 10, f" - Shower: {shower_water:,.2f}", ln=1)
#         pdf.cell(0, 10, f" - Tooth brushing: {toothbrush_water:,.2f}", ln=1)
#         pdf.cell(0, 10, f" - Laundry machine: {laundry_water:,.2f}", ln=1)
#         pdf.cell(0, 10, f" - Dishwasher: {dishwasher_water:,.2f}", ln=1)
#         pdf.ln(5)
#         pdf.cell(0, 10, "Water Conservation Tips:", ln=1)
#         tips = ("- Fix leaking faucets promptly to save thousands of liters per year.\n"
#                 "- Take shorter showers; reducing 1 minute can save up to 9 liters.\n"
#                 "- Use washing machines and dishwashers with full loads to maximize efficiency.\n"
#                 "- Turn off the tap while brushing your teeth.\n"
#                 "- Reuse water when possible, such as for gardening.")
#         pdf.multi_cell(0, 10, tips)
#         pdf.ln(10)
#         pdf.set_font("Arial", size=10)
#         pdf.cell(0, 10, "Connect with me:", ln=1)
#         pdf.cell(0, 10, "LinkedIn: https://www.linkedin.com/in/yourprofile", ln=1)
#         pdf.cell(0, 10, "Email: your.email@example.com", ln=1)
#         pdf.cell(0, 10, "Buy Me a Coffee: https://www.buymeacoffee.com/yourprofile", ln=1)
#         return pdf.output(dest="S").encode("latin1")

#     pdf_bytes = create_pdf()
#     b64 = base64.b64encode(pdf_bytes).decode()

#     st.markdown(f"[📄 Download PDF report](data:application/octet-stream;base64,{b64})")

#     st.markdown("---")
#     st.markdown("""
#     ### Connect with me:
#     [LinkedIn](https://www.linkedin.com/in/yourprofile)
#    """)

# ######################

# import streamlit as st
# import matplotlib.pyplot as plt
# from fpdf import FPDF
# import io

# st.set_page_config(page_title="Water Footprint Calculator", layout="wide")

# st.title("💧 Water Footprint Calculator")

# st.markdown("""
# This app helps you estimate your daily and annual water footprint based on your habits.
# Please fill in the details below, then press **Calculate** to see your water consumption and get useful tips.
# """)

# # ----- Inputs -----
# st.header("Your Daily Water Usage")

# # Toilet visits (flushes)
# toilet_visits = st.number_input("How many times do you go to the toilet daily?", min_value=0, step=1, value=5)
# flush_liters = 6  # average liters per flush

# # Hand washing after toilet
# hand_washing = st.radio("Do you wash your hands after toilet visits?", ("Yes", "No"))
# hand_washing_liters = 2  # liters used per hand wash

# # Tooth brushing
# tooth_brush_sessions = st.number_input("How many times do you brush your teeth daily?", min_value=0, step=1, value=2)
# tooth_brush_liters = 1.5  # liters per brushing session

# # Shower
# shower_freq_per_week = st.number_input("How many times do you take a shower per week?", min_value=0, step=1, value=7)
# shower_duration = st.number_input("Average duration of your shower in minutes?", min_value=0, step=1, value=10)
# shower_flow_rate = 9  # liters per minute

# # Washing clothes (weekly)
# laundry_loads_per_week = st.number_input("How many loads of laundry do you do per week?", min_value=0, step=1, value=3)
# laundry_water_per_load = 50  # average liters per laundry load

# # Washing dishes (weekly)
# dishwashing_loads_per_week = st.number_input("How many dishwashing sessions per week?", min_value=0, step=1, value=7)
# dishwashing_water_per_load = 20  # average liters per dishwashing session

# # Tooth brushing water on/off
# tooth_brush_water_on = st.radio("Do you leave the water running while brushing your teeth?", ("Yes", "No"))

# # Laundry water saving tip
# st.markdown("""
# ---
# ### Tips & Awareness 💡

# - Try turning off the tap while brushing your teeth to save water.
# - Use water-efficient showerheads to reduce flow rate.
# - Full loads of laundry save water and energy.
# - Hand washing uses less water if you turn off the tap when lathering.
# """)

# # ----- Calculation -----

# def calculate_daily_water_use():
#     total = 0
#     total += toilet_visits * flush_liters
#     if hand_washing == "Yes":
#         total += toilet_visits * hand_washing_liters
#     if tooth_brush_water_on == "Yes":
#         total += tooth_brush_sessions * tooth_brush_liters
#     else:
#         total += tooth_brush_sessions * (tooth_brush_liters / 3)  # saving estimate if tap off
    
#     total += (shower_freq_per_week / 7) * shower_duration * shower_flow_rate
#     total += (laundry_loads_per_week / 7) * laundry_water_per_load
#     total += (dishwashing_loads_per_week / 7) * dishwashing_water_per_load
    
#     return total

# if st.button("Calculate"):
#     daily_water = calculate_daily_water_use()
#     annual_water = daily_water * 365
#     st.success(f"Your estimated daily water footprint: {daily_water:.2f} liters 💧")
#     st.success(f"Your estimated annual water footprint: {annual_water:,.0f} liters 💧")
    
#     # ----- Graphs -----
#     graph_type = st.selectbox("Choose graph type:", ["Bar Chart", "Line Chart", "Pie Chart"])
    
#     # Data for graphs
#     labels = [
#         "Toilet Flush",
#         "Hand Washing",
#         "Teeth Brushing",
#         "Shower",
#         "Laundry",
#         "Dishwashing"
#     ]
#     values = [
#         toilet_visits * flush_liters,
#         toilet_visits * hand_washing_liters if hand_washing == "Yes" else 0,
#         tooth_brush_sessions * tooth_brush_liters if tooth_brush_water_on == "Yes" else tooth_brush_sessions * (tooth_brush_liters / 3),
#         (shower_freq_per_week / 7) * shower_duration * shower_flow_rate,
#         (laundry_loads_per_week / 7) * laundry_water_per_load,
#         (dishwashing_loads_per_week / 7) * dishwashing_water_per_load
#     ]

#     fig, ax = plt.subplots(figsize=(8,5))
    
#     if graph_type == "Bar Chart":
#         ax.bar(labels, values, color='cornflowerblue')
#         ax.set_ylabel("Liters per day")
#         ax.set_title("Daily Water Consumption by Activity")
#         plt.xticks(rotation=30)
#     elif graph_type == "Line Chart":
#         ax.plot(labels, values, marker='o', linestyle='-', color='teal')
#         ax.set_ylabel("Liters per day")
#         ax.set_title("Daily Water Consumption by Activity")
#     elif graph_type == "Pie Chart":
#         ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
#         ax.set_title("Water Consumption Distribution")

#     st.pyplot(fig)
    
#     # ----- PDF generation -----
#     pdf_buffer = io.BytesIO()

#     class PDFReport(FPDF):
#         def header(self):
#             self.set_font('Arial', 'B', 16)
#             self.cell(0, 10, 'Water Footprint Report', ln=True, align='C')
#             self.ln(10)
#         def footer(self):
#             self.set_y(-15)
#             self.set_font('Arial', 'I', 8)
#             self.cell(0, 10, 'Generated with Water Footprint Calculator', 0, 0, 'C')
    
#     pdf = PDFReport()
#     pdf.add_page()
#     pdf.set_font("Arial", size=12)
    
#     pdf.cell(0, 10, "Your Estimated Water Usage:", ln=True)
#     pdf.cell(0, 10, f"Daily: {daily_water:.2f} liters", ln=True)
#     pdf.cell(0, 10, f"Annual: {annual_water:,.0f} liters", ln=True)
#     pdf.ln(10)
    
#     pdf.cell(0, 10, "Breakdown by activity (liters per day):", ln=True)
#     for label, value in zip(labels, values):
#         pdf.cell(0, 10, f"{label}: {value:.2f}", ln=True)
    
#     pdf.ln(10)
#     pdf.multi_cell(0, 10, "Tips to save water:\n- Turn off tap while brushing teeth.\n- Take shorter showers.\n- Use full loads for laundry and dishwashing.\n- Use water-efficient devices.")
    
#     pdf.output(pdf_buffer)
#     pdf_buffer.seek(0)
    
#     st.download_button(
#         label="Download PDF Report",
#         data=pdf_buffer,
#         file_name="water_footprint_report.pdf",
#         mime="application/pdf"
#     )

# # ----- Footer with contact -----
# st.markdown("---")
# st.markdown("""
# ### Connect with me:
# [LinkedIn](https://www.linkedin.com/in/yourprofile)  
# [Email](mailto:your.email@example.com)  
# [Buy Me a Coffee](https://www.buymeacoffee.com/yourprofile)
# """)

############
# import streamlit as st
# import matplotlib.pyplot as plt
# from fpdf import FPDF
# import io

# st.set_page_config(page_title="Water Footprint Calculator", layout="wide")

# st.title("💧 Water Footprint Calculator")

# st.markdown("""
# This app helps you estimate your daily and annual water footprint based on your habits.
# Please fill in the details below, then press **Calculate** to see your water consumption and get useful tips.
# """)

# # ----- Inputs -----
# st.header("Your Daily Water Usage")

# toilet_visits = st.number_input("How many times do you go to the toilet daily?", min_value=0, step=1, value=5)
# flush_liters = 6

# hand_washing = st.radio("Do you wash your hands after toilet visits?", ("Yes", "No"))
# hand_washing_liters = 2

# tooth_brush_sessions = st.number_input("How many times do you brush your teeth daily?", min_value=0, step=1, value=2)
# tooth_brush_liters = 1.5

# shower_freq_per_week = st.number_input("How many times do you take a shower per week?", min_value=0, step=1, value=7)
# shower_duration = st.number_input("Average duration of your shower in minutes?", min_value=0, step=1, value=10)
# shower_flow_rate = 9

# laundry_loads_per_week = st.number_input("How many loads of laundry do you do per week?", min_value=0, step=1, value=3)
# laundry_water_per_load = 50

# dishwashing_loads_per_week = st.number_input("How many dishwashing sessions per week?", min_value=0, step=1, value=7)
# dishwashing_water_per_load = 20

# tooth_brush_water_on = st.radio("Do you leave the water running while brushing your teeth?", ("Yes", "No"))

# st.markdown("""
# ---
# ### Tips & Awareness 💡

# - Try turning off the tap while brushing your teeth to save water.
# - Use water-efficient showerheads to reduce flow rate.
# - Full loads of laundry save water and energy.
# - Hand washing uses less water if you turn off the tap when lathering.
# """)

# def calculate_daily_water_use():
#     total = 0
#     total += toilet_visits * flush_liters
#     if hand_washing == "Yes":
#         total += toilet_visits * hand_washing_liters
#     if tooth_brush_water_on == "Yes":
#         total += tooth_brush_sessions * tooth_brush_liters
#     else:
#         total += tooth_brush_sessions * (tooth_brush_liters / 3)
#     total += (shower_freq_per_week / 7) * shower_duration * shower_flow_rate
#     total += (laundry_loads_per_week / 7) * laundry_water_per_load
#     total += (dishwashing_loads_per_week / 7) * dishwashing_water_per_load
#     return total

# graph_type = st.selectbox("Choose graph type:", ["Bar Chart", "Line Chart", "Pie Chart"])

# if st.button("Calculate"):
#     daily_water = calculate_daily_water_use()
#     annual_water = daily_water * 365
#     st.success(f"Your estimated daily water footprint: {daily_water:.2f} liters 💧")
#     st.success(f"Your estimated annual water footprint: {annual_water:,.0f} liters 💧")

#     if toilet_visits > 0 and hand_washing == "No":
#         st.info("Hope you wash your hands after toilet visits! Remember, hand washing uses some extra water but is very important 🧼")

#     labels = [
#         "Toilet Flush",
#         "Hand Washing",
#         "Teeth Brushing",
#         "Shower",
#         "Laundry",
#         "Dishwashing"
#     ]
#     values = [
#         toilet_visits * flush_liters,
#         toilet_visits * hand_washing_liters if hand_washing == "Yes" else 0,
#         tooth_brush_sessions * tooth_brush_liters if tooth_brush_water_on == "Yes" else tooth_brush_sessions * (tooth_brush_liters / 3),
#         (shower_freq_per_week / 7) * shower_duration * shower_flow_rate,
#         (laundry_loads_per_week / 7) * laundry_water_per_load,
#         (dishwashing_loads_per_week / 7) * dishwashing_water_per_load
#     ]

#     fig, ax = plt.subplots(figsize=(8,5))
    
#     if graph_type == "Bar Chart":
#         ax.bar(labels, values, color='cornflowerblue')
#         ax.set_ylabel("Liters per day")
#         ax.set_title("Daily Water Consumption by Activity")
#         plt.xticks(rotation=30)
#     elif graph_type == "Line Chart":
#         ax.plot(labels, values, marker='o', linestyle='-', color='teal')
#         ax.set_ylabel("Liters per day")
#         ax.set_title("Daily Water Consumption by Activity")
#     elif graph_type == "Pie Chart":
#         ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
#         ax.set_title("Water Consumption Distribution")

#     st.pyplot(fig)

#     # PDF generation
#     pdf_buffer = io.BytesIO()

#     class PDFReport(FPDF):
#         def header(self):
#             self.set_font('Arial', 'B', 16)
#             self.cell(0, 10, 'Water Footprint Report', ln=True, align='C')
#             self.ln(10)
#         def footer(self):
#             self.set_y(-15)
#             self.set_font('Arial', 'I', 8)
#             self.cell(0, 10, 'Generated with Water Footprint Calculator', 0, 0, 'C')
    
#     pdf = PDFReport()
#     pdf.add_page()
#     pdf.set_font("Arial", size=12)

#     pdf.cell(0, 10, "Your Estimated Water Usage:", ln=True)
#     pdf.cell(0, 10, f"Daily: {daily_water:.2f} liters", ln=True)
#     pdf.cell(0, 10, f"Annual: {annual_water:,.0f} liters", ln=True)
#     pdf.ln(10)

#     pdf.cell(0, 10, "Breakdown by activity (liters per day):", ln=True)
#     for label, value in zip(labels, values):
#         pdf.cell(0, 10, f"{label}: {value:.2f}", ln=True)

#     pdf.ln(10)
#     pdf.multi_cell(0, 10, "Tips to save water:\n- Turn off tap while brushing teeth.\n- Take shorter showers.\n- Use full loads for laundry and dishwashing.\n- Use water-efficient devices.")

#     pdf.output(pdf_buffer)
#     pdf_buffer.seek(0)

#     st.download_button(
#         label="Download PDF Report",
#         data=pdf_buffer,
#         file_name="water_footprint_report.pdf",
#         mime="application/pdf"
#     )

# st.markdown("---")
# st.markdown("""
# ### Connect with me:
# [LinkedIn](https://www.linkedin.com/in/yourprofile)  
# [Email](mailto:your.email@example.com)  
# [Buy Me a Coffee](https://www.buymeacoffee.com/yourprofile)
# """)

#################################
# import streamlit as st
# import matplotlib.pyplot as plt
# from fpdf import FPDF
# import io

# # Tema ayarları
# st.set_page_config(
#     page_title="Water Footprint Calculator",
#     page_icon="💧",
#     layout="centered",
#     initial_sidebar_state="expanded"
# )

# # Sayfa başlığı ve kısa açıklama
# st.title("💧 Water Footprint Calculator")
# st.markdown("""
# Welcome! This app calculates your estimated water footprint based on your daily and weekly habits.
# """)

# # --- Kullanıcı girdileri ---
# st.header("Please enter your water usage details:")

# toilet_visits = st.number_input("How many times do you use the toilet per day?", min_value=0, step=1)

# if toilet_visits > 0:
#     st.info("Hope you wash your hands every time! 💧 Hand washing uses about 2 liters per wash.")

# shower_minutes = st.number_input("How many minutes do you shower daily?", min_value=0, step=1)

# laundry_times = st.number_input("How many times do you do laundry weekly?", min_value=0, step=1)
# dishwasher_times = st.number_input("How many times do you run dishwasher weekly?", min_value=0, step=1)

# # Sabit ortalamalar litre cinsinden
# LITERS_TOILET_FLUSH = 6        # 1 sifonda 6 litre su gider (ortalama)
# LITERS_HAND_WASH = 2           # 1 el yıkamada 2 litre
# LITERS_SHOWER_PER_MIN = 9      # 1 dakika duşta 9 litre su
# LITERS_LAUNDRY = 50            # 1 kere çamaşır yıkamada 50 litre su
# LITERS_DISHWASHER = 15         # 1 kere bulaşık makinası kullanımı 15 litre

# # --- Hesapla butonu ---
# if st.button("Calculate"):

#     toilet_water = toilet_visits * LITERS_TOILET_FLUSH
#     handwash_water = toilet_visits * LITERS_HAND_WASH
#     shower_water = shower_minutes * LITERS_SHOWER_PER_MIN
#     laundry_water = laundry_times * LITERS_LAUNDRY / 7  # Haftalık suyu günlük ortalama yaptık
#     dishwasher_water = dishwasher_times * LITERS_DISHWASHER / 7

#     total_daily_water = toilet_water + handwash_water + shower_water + laundry_water + dishwasher_water

#     st.subheader("Your estimated daily water footprint:")
#     st.write(f"**{total_daily_water:,.0f} liters per day** 💧")

#     # Grafik tipi seçimi
#     chart_type = st.selectbox("Select chart type:", ["Bar Chart", "Pie Chart"])

#     labels = ["Toilet Flush", "Hand Washing", "Shower", "Laundry (daily avg)", "Dishwasher (daily avg)"]
#     values = [toilet_water, handwash_water, shower_water, laundry_water, dishwasher_water]

#     fig, ax = plt.subplots(figsize=(7,5))

#     if chart_type == "Bar Chart":
#         ax.bar(labels, values, color=['#1f77b4', '#2ca02c', '#ff7f0e', '#9467bd', '#8c564b'])
#         ax.set_ylabel("Water Consumption (liters)")
#         ax.set_title("Water Usage Breakdown")
#         plt.xticks(rotation=30, ha='right')
#     else:
#         ax.pie(values, labels=labels, autopct='%1.1f%%', colors=['#1f77b4', '#2ca02c', '#ff7f0e', '#9467bd', '#8c564b'])
#         ax.set_title("Water Usage Breakdown")

#     st.pyplot(fig)

#     # --- PDF raporu oluştur ---
#     pdf_buffer = io.BytesIO()

#     class PDFReport(FPDF):
#         def header(self):
#             self.set_font('Arial', 'B', 14)
#             self.cell(0, 10, 'Water Footprint Report', 0, 1, 'C')

#         def footer(self):
#             self.set_y(-15)
#             self.set_font('Arial', 'I', 8)
#             self.cell(0, 10, 'Generated by Water Footprint Calculator', 0, 0, 'C')

#     pdf = PDFReport()
#     pdf.add_page()
#     pdf.set_font("Arial", size=12)
#     pdf.cell(0, 10, "Estimated Daily Water Footprint Report", 0, 1, "C")
#     pdf.ln(10)

#     pdf.cell(0, 10, f"Toilet flush water: {toilet_water:.1f} liters/day", 0, 1)
#     pdf.cell(0, 10, f"Hand washing water: {handwash_water:.1f} liters/day", 0, 1)
#     pdf.cell(0, 10, f"Shower water: {shower_water:.1f} liters/day", 0, 1)
#     pdf.cell(0, 10, f"Laundry water (daily average): {laundry_water:.1f} liters/day", 0, 1)
#     pdf.cell(0, 10, f"Dishwasher water (daily average): {dishwasher_water:.1f} liters/day", 0, 1)
#     pdf.ln(5)
#     pdf.set_font("Arial", 'B', 12)
#     pdf.cell(0, 10, f"Total Daily Water Footprint: {total_daily_water:.1f} liters/day", 0, 1)

#     # Grafik resmi PDF'ye ekleme
#     # matplotlib figürünü resim dosyası olarak PDF'ye eklemek için:
#     import tempfile
#     import os

#     with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
#         fig.savefig(tmpfile.name)
#         pdf.image(tmpfile.name, x=10, w=pdf.w - 20)
#     os.unlink(tmpfile.name)

#     pdf.output(pdf_buffer)
#     pdf_buffer.seek(0)

#     st.download_button(
#         label="Download PDF Report",
#         data=pdf_buffer,
#         file_name="water_footprint_report.pdf",
#         mime="application/pdf"
#     )

# # --- Alt bilgi ve bağlantılar ---
# st.markdown("---")
# st.markdown("""
# Connect with me:  
# [LinkedIn](https://www.linkedin.com/in/yourprofile) | [Email](mailto:your.email@example.com) | [Buy me a coffee ☕](https://www.buymeacoffee.com/yourprofile)
# """)

################################

# import streamlit as st
# import matplotlib.pyplot as plt
# from fpdf import FPDF
# import io

# # --- Tema ve stil ---
# st.set_page_config(page_title="Water Footprint Calculator", layout="wide")

# st.markdown("""
#     <style>
#     .main {
#         background-color: #e0f7fa;
#         color: #006064;
#         font-family: 'Arial', sans-serif;
#     }
#     .sidebar .sidebar-content {
#         background-color: #004d40;
#         color: white;
#     }
#     </style>
# """, unsafe_allow_html=True)


# # --- Yardımcı fonksiyon: PDF oluşturma (fpdf2 Unicode destekli) ---
# class PDF(FPDF):
#     def header(self):
#         self.set_font("DejaVu", "", 16)
#         self.cell(0, 10, "Water Footprint Report", ln=True, align="C")
#         self.ln(10)

#     def footer(self):
#         self.set_y(-15)
#         self.set_font("DejaVu", "", 10)
#         self.cell(0, 10, "Page %s" % self.page_no(), align="C")


# def create_pdf(data_dict, total_consumption, tips_text):
#     pdf = PDF()
#     pdf.add_page()

#     # Unicode destekli font ekle (fpdf2 ile)
#     #pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
#     #pdf.set_font("DejaVu", "", 12)
#     pdf.set_font("Helvetica", size=16)


#     pdf.cell(0, 10, "Summary of Your Water Consumption:", ln=True)
#     pdf.ln(5)
#     for k, v in data_dict.items():
#         pdf.cell(0, 10, f"{k}: {v} liters", ln=True)
#     pdf.ln(10)
#     pdf.cell(0, 10, f"Total Weekly Water Consumption: {total_consumption:.2f} liters", ln=True)
#     pdf.ln(10)
#     pdf.multi_cell(0, 10, "Tips for Water Conservation:\n" + tips_text)
#     pdf.ln(10)
#     pdf.cell(0, 10, "Created by Water Conservation Team", ln=True)
#     pdf.cell(0, 10, "Support us: https://www.buymeacoffee.com/yourprofile", ln=True)

#     pdf_output = pdf.output(dest="S").encode("latin1", "replace")  # fpdf2 için Latin1 kodlaması
#     return pdf_output


# # --- Ana program ---

# st.title("💧 Water Footprint Calculator")

# st.sidebar.header("Customize your inputs")

# # Haftalık duş bilgisi (süre ve kaç gün)
# shower_days = st.sidebar.slider("Days you take shower per week", 0, 7, 7)
# avg_shower_min = st.sidebar.slider("Average minutes per shower", 0, 60, 10)

# # Haftalık çamaşır ve bulaşık sayısı
# laundry_loads = st.sidebar.number_input("Laundry loads per week", min_value=0, max_value=20, value=5)
# dishwasher_loads = st.sidebar.number_input("Dishwasher loads per week", min_value=0, max_value=20, value=5)

# # Tuvalet ziyaret sayısı (haftalık)
# toilet_visits = st.sidebar.number_input("Number of toilet visits per week", min_value=0, max_value=100, value=35)

# # Grafik tipi seçimi
# chart_type = st.sidebar.selectbox("Select chart type", ["Bar Chart", "Pie Chart"])

# # Bilinçlendirme ve su tasarrufu ipuçları
# tips = [
#     "Turn off the tap while brushing your teeth - save up to 15 liters per day.",
#     "Reduce shower time by 1-2 minutes to save 9-18 liters per shower.",
#     "Use full loads for laundry and dishwasher.",
#     "Fix leaks promptly to avoid waste.",
#     "Consider water-saving devices like low-flow showerheads and dual-flush toilets.",
#     "Hand washing after toilet uses approx 2 liters of water, important for hygiene."
# ]
# tips_text = "\n- ".join([""] + tips)

# st.sidebar.markdown("### 💡 Tips for Water Conservation")
# for tip in tips:
#     st.sidebar.markdown(f"- {tip}")

# # --- Hesaplamalar ---

# # Sabit su tüketimleri litre cinsinden
# water_per_min_shower = 9  # litre/dakika
# water_per_laundry_load = 50  # litre
# water_per_dishwasher_load = 15  # litre
# water_per_toilet_visit = 6  # litre
# water_per_hand_wash = 2  # litre, espri ile belirtilecek

# # Tüketimler
# shower_consumption = shower_days * avg_shower_min * water_per_min_shower
# laundry_consumption = laundry_loads * water_per_laundry_load
# dishwasher_consumption = dishwasher_loads * water_per_dishwasher_load
# toilet_consumption = toilet_visits * water_per_toilet_visit
# hand_wash_consumption = toilet_visits * water_per_hand_wash  # Tuvalet sonrası el yıkama

# # Kullanıcı cevabı 0 ise değerler de 0 olsun diye kontrol
# if shower_days == 0 or avg_shower_min == 0:
#     shower_consumption = 0

# # --- Ana ekran ---
# st.header("Your Weekly Water Consumption")

# data = {
#     "Shower Water Usage": shower_consumption,
#     "Laundry Water Usage": laundry_consumption,
#     "Dishwasher Water Usage": dishwasher_consumption,
#     "Toilet Water Usage": toilet_consumption,
#     "Hand Washing Water Usage": hand_wash_consumption
# }

# total_consumption = sum(data.values())

# # Grafik çizimi fonksiyonu
# def plot_chart(data, chart_type):
#     labels = list(data.keys())
#     values = list(data.values())
#     fig, ax = plt.subplots(figsize=(8, 5))

#     if chart_type == "Bar Chart":
#         ax.bar(labels, values, color="#00796b")
#         ax.set_ylabel("Liters")
#         ax.set_title("Weekly Water Consumption by Activity")
#     else:  # Pie Chart
#         ax.pie(values, labels=labels, autopct="%1.1f%%", startangle=140, colors=plt.cm.PuBu(np.linspace(0.4, 0.8, len(values))))
#         ax.axis("equal")
#         ax.set_title("Weekly Water Consumption by Activity")

#     st.pyplot(fig)


# import numpy as np

# plot_chart(data, chart_type)

# # Tuvalet esprisi ve bilgilendirme (cevap varsa göster)
# if toilet_visits > 0:
#     st.info("Hope you remember to wash your hands after every visit! 🧼")
#     st.write(f"Hand washing consumes approx. {water_per_hand_wash} liters of water per visit, which we've added to your total water footprint.")

# # PDF oluşturma butonu
# if st.button("Download PDF Report"):
#     pdf_bytes = create_pdf(data, total_consumption, tips_text)
#     st.download_button(label="Download PDF", data=pdf_bytes, file_name="water_footprint_report.pdf", mime="application/pdf")

# # Kurumsal ve sosyal bağlantılar
# st.markdown("---")
# st.markdown(
#     """
#     <div style="background-color:#004d40; padding: 10px; border-radius: 8px; color: white; font-size:14px;">
#     Created by Water Conservation Team &nbsp;|&nbsp;
#     <a href="https://www.buymeacoffee.com/yourprofile" target="_blank" style="color:#ffdd57;">☕ Buy Me Coffee</a> &nbsp;|&nbsp;
#     <a href="mailto:your.email@example.com" target="_blank" style="color:#ffdd57;">📧 Email</a> &nbsp;|&nbsp;
#     <a href="https://www.linkedin.com/in/yourprofile" target="_blank" style="color:#ffdd57;">LinkedIn</a>
#     </div>
#     """,
#     unsafe_allow_html=True,
# )

###################
# import streamlit as st
# import matplotlib.pyplot as plt
# import io
# from fpdf import FPDF

# # Sabitler
# HAND_WASH_LITERS_PER_WASH = 2.0  # 2 liters per hand wash approx.

# def calculate_water_use(shower_time_min, toilet_times, laundry_times, dishwashing_times, teeth_brush_times):
#     # Basit su tüketimleri (litre cinsinden tahmini)
#     shower_use = shower_time_min * 9  # 9 L per minute shower
#     toilet_use = toilet_times * 6     # 6 L per flush approx
#     laundry_use = laundry_times * 50  # 50 L per laundry cycle approx
#     dishwashing_use = dishwashing_times * 10  # 10 L per dishwasher use approx
#     teeth_brush_use = teeth_brush_times * 1.5  # 1.5 L per brushing approx

#     # El yıkama sayısı = tuvalet sayısı, su kullanımı el yıkamada
#     handwash_use = toilet_times * HAND_WASH_LITERS_PER_WASH

#     total = shower_use + toilet_use + laundry_use + dishwashing_use + teeth_brush_use + handwash_use

#     breakdown = {
#         "Shower (L)": shower_use,
#         "Toilet flushes (L)": toilet_use,
#         "Laundry (L)": laundry_use,
#         "Dishwashing (L)": dishwashing_use,
#         "Teeth brushing (L)": teeth_brush_use,
#         "Hand washing (L)": handwash_use,
#         "Total (L)": total
#     }
#     return breakdown

# def plot_water_use(breakdown, chart_type="bar"):
#     labels = list(breakdown.keys())[:-1]  # Total hariç
#     values = [breakdown[k] for k in labels]

#     fig, ax = plt.subplots()
#     if chart_type == "bar":
#         ax.bar(labels, values, color='skyblue')
#         ax.set_ylabel("Water Use (liters)")
#         ax.set_title("Estimated Water Use by Activity")
#         plt.xticks(rotation=45, ha='right')
#     elif chart_type == "pie":
#         ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
#         ax.set_title("Water Use Distribution by Activity")
#     plt.tight_layout()
#     return fig

# # PDF oluşturma fonksiyonu
# def create_pdf(breakdown, tips_text):
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Helvetica", "B", 16)
#     pdf.cell(0, 10, "Water Use Report", ln=True, align='C')
#     pdf.ln(10)

#     pdf.set_font("Helvetica", "", 12)
#     for k, v in breakdown.items():
#         pdf.cell(0, 8, f"{k}: {v:.2f} liters", ln=True)

#     pdf.ln(10)
#     pdf.set_font("Helvetica", "I", 12)
#     pdf.multi_cell(0, 8, "Tips & Awareness:")
#     pdf.set_font("Helvetica", "", 12)

#     # tips_text içindeki emoji, özel karakterleri kaldır
#     safe_tips = tips_text.replace("💡", "").replace("✔", "").replace("→", "")

#     pdf.multi_cell(0, 8, safe_tips)

#     pdf.ln(15)
#     pdf.set_font("Helvetica", "I", 10)
#     pdf.cell(0, 6, "Developed by a freelance environmental engineer to raise awareness about water use and sustainability.", ln=True, align="C")
#     pdf.cell(0, 6, "© 2025", ln=True, align="C")

#     return pdf.output(dest="S").encode('latin1')


# # Ana Streamlit uygulaması
# def main():
#     st.set_page_config(page_title="Water Footprint Calculator", layout="wide")

#     st.title("Water Footprint Calculator 💧")

#     st.sidebar.header("Select chart type")
#     chart_type = st.sidebar.selectbox("Chart Type", options=["bar", "pie"])

#     with st.form(key='input_form'):
#         st.header("Enter your weekly water use data:")

#         shower_time = st.number_input("Average shower time per week (minutes):", min_value=0, max_value=1000, value=30)
#         toilet_times = st.number_input("Number of toilet flushes per week:", min_value=0, max_value=500, value=20)
#         laundry_times = st.number_input("Number of laundry cycles per week:", min_value=0, max_value=50, value=3)
#         dishwashing_times = st.number_input("Number of dishwashing cycles per week:", min_value=0, max_value=50, value=5)
#         teeth_brush_times = st.number_input("Number of teeth brushings per week:", min_value=0, max_value=100, value=14)

#         submit_button = st.form_submit_button("Calculate")

#     if submit_button:
#         data = calculate_water_use(shower_time, toilet_times, laundry_times, dishwashing_times, teeth_brush_times)

#         # Espri ve el yıkama bilgilendirmesi
#         joke = f"Hope you're not leaving the water running while brushing your teeth! 😄"
#         handwash_info = f"Also, washing your hands after toilet flushes consumes about {data['Hand washing (L)']:.1f} liters of water weekly."

#         st.success(joke)
#         st.info(handwash_info)

#         # Bilinçlendirme ve ipuçları
#         tips = (
#             " Tips to save water:\n"
#             "- Take shorter showers.\n"
#             "- Turn off the tap while brushing your teeth.\n"
#             "- Use water-efficient appliances.\n"
#             "- Fix leaks promptly.\n"
#             "- Reuse water where possible."
#         )
#         st.markdown("### Awareness & Tips")
#         st.markdown(tips)

#         # Grafik gösterimi
#         fig = plot_water_use(data, chart_type)
#         st.pyplot(fig)

#         # PDF indirme linki
#         pdf_bytes = create_pdf(data, tips)
#         st.download_button(
#             label="Download Water Use Report (PDF)",
#             data=pdf_bytes,
#             file_name="water_use_report.pdf",
#             mime="application/pdf"
#         )

#     # Kurumsal altbilgi ve destek placeholder
#     st.markdown("---")
#     st.markdown(
#         "<small>Developed by a freelance environmental engineer to raise awareness about water use and sustainability. © 2025</small>",
#         unsafe_allow_html=True
#     )
#     st.markdown(
#         """
#         <p>If you'd like to support this project in the future, a donation link will be available here. ☕</p>
#         """,
#         unsafe_allow_html=True
#     )


# if __name__ == "__main__":
#     main()
    
    
################

# import streamlit as st
# import matplotlib.pyplot as plt
# from fpdf import FPDF
# import io
# import textwrap

# def calculate_weekly_consumption(data):
#     # Günlük olanları haftalık yap
#     toilet_weekly = data['toilet_daily'] * 7
#     teeth_weekly = data['teeth_daily'] * 7

#     # Haftalık direkt olanlar
#     laundry_weekly = data['laundry_weekly']
#     dish_weekly = data['dish_weekly']

#     # Shower toplam su tüketimi: hafta içi kaç kere * ortalama dakika * litre/dakika
#     # Ortalama 10 litre/dakika duş suyu tüketimi kabul ettim
#     shower_weekly = data['shower_times_weekly'] * data['shower_avg_minutes'] * 10

#     total_weekly = toilet_weekly + teeth_weekly + laundry_weekly + dish_weekly + shower_weekly
#     return {
#         'toilet_weekly': toilet_weekly,
#         'teeth_weekly': teeth_weekly,
#         'laundry_weekly': laundry_weekly,
#         'dish_weekly': dish_weekly,
#         'shower_weekly': shower_weekly,
#         'total_weekly': total_weekly
#     }

# def create_pdf(data, tips_text):
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_auto_page_break(auto=True, margin=15)
#     pdf.set_font("Helvetica", size=14)

#     pdf.cell(0, 10, "Water Footprint Report (Weekly)", ln=True, align="C")
#     pdf.ln(5)

#     # Verileri yazdır
#     pdf.set_font("Helvetica", size=12)
#     for key, value in data.items():
#         text_line = f"{key.replace('_weekly', '').replace('_', ' ').capitalize()}: {value:.2f} liters"
#         pdf.cell(0, 10, text_line, ln=True)

#     pdf.ln(10)
#     pdf.set_font("Helvetica", size=12)
#     # Uzun metni düzgün sarmak için textwrap kullanalım
#     wrapper = textwrap.TextWrapper(width=90)
#     lines = wrapper.wrap(text=tips_text)
#     for line in lines:
#         pdf.multi_cell(0, 8, line)

#     pdf.ln(20)
#     pdf.set_font("Helvetica", size=10)
#     pdf.cell(0, 10, "Developed by: YourName or YourCompany", ln=True, align="L")
#     pdf.cell(0, 10, "Support the project: Buy me a coffee ☕️ https://www.buymeacoffee.com/yourprofile", ln=True, align="L")
#     pdf.cell(0, 10, "Visit our corporate website: https://yourcompany.com", ln=True, align="L")

#     pdf_output = io.BytesIO()
#     pdf.output(pdf_output)
#     pdf_output.seek(0)
#     return pdf_output

# def main():
#     st.title("Water Footprint Calculator 💧")

#     st.markdown("### Please enter your water usage details:")

#     # Haftalık sorular
#     laundry = st.number_input("Laundry loads per week", min_value=0, step=1, format="%d")
#     dish = st.number_input("Dishwasher loads per week", min_value=0, step=1, format="%d")

#     # Günlük sorular
#     toilet = st.number_input("How many times do you use the toilet daily? 🚽 (Do you always wash your hands afterwards?)", min_value=0, step=1, format="%d")
#     teeth = st.number_input("How many times do you brush your teeth daily? 🦷 (Keep the tap off while brushing!)", min_value=0, step=1, format="%d")

#     # Duş bilgileri
#     shower_times = st.number_input("How many times do you shower weekly? 🚿", min_value=0, step=1, format="%d")
#     shower_avg = st.number_input("Average shower duration (minutes)", min_value=0.0, step=0.5, format="%.1f")

#     # Hesapla butonu
#     if st.button("Calculate water consumption 💧"):
#         input_data = {
#             'laundry_weekly': laundry * 50,  # Ortalama 50 litre / yük
#             'dish_weekly': dish * 15,        # Ortalama 15 litre / yük
#             'toilet_daily': toilet * 5,      # Ortalama 5 litre / tuvalet kullanımı
#             'teeth_daily': teeth * 2,        # Ortalama 2 litre / diş fırçalama
#             'shower_times_weekly': shower_times,
#             'shower_avg_minutes': shower_avg,
#         }

#         result = calculate_weekly_consumption(input_data)

#         st.success(f"Estimated weekly water consumption: {result['total_weekly']:.2f} liters")

#         # Grafik çizimi
#         categories = ['Toilet', 'Teeth brushing', 'Laundry', 'Dish wash', 'Shower']
#         values = [result['toilet_weekly'], result['teeth_weekly'], result['laundry_weekly'], result['dish_weekly'], result['shower_weekly']]

#         fig, ax = plt.subplots()
#         ax.bar(categories, values, color='skyblue')
#         ax.set_ylabel("Water consumption (liters per week)")
#         ax.set_title("Weekly Water Consumption Breakdown")
#         st.pyplot(fig)

#         # Espirili bilinçlendirme metni
#         tip_text = (
#             "💡 Remember: Always turn off the tap while brushing your teeth! 🦷\n"
#             "🚽 Washing hands after toilet use saves more than just water – it keeps you healthy!\n"
#             "🚿 Shorter showers save water and energy – aim for under 5 minutes!\n"
#             "👕 Laundry and dishwashers should be run only with full loads to save water.\n"
#             "\n"
#             "Thanks for caring about water conservation! 🌍"
#         )

#         # PDF oluşturup indir butonu
#         pdf_file = create_pdf(result, tip_text)
#         st.download_button("Download PDF report 📄", pdf_file, file_name="water_footprint_report.pdf", mime="application/pdf")

#     # Alt bilgi - footer
#     st.markdown("---")
#     st.markdown(
#         """
#         "<small>Developed by a freelance environmental engineer to raise awareness about water use and sustainability. © 2025</small>",| 
#         [Buy me a coffee ☕️](https://www.buymeacoffee.com/yourprofile) | 
#         [Corporate Website](https://yourcompany.com)
#         """,
#         unsafe_allow_html=True
#     )


# if __name__ == "__main__":
#     main()

###################

# import streamlit as st
# import matplotlib.pyplot as plt
# from fpdf import FPDF
# import io
# import textwrap

# def calculate_weekly_consumption(data):
#     toilet_weekly = data['toilet_daily'] * 7
#     teeth_weekly = data['teeth_daily'] * 7
#     laundry_weekly = data['laundry_weekly']
#     dish_weekly = data['dish_weekly']
#     shower_weekly = data['shower_times_weekly'] * data['shower_avg_minutes'] * 10
#     total_weekly = toilet_weekly + teeth_weekly + laundry_weekly + dish_weekly + shower_weekly
#     return {
#         'toilet_weekly': toilet_weekly,
#         'teeth_weekly': teeth_weekly,
#         'laundry_weekly': laundry_weekly,
#         'dish_weekly': dish_weekly,
#         'shower_weekly': shower_weekly,
#         'total_weekly': total_weekly
#     }

# def create_pdf(data, tips_text):
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_auto_page_break(auto=True, margin=15)
#     pdf.set_font("Helvetica", size=14)

#     pdf.cell(0, 10, "Water Footprint Report (Weekly)", ln=True, align="C")
#     pdf.ln(5)

#     pdf.set_font("Helvetica", size=12)
#     for key, value in data.items():
#         text_line = f"{key.replace('_weekly', '').replace('_', ' ').capitalize()}: {value:.2f} liters"
#         pdf.cell(0, 10, text_line, ln=True)

#     pdf.ln(10)
#     wrapper = textwrap.TextWrapper(width=90)
#     lines = wrapper.wrap(text=tips_text)
#     for line in lines:
#         pdf.multi_cell(0, 8, line)

#     pdf.ln(20)
#     pdf.set_font("Helvetica", size=10)
#     pdf.cell(0, 10, "Developed by: YourName or YourCompany", ln=True, align="L")
#     pdf.cell(0, 10, "Support the project: Buy me a coffee  https://www.buymeacoffee.com/yourprofile", ln=True, align="L")
#     pdf.cell(0, 10, "Visit our corporate website: https://yourcompany.com", ln=True, align="L")

#     pdf_output = io.BytesIO()
#     pdf.output(pdf_output)
#     pdf_output.seek(0)
#     return pdf_output

# def main():
#     st.title("Water Footprint Calculator 💧")
#     st.markdown("### Please enter your water usage details:")

#     laundry = st.number_input("Laundry loads per week", min_value=0, step=1, format="%d")
#     dish = st.number_input("Dishwasher loads per week", min_value=0, step=1, format="%d")
#     toilet = st.number_input("How many times do you use the toilet daily?", min_value=0, step=1, format="%d")
#     teeth = st.number_input("How many times do you brush your teeth daily?", min_value=0, step=1, format="%d")
#     shower_times = st.number_input("How many times do you shower weekly?", min_value=0, step=1, format="%d")
#     shower_avg = st.number_input("Average shower duration (minutes)", min_value=0.0, step=0.5, format="%.1f")

#     chart_type = st.selectbox("Select chart type", ["Bar Chart", "Pie Chart"])

#     if st.button("Calculate water consumption"):
#         input_data = {
#             'laundry_weekly': laundry * 50,
#             'dish_weekly': dish * 15,
#             'toilet_daily': toilet * 5,
#             'teeth_daily': teeth * 2,
#             'shower_times_weekly': shower_times,
#             'shower_avg_minutes': shower_avg,
#         }

#         result = calculate_weekly_consumption(input_data)
#         st.success(f"Estimated weekly water consumption: {result['total_weekly']:.2f} liters")

#         categories = ['Toilet', 'Teeth brushing', 'Laundry', 'Dish wash', 'Shower']
#         values = [result['toilet_weekly'], result['teeth_weekly'], result['laundry_weekly'], result['dish_weekly'], result['shower_weekly']]

#         fig, ax = plt.subplots()
#         if chart_type == "Bar Chart":
#             ax.bar(categories, values, color='skyblue')
#             ax.set_ylabel("Water consumption (liters per week)")
#             ax.set_title("Weekly Water Consumption Breakdown")
#         else:
#             ax.pie(values, labels=categories, autopct='%1.1f%%', startangle=140)
#             ax.set_title("Weekly Water Consumption Breakdown (Pie Chart)")
#             ax.axis('equal')
#         st.pyplot(fig)

#         tip_text = (
#             "Remember: Always turn off the tap while brushing your teeth! \n"
#             "Washing hands after toilet use saves more than just water. It keeps you healthy!\n"
#             "Shorter showers save water and energy. Aim for under 5 minutes!\n"
#             "Laundry and dishwashers should be run only with full loads to save water.\n"
#             "\n"
#             "Thanks for caring about water conservation!"
#         )
#         st.info(tip_text)

#         pdf_file = create_pdf(result, tip_text)
#         st.download_button("Download PDF report", data=pdf_file, file_name="water_footprint_report.pdf", mime="application/pdf")

#     st.markdown("---")
#     st.markdown(
#         """
#         <small>Developed by a freelance environmental engineer to raise awareness about water use and sustainability. © 2025</small> | 
#         [Buy me a coffee ☕️](https://www.buymeacoffee.com/yourprofile) | 
#         [Corporate Website](https://yourcompany.com)
#         """,
#         unsafe_allow_html=True
#     )

# if __name__ == "__main__":
#     main()

##################
# import streamlit as st
# import matplotlib.pyplot as plt
# from fpdf import FPDF
# import os

# # Set page config
# st.set_page_config(page_title="Water Footprint Calculator", layout="centered")
# st.title("💧 Personal Water Consumption Calculator")

# # Input section
# st.header("1. Enter Your Daily Water Usage:")
# shower = st.number_input("🚿 Shower time (minutes)", min_value=0, value=5)
# teeth = st.number_input("🪥 Teeth brushing time (minutes)", min_value=0, value=2)
# toilet = st.number_input("🚽 Toilet flushes per day", min_value=0, value=5)
# laundry = st.number_input("👕 Laundry loads per week", min_value=0, value=3)
# dishes = st.number_input("🍽️ Dishwashing sessions per week", min_value=0, value=5)

# # Calculate button
# if st.button("💧 Calculate Water Consumption"):
#     # Estimated water usage (liters)
#     shower_water = shower * 9
#     teeth_water = teeth * 2
#     toilet_water = toilet * 6
#     laundry_water = laundry * 50 / 7
#     dishes_water = dishes * 40 / 7

#     total_water = round(shower_water + teeth_water + toilet_water + laundry_water + dishes_water, 2)

#     st.success(f"Your estimated **daily water consumption** is: **{total_water} liters**")

#     # Fun messages
#     st.markdown("### 🧠 Water-Saving Thoughts:")
#     if toilet > 0:
#         st.info("🧻 *Hopefully you wash your hands after using the toilet!* (Handwashing uses about 2 liters of water each time.)")
#     if teeth > 0:
#         st.info("🪥 *Hopefully you don’t leave the tap running while brushing!* (That can waste 5–6 liters each time.)")

#     # Visualization
#     st.markdown("### 📊 Choose a Chart Type:")
#     chart_type = st.selectbox("Select a chart to visualize your consumption", ["Pie Chart", "Bar Chart"])

#     labels = ["Shower", "Teeth", "Toilet", "Laundry", "Dishes"]
#     values = [shower_water, teeth_water, toilet_water, laundry_water, dishes_water]

#     fig, ax = plt.subplots()
#     if chart_type == "Pie Chart":
#         ax.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
#         ax.axis("equal")
#     else:
#         ax.bar(labels, values, color="lightblue")
#         ax.set_ylabel("Liters")

#     st.pyplot(fig)

#     # PDF Export
#     st.markdown("### 📄 Download Your Report as PDF")
#     if st.button("📥 Generate PDF Report"):
#         try:
#             class PDF(FPDF):
#                 def header(self):
#                     self.set_font("DejaVu", 'B', 14)
#                     self.cell(0, 10, "Personal Water Consumption Report", ln=True, align='C')

#                 def footer(self):
#                     self.set_y(-15)
#                     self.set_font("DejaVu", "I", 8)
#                     self.cell(0, 10, f"Page {self.page_no()}", align='C')

#             # Load font
#             font_path = "DejaVuSans.ttf"
#             if not os.path.exists(font_path):
#                 st.error("⚠️ Please ensure 'DejaVuSans.ttf' is in the same directory.")
#             else:
#                 pdf = PDF()
#                 pdf.add_page()
#                 pdf.add_font("DejaVu", "", font_path, uni=True)
#                 pdf.add_font("DejaVu", "B", font_path, uni=True)
#                 pdf.add_font("DejaVu", "I", font_path, uni=True)
#                 pdf.set_font("DejaVu", size=12)

#                 pdf.cell(0, 10, f"Estimated daily water consumption: {total_water} liters", ln=True)
#                 pdf.ln(5)

#                 for label, val in zip(labels, values):
#                     pdf.cell(0, 10, f"{label}: {round(val, 2)} liters", ln=True)

#                 pdf.output("water_report.pdf")

#                 with open("water_report.pdf", "rb") as f:
#                     st.download_button(
#                         label="📎 Download PDF Report",
#                         data=f,
#                         file_name="water_report.pdf",
#                         mime="application/pdf"
#                     )
#         except Exception as e:
#             st.error(f"PDF generation failed: {e}")

#############

#PDF CALISAN ÖRNEK

# import streamlit as st
# import matplotlib.pyplot as plt
# from fpdf import FPDF
# import io

# st.set_page_config(page_title="Water Footprint Calculator", page_icon="💧", layout="centered")

# st.title("💧 Water Footprint Calculator")

# st.markdown("""
# Calculate your weekly water consumption based on daily activities.
# Enter your usage below and click **Calculate** to see your total water use and graphs.
# """)

# # --- User inputs ---
# laundry = st.number_input("Laundry loads per week", min_value=0, step=1, format="%d")
# dishes = st.number_input("Dishwasher loads per week", min_value=0, step=1, format="%d")
# toilet = st.number_input("Toilet uses per day", min_value=0, step=1, format="%d")
# teeth_brush = st.number_input("Teeth brushing times per day", min_value=0, step=1, format="%d")
# shower_times = st.number_input("Showers per week", min_value=0, step=1, format="%d")
# shower_avg = st.number_input("Average shower duration (minutes)", min_value=0.0, step=0.5, format="%.1f")

# # Espri kısmı - kullanıcı herhangi bir değer girdiğinde görünür
# if (laundry + dishes + toilet + teeth_brush + shower_times + shower_avg) > 0:
#     st.markdown("💬 **Hope you wash your hands properly after using the toilet!**")
#     st.caption("💧 Handwashing can use about 3 liters of water per wash.")
    
#     st.markdown("💬 **And please don’t leave the tap running while brushing your teeth!**")
#     st.caption("💧 This can waste up to 6 liters of water per minute.")

# calculate_button = st.button("Calculate")

# if calculate_button:
#     # Sabit su tüketimleri (liters)
#     laundry_per_load = 50        # Laundry load water consumption (liters)
#     dishes_per_load = 20         # Dishwasher per load (liters)
#     toilet_per_use = 6           # Toilet flush (liters)
#     teeth_brush_per_minute = 6  # Water used if tap left open (liters per minute)
#     shower_per_minute = 9        # Shower per minute water consumption (liters)
#     handwash_per_use = 3         # Handwashing per use (liters)

#     # Haftalık hesaplamalar
#     laundry_total = laundry * laundry_per_load
#     dishes_total = dishes * dishes_per_load
#     toilet_total = toilet * 7 * toilet_per_use  # daily to weekly
#     teeth_total = teeth_brush * 7 * 2 * teeth_brush_per_minute  # assuming 2 minutes per brush
#     shower_total = shower_times * shower_avg * shower_per_minute
#     handwash_total = toilet * 7 * handwash_per_use  # assuming one handwash per toilet use

#     total_water = laundry_total + dishes_total + toilet_total + teeth_total + shower_total + handwash_total

#     st.subheader("💦 Your weekly water consumption:")
#     st.write(f"**{total_water:.2f} liters**")

#     # Grafik seçimi
#     graph_type = st.radio("Select a graph type to visualize your consumption:", ("Bar Chart", "Pie Chart"))

#     labels = ['Laundry', 'Dishwasher', 'Toilet flush', 'Teeth brushing', 'Shower', 'Handwashing']
#     values = [laundry_total, dishes_total, toilet_total, teeth_total, shower_total, handwash_total]

#     fig, ax = plt.subplots(figsize=(7,4))

#     if graph_type == "Bar Chart":
#         ax.bar(labels, values, color='skyblue')
#         ax.set_ylabel("Water Consumption (liters)")
#         ax.set_title("Weekly Water Consumption Breakdown")
#         plt.xticks(rotation=30)
#     else:
#         ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
#         ax.set_title("Weekly Water Consumption Breakdown")

#     st.pyplot(fig)

#     # PDF oluşturma
#     pdf_buffer = io.BytesIO()
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", "B", 16)
#     pdf.cell(0, 10, "Water Footprint Report", ln=True, align="C")

#     pdf.set_font("Arial", size=12)
#     pdf.ln(10)
#     pdf.cell(0, 10, f"Weekly Water Consumption: {total_water:.2f} liters", ln=True)
#     pdf.ln(5)
#     pdf.cell(0, 10, f"Laundry (per week): {laundry_total:.2f} liters", ln=True)
#     pdf.cell(0, 10, f"Dishwasher (per week): {dishes_total:.2f} liters", ln=True)
#     pdf.cell(0, 10, f"Toilet flush (per week): {toilet_total:.2f} liters", ln=True)
#     pdf.cell(0, 10, f"Teeth brushing (per week): {teeth_total:.2f} liters", ln=True)
#     pdf.cell(0, 10, f"Shower (per week): {shower_total:.2f} liters", ln=True)
#     pdf.cell(0, 10, f"Handwashing (per week): {handwash_total:.2f} liters", ln=True)
#     pdf.ln(10)
#     pdf.cell(0, 10, "Thank you for using the Water Footprint Calculator!", ln=True)
#     pdf.ln(10)
#     pdf.set_font("Arial", "I", 10)
#     pdf.cell(0, 10, "Developed by an Environmental Engineer, 2025", ln=True)

#     pdf.output(pdf_buffer)
#     pdf_buffer.seek(0)

#     st.download_button(
#         label="📄 Download PDF Report",
#         data=pdf_buffer,
#         file_name="water_footprint_report.pdf",
#         mime="application/pdf"
#     )

# st.markdown("---")
# st.markdown("© 2025 Green Solutions Inc. | Developed by an Environmental Engineer")
# st.markdown("[☕ Buy me a coffee](https://www.buymeacoffee.com/yourprofile)")

##############
#CALISAN ÖRDEK
# import streamlit as st
# import matplotlib.pyplot as plt
# from fpdf import FPDF
# import io

# st.set_page_config(page_title="Water Footprint Calculator", page_icon="💧", layout="centered")

# st.title("💧 Water Footprint Calculator")

# st.markdown("""
# Calculate your weekly water consumption based on daily activities.
# Enter your usage below and click **Calculate** to see your total water use and graphs.
# """)

# # --- User inputs with related tips ---
# laundry = st.number_input("Laundry loads per week", min_value=0, step=1, format="%d")
# st.caption("💧 Each laundry load uses about 50 liters of water.")

# dishes = st.number_input("Dishwasher loads per week", min_value=0, step=1, format="%d")
# st.caption("💧 A dishwasher cycle uses roughly 20 liters.")

# toilet = st.number_input("Toilet uses per day", min_value=0, step=1, format="%d")
# st.caption("💬 Hope you wash your hands properly after using the toilet! (~3 liters per wash)")

# teeth_brush = st.number_input("Teeth brushing times per day", min_value=0, step=1, format="%d")
# st.caption("💬 Don’t leave the tap running while brushing your teeth! (up to 6 liters/min wasted)")

# shower_times = st.number_input("Showers per week", min_value=0, step=1, format="%d")
# shower_avg = st.number_input("Average shower duration (minutes)", min_value=0.0, step=0.5, format="%.1f")
# st.caption("💧 Showers consume ~9 liters per minute on average.")

# calculate_button = st.button("Calculate")

# if calculate_button:
#     # Constants liters per activity
#     laundry_per_load = 50
#     dishes_per_load = 20
#     toilet_per_use = 6
#     teeth_brush_per_minute = 6
#     shower_per_minute = 9
#     handwash_per_use = 3

#     # Calculate weekly consumption
#     laundry_total = laundry * laundry_per_load
#     dishes_total = dishes * dishes_per_load
#     toilet_total = toilet * 7 * toilet_per_use
#     teeth_total = teeth_brush * 7 * 2 * teeth_brush_per_minute
#     shower_total = shower_times * shower_avg * shower_per_minute
#     handwash_total = toilet * 7 * handwash_per_use

#     total_water = laundry_total + dishes_total + toilet_total + teeth_total + shower_total + handwash_total

#     st.subheader("💦 Your weekly water consumption:")
#     st.write(f"**{total_water:.2f} liters**")

#     # Graph selection
#     graph_type = st.radio("Select a graph type to visualize your consumption:", ("Bar Chart", "Pie Chart"))

#     labels = ['Laundry', 'Dishwasher', 'Toilet flush', 'Teeth brushing', 'Shower', 'Handwashing']
#     values = [laundry_total, dishes_total, toilet_total, teeth_total, shower_total, handwash_total]

#     fig, ax = plt.subplots(figsize=(7,4))
#     if graph_type == "Bar Chart":
#         ax.bar(labels, values, color='skyblue')
#         ax.set_ylabel("Water Consumption (liters)")
#         ax.set_title("Weekly Water Consumption Breakdown")
#         plt.xticks(rotation=30)
#         plt.tight_layout()
#     else:
#         ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
#         ax.set_title("Weekly Water Consumption Breakdown")
#         plt.tight_layout()

#     st.pyplot(fig)

#     # Save plot to image buffer for PDF
#     img_buffer = io.BytesIO()
#     fig.savefig(img_buffer, format='PNG')
#     img_buffer.seek(0)

#     # Create PDF and insert plot image
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", "B", 16)
#     pdf.cell(0, 10, "Water Footprint Report", ln=True, align="C")

#     pdf.set_font("Arial", size=12)
#     pdf.ln(10)
#     pdf.cell(0, 10, f"Weekly Water Consumption: {total_water:.2f} liters", ln=True)
#     pdf.ln(5)
#     pdf.cell(0, 10, f"Laundry (per week): {laundry_total:.2f} liters", ln=True)
#     pdf.cell(0, 10, f"Dishwasher (per week): {dishes_total:.2f} liters", ln=True)
#     pdf.cell(0, 10, f"Toilet flush (per week): {toilet_total:.2f} liters", ln=True)
#     pdf.cell(0, 10, f"Teeth brushing (per week): {teeth_total:.2f} liters", ln=True)
#     pdf.cell(0, 10, f"Shower (per week): {shower_total:.2f} liters", ln=True)
#     pdf.cell(0, 10, f"Handwashing (per week): {handwash_total:.2f} liters", ln=True)
#     pdf.ln(10)
#     pdf.cell(0, 10, f"Graph type: {graph_type}", ln=True)
#     pdf.ln(10)

#     # Insert image (graph) to PDF (centered, width=160)
#     pdf.image(img_buffer, x=25, w=160)

#     pdf.ln(10)
#     pdf.cell(0, 10, "Thank you for using the Water Footprint Calculator!", ln=True)
#     pdf.ln(10)
#     pdf.set_font("Arial", "I", 10)
#     pdf.cell(0, 10, "Developed by an Environmental Engineer, 2025", ln=True)

#     pdf_output = io.BytesIO()
#     pdf.output(pdf_output)
#     pdf_output.seek(0)

#     st.download_button(
#         label="📄 Download PDF Report",
#         data=pdf_output,
#         file_name="water_footprint_report.pdf",
#         mime="application/pdf"
#     )

# st.markdown("---")
# st.markdown("© 2025 Green Solutions Inc. | Developed by an Environmental Engineer")
# st.markdown("[☕ Buy me a coffee](https://www.buymeacoffee.com/yourprofile)")


#############

# import streamlit as st
# import matplotlib.pyplot as plt
# from fpdf import FPDF
# import io

# st.set_page_config(page_title="Water Footprint Calculator", page_icon="💧", layout="centered")

# st.title("💧 Water Footprint Calculator")

# st.markdown("""
# Calculate your weekly water consumption based on daily activities.
# Enter your usage below and click **Calculate** to see your total water use and graphs.
# """)

# # --- Input with dynamic tips (shown if input > 0) ---

# laundry = st.number_input("Laundry loads per week", min_value=0, step=1, format="%d")
# if laundry > 0:
#     st.markdown("💧 *Each laundry load uses about 50 liters of water.*")

# dishes = st.number_input("Dishwasher loads per week", min_value=0, step=1, format="%d")
# if dishes > 0:
#     st.markdown("💧 *A dishwasher cycle uses roughly 20 liters.*")

# toilet = st.number_input("Toilet uses per day", min_value=0, step=1, format="%d")
# if toilet > 0:
#     st.markdown("💬 *Hope you wash your hands properly after using the toilet! (~3 liters per wash)*")

# teeth_brush = st.number_input("Teeth brushing times per day", min_value=0, step=1, format="%d")
# if teeth_brush > 0:
#     st.markdown("💬 *Don’t leave the tap running while brushing your teeth! (up to 6 liters/min wasted)*")

# shower_times = st.number_input("Showers per week", min_value=0, step=1, format="%d")
# shower_avg = st.number_input("Average shower duration (minutes)", min_value=0.0, step=0.5, format="%.1f")
# if shower_times > 0 and shower_avg > 0:
#     st.markdown("💧 *Showers consume ~9 liters per minute on average.*")

# calculate_button = st.button("Calculate")

# if calculate_button:
#     # Constants liters per activity
#     laundry_per_load = 50
#     dishes_per_load = 20
#     toilet_per_use = 6
#     teeth_brush_per_minute = 6
#     shower_per_minute = 9
#     handwash_per_use = 3

#     # Calculations
#     laundry_total = laundry * laundry_per_load
#     dishes_total = dishes * dishes_per_load
#     toilet_total = toilet * 7 * toilet_per_use
#     teeth_total = teeth_brush * 7 * 2 * teeth_brush_per_minute
#     shower_total = shower_times * shower_avg * shower_per_minute
#     handwash_total = toilet * 7 * handwash_per_use

#     total_water = laundry_total + dishes_total + toilet_total + teeth_total + shower_total + handwash_total

#     st.subheader("💦 Your weekly water consumption:")
#     st.write(f"**{total_water:.2f} liters**")

#     # Graph selection
#     graph_type = st.radio("Select a graph type to visualize your consumption:", ("Bar Chart", "Pie Chart"))

#     labels = ['Laundry', 'Dishwasher', 'Toilet flush', 'Teeth brushing', 'Shower', 'Handwashing']
#     values = [laundry_total, dishes_total, toilet_total, teeth_total, shower_total, handwash_total]

#     # Prevent pie chart crash: remove zero values and labels
#     filtered_labels = []
#     filtered_values = []
#     for lbl, val in zip(labels, values):
#         if val > 0:
#             filtered_labels.append(lbl)
#             filtered_values.append(val)

#     fig, ax = plt.subplots(figsize=(7,4))

#     # if graph_type == "Bar Chart":
#     #     ax.bar(labels, values, color='skyblue')
#     #     ax.set_ylabel("Water Consumption (liters)")
#     #     ax.set_title("Weekly Water Consumption Breakdown")
#     #     plt.xticks(rotation=30)
#     #     plt.tight_layout()
#     # else:
#     #     if sum(filtered_values) == 0:
#     #         st.warning("No water consumption data to show in Pie Chart.")
#     #     else:
#     #         ax.pie(filtered_values, labels=filtered_labels, autopct='%1.1f%%', startangle=140)
#     #         ax.set_title("Weekly Water Consumption Breakdown")

#     # st.pyplot(fig)
    
#     if graph_type == "Bar Chart":
#         ax.bar(labels, values, color='skyblue')
#         ax.set_ylabel("Water Consumption (liters)")
#         ax.set_title("Weekly Water Consumption Breakdown")
#         plt.xticks(rotation=30)
#         plt.tight_layout()
#     else:
#         if sum(filtered_values) == 0:
#             st.warning("No water consumption data to show in Pie Chart.")
#         else:
#             ax.clear()
#             wedges, texts, autotexts = ax.pie(filtered_values, labels=filtered_labels, autopct='%1.1f%%', startangle=140)
#             for autotext in autotexts:
#                 autotext.set_color('white')
#             ax.set_title("Weekly Water Consumption Breakdown")

#     st.pyplot(fig)
    
 
#     # Tips below the chart
#     st.markdown("---")
#     st.markdown("""
#     ### 💡 Water Saving Tips:
#     - Remember: Always turn off the tap while brushing your teeth!
#     - Washing hands after toilet use saves more than just water. It keeps you healthy!
#     - Shorter showers save water and energy. Aim for under 5 minutes!
#     - Laundry and dishwashers should be run only with full loads to save water.
    
#     Thanks for caring about water conservation! 💧
#     """)

#     # Save plot image for PDF
#     img_buffer = io.BytesIO()
#     fig.savefig(img_buffer, format='PNG')
#     img_buffer.seek(0)

#     # Create PDF report with plot image
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", "B", 16)
#     pdf.cell(0, 10, "Water Footprint Report", ln=True, align="C")

#     pdf.set_font("Arial", size=12)
#     pdf.ln(10)
#     pdf.cell(0, 10, f"Weekly Water Consumption: {total_water:.2f} liters", ln=True)
#     pdf.ln(5)
#     pdf.cell(0, 10, f"Laundry (per week): {laundry_total:.2f} liters", ln=True)
#     pdf.cell(0, 10, f"Dishwasher (per week): {dishes_total:.2f} liters", ln=True)
#     pdf.cell(0, 10, f"Toilet flush (per week): {toilet_total:.2f} liters", ln=True)
#     pdf.cell(0, 10, f"Teeth brushing (per week): {teeth_total:.2f} liters", ln=True)
#     pdf.cell(0, 10, f"Shower (per week): {shower_total:.2f} liters", ln=True)
#     pdf.cell(0, 10, f"Handwashing (per week): {handwash_total:.2f} liters", ln=True)
#     pdf.ln(10)
#     pdf.cell(0, 10, f"Graph type: {graph_type}", ln=True)
#     pdf.ln(10)

#     # Insert image (graph)
#     pdf.image(img_buffer, x=25, w=160)

#     pdf.ln(10)
#     pdf.cell(0, 10, "Thank you for using the Water Footprint Calculator!", ln=True)
#     pdf.ln(10)
#     pdf.set_font("Arial", "I", 10)
#     pdf.cell(0, 10, "Developed by an Environmental Engineer, 2025", ln=True)

#     pdf_output = io.BytesIO()
#     pdf.output(pdf_output)
#     pdf_output.seek(0)

#     st.download_button(
#         label="📄 Download PDF Report",
#         data=pdf_output,
#         file_name="water_footprint_report.pdf",
#         mime="application/pdf"
#     )

# st.markdown("---")
# st.markdown("© 2025 Green Solutions Inc. | Developed by an Environmental Engineer")
# st.markdown("[☕ Buy me a coffee](https://www.buymeacoffee.com/yourprofile)")

#############

#CALISIYOR11

# import streamlit as st
# import matplotlib.pyplot as plt
# from fpdf import FPDF
# import io

# st.set_page_config(page_title="Water Footprint Calculator", page_icon="💧", layout="centered")

# st.title("💧 Water Footprint Calculator")

# st.markdown("""
# Calculate your weekly water consumption based on daily activities.
# Enter your usage below and click **Calculate** to see your total water use and graph.
# """)

# # Inputs with tips
# laundry = st.number_input("Laundry loads per week", min_value=0, step=1, format="%d")
# if laundry > 0:
#     st.markdown("💧 *Each laundry load uses about 50 liters of water.*")

# dishes = st.number_input("Dishwasher loads per week", min_value=0, step=1, format="%d")
# if dishes > 0:
#     st.markdown("💧 *A dishwasher cycle uses roughly 20 liters.*")

# toilet = st.number_input("Toilet uses per day", min_value=0, step=1, format="%d")
# if toilet > 0:
#     st.markdown("💬 *Hope you wash your hands properly after using the toilet! (~3 liters per wash)*")

# teeth_brush = st.number_input("Teeth brushing times per day", min_value=0, step=1, format="%d")
# if teeth_brush > 0:
#     st.markdown("💬 *Don’t leave the tap running while brushing your teeth! (up to 6 liters/min wasted)*")

# shower_times = st.number_input("Showers per week", min_value=0, step=1, format="%d")
# shower_avg = st.number_input("Average shower duration (minutes)", min_value=0.0, step=0.5, format="%.1f")
# if shower_times > 0 and shower_avg > 0:
#     st.markdown("💧 *Showers consume ~9 liters per minute on average.*")

# calculate_button = st.button("Calculate")

# if calculate_button:
#     # Constants liters per activity
#     laundry_per_load = 50
#     dishes_per_load = 20
#     toilet_per_use = 6
#     teeth_brush_per_minute = 6
#     shower_per_minute = 9
#     handwash_per_use = 3

#     # Calculations
#     laundry_total = laundry * laundry_per_load
#     dishes_total = dishes * dishes_per_load
#     toilet_total = toilet * 7 * toilet_per_use
#     teeth_total = teeth_brush * 7 * 2 * teeth_brush_per_minute
#     shower_total = shower_times * shower_avg * shower_per_minute
#     handwash_total = toilet * 7 * handwash_per_use

#     total_water = laundry_total + dishes_total + toilet_total + teeth_total + shower_total + handwash_total

#     st.subheader("💦 Your weekly water consumption:")
#     st.write(f"**{total_water:.2f} liters**")

#     # Pie chart only
#     labels = ['Laundry', 'Dishwasher', 'Toilet flush', 'Teeth brushing', 'Shower', 'Handwashing']
#     values = [laundry_total, dishes_total, toilet_total, teeth_total, shower_total, handwash_total]

#     filtered_labels = []
#     filtered_values = []
#     for lbl, val in zip(labels, values):
#         if val > 0:
#             filtered_labels.append(lbl)
#             filtered_values.append(val)

#     if sum(filtered_values) == 0:
#         st.warning("No water consumption data to show in Pie Chart.")
#     else:
#         fig, ax = plt.subplots(figsize=(6,6))
#         wedges, texts, autotexts = ax.pie(filtered_values, labels=filtered_labels, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
#         for autotext in autotexts:
#             autotext.set_color('white')
#         ax.set_title("Weekly Water Consumption Breakdown")
#         ax.axis('equal')
#         st.pyplot(fig)

#         # Tips below the chart
#         st.markdown("---")
#         st.markdown("""
#         ### 💡 Water Saving Tips:
#         - Remember: Always turn off the tap while brushing your teeth!
#         - Washing hands after toilet use saves more than just water. It keeps you healthy!
#         - Shorter showers save water and energy. Aim for under 5 minutes!
#         - Laundry and dishwashers should be run only with full loads to save water.
        
#         Thanks for caring about water conservation! 💧
#         """)

#         # Save plot image for PDF
#         img_buffer = io.BytesIO()
#         fig.savefig(img_buffer, format='PNG')
#         img_buffer.seek(0)

#         # Create PDF report with plot image
#         pdf = FPDF()
#         pdf.add_page()
#         pdf.set_font("Arial", "B", 16)
#         pdf.cell(0, 10, "Water Footprint Report", ln=True, align="C")

#         pdf.set_font("Arial", size=12)
#         pdf.ln(10)
#         pdf.cell(0, 10, f"Weekly Water Consumption: {total_water:.2f} liters", ln=True)
#         pdf.ln(5)
#         pdf.cell(0, 10, f"Laundry (per week): {laundry_total:.2f} liters", ln=True)
#         pdf.cell(0, 10, f"Dishwasher (per week): {dishes_total:.2f} liters", ln=True)
#         pdf.cell(0, 10, f"Toilet flush (per week): {toilet_total:.2f} liters", ln=True)
#         pdf.cell(0, 10, f"Teeth brushing (per week): {teeth_total:.2f} liters", ln=True)
#         pdf.cell(0, 10, f"Shower (per week): {shower_total:.2f} liters", ln=True)
#         pdf.cell(0, 10, f"Handwashing (per week): {handwash_total:.2f} liters", ln=True)
#         pdf.ln(10)
#         pdf.cell(0, 10, f"Graph type: Pie Chart", ln=True)
#         pdf.ln(10)

#         pdf.image(img_buffer, x=25, w=160)

#         pdf.ln(10)
#         pdf.cell(0, 10, "Thank you for using the Water Footprint Calculator!", ln=True)
#         pdf.ln(10)
#         pdf.set_font("Arial", "I", 10)
#         pdf.cell(0, 10, "Developed by an Environmental Engineer, 2025", ln=True)

#         pdf_output = io.BytesIO()
#         pdf.output(pdf_output)
#         pdf_output.seek(0)

#         st.download_button(
#             label="📄 Download PDF Report",
#             data=pdf_output,
#             file_name="water_footprint_report.pdf",
#             mime="application/pdf"
#         )

# st.markdown("---")
# st.markdown("© 2025 Green Solutions Inc. | Developed by an Environmental Engineer")
# st.markdown("[☕ Buy me a coffee](https://www.buymeacoffee.com/yourprofile)")


#####

# #PDFi daha iyi olamali

# import streamlit as st
# import matplotlib.pyplot as plt
# from fpdf import FPDF
# import io

# st.set_page_config(page_title="Water Footprint Calculator", page_icon="💧", layout="centered")

# st.title("💧 Water Footprint Calculator")

# st.markdown("""
# Calculate your weekly water consumption based on daily activities.
# Enter your usage below and click **Calculate** to see your total water use and graphs.
# """)

# # --- Inputs ---
# laundry = st.number_input("Laundry loads per week", min_value=0, step=1, format="%d")
# if laundry > 0:
#     st.markdown("💧 *Each laundry load uses about 50 liters of water.*")

# dishes = st.number_input("Dishwasher loads per week", min_value=0, step=1, format="%d")
# if dishes > 0:
#     st.markdown("💧 *A dishwasher cycle uses roughly 20 liters.*")

# toilet = st.number_input("Toilet uses per day", min_value=0, step=1, format="%d")
# if toilet > 0:
#     st.markdown("💬 *Hope you wash your hands properly after using the toilet! (~3 liters per wash)*")

# teeth_brush = st.number_input("Teeth brushing times per day", min_value=0, step=1, format="%d")
# if teeth_brush > 0:
#     st.markdown("💬 *Don’t leave the tap running while brushing your teeth! (up to 6 liters/min wasted)*")

# shower_times = st.number_input("Showers per week", min_value=0, step=1, format="%d")
# shower_avg = st.number_input("Average shower duration (minutes)", min_value=0.0, step=0.5, format="%.1f")
# if shower_times > 0 and shower_avg > 0:
#     st.markdown("💧 *Showers consume ~9 liters per minute on average.*")

# calculate_button = st.button("Calculate")

# if calculate_button:
#     # Constants
#     laundry_per_load = 50
#     dishes_per_load = 20
#     toilet_per_use = 6
#     teeth_brush_per_minute = 6
#     shower_per_minute = 9
#     handwash_per_use = 3

#     # Calculations
#     laundry_total = laundry * laundry_per_load
#     dishes_total = dishes * dishes_per_load
#     toilet_total = toilet * 7 * toilet_per_use
#     teeth_total = teeth_brush * 7 * 2 * teeth_brush_per_minute
#     shower_total = shower_times * shower_avg * shower_per_minute
#     handwash_total = toilet * 7 * handwash_per_use

#     total_water = laundry_total + dishes_total + toilet_total + teeth_total + shower_total + handwash_total

#     st.subheader("💦 Your weekly water consumption:")
#     st.write(f"**{total_water:.2f} liters**")

#     labels = ['Laundry', 'Dishwasher', 'Toilet flush', 'Teeth brushing', 'Shower', 'Handwashing']
#     values = [laundry_total, dishes_total, toilet_total, teeth_total, shower_total, handwash_total]

#     # Remove zero values for pie chart
#     filtered_labels = []
#     filtered_values = []
#     for lbl, val in zip(labels, values):
#         if val > 0:
#             filtered_labels.append(lbl)
#             filtered_values.append(val)

#     fig, ax = plt.subplots(figsize=(7,4))

#     if sum(filtered_values) == 0:
#         st.warning("No water consumption data to show in Pie Chart.")
#     else:
#         wedges, texts, autotexts = ax.pie(filtered_values, labels=filtered_labels, autopct='%1.1f%%', startangle=140)
#         for autotext in autotexts:
#             autotext.set_color('white')
#         ax.set_title("Weekly Water Consumption Breakdown")

#     st.pyplot(fig)

#     # Save plot image for PDF
#     img_buffer = io.BytesIO()
#     fig.savefig(img_buffer, format='PNG')
#     img_buffer.seek(0)

#     # Create PDF report with plot image and tips
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", "B", 16)
#     pdf.cell(0, 10, "Water Footprint Report", ln=True, align="C")

#     pdf.set_font("Arial", size=12)
#     pdf.ln(10)
#     pdf.cell(0, 10, f"Weekly Water Consumption: {total_water:.2f} liters", ln=True)
#     pdf.ln(5)
#     pdf.cell(0, 10, f"Laundry (per week): {laundry_total:.2f} liters", ln=True)
#     pdf.cell(0, 10, f"Dishwasher (per week): {dishes_total:.2f} liters", ln=True)
#     pdf.cell(0, 10, f"Toilet flush (per week): {toilet_total:.2f} liters", ln=True)
#     pdf.cell(0, 10, f"Teeth brushing (per week): {teeth_total:.2f} liters", ln=True)
#     pdf.cell(0, 10, f"Shower (per week): {shower_total:.2f} liters", ln=True)
#     pdf.cell(0, 10, f"Handwashing (per week): {handwash_total:.2f} liters", ln=True)
#     pdf.ln(10)

#     # Add the smaller image to PDF
#     pdf.image(img_buffer, x=30, w=140)

#     pdf.ln(10)

#     # Water Saving Tips section
#     pdf.set_font("Arial", "B", 14)
#     pdf.cell(0, 10, " Water Saving Tips:", ln=True)
#     # pdf.set_font("Arial", size=11)
#     # tips = [
#     #     "Remember: Always turn off the tap while brushing your teeth!",
#     #     "Washing hands after toilet use saves more than just water. It keeps you healthy!",
#     #     "Shorter showers save water and energy. Aim for under 5 minutes!",
#     #     "Laundry and dishwashers should be run only with full loads to save water.",
#     #     "Thanks for caring about water conservation! 💧"
#     # ]
#     # for tip in tips:
#     #     pdf.multi_cell(0, 8, f"- {tip}")
        
#     pdf.set_font("Arial", size=11)  # Yazı fontu ve boyutu
#     tips = [
#         "Remember: Always turn off the tap while brushing your teeth!",
#         "Washing hands after toilet use saves more than just water. It keeps you healthy!",
#         "Shorter showers save water and energy. Aim for under 5 minutes!",
#         "Laundry and dishwashers should be run only with full loads to save water.",
#         "Thanks for caring about water conservation!"
#     ]
#     for tip in tips:
#         pdf.multi_cell(180, 8, f"- {tip}")  # 0 yerine 180 verdik, sabit genişlik


#     pdf.ln(10)
#     pdf.cell(0, 10, "Thank you for using the Water Footprint Calculator!", ln=True)
#     pdf.ln(10)
#     pdf.set_font("Arial", "I", 10)
#     pdf.cell(0, 10, "Developed by an Environmental Engineer, 2025", ln=True)

#     pdf_output = io.BytesIO()
#     pdf.output(pdf_output)
#     pdf_output.seek(0)

#     st.download_button(
#         label="📄 Download PDF Report",
#         data=pdf_output,
#         file_name="water_footprint_report.pdf",
#         mime="application/pdf"
#     )

# st.markdown("---")
# st.markdown("Developed by an Environmental Engineer © 2025")
# st.markdown("[☕ Buy me a coffee](https://www.buymeacoffee.com/yourprofile)")

#####

# #CALISAN BIR SKRIPT SADECE PDFTE TIPPS GÜZEL GÖZÜKMÜYOR

# import streamlit as st
# import matplotlib.pyplot as plt
# from fpdf import FPDF
# import io
# import tempfile

# st.set_page_config(page_title="Water Footprint Calculator", page_icon="💧", layout="centered")

# st.title("💧 Water Footprint Calculator")

# st.markdown("""
# Calculate your weekly water consumption based on daily activities.
# Enter your usage below and click **Calculate** to see your total water use and graphs.
# """)

# # --- Inputs ---
# laundry = st.number_input("Laundry loads per week", min_value=0, step=1, format="%d")
# if laundry > 0:
#     st.markdown("💧 *Each laundry load uses about 50 liters of water.*")

# dishes = st.number_input("Dishwasher loads per week", min_value=0, step=1, format="%d")
# if dishes > 0:
#     st.markdown("💧 *A dishwasher cycle uses roughly 20 liters.*")

# toilet = st.number_input("Toilet uses per day", min_value=0, step=1, format="%d")
# if toilet > 0:
#     st.markdown("💬 *Hope you wash your hands properly after using the toilet! (~3 liters per wash)*")

# teeth_brush = st.number_input("Teeth brushing times per day", min_value=0, step=1, format="%d")
# if teeth_brush > 0:
#     st.markdown("💬 *Don’t leave the tap running while brushing your teeth! (up to 6 liters/min wasted)*")

# shower_times = st.number_input("Showers per week", min_value=0, step=1, format="%d")
# shower_avg = st.number_input("Average shower duration (minutes)", min_value=0.0, step=0.5, format="%.1f")
# if shower_times > 0 and shower_avg > 0:
#     st.markdown("💧 *Showers consume ~9 liters per minute on average.*")

# calculate_button = st.button("Calculate")

# if calculate_button:
#     # Constants
#     laundry_per_load = 50
#     dishes_per_load = 20
#     toilet_per_use = 6
#     teeth_brush_per_minute = 6
#     shower_per_minute = 9
#     handwash_per_use = 3

#     # Calculations
#     laundry_total = laundry * laundry_per_load
#     dishes_total = dishes * dishes_per_load
#     toilet_total = toilet * 7 * toilet_per_use
#     teeth_total = teeth_brush * 7 * 2 * teeth_brush_per_minute
#     shower_total = shower_times * shower_avg * shower_per_minute
#     handwash_total = toilet * 7 * handwash_per_use

#     total_water = laundry_total + dishes_total + toilet_total + teeth_total + shower_total + handwash_total

#     st.subheader("💦 Your weekly water consumption:")
#     st.write(f"**{total_water:.2f} liters**")

#     labels = ['Laundry', 'Dishwasher', 'Toilet flush', 'Teeth brushing', 'Shower', 'Handwashing']
#     values = [laundry_total, dishes_total, toilet_total, teeth_total, shower_total, handwash_total]

#     # Remove zero values for pie chart
#     filtered_labels = []
#     filtered_values = []
#     for lbl, val in zip(labels, values):
#         if val > 0:
#             filtered_labels.append(lbl)
#             filtered_values.append(val)

#     fig, ax = plt.subplots(figsize=(7,4))

#     if sum(filtered_values) == 0:
#         st.warning("No water consumption data to show in Pie Chart.")
#     else:
#         wedges, texts, autotexts = ax.pie(filtered_values, labels=filtered_labels, autopct='%1.1f%%', startangle=140)
#         for autotext in autotexts:
#             autotext.set_color('white')
#         ax.set_title("Weekly Water Consumption Breakdown")

#     st.pyplot(fig)

#     # Save plot image for PDF using a temporary file
#     with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmpfile:
#         fig.savefig(tmpfile.name, format='PNG')
#         tmp_img_path = tmpfile.name

#     # Create PDF report with plot image and tips
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", "B", 16)
#     pdf.cell(0, 10, "Water Footprint Report", ln=True, align="C")

#     pdf.set_font("Arial", size=12)
#     pdf.ln(10)
#     pdf.cell(0, 10, f"Weekly Water Consumption: {total_water:.2f} liters", ln=True)
#     pdf.ln(5)
#     pdf.cell(0, 10, f"Laundry (per week): {laundry_total:.2f} liters", ln=True)
#     pdf.cell(0, 10, f"Dishwasher (per week): {dishes_total:.2f} liters", ln=True)
#     pdf.cell(0, 10, f"Toilet flush (per week): {toilet_total:.2f} liters", ln=True)
#     pdf.cell(0, 10, f"Teeth brushing (per week): {teeth_total:.2f} liters", ln=True)
#     pdf.cell(0, 10, f"Shower (per week): {shower_total:.2f} liters", ln=True)
#     pdf.cell(0, 10, f"Handwashing (per week): {handwash_total:.2f} liters", ln=True)
#     pdf.ln(10)

#     # Add the saved plot image to PDF
#     pdf.image(tmp_img_path, x=30, w=170)
#     pdf.ln(10)

#     # # Water Saving Tips section
#     # pdf.set_font("Arial", "B", 14)
#     # pdf.cell(0, 10, "Water Saving Tips:", ln=True)
#     # pdf.set_font("Arial", size=10)
#     # tips = [
#     #     "Remember: Always turn off the tap while brushing your teeth!",
#     #     "Washing hands after toilet use saves more than just water. It keeps you healthy!",
#     #     "Shorter showers save water and energy. Aim for under 5 minutes!",
#     #     "Laundry and dishwashers should be run only with full loads to save water.",
#     #     "Thanks for caring about water conservation!"
#     # ]
#     # for tip in tips:
#     #     pdf.multi_cell(0, 7, f"- {tip}")
        

#     # Water Saving Tips section
#     pdf.set_font("Arial", "B", 14)
#     pdf.cell(0, 10, "Water Saving Tips:", ln=True)
#     pdf.set_font("Arial", size=10)
#     page_width = pdf.w - 2 * pdf.l_margin
    
    
            
#     tips = [
#         "Remember: Always turn off the tap while brushing your teeth!",
#         "Washing hands after toilet use saves more than just water. It keeps you healthy!",
#         "Shorter showers save water and energy. Aim for under 5 minutes!",
#         "Laundry and dishwashers should be run only with full loads to save water.",
#         "Thanks for caring about water conservation!"
#     ]
#     # for tip in tips:
#     #     pdf.multi_cell(page_width, 8, f"- {tip}")
    
#     for tip in tips:
#         sentences = tip.split(". ")
#         for sentence in sentences:
#             if sentence.strip():
#                 # Cümlenin sonunda nokta yoksa ekleyelim
#                 if not sentence.endswith(('.', '!', '?')):
#                     sentence += '.'
#                 pdf.multi_cell(page_width, 8, f"- {sentence.strip()}")


#     pdf.ln(10)
#     pdf.cell(0, 10, "Thank you for using the Water Footprint Calculator!", ln=True)
#     pdf.ln(10)
#     pdf.set_font("Arial", "I", 10)
#     pdf.cell(0, 10, "Developed by a freelance environmental engineer to raise awareness about water use and sustainability. © 2025", ln=True)

#     pdf_output = io.BytesIO()
#     pdf.output(pdf_output)
#     pdf_output.seek(0)

#     st.download_button(
#         label="📄 Download PDF Report",
#         data=pdf_output,
#         file_name="water_footprint_report.pdf",
#         mime="application/pdf"
#     )

# st.markdown("---")
# st.markdown("Developed by a freelance environmental engineer to raise awareness about water use and sustainability. © 2025")
# st.markdown("[☕ Buy me a coffee](https://www.buymeacoffee.com/yourprofile)")


#################
#süper calisan skript

# import streamlit as st
# import matplotlib.pyplot as plt
# from fpdf import FPDF
# import io
# import tempfile

# st.set_page_config(page_title="Water Footprint Calculator", page_icon="💧", layout="centered")

# st.title("💧 Water Footprint Calculator")

# st.markdown("""
# Calculate your weekly water consumption based on daily activities.
# Enter your usage below and click **Calculate** to see your total water use and graphs.
# """)

# # --- Inputs ---
# laundry = st.number_input("Laundry loads per week", min_value=0, step=1, format="%d")
# if laundry > 0:
#     st.markdown("💧 *Each laundry load uses about 50 liters of water.*")

# dishes = st.number_input("Dishwasher loads per week", min_value=0, step=1, format="%d")
# if dishes > 0:
#     st.markdown("💧 *A dishwasher cycle uses roughly 20 liters.*")

# toilet = st.number_input("Toilet uses per day", min_value=0, step=1, format="%d")
# if toilet > 0:
#     st.markdown("💬 *Hope you wash your hands properly after using the toilet! (~3 liters per wash)*")

# teeth_brush = st.number_input("Teeth brushing times per day", min_value=0, step=1, format="%d")
# if teeth_brush > 0:
#     st.markdown("💬 *Don’t leave the tap running while brushing your teeth! (up to 6 liters/min wasted)*")

# shower_times = st.number_input("Showers per week", min_value=0, step=1, format="%d")
# shower_avg = st.number_input("Average shower duration (minutes)", min_value=0.0, step=0.5, format="%.1f")
# if shower_times > 0 and shower_avg > 0:
#     st.markdown("💧 *Showers consume ~9 liters per minute on average.*")

# calculate_button = st.button("Calculate")

# if calculate_button:
#     # Constants
#     laundry_per_load = 50
#     dishes_per_load = 20
#     toilet_per_use = 6
#     teeth_brush_per_minute = 6
#     shower_per_minute = 9
#     handwash_per_use = 3

#     # Calculations
#     laundry_total = laundry * laundry_per_load
#     dishes_total = dishes * dishes_per_load
#     toilet_total = toilet * 7 * toilet_per_use
#     teeth_total = teeth_brush * 7 * 2 * teeth_brush_per_minute
#     shower_total = shower_times * shower_avg * shower_per_minute
#     handwash_total = toilet * 7 * handwash_per_use

#     total_water = laundry_total + dishes_total + toilet_total + teeth_total + shower_total + handwash_total

#     st.subheader("💦 Your weekly water consumption:")
#     st.write(f"**{total_water:.2f} liters**")

#     labels = ['Laundry', 'Dishwasher', 'Toilet flush', 'Teeth brushing', 'Shower', 'Handwashing']
#     values = [laundry_total, dishes_total, toilet_total, teeth_total, shower_total, handwash_total]

#     # Remove zero values for pie chart
#     filtered_labels = []
#     filtered_values = []
#     for lbl, val in zip(labels, values):
#         if val > 0:
#             filtered_labels.append(lbl)
#             filtered_values.append(val)

#     fig, ax = plt.subplots(figsize=(7,4))

#     if sum(filtered_values) == 0:
#         st.warning("No water consumption data to show in Pie Chart.")
#     else:
#         wedges, texts, autotexts = ax.pie(filtered_values, labels=filtered_labels, autopct='%1.1f%%', startangle=140)
#         for autotext in autotexts:
#             autotext.set_color('white')
#         ax.set_title("Weekly Water Consumption Breakdown")

#     st.pyplot(fig)

#     # Save plot image for PDF using a temporary file
#     with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmpfile:
#         fig.savefig(tmpfile.name, format='PNG')
#         tmp_img_path = tmpfile.name

#     # Create PDF report with plot image and tips
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", "B", 16)
#     pdf.cell(0, 10, "Water Footprint Report", ln=True, align="C")

#     pdf.set_font("Arial", size=12)
#     pdf.ln(10)
#     pdf.cell(0, 10, f"Weekly Water Consumption: {total_water:.2f} liters", ln=True)
#     pdf.ln(5)
#     pdf.cell(0, 10, f"Laundry (per week): {laundry_total:.2f} liters", ln=True)
#     pdf.cell(0, 10, f"Dishwasher (per week): {dishes_total:.2f} liters", ln=True)
#     pdf.cell(0, 10, f"Toilet flush (per week): {toilet_total:.2f} liters", ln=True)
#     pdf.cell(0, 10, f"Teeth brushing (per week): {teeth_total:.2f} liters", ln=True)
#     pdf.cell(0, 10, f"Shower (per week): {shower_total:.2f} liters", ln=True)
#     pdf.cell(0, 10, f"Handwashing (per week): {handwash_total:.2f} liters", ln=True)
#     pdf.ln(10)

#     # Add the saved plot image to PDF
#     pdf.image(tmp_img_path, x=30, w=170)
#     pdf.ln(10)

#     # # Water Saving Tips section
#     # pdf.set_font("Arial", "B", 14)
#     # pdf.cell(0, 10, "Water Saving Tips:", ln=True)
#     # pdf.set_font("Arial", size=10)
#     # tips = [
#     #     "Remember: Always turn off the tap while brushing your teeth!",
#     #     "Washing hands after toilet use saves more than just water. It keeps you healthy!",
#     #     "Shorter showers save water and energy. Aim for under 5 minutes!",
#     #     "Laundry and dishwashers should be run only with full loads to save water.",
#     #     "Thanks for caring about water conservation!"
#     # ]
#     # for tip in tips:
#     #     pdf.multi_cell(0, 7, f"- {tip}")
        

#     # Water Saving Tips section
#     pdf.set_font("Arial", "B", 14)
#     pdf.cell(0, 10, "Water Saving Tips:", ln=True)
#     pdf.set_font("Arial", size=10)
#     page_width = pdf.w - 2 * pdf.l_margin
    
    
            
#     tips = [
#         "Remember: Always turn off the tap while brushing your teeth!",
#         "Washing hands after toilet use saves more than just water. It keeps you healthy!",
#         "Shorter showers save water and energy. Aim for under 5 minutes!",
#         "Laundry and dishwashers should be run only with full loads to save water.",
#         "Thanks for caring about water conservation!"
#     ]
#     # for tip in tips:
#     #     pdf.multi_cell(page_width, 8, f"- {tip}")
    
#     safe_width = 180  # Genişliği sabit tanımla

#     for tip in tips:
#         sentences = tip.split(". ")
#         for sentence in sentences:
#             sentence = sentence.strip()
#             if not sentence.endswith(('.', '!', '?')):
#                 sentence += '.'
#             pdf.multi_cell(w=safe_width, h=8, txt=f"- {sentence}", align="L")
#             pdf.ln(1)


#     pdf.ln(10)
#     pdf.cell(0, 10, "Thank you for using the Water Footprint Calculator!", ln=True)
#     pdf.ln(10)
#     pdf.set_font("Arial", "I", 10)
#     pdf.cell(0, 10, "Developed by a freelance environmental engineer to raise awareness about water use and sustainability. © 2025", ln=True)

#     pdf_output = io.BytesIO()
#     pdf.output(pdf_output)
#     pdf_output.seek(0)

#     st.download_button(
#         label="📄 Download PDF Report",
#         data=pdf_output,
#         file_name="water_footprint_report.pdf",
#         mime="application/pdf"
#     )

# st.markdown("---")
# st.markdown("Developed by a freelance environmental engineer to raise awareness about water use and sustainability. © 2025")
# st.markdown("[☕ Buy me a coffee](https://www.buymeacoffee.com/yourprofile)")

#############

# #LOCALDE CALISAN ÖRDEK
# import streamlit as st
# import matplotlib.pyplot as plt
# from fpdf import FPDF
# import io
# import tempfile

# st.set_page_config(page_title="Water Footprint Calculator", page_icon="💧", layout="centered")

# st.title("💧 Water Footprint Calculator")

# st.markdown("""
# Calculate your weekly water consumption based on daily activities.
# Enter your usage below and click **Calculate** to see your total water use and graphs.
# """)

# # --- Inputs ---
# laundry = st.number_input("Laundry loads per week", min_value=0, step=1, format="%d")
# if laundry > 0:
#     st.markdown("💧 *Each laundry load uses about 50 liters of water.*")

# dishes = st.number_input("Dishwasher loads per week", min_value=0, step=1, format="%d")
# if dishes > 0:
#     st.markdown("💧 *A dishwasher cycle uses roughly 20 liters.*")

# toilet = st.number_input("Toilet uses per day", min_value=0, step=1, format="%d")
# if toilet > 0:
#     st.markdown("🚽 *Each toilet flush uses approximately 6 liters of water.*")
#     st.markdown("🧼 *And hopefully you're washing your hands too 😄 — each hand wash uses around 3 liters.*")
#     #st.markdown("🧮 *That’s 9 liters per toilet visit (flush + handwashing). Included in the total calculation.*")

# teeth_brush = st.number_input("Teeth brushing times per day", min_value=0, step=1, format="%d")
# if teeth_brush > 0:
#     st.markdown("💬 *Don’t leave the tap running while brushing your teeth! (up to 6 liters/min wasted)*")

# shower_times = st.number_input("Showers per week", min_value=0, step=1, format="%d")
# shower_avg = st.number_input("Average shower duration (minutes)", min_value=0, step=1, format="%d")  # Tam sayı yapıldı
# if shower_times > 0 and shower_avg > 0:
#     st.markdown("💧 *Showers consume ~9 liters per minute on average.*")

# calculate_button = st.button("Calculate")

# if calculate_button:
#     # Constants
#     laundry_per_load = 50
#     dishes_per_load = 20
#     toilet_per_use = 6
#     handwash_per_use = 3
#     teeth_brush_per_minute = 6
#     shower_per_minute = 9

#     # Calculations
#     laundry_total = laundry * laundry_per_load
#     dishes_total = dishes * dishes_per_load
#     toilet_total = toilet * 7 * (toilet_per_use + handwash_per_use)  # Güncellendi
#     teeth_total = teeth_brush * 7 * 2 * teeth_brush_per_minute
#     shower_total = shower_times * shower_avg * shower_per_minute

#     total_water = laundry_total + dishes_total + toilet_total + teeth_total + shower_total

#     st.subheader("💦 Your weekly water consumption:")
#     st.write(f"**{total_water:.2f} liters**")

#     labels = ['Laundry', 'Dishwasher', 'Toilet visit (flush + handwashing)', 'Teeth brushing', 'Shower']
#     values = [laundry_total, dishes_total, toilet_total, teeth_total, shower_total]

#     # Remove zero values for pie chart
#     filtered_labels = []
#     filtered_values = []
#     for lbl, val in zip(labels, values):
#         if val > 0:
#             filtered_labels.append(lbl)
#             filtered_values.append(val)

#     fig, ax = plt.subplots(figsize=(8, 5))

#     if sum(filtered_values) == 0:
#         st.warning("No water consumption data to show in Pie Chart.")
#     else:
#         wedges, texts, autotexts = ax.pie(filtered_values, labels=filtered_labels, autopct='%1.1f%%', startangle=140)
#         for autotext in autotexts:
#             autotext.set_color('white')
#         ax.set_title("Weekly Water Consumption Breakdown")

#     st.pyplot(fig)

#     # Save plot image for PDF using a temporary file
#     with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmpfile:
#         fig.savefig(tmpfile.name, format='PNG')
#         tmp_img_path = tmpfile.name

#     # Create PDF report
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", "B", 16)
#     pdf.cell(0, 10, "Water Footprint Report", ln=True, align="C")

#     pdf.set_font("Arial", size=12)
#     pdf.ln(10)
#     pdf.cell(0, 10, f"Weekly Water Consumption: {total_water:.2f} liters", ln=True)
#     pdf.ln(5)
#     pdf.cell(0, 10, f"Laundry (per week): {laundry_total:.2f} liters", ln=True)
#     pdf.cell(0, 10, f"Dishwasher (per week): {dishes_total:.2f} liters", ln=True)
#     pdf.cell(0, 10, f"Toilet visits (flush + handwashing): {toilet_total:.2f} liters", ln=True)
#     pdf.cell(0, 10, f"Teeth brushing (per week): {teeth_total:.2f} liters", ln=True)
#     pdf.cell(0, 10, f"Shower (per week): {shower_total:.2f} liters", ln=True)
#     pdf.ln(10)

#     pdf.image(tmp_img_path, x=30, w=170)
#     pdf.ln(10)

#     pdf.set_font("Arial", "B", 14)
#     pdf.cell(0, 10, "Water Saving Tips:", ln=True)
#     pdf.set_font("Arial", size=10)

#     tips = [
#         "Each toilet visit includes 6 liters for flushing and 3 liters for handwashing.",
#         "Remember: Always turn off the tap while brushing your teeth!",
#         "Shorter showers save water and energy. Aim for under 5 minutes!",
#         "Laundry and dishwashers should be run only with full loads to save water.",
#         "Thanks for caring about water conservation!"
#     ]

#     safe_width = 180
#     for tip in tips:
#         sentences = tip.split(". ")
#         for sentence in sentences:
#             sentence = sentence.strip()
#             if not sentence.endswith(('.', '!', '?')):
#                 sentence += '.'
#             pdf.multi_cell(w=safe_width, h=8, txt=f"- {sentence}", align="L")
#             pdf.ln(1)

#     pdf.ln(10)
#     pdf.cell(0, 10, "Thank you for using the Water Footprint Calculator!", ln=True)
#     pdf.ln(10)
#     pdf.set_font("Arial", "I", 10)
#     pdf.cell(0, 10, "Developed by a freelance environmental engineer to raise awareness about water use and sustainability. © 2025", ln=True)

#     from io import BytesIO 
#     pdf_output = io.BytesIO()
#     #pdf.output(pdf_output)
#     pdf.output(pdf_output, 'F')
#     pdf_output.seek(0)

#     st.download_button(
#         label="📄 Download PDF Report",
#         data=pdf_output,
#         file_name="water_footprint_report.pdf",
#         mime="application/pdf"
#     )

# st.markdown("---")
# st.markdown("Developed by a freelance environmental engineer to raise awareness about water use and sustainability. © 2025")
# st.markdown("[☕ Buy me a coffee](https://www.buymeacoffee.com/yourprofile)")


#ACABA STREAMLITTE PDF CALISACAK MI?
import streamlit as st
import matplotlib.pyplot as plt
from fpdf import FPDF
import io
import tempfile

st.set_page_config(page_title="Water Footprint Calculator", page_icon="💧", layout="centered")

st.title("💧 Water Footprint Calculator")

st.markdown("""
Calculate your weekly water consumption based on daily activities.
Enter your usage below and click **Calculate** to see your total water use and graphs.
""")

# --- Inputs ---
laundry = st.number_input("Laundry loads per week", min_value=0, step=1, format="%d")
if laundry > 0:
    st.markdown("💧 *Each laundry load uses about 50 liters of water.*")

dishes = st.number_input("Dishwasher loads per week", min_value=0, step=1, format="%d")
if dishes > 0:
    st.markdown("💧 *A dishwasher cycle uses roughly 20 liters.*")

toilet = st.number_input("Toilet uses per day", min_value=0, step=1, format="%d")
if toilet > 0:
    st.markdown("🚽 *Each toilet flush uses approximately 6 liters of water.*")
    st.markdown("🧼 *And hopefully you're washing your hands too 😄 — each hand wash uses around 3 liters.*")
    #st.markdown("🧮 *That’s 9 liters per toilet visit (flush + handwashing). Included in the total calculation.*")

teeth_brush = st.number_input("Teeth brushing times per day", min_value=0, step=1, format="%d")
if teeth_brush > 0:
    st.markdown("💬 *Don’t leave the tap running while brushing your teeth! (up to 6 liters/min wasted)*")

shower_times = st.number_input("Showers per week", min_value=0, step=1, format="%d")
shower_avg = st.number_input("Average shower duration (minutes)", min_value=0, step=1, format="%d")  # Tam sayı yapıldı
if shower_times > 0 and shower_avg > 0:
    st.markdown("💧 *Showers consume ~9 liters per minute on average.*")

calculate_button = st.button("Calculate")

if calculate_button:
    # Constants
    laundry_per_load = 50
    dishes_per_load = 20
    toilet_per_use = 6
    handwash_per_use = 3
    teeth_brush_per_minute = 6
    shower_per_minute = 9

    # Calculations
    laundry_total = laundry * laundry_per_load
    dishes_total = dishes * dishes_per_load
    toilet_total = toilet * 7 * (toilet_per_use + handwash_per_use)  # Güncellendi
    teeth_total = teeth_brush * 7 * 2 * teeth_brush_per_minute
    shower_total = shower_times * shower_avg * shower_per_minute

    total_water = laundry_total + dishes_total + toilet_total + teeth_total + shower_total

    st.subheader("💦 Your weekly water consumption:")
    st.write(f"**{total_water:.2f} liters**")

    labels = ['Laundry', 'Dishwasher', 'Toilet visit (flush + handwashing)', 'Teeth brushing', 'Shower']
    values = [laundry_total, dishes_total, toilet_total, teeth_total, shower_total]

    # Remove zero values for pie chart
    filtered_labels = []
    filtered_values = []
    for lbl, val in zip(labels, values):
        if val > 0:
            filtered_labels.append(lbl)
            filtered_values.append(val)

    fig, ax = plt.subplots(figsize=(8, 5))

    if sum(filtered_values) == 0:
        st.warning("No water consumption data to show in Pie Chart.")
    else:
        wedges, texts, autotexts = ax.pie(filtered_values, labels=filtered_labels, autopct='%1.1f%%', startangle=140)
        for autotext in autotexts:
            autotext.set_color('white')
        ax.set_title("Weekly Water Consumption Breakdown")

    st.pyplot(fig)

    # Save plot image for PDF using a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmpfile:
        fig.savefig(tmpfile.name, format='PNG')
        tmp_img_path = tmpfile.name

    # Create PDF report
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Water Footprint Report", ln=True, align="C")

    pdf.set_font("Arial", size=12)
    pdf.ln(10)
    pdf.cell(0, 10, f"Weekly Water Consumption: {total_water:.2f} liters", ln=True)
    pdf.ln(5)
    pdf.cell(0, 10, f"Laundry (per week): {laundry_total:.2f} liters", ln=True)
    pdf.cell(0, 10, f"Dishwasher (per week): {dishes_total:.2f} liters", ln=True)
    pdf.cell(0, 10, f"Toilet visits (flush + handwashing): {toilet_total:.2f} liters", ln=True)
    pdf.cell(0, 10, f"Teeth brushing (per week): {teeth_total:.2f} liters", ln=True)
    pdf.cell(0, 10, f"Shower (per week): {shower_total:.2f} liters", ln=True)
    pdf.ln(10)

    pdf.image(tmp_img_path, x=30, w=170)
    pdf.ln(10)

    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Water Saving Tips:", ln=True)
    pdf.set_font("Arial", size=10)

    tips = [
        "Each toilet visit includes 6 liters for flushing and 3 liters for handwashing.",
        "Remember: Always turn off the tap while brushing your teeth!",
        "Shorter showers save water and energy. Aim for under 5 minutes!",
        "Laundry and dishwashers should be run only with full loads to save water.",
        "Thanks for caring about water conservation!"
    ]

    safe_width = 180
    for tip in tips:
        sentences = tip.split(". ")
        for sentence in sentences:
            sentence = sentence.strip()
            if not sentence.endswith(('.', '!', '?')):
                sentence += '.'
            pdf.multi_cell(w=safe_width, h=8, txt=f"- {sentence}", align="L")
            pdf.ln(1)

    pdf.ln(10)
    pdf.cell(0, 10, "Thank you for using the Water Footprint Calculator!", ln=True)
    pdf.ln(10)
    pdf.set_font("Arial", "I", 10)
    pdf.cell(0, 10, "Developed by a freelance environmental engineer to raise awareness about water use and sustainability. © 2025", ln=True)

    from io import BytesIO 
    # pdf_output = io.BytesIO()
    # #pdf.output(pdf_output)
    # pdf.output(pdf_output, 'F')
    # pdf_output.seek(0)
    
    pdf_output = io.BytesIO()
    # pdf_data = pdf.output(dest='S')  # PDF verisini string olarak al ve byte'lara çevir
    # pdf_output.write(pdf_data)  # BytesIO içine yaz
    # pdf_output.seek(0)
    
    #pdf_bytes = pdf.output(dest='S')  # bytes olarak PDF içeriği al
    
    pdf_data = pdf.output(dest='S')

    # Eğer çıktı str ise encode et, değilse olduğu gibi kullan
    if isinstance(pdf_data, str):
        pdf_bytes = pdf_data.encode('latin1')
    else:
        pdf_bytes = pdf_data
    
    pdf_output = io.BytesIO(pdf_bytes)
    pdf_output.seek(0)

    
    pdf_output = io.BytesIO(pdf_bytes)  # bytes'ı BytesIO'ya koy
    pdf_output.seek(0)  # başa dön


    st.download_button(
        label="📄 Download PDF Report",
        data=pdf_output,
        file_name="water_footprint_report.pdf",
        mime="application/pdf"
    )

st.markdown("---")
st.markdown("Developed by a freelance environmental engineer to raise awareness about water use and sustainability. © 2025")
st.markdown("[☕ Buy me a coffee](https://www.buymeacoffee.com/yourprofile)")
