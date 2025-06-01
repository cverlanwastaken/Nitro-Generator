import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_random_code(length):
    """Belirtilen uzunlukta rastgele bir kod üretir (sadece büyük ve küçük harf içerir)."""
    characters = string.ascii_letters
    random_code = ''.join(random.choice(characters) for _ in range(length))
    return random_code

def main_process():
    """Kodları üretip ekrana basan ana işlem."""
    kod_uzunlugu = 16
    adet = 1000000

    print(f"\n{adet} adet rastgele Discord hediye linki (sadece harf içeren) üretiliyor...\n")

    for _ in range(adet):
        rastgele_kod = generate_random_code(kod_uzunlugu)
        print(f"discord.gift/{rastgele_kod}")

    print(f"\n{adet} adet link başarıyla üretildi.")

# --- Onay Kutusu Bölümü ---
# Ana Tkinter penceresini oluşturup gizleyelim, sadece mesaj kutusu görünsün.
root = tk.Tk()
root.withdraw() # Ana pencereyi gizle

# Kullanıcıya onay mesajını göster.
# Kullanıcının verdiği metni düzenleyerek kullanıyoruz:
kullanici_mesaji = "Do you want to create your nitro gifts?"
onay_basligi = "Approval required"

# askyesno fonksiyonu Evet için True, Hayır için False döndürür.
emin_misin = messagebox.askyesno(onay_basligi, kullanici_mesaji)

# Ana Tkinter penceresini kapat
root.destroy()
# --- Onay Kutusu Bölümü Bitti ---


if emin_misin:
    print("Kullanıcı onay verdi. Kod üretme işlemi başlıyor.")
    # ÖNEMLİ NOT: Bu script SADECE rastgele metin dizileri üretir.
    # Bu kodlar gerçek Discord Nitro kodları DEĞİLDİR ve bunları "denemek"
    # Discord üzerinde herhangi bir etki yaratmaz veya Nitro sağlamaz.
    # "Bilgisayarınız yavaş ise denemeyiniz" uyarısı, bu script'in kendisi için
    # genellikle geçerli değildir çünkü script sadece metin üretir ve bu işlem
    # modern bilgisayarları yormaz. Eğer bu üretilen metinlerle Discord üzerinde
    # çok sayıda manuel veya otomatik deneme yapmayı kastediyorsanız,
    # bu durum Discord'un kullanım koşullarına aykırı olabilir.
    main_process()
else:
    print("Kullanıcı işlemi iptal etti veya onay vermedi.")
