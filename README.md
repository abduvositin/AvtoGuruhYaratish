# 🚗 AvtoGuruhYaratish

**AvtoGuruhYaratish** — bu Python yordamida avtomatik tarzda **Telegram superguruh** yaratadigan va unga oldindan belgilangan **botlarni qo‘shib, admin qiladigan** scriptdir.

Bu script sizga avtomatik ravishda quyidagi ishlarni bajaradi:
- Telegram hisobingiz orqali yangi superguruh ochadi
- Guruh nomini va ID sini faylga yozadi
- Guruh tarixini ochadi (ko‘rinadigan qiladi)
- Belgilangan botlarni guruhga qo‘shadi
- Har bir botga kerakli admin huquqlarini beradi

---

## 📦 Talablar

Quyidagi kutubxonani o‘rnatishingiz kerak:

```bash
pip install telethon
```

---

## ⚙️ Sozlamalar

```python
api_id = API_ID
api_hash = 'API_HASH'
phone = 'PHONE NUMBER'

BOT_USERNAMES = ['sokmang_bot', 'JoinDelBot', 'TozaIovchi_Bot']
```

> ⚠️ `api_id`, `api_hash` va `phone` o‘z hisobingizga tegishli bo‘lishi kerak. Maxfiy ma’lumotlarni `.env` orqali saqlash tavsiya etiladi.
> Api id va hashni [my.telegram.org](https://my.telegram.org/auth) sayitidan olasiz

---

## 💻 Ishlash prinsipi

1. **Telegram hisobiga ulanadi**  
2. **Yangi superguruh yaratadi** (`SupperGuruh YYYY-MM-DD-HH-MM-SS` nomi bilan)
3. **Guruh ID va nomini** `2025/IYUN2/guruhlar.txt` fayliga yozadi
4. **Guruh tarixini ochadi** (chat tarixi ko‘rinadigan bo‘ladi)
5. **Botlarni guruhga qo‘shadi**
6. **Botlarni admin qiladi** quyidagi huquqlar bilan:
   - Post yuborish
   - Xabar o‘chirish
   - Xabar tahrirlash
   - Pin qo‘yish
   - Odam qo‘shish

---

## 🕒 Takroriy ish

Skript har 10 soniyada yangi guruh yaratadi:

```python
while True:
    await create_supergroup()
    await asyncio.sleep(10)
```

---

## 🧾 Guruhlar ro‘yxati fayli

Har bir yaratilgan guruh quyidagi faylga yoziladi:

```
📁 2025/guruhlar.txt

Guruh nomi: SupperGuruh 2025-08-07-22-30-12
Guruh ID: 123456789
------------------------------
```

---

## 🔐 Maxfiylik

- API ID va HASH maxfiy saqlanishi kerak
- Agar hisobingizda **2 bosqichli autentifikatsiya (2FA)** bo‘lsa, script sizdan parolni so‘raydi
- Faollikni cheklash uchun Telegram limitlariga e’tibor bering

---

## 📂 Loyihaning tuzilishi

```
AvtoGuruhYaratish/
├── my_session.session       # Telegram sessiyasi fayli
├── guruhlar.txt             # Yaratilgan guruhlar log fayli
└── main.py                  # Asosiy script
```

