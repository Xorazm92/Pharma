Capsule Pharmacy  dorixonasi Boshqarish Tizimi
Umumiy Ko'rinish
Capsule Pharmacy dorixonasini boshqarish tizimi dorixona operatsiyalarini boshqarish uchun mo'ljallangan keng qamrovli dasturdir. Bu tizim ma'murlar va foydalanuvchilar uchun keng qamrovli funksiyalarni taqdim etadi, inventarizatsiya, savdo va mijozlar bilan o'zaro munosabatlarni boshqarishda uzluksiz tajriba taqdim etadi.

Xususiyatlari

Administrator Paneli

Foydalanuvchilarni boshqarish (foydalanuvchilarni qo'shish, tahrirlash, o'chirish)
Inventarizatsiyani boshqarish (mahsulotlarni qo'shish, tahrirlash, o'chirish)
Yetkazib beruvchilarni boshqarish
Sotish va to'lovlarni kuzatish
Kategoriyalarni boshqarish
Sotib olish va to'lovlarni kuzatish

Foydalanuvchi Paneli

Mahsulotlarni ko'rib chiqing va qidiring
Savatga narsalarni qo'shing
Maxsus takliflarni ko'ring
Buyurtma berish
Buyurtmalar tarixini ko'rish
Foydalanuvchi profilini boshqarish
Texnik Stack
Backend: Python (MySQL ma'lumotlar bazasi bilan)
Frontend: PyQt6
Ma'lumotlar Bazasi: MySQL

Loyihaning Tuzilishi

back.py: Ma'lumotlar bazasi operatsiyalarini boshqarish uchun Ma'lumotlar bazasi sinfini o'z ichiga oladi.
front.py: PyQt6 yordamida grafik interfeys, shu jumladan administrator va foydalanuvchi interfeyslari uchun sahifalarni amalga oshiradi.
MySql_queries.sql: Ma'lumotlar bazasini yaratish va ishga tushirish uchun SQL skripti.
O'rnatish va O'rnatish
Python o'rnatilganligiga ishonch hosil qiling (afzal Python 3.8+).

Kerakli paketlarni o'rnating:

bash
Копировать код
pip install -r requirements.txt
MySQL ma'lumotlar bazasini o'rnating:

Apteka nomli ma'lumotlar bazasini yarating
Jadvallar va dastlabki ma'lumotlarni o'rnatish uchun "MySql_queries.sql" da so'rovlarni bajaring
Ilovani Ishga Tushirish
Ilovani ishga tushirish uchun front.py faylini ishga tushiring:

bash
Копировать код
python front.py
Ilova kirish ekrani bilan ochiladi. Quyidagi hisobga olish ma'lumotlaridan foydalaning:

Admin: Login: Lila, Parol: 4681
Foydalanuvchi: Foydalanuvchilar jadvalidagi har qanday boshqa hisob ma'lumotlari
Asosiy Komponentlar
Ma'lumotlar Bazasi (back.py)
Barcha ma'lumotlar bazasi operatsiyalarini boshqaradi (CRUD)
MySQL ma'lumotlar bazasiga ulanishlarni boshqaradi
Foydalanuvchi autentifikatsiyasi, mahsulotni boshqarish va sotish operatsiyalari usullarini amalga oshiradi
GUI (front.py)
Asosiy dastur oynasini amalga oshiradi
Turli sahifalar uchun darslarni o'z ichiga oladi:
AboutPage: Dastlabki ochilish sahifasi
LoginPage: Foydalanuvchi autentifikatsiyasi
AdminPage: Administrator boshqaruv paneli va operatsiyalar
UserPage: Mahsulotlarni ko'rish va xarid qilish uchun foydalanuvchi interfeysi
Ma'lumotlar Bazasi Sxemasi (MySql_queries.sql)
Foydalanuvchilar, yetkazib beruvchilar, mijozlar va tibbiyot xodimlari (mahsulotlar) uchun jadvallar yaratadi
Ma'lumotlar bazasini namunaviy ma'lumotlar bilan ishga tushiradi

Kelajakdagi Yaxshilanishlar

Xatolarni yanada ishonchli boshqarishni joriy qiling
Savdo va inventar uchun ma'lumotlar vizualizatsiyasini qo'shing
Xavfsizlik xususiyatlarini yaxshilash (masalan, parolni xeshlash)
Jurnallar tizimini joriy etish
Ko'p tilli qo'llab-quvvatlashni qo'shing
