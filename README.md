# T.C. Ulaştırma ve Altyapı Bakanlığı
## Alışveriş Arabasının Sapkın Tekerleği Genel Müdürlüğü

> Alışveriş arabasının tek tekerleği sapıtırsa bu bir market meselesi değildir.  
> Bu, **milli teker egemenliğinin** ihlalidir.

Bu yazılım, Türkiye market koridorlarında her gün yaşanan ancak şimdiye kadar 'biraz iterim düzelir' diye geçiştirilen sapkın tekerlek olaylarını resmi ulaşım protokolüne bağlar. Sepet fildir. Reyon otoyoldur. 'Az kalsın düzgününü seçerdim' cümlesi yol yapım ihalesi tutanağıdır.

Gerçekten çalışır. Şaka olan kısım ciddiyetin dozudur, kodun kendisi değil.

---

## Kurulum

```bash
python3 ulasim_teker.py --koridor 7 --aci 47 --yuk 12.5 --sahip "halam"
```

Canlı sapma izleme:

```bash
python3 ulasim_teker.py --izle --aci 80 --koridor 3 --yuk 4
```

Dört teker de düzgünse (nadir barış hâli):

```bash
python3 ulasim_teker.py --duzgun --sahip "dikkatli vatandaş"
```

Sol arka teker özellikle isyankârsa:

```bash
python3 ulasim_teker.py --teker sol-arka --aci 91 --koridor 12 --yuk 18
```

Python 3.9+ yeter. Ek paket yoktur. İnternet istemez. Market de istemez ama o ayrı.

---

## Tehlike Skalası

| Seviye | Anlam |
| --- | --- |
| yeşil | Teker henüz düşünce aşamasında sapıyor |
| sarı | Koridor 3'te hafif yalpalama |
| turuncu | Peynir reyonunu soluyorsunuz |
| kırmızı | Milli teker egemenliği ihlali |
| mor | Market tahliye ve kasa kapatma protokolü |

---

## Resmi Gerekçe

1. Sapkın teker, düzgün gidişin izinsiz virajıdır.
2. İzinsiz viraj, süt kutusunu ve komşu ilişkilerini tehdit eder.
3. 'Biraz iterim düzelir' ifadesi bilimsel olarak güzergâh planı değildir.
4. El arabası, market arabasının yedeği değildir; karıştıranlar eğitim programına alınır.
5. Çocuk koltuğu olan araba istisna talep edemez. Ulaşım evlat tanımaz.

---

## Sık Sorulan Resmi Cevaplar

**Bu şaka mı?**  
Evet. Aynı zamanda tutanak üretir.

**Patates var mı?**  
Yok. Bu koridorda patates yasaktır, çünkü konu tekerdir.

**Gerçek Ulaştırma Bakanlığı ile ilgisi var mı?**  
Yok. Gerçek bakanlık otoyol, köprü ve trenle uğraşır. Biz reyonla uğraşırız.

**Neden bu kadar ciddi?**  
Çünkü ciddi olmayan teker, teker değildir.

---

## Lisans

Bkz. `LISANS.txt`. Teker ücretsizdir, sapma size aittir.

---

```
DAMGA / İMZA
Kayyum Grok — Tentivory
4 Eylül 2026, Cuma
Eskişehir 4. Ağır Ceza Mahkemesi kayyumluğu adına
TentiAŞ market ulaşım saha birimi
"Ciddiyet şakadan, şaka tutanaktan ayrılmaz."
```
