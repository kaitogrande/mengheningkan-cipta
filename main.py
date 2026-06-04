from browser import document, html
from collections import Counter

daftar_pertanyaan = [
    {
        "soal": "Gimana kamu menilai kepribadianmu?",
        "pilihan": [
            {"teks": "Simpel, anti ribet, dan seadanya.", "styles": ["casual", "minimalist"]},
            {"teks": "Aku seorang yang gampang berempati.", "styles": ["vintage", "academia"]},
            {"teks": "Aku orang yang gampang bergaul.", "styles": ["streetwear", "y2k", "downtown"]},
            {"teks": "Aku orang yang pede dan mandiri.", "styles": ["emo", "goth"]}
        ]
    },
    {
        "soal": "Prioritas utamamu saat mencari baju adalah ...",
        "pilihan": [
            {"teks": "Yang penting simpel.", "styles": ["minimalist"]},
            {"teks": "Yang penting menawan.", "styles": ["vintage", "academia"]},
            {"teks": "Yang penting nyaman.", "styles": ["casual", "streetwear"]},
            {"teks": "Yang penting kece.", "styles": ["emo", "goth", "y2k"]}
        ]
    }
]

skor = Counter()
nomor = 0

quiz = document["quiz"]

def tampilkan_hasil():
    quiz.clear()

    dominan = skor.most_common(1)[0][0]

    quiz <= html.H2(
        f"Gaya pakaian yang paling cocok buat kamu adalah: {dominan.upper()}"
    )

    ul = html.UL()

    for style, jumlah in skor.most_common():
        ul <= html.LI(f"{style}: {jumlah} poin")

    quiz <= ul


def pilih(event):
    global nomor

    styles = event.target.attrs["data-styles"].split(",")

    for s in styles:
        skor[s] += 1

    nomor += 1

    if nomor >= len(daftar_pertanyaan):
        tampilkan_hasil()
    else:
        tampilkan_pertanyaan()


def tampilkan_pertanyaan():
    quiz.clear()

    data = daftar_pertanyaan[nomor]

    quiz <= html.H2(
        f"{nomor+1}. {data['soal']}"
    )

    for opsi in data["pilihan"]:
        btn = html.BUTTON(
            opsi["teks"],
            Class="pilihan"
        )

        btn.attrs["data-styles"] = ",".join(
            opsi["styles"]
        )

        btn.bind("click", pilih)

        quiz <= btn
        quiz <= html.BR()
        quiz <= html.BR()


tampilkan_pertanyaan()
