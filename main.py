# -*- coding: utf-8 -*-
from collections import Counter

def kuis_fashion_style():
    # 1. Daftar pertanyaan lengkap beserta bobot multi-style hasil pemetaan dari catatanmu
    daftar_pertanyaan = [
        {
            "soal": "Gimana kamu menilai kepribadianmu?",
            "pilihan": [
                {"teks": "A. Simpel, anti ribet, dan seadanya.", "styles": ["casual", "minimalist"]},
                {"teks": "B. Aku seorang yang gampang berempati, sedikit sensitif, dan menyukai hal yang indah.", "styles": ["vintage", "academia"]},
                {"teks": "C. Aku orang yang gampang bergaul, humoris, dan petualang.", "styles": ["streetwear", "y2k", "downtown"]},
                {"teks": "D. Aku, sih orang yang pede, mandiri, dan blak-blakan, ya.", "styles": ["emo", "goth"]}
            ]
        },
        {
            "soal": "Prioritas utamamu saat mencari baju adalah ...",
            "pilihan": [
                {"teks": "A. Yang penting simpel.", "styles": ["minimalist"]},
                {"teks": "B. Yang penting menawan.", "styles": ["vintage", "academia"]},
                {"teks": "C. Yang penting nyaman.", "styles": ["casual", "streetwear", "downtown"]},
                {"teks": "D. Yang penting kece.", "styles": ["emo", "goth", "y2k"]}
            ]
        },
        {
            "soal": "Berapa lama kamu memilih baju?",
            "pilihan": [
                {"teks": "A. Kurang lebih 10 menitan.", "styles": ["casual", "streetwear", "downtown"]},
                {"teks": "B. Kurang lebih satu jam, karena enggak pengin salah kostum.", "styles": ["academia", "vintage"]},
                {"teks": "C. Kurang dari 5 menit, ambil apapun yang terlihat mata.", "styles": ["minimalist"]},
                {"teks": "D. Terlalu lama! Aku biasanya mencoba beragam baju sebelum menentukan satu pilihan.", "styles": ["emo", "goth", "y2k"]}
            ]
        },
        {
            "soal": "Fashion item kesukaanmu adalah ...",
            "pilihan": [
                {"teks": "A. Kaos.", "styles": ["casual", "minimalist"]},
                {"teks": "B. Aksesoris keren.", "styles": ["vintage", "academia"]},
                {"teks": "C. Jeans.", "styles": ["streetwear", "downtown"]},
                {"teks": "D. Apapun dengan motif yang ramai dan unik.", "styles": ["emo", "goth", "y2k"]}
            ]
        },
        {
            "soal": "Sepatu seperti apa yang biasanya sering kamu pakai?",
            "pilihan": [
                {"teks": "A. Flat shoes", "styles": ["casual", "minimalist", "academia"]},
                {"teks": "B. Sneakers", "styles": ["downtown", "streetwear", "y2k"]},
                {"teks": "C. Boots.", "styles": ["goth", "emo"]}
            ]
        },
        {
            "soal": "Kalau lagi jalan - jalan di mall, toko mana yang pasti kamu kunjungi?",
            "pilihan": [
                {"teks": "A. Toko brand lokal dengan desain unik", "styles": ["y2k", "emo", "goth"]},
                {"teks": "B. Butik desainer ternama", "styles": ["academia", "casual"]},
                {"teks": "C. Fashion thrift shop", "styles": ["minimalist", "vintage", "downtown", "streetwear"]}
            ]
        },
        {
            "soal": "Apa yang kamu pilih untuk acara hangout sore di cafe kekinian?",
            "pilihan": [
                {"teks": "A. Kemeja", "styles": ["minimalist", "academia", "vintage"]},
                {"teks": "B. Basic outfit dengan cardigan", "styles": ["casual"]},
                {"teks": "C. Jeans favorit dengan baju vintage", "styles": ["streetwear", "downtown"]},
                {"teks": "D. Outfit dengan banyak aksesoris", "styles": ["emo", "goth", "y2k"]}
            ]
        },
        {
            "soal": "Desain sepatu apa yang paling kamu suka?",
            "pilihan": [
                {"teks": "A. Sneakers yang eye catching", "styles": ["streetwear", "downtown"]},
                {"teks": "B. Sepatu kulit", "styles": ["academia", "vintage"]},
                {"teks": "C. Sandal slip-on / crocs", "styles": ["casual", "vintage"]},
                {"teks": "D. Boots second (hidden gem)", "styles": ["y2k", "emo", "goth"]}
            ]
        },
        {
            "soal": "Apa warna utama dari koleksi pakaian kamu?",
            "pilihan": [
                {"teks": "A. Warna-warna ceria kayak kuning dan hijau", "styles": ["y2k", "casual"]},
                {"teks": "B. Gradasi netral seperti hitam, putih, dan abu abu", "styles": ["minimalist", "streetwear", "downtown", "emo", "goth"]},
                {"teks": "C. Warm tone seperti coklat dan maroon", "styles": ["vintage", "academia"]}
            ]
        },
        {
            "soal": "Bagaimana caramu mengungkapkan diri lewat fashion?",
            "pilihan": [
                {"teks": "A. Melalui pernak pernik aksesoris lucu", "styles": ["y2k", "emo", "goth"]},
                {"teks": "B. Pakaian yang elegan dan glamour", "styles": ["academia", "casual", "vintage"]},
                {"teks": "C. Style yang nyaman dan simple", "styles": ["minimalist", "streetwear", "downtown"]}
            ]
        },
        {
            "soal": "Apa manfaat fashion bagi kalian?",
            "pilihan": [
                {"teks": "A. Jadi lebih percaya diri", "styles": ["emo", "goth", "gyaru", "y2k"]},
                {"teks": "B. Hanya untuk penampilan", "styles": ["casual", "vintage", "academia"]},
                {"teks": "C. Tidak ada", "styles": ["minimalist", "casual", "streetwear", "downtown"]},
                {"teks": "D. Membuat orang lain terkesan", "styles": ["goth", "emo", "y2k"]}
            ]
        },
        {
            "soal": "Apa yang saat kalian rasakan saat menemukan outfit yang cocok?",
            "pilihan": [
                {"teks": "A. Bingung", "styles": ["academia"]},
                {"teks": "B. Percaya diri", "styles": ["goth", "y2k", "academia", "emo", "casual", "vintage"]},
                {"teks": "C. Tidak peduli", "styles": ["minimalist", "downtown", "streetwear"]}
            ]
        },
        {
            "soal": "Apa yang bisa meningkatkan rasa percaya diri?",
            "pilihan": [
                {"teks": "A. Penampilan yang menarik", "styles": ["emo", "goth", "gyaru", "y2k"]},
                {"teks": "B. Kualitas bahan pakaian", "styles": ["vintage", "academia"]},
                {"teks": "C. Harga pakaian yang terjangkau", "styles": ["vintage", "streetwear", "downtown", "casual", "minimalist"]},
                {"teks": "D. Model pakaian trendy", "styles": ["casual", "minimalist"]}
            ]
        }
    ]

    # Tempat mengumpulkan semua poin untuk tiap style
    skor_style = Counter()

    # Tampilan Judul Resmi
    print("==================================================")
    print("            FaSHion : Show Your Fits!             ")
    print("      Cari tahu fashion style tersembunyimu      ")
    print("==================================================\n")

    # 2. Perulangan untuk menjalankan kuis
    for i, item in enumerate(daftar_pertanyaan, 1):
        print(f"{i}. {item['soal']}")

        # Membuat penanda pilihan otomatis (A, B, C, D)
        pilihan_valid = [chr(65 + idx) for idx in range(len(item['pilihan']))]

        for opsi in item['pilihan']:
            print(opsi['teks'])

        # Mengunci input pengguna agar tidak eror
        while True:
            jawaban = input(f"Jawabanmu ({'/'.join(pilihan_valid)}): ").upper()
            if jawaban in pilihan_valid:
                indeks_pilihan = pilihan_valid.index(jawaban)
                styles_terpilih = item['pilihan'][indeks_pilihan]['styles']

                # Menambahkan poin ke setiap style yang terkait dengan pilihan tersebut
                for s in styles_terpilih:
                    skor_style[s] += 1

                print("-" * 50)
                break
            else:
                print(f"Input salah! Silakan pilih antara {' atau '.join(pilihan_valid)}.")

    # 3. Menentukan pemenang style berdasarkan skor tertinggi
    style_dominan = skor_style.most_common(1)[0][0]

    # 4. Tampilan Hasil Akhir Kuis
    print("\n" + "="*18 + " FaSHion SHOW RESULTS " + "="*18)
    print(f" Gaya pakaian yang paling cocok buat kamu adalah: ✨ {style_dominan.upper()} ✨")
    print("=" * 58)

    print("\nGrafik perolehan poin gayamu:")
    # Menampilkan semua poin dari yang tertinggi ke terendah
    for style, jumlah in skor_style.most_common():
        print(f"- {style.capitalize()}: {jumlah} poin")

if __name__ == "__main__":
    kuis_fashion_style()