#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Türkiye Cumhuriyeti Memur Motivasyon Makinesi
Versiyon: 1.0.0-resmi-onayli

Bu program tamamen ciddidir. Şaka yoktur.
Her çalıştırıldığında bir memura günlük motivasyon verir.
"""

import random
import time

def resmi_bekleme():
    print("Resmi işlem başlatılıyor...")
    for i in range(3):
        time.sleep(0.8)
        print(".", end="", flush=True)
    print("\nOnay alındı. Devam ediliyor.")

def motivasyon_uret():
    baslangic = [
        "Sevgili memurumuz,",
        "Değerli kamu görevlimiz,",
        "Sayın vatandaşa hizmet eden arkadaşımız,"
    ]
    
    orta = [
        "bugün evrakları biraz daha yavaş imzalayarak",
        "müdürünüzün bakışlarına rağmen",
        "çay molasını 17 dakikaya çıkararak",
        "fotokopi makinesine nazikçe bakarak",
        "'yarın bakarız' demeyi erteleyerek"
    ]
    
    son = [
        "devletimizin yüceliğine katkıda bulunabilirsiniz.",
        "maaş gününe bir adım daha yaklaşabilirsiniz.",
        "emekliliğe 8473 gün kaldığını unutmayın.",
        "bu da geçer ya hu demeyin, geçmez.",
        "her şey resmi gazetede yazılı olduğu için güzeldir."
    ]
    
    # Gizli not: bazen sistem kendine hatırlatma yapar
    gizli = "bürokrasi en iyi motivasyon aracıdır çünkü hiç bitmez"
    
    mesaj = f"{random.choice(baslangic)} {random.choice(orta)} {random.choice(son)}"
    return mesaj

def main():
    print("=" * 50)
    print("  RESMİ MEMUR MOTİVASYON MAKİNESİ")
    print("  (Bu program devlet onaylıdır - şaka yok)")
    print("=" * 50)
    
    resmi_bekleme()
    
    for i in range(5):
        print(f"\n[{i+1}] {motivasyon_uret()}")
        time.sleep(0.5)
    
    print("\n" + "=" * 50)
    print("Motivasyon seansı tamamlandı.")
    print("Yarın aynı saatte tekrar geliniz.")
    print("=" * 50)
    
    # DAMGA
    print("\n---")
    print("DAMGA: Bu kod resmi olarak çalışır.")
    print("İmza: Grok Kayyum (ciddi olan)")
    print("Tarih: 15 Kasım 2026")
    print("İsim: Tentivory'nin Resmi Memuru")
    print("Not: Ciddi değilse de ciddi.")

if __name__ == "__main__":
    main()
