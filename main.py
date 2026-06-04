  <title>FaSHion : Show Your Fits!</title>

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

from browser import document, html
from collections import Counter

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

skor_style = Counter()
nomor_soal = 0
quiz = document["quiz"]

def tampilkan_hasil():
    quiz.clear()

    style_dominan = skor_style.most_common(1)[0][0]

    box = html.DIV(Class="hasil")

    box <= html.H2("FaSHion SHOW RESULTS")
    box <= html.H3(
        f"Gaya pakaian yang paling cocok buat kamu adalah: ✨ {style_dominan.upper()} ✨"
    )

    box <= html.H4("Grafik Perolehan Poin")

    ul = html.UL()

    for style, jumlah in skor_style.most_common():
        ul <= html.LI(f"{style.capitalize()} : {jumlah} poin")

    box <= ul
    quiz <= box

def pilih(event):
    global nomor_soal

    styles = event.target.attrs["data-styles"].split(",")

    for s in styles:
        skor_style[s] += 1

    nomor_soal += 1

    if nomor_soal >= len(daftar_pertanyaan):
        tampilkan_hasil()
    else:
        tampilkan_soal()

def tampilkan_soal():
    quiz.clear()

    soal = daftar_pertanyaan[nomor_soal]

    quiz <= html.H2(
        f"Soal {nomor_soal+1} dari {len(daftar_pertanyaan)}"
    )

    quiz <= html.P(soal["soal"])

    for opsi in soal["pilihan"]:
        tombol = html.BUTTON(opsi["teks"])

        tombol.attrs["data-styles"] = ",".join(
            opsi["styles"]
        )

        tombol.bind("click", pilih)

        quiz <= tombol

tampilkan_soal()

</script>
