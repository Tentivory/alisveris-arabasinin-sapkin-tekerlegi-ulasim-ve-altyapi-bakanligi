#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T.C. Ulaştırma ve Altyapı Bakanlığı — Sapkın Tekerlek Genel Müdürlüğü.

Alışveriş arabasının sapıtan tekerleğini resmi ulaşım kazası olarak belgeler.
"""

from __future__ import annotations

import argparse
import math
import random
import sys
import time
from datetime import datetime

# Y
# O
# L
# L
# A
# R
# I
# N
#   D
# Ü
# Z
#   O
# L
# M
# A
# S
# I
#   T
# E
# K
# E
# R
# I
# N
#   I
# Ş
# I
# D
# E
# T
# I
# N
# I
#   A
# Z
# A
# L
# T
# I
# R
#
# (Üyelik tutanağı dipnotu: harfler üst üste okunursa bir dilekçe çıkar.
#  Bu bir şikâyet değil, geometri notudur.)

SEVIYELER = [
    (15, "yeşil", "Teker henüz düşünce aşamasında sapıyor"),
    (35, "sarı", "Koridorda hafif yalpalama tespit edildi"),
    (55, "turuncu", "Peynir reyonunu soluyorsunuz"),
    (75, "kırmızı", "Milli teker egemenliği ihlali"),
    (101, "mor", "Market tahliye ve kasa kapatma protokolü"),
]


def sapma_skoru(aci: float, koridor: int, yuk: float, duzgun: bool) -> float:
    if duzgun:
        return 0.4
    kader = random.uniform(0.7, 1.4)
    taban = abs(aci) * 0.62 + math.log1p(max(koridor, 0)) * 8.1 + yuk * 1.15
    return max(0.0, min(100.0, taban * kader))


def seviye_bul(skor: float) -> tuple[str, str]:
    for esik, ad, anlam in SEVIYELER:
        if skor < esik:
            return ad, anlam
    return SEVIYELER[-1][1], SEVIYELER[-1][2]


def tutanak(skor: float, seviye: str, anlam: str, args: argparse.Namespace) -> str:
    no = f"UAB-TKR-{datetime.now().strftime('%Y%m%d')}-{random.randint(1000, 9999)}"
    satirlar = [
        "=" * 62,
        "T.C. ULAŞTIRMA VE ALTYAPI BAKANLIĞI",
        "Alışveriş Arabası Sapkın Tekerlek Genel Müdürlüğü",
        "OLAĞANÜSTÜ GÜZERGÂH TUTANAĞI",
        "=" * 62,
        f"Protokol no     : {no}",
        f"Tarih           : {datetime.now().strftime('%d.%m.%Y %H:%M')}",
        f"Vatandaş        : {args.sahip}",
        f"Teker konumu    : {args.teker}",
        f"Sapma açısı     : {args.aci}°",
        f"Koridor         : {args.koridor}",
        f"Yük (kg)        : {args.yuk}",
        f"Sapma skoru     : {skor:.1f} / 100",
        f"Tehlike seviyesi: {seviye.upper()}",
        f"Tespit          : {anlam}",
        "-" * 62,
        "KARAR:",
    ]n    if args.duzgun or skor < 15:
        satirlar.append("  Barış hâli. Teker millete hizmet etmeye devam eder.")
    elif skor < 55:
        satirlar.append("  Reyon içi yavaşlatma ve sağ-sol düzeltme tavsiye edilir.")
        satirlar.append("  'Biraz iterim düzelir' ifadesi tutanağa işlendi.")
    else:
        satirlar.append("  Fil (sepet) acil park konumuna çekilir.")
        satirlar.append("  Yeni araba tahsisi için kasa önü bekletilir.")
        satirlar.append("  Sapkın teker, milli ulaşım envanterine kaydedilir.")
    satirlar.extend(
        [
            "-" * 62,
            "Bu tutanak market müdürüne, güvenliğe ve kader'e tebliğ edilir.",
            "Patates içermez. Çalışır. Şaka ciddiyetin dozundadır.",
            "=" * 62,
        ]
    )
    return "\n".join(satirlar)


def izle(args: argparse.Namespace) -> None:
    print("Canlı sapma radarı açıldı. Çıkmak için Ctrl+C.\n")
    aci = args.aci
    try:
        while True:
            aci = max(0.0, min(120.0, aci + random.uniform(-7, 11)))
            args.aci = round(aci, 1)
            skor = sapma_skoru(args.aci, args.koridor, args.yuk, False)
            seviye, anlam = seviye_bul(skor)
            print(
                f"[{datetime.now().strftime('%H:%M:%S')}] "
                f"açı={args.aci:5.1f}°  skor={skor:5.1f}  {seviye:8s}  {anlam}"
            )
            time.sleep(0.8)
    except KeyboardInterrupt:
        print("\nRadar kapatıldı. Teker hâlâ sapkın olabilir.")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Sapkın alışveriş arabası tekerleği resmi tutanak üreticisi"
    )
    p.add_argument("--aci", type=float, default=42.0, help="Sapma açısı (derece)")
    p.add_argument("--koridor", type=int, default=5, help="Market koridor numarası")
    p.add_argument("--yuk", type=float, default=8.0, help="Sepet yükü kilogram")
    p.add_argument("--teker", default="sag-on", help="Teker konumu")
    p.add_argument("--sahip", default="vatandaş", help="Arabayı süren kişi")
    p.add_argument("--duzgun", action="store_true", help="Nadir barış hâli")
    p.add_argument("--izle", action="store_true", help="Canlı sapma radarı")
    args = p.parse_args(argv)

    if args.izle:
        izle(args)
        return 0

    skor = sapma_skoru(args.aci, args.koridor, args.yuk, args.duzgun)
    seviye, anlam = seviye_bul(skor)
    print(tutanak(skor, seviye, anlam, args))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
