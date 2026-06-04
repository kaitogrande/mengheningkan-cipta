  <title>FaSHion : What's Your Style!</title>

    <script src="https://cdn.jsdelivr.net/npm/brython@3/brython.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/brython@3/brython_stdlib.js"></script>

    <style>
        body{
            font-family: Arial, sans-serif;
            max-width:800px;
            margin:auto;
            padding:20px;
        }

        button{
            display:block;
            width:100%;
            margin:10px 0;
            padding:12px;
            cursor:pointer;
        }

        .hasil{
            background:#f4f4f4;
            padding:15px;
            border-radius:10px;
        }
    </style>
</head>

<body onload="brython()">

<h1>FaSHion : Show Your Fits!</h1>
<p>Cari tahu fashion style tersembunyimu</p>

<div id="quiz"></div>

<script type="text/python">
from browser import document, html, window

# 1. Menggunakan daftar pertanyaan asli milikmu dengan sistem pencatatan bobot gaya (styles)
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

# 2. PROSES OTOMATIS MERENDER PERTANYAAN KE WEBPAGE
zone_quiz = document["quiz"]

for idx, item in enumerate(daftar_pertanyaan, 1):
    p_soal = html.P(html.B(f"{idx}. {item['soal']}"))
    select_opsi = html.SELECT(id=f"q{idx}")
    
    # Memasukkan pilihan jawaban ke menu dropdown select
    for o_idx, opsi in enumerate(item["pilihan"]):
        select_opsi <= html.OPTION(opsi["teks"], value=str(o_idx))
        
    zone_quiz <= p_soal
    zone_quiz <= select_opsi

# Menyiapkan elemen tombol kirim kuis dan kotak hasil visual
tombol_submit = html.BUTTON("Cek Hasil Style Kamu", id="submit")
div_hasil = html.DIV(id="hasil")
zone_quiz <= tombol_submit
zone_quiz <= div_hasil

# Fungsi pengarah tautan ketika tombol "Learn More" ditekan
def buka_canva(ev):
    # GANTI LINK DI BAWAH INI DENGAN TAUTAN CANVA MILIKMU
    link_canva = "https://www.canva.com"
    window.open(link_canva, "_blank")

# 3. FUNGSI LOGIKA MENGHITUNG MULTI-STYLE DENGAN SIMULASI COUNTER
def cek(ev):
    # Menggunakan dictionary biasa untuk mensimulasikan sistem kerja Counter
    skor_style = {}
    
    for i in range(1, 14):
        o_idx = int(document[f"q{i}"].value)
        styles_terpilih = daftar_pertanyaan[i-1]["pilihan"][o_idx]["styles"]
        
        # Tambahkan poin ke style yang cocok dengan pilihan pengguna
        for s in styles_terpilih:
            skor_style[s] = skor_style.get(s, 0) + 1
            
    # Mencari style dengan nilai poin tertinggi
    style_dominan = max(skor_style, key=skor_style.get)
    
    # Menyusun teks rincian poin grafik untuk ditampilkan
    rincian_poin = ""
    for style, jumlah in sorted(skor_style.items(), key=lambda item: item[1], reverse=True):
        rincian_poin += f"<li><b>{style.capitalize()}</b>: {jumlah} poin</li>"

    # Menampilkan container kotak hasil kuis
    document["hasil"].style.display = "block"
    
    # 4. MEMBUAT TAMPILAN HASIL DAN TOMBOL LEARN MORE DI BAWAHNYA
    document["hasil"].html = f"""
        <h2>============== FaSHion SHOW RESULTS! ==============</h2>
        <h3>Gaya pakaian yang paling cocok buat kamu adalah: <br>
            <b style='color:#ff4081; font-size:24px;'>✨ {style_dominan.upper()} ✨</b>
        </h3>
        <p>Grafik perolehan poin gayamu:</p>
        <ul>{rincian_poin}</ul>
        <br>
        <button id='btn-learn-more' style='background-color: #00c4cc; color: white; border: none; padding: 12px; width: 100%; border-radius: 5px; font-weight: bold; cursor: pointer; font-size: 16px;'>
            📖 Learn More (Buka PPT Canva)
        </button>
    """
    
    # Mengaktifkan fungsi klik link Canva pada tombol Learn More baru
    document["btn-learn-more"].bind("click", buka_canva)

# Mengikat tombol submit utama dengan fungsi penghitung kalkulasi skor
document["submit"].bind("click", cek)
</body>
</html>
