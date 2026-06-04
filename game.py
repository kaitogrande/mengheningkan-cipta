from browser import document, html

# 1. DAFTAR 13 PERTANYAAN KUIS BESERTA SKOR VALUE-NYA
daftar_pertanyaan = [
    {
        "soal": "Gimana kamu menilai kepribadianmu?",
        "pilihan": [
            {"teks": "A. Simpel, anti ribet, dan seadanya.", "value": 2},
            {"teks": "B. Aku seorang yang gampang berempati, sedikit sensitif, dan menyukai hal yang indah.", "value": 3},
            {"teks": "C. Aku orang yang gampang bergaul, humoris, dan petualang.", "value": 4},
            {"teks": "D. Aku, sih orang yang pede, mandiri, dan blak-blakan, ya.", "value": 1}
        ]
    },
    {
        "soal": "Prioritas utamamu saat mencari baju adalah ...",
        "pilihan": [
            {"teks": "A. Yang penting simpel.", "value": 2},
            {"teks": "B. Yang penting menawan.", "value": 3},
            {"teks": "C. Yang penting nyaman.", "value": 2},
            {"teks": "D. Yang penting kece.", "value": 4}
        ]
    },
    {
        "soal": "Berapa lama kamu memilih baju?",
        "pilihan": [
            {"teks": "A. Kurang lebih 10 menitan.", "value": 2},
            {"teks": "B. Kurang lebih satu jam, karena enggak pengin salah kostum.", "value": 3},
            {"teks": "C. Kurang dari 5 menit, ambil apapun yang terlihat mata.", "value": 2},
            {"teks": "D. Terlalu lama! Aku biasanya mencoba beragam baju sebelum menentukan satu pilihan.", "value": 4}
        ]
    },
    {
        "soal": "Fashion item kesukaanmu adalah ...",
        "pilihan": [
            {"teks": "A. Kaos.", "value": 2},
            {"teks": "B. Aksesoris keren.", "value": 3},
            {"teks": "C. Jeans.", "value": 4},
            {"teks": "D. Apapun dengan motif yang ramai dan unik.", "value": 1}
        ]
    },
    {
        "soal": "Sepatu seperti apa yang biasanya sering kamu pakai?",
        "pilihan": [
            {"teks": "A. Flat shoes", "value": 2},
            {"teks": "B. Sneakers", "value": 4},
            {"teks": "C. Boots.", "value": 1}
        ]
    },
    {
        "soal": "Kalau lagi jalan - jalan di mall, toko mana yang pasti kamu kunjungi?",
        "pilihan": [
            {"teks": "A. Toko brand lokal dengan desain unik", "value": 4},
            {"teks": "B. Butik desainer ternama", "value": 2},
            {"teks": "C. Fashion thrift shop", "value": 3}
        ]
    },
    {
        "soal": "Apa yang kamu pilih untuk acara hangout sore di cafe kekinian?",
        "pilihan": [
            {"teks": "A. Kemeja", "value": 3},
            {"teks": "B. Basic outfit dengan cardigan", "value": 2},
            {"teks": "C. Jeans favorit dengan baju vintage", "value": 4},
            {"teks": "D. Outfit dengan banyak aksesoris", "value": 1}
        ]
    },
    {
        "soal": "Desain sepatu apa yang paling kamu suka?",
        "pilihan": [
            {"teks": "A. Sneakers yang eye catching", "value": 4},
            {"teks": "B. Sepatu kulit", "value": 3},
            {"teks": "C. Sandal slip-on / crocs", "value": 2},
            {"teks": "D. Boots second (hidden gem)", "value": 1}
        ]
    },
    {
        "soal": "Apa warna utama dari koleksi pakaian kamu?",
        "pilihan": [
            {"teks": "A. Warna-warna ceria kayak kuning dan hijau", "value": 4},
            {"teks": "B. Gradasi netral seperti hitam, putih, dan abu abu", "value": 2},
            {"teks": "C. Warm tone seperti coklat dan maroon", "value": 3}
        ]
    },
    {
        "soal": "Bagaimana caramu mengungkapkan diri lewat fashion?",
        "pilihan": [
            {"teks": "A. Melalui pernak pernik aksesoris lucu", "value": 4},
            {"teks": "B. Pakaian yang elegan dan glamour", "value": 3},
            {"teks": "C. Style yang nyaman dan simple", "value": 2}
        ]
    },
    {
        "soal": "Apa manfaat fashion bagi kalian?",
        "pilihan": [
            {"teks": "A. Jadi lebih percaya diri", "value": 4},
            {"teks": "B. Hanya untuk penampilan", "value": 3},
            {"teks": "C. Tidak ada", "value": 2},
            {"teks": "D. Membuat orang lain terkesan", "value": 1}
        ]
    },
    {
        "soal": "Apa yang saat kalian rasakan saat menemukan outfit yang cocok?",
        "pilihan": [
            {"teks": "A. Bingung", "value": 3},
            {"teks": "B. Percaya diri", "value": 4},
            {"teks": "C. Tidak peduli", "value": 2}
        ]
    },
    {
        "soal": "Apa yang bisa meningkatkan rasa percaya diri?",
        "pilihan": [
            {"teks": "A. Penampilan yang menarik", "value": 4},
            {"teks": "B. Kualitas bahan pakaian", "value": 3},
            {"teks": "C. Harga pakaian yang terjangkau", "value": 2},
            {"teks": "D. Model pakaian trendy", "value": 2}
        ]
    }
]

# 2. PROSES MEMASUKKAN SOAL-SOAL KE HALAMAN WEB SECARA OTOMATIS
zone_quiz = document["quiz"]

for idx, item in enumerate(daftar_pertanyaan, 1):
    # Membuat teks pertanyaan <p><b>
    p_soal = html.P(html.B(f"{idx}. {item['soal']}"))
    
    # Membuat kotak pilihan dropdown <select>
    select_opsi = html.SELECT(id=f"q{idx}")
    for opsi in item["pilihan"]:
        select_opsi <= html.OPTION(opsi["teks"], value=str(opsi["value"]))
        
    # Memasukkan ke dalam elemen id="quiz"
    zone_quiz <= p_soal
    zone_quiz <= select_opsi

# 3. MEMBUAT TOMBOL SUBMIT DAN KOTAK HASIL DI BAWAH SOAL
tombol_submit = html.BUTTON("Cek Hasil Style Kamu", id="submit")
div_hasil = html.DIV(id="hasil")

zone_quiz <= tombol_submit
zone_quiz <= div_hasil

# 4. FUNGSI LOGIKA MENGHITUNG TOTAL SKOR DAN MENENTUKAN STYLE
def cek(ev):
    total = 0
    # Mengambil nilai angka q1 sampai q13 lalu dijumlahkan
    for i in range(1, 14):
        nilai = int(document[f"q{i}"].value)
        total += nilai
        
    # Pembagian kategori style fashion berdasarkan rentang total skor harian
    if total >= 42:
        style = "STREETWEAR / Y2K"
        detail = "Gaya kamu bold, penuh warna, dan selalu up-to-date sama tren masa kini!"
    elif total >= 32:
        style = "ACADEMIA / VINTAGE"
        detail = "Kamu suka vibes yang estetik, rapi, klasik, dan kelihatan cerdas banget!"
    elif total >= 22:
        style = "CASUAL / MINIMALIST"
        detail = "Kamu tipe yang mengutamakan kenyamanan! Simpel, anti ribet, tapi tetep rapi."
    else:
        style = "EMO / GOTH"
        detail = "Misterius, penuh ekspresi, cool, dan didominasi aura warna gelap yang kuat!"

    # Menampilkan hasil kuis ke layar browser
    document["hasil"].style.display = "block"
    document["hasil"].html = f"<h3>Fashion Style kamu adalah:<br><b style='color:#ff4081; font-size:22px;'>{style}</b></h3><p>{detail}</p><hr><small>Total Skor Anda: {total}</small>"

# Menyambungkan tombol klik dengan fungsi cek matematika di atas
document["submit"].bind("click", cek)
