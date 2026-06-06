from browser import document, html, alert

styles = {
    "casual": 0,
    "minimalist": 0,
    "vintage": 0,
    "academia": 0,
    "streetwear": 0,
    "y2k": 0,
    "downtown": 0,
    "emo": 0,
    "goth": 0,
    "gyaru": 0
}

questions = [
    {
        "question": "Misalnya kamu lagi nge-scroll sosmed, jenis foto OOTD mana yang paling sering bikin kamu pencet tombol like?",
        "options": {
            "a": ("Foto ala Pinterest girl/boy yang rapi, estetik, dan minimalis", ["academia", "minimalist", "vintage"]),
            "b": ("Mirror selfie gelap misterius yang kelihatan cool dan anak musik banget", ["goth", "emo", "downtown"]),
            "c": ("Gaya tabrak warna yang rame dengan aksesoris, unik, atau tren Y2K yang lagi viral", ["streetwear", "y2k", "gyaru", "casual"]),
        }
    },
    {
        "question": "Kalau diajakin jalan dadakan di hari Sabtu, jaket/luaran (outer) apa yang akan langsung kamu ambil dari lemari?",
        "options": {
            "a": ("Blazer polos bersih atau cardigan tipis biar kelihatan rapi dan instan", ["minimalist", "academia", "casual"]),
            "b": ("Jaket kulit hitam biar sangar atau kemeja flanel oversized biar dapet vibes anak senja", ["goth", "emo", "vintage", "downtown"]),
            "c": ("Jaket denim penuh patch, hoodie oversized mencolok, atau bolero rajut warna-warni", ["gyaru", "streetwear", "y2k"]),
        }
    },
    {
        "question": "Biar bisa keliling seharian tanpa kaki pegal tapi tetep kelihatan keren, kamu bakal pilih pakai sepatu apa?",
        "options": {
            "a": ("Sepatu kulit model pantofel, loafers, atau flat shoes polos biar kelihatan pinter", ["academia", "vintage", "minimalist"]),
            "b": ("Sepatu boots hitam tebal yang kokoh atau Converse buluk yang makin kotor makin keren", ["goth", "emo", "downtown"]),
            "c": ("Chunky sneakers sol tebal, sandal Crocs penuh pin lucu, atau platform heels yang cetar", ["streetwear", "casual", "gyaru", "y2k"])
        }
    },
    {
        "question": "Kalau dikasih voucher belanja gratis di mall, toko mana yang bakal kamu datangi duluan sambil lari?",
        "options": {
            "a": ("Toko thrift (baju bekas) demi berburu kaos vintage langka atau jaket retro one of a kind", ["vintage", "emo", "downtown"]),
            "b": ("Butik minimalis Korea/Jepang yang bajunya polos, rapi, dan warnanya serba netral", ["academia", "minimalist", "casual"]),
            "c": ("Distro streetwear beken atau toko online pernak-pernik gemas ala tahun 2000-an", ["goth", "y2k", "gyaru", "minimalist"]),
        }
    },
    {
        "question": "Pas lagi jalan, tiba-tiba ada orang asing bilang: 'Style kamu keren banget!'. Bagian OOTD-mu yang mana yang bikin mereka salfok?",
        "options": {
            "a": ("Kesan pakaianku yang rapi, berkelas, dan estetik meskipun kelihatan simpel", ["academia", "vintage", "minimalist", "casual"]),
            "b": ("Vibes aku yang kelihatan misterius, cuek tapi artsy, dan beraura gelap yang kuat", ["downtown", "emo", "goth"]),
            "c": ("Aksesorisku yang rame (kayak topi beanie, headphone gede di leher, atau nail art warna-warni)", ["streetwear", "gyaru", "y2k"])
        }
    }
]

quiz_div = document["quiz"]

for i, q in enumerate(questions):
    quiz_div <= html.H3(f"{i+1}. {q['question']}")

    for key, (text, _) in q["options"].items():
        radio = html.INPUT(
            type="radio",
            name=f"q{i}",
            value=key
        )

        label = html.LABEL(f" {key}. {text}")

        container = html.DIV(Class="option")
        container <= radio
        container <= label

        quiz_div <= container

submit_btn = html.BUTTON("Lihat Hasil")
quiz_div <= submit_btn


def calculate(ev):
    global styles

    for style in styles:
        styles[style] = 0

    for i, q in enumerate(questions):

    question_box = html.DIV(Class="question-box")

    question_box <= html.H3(
        f"{i+1}. {q['question']}"
    )

    for key, (text, _) in q["options"].items():

        radio = html.INPUT(
            type="radio",
            name=f"q{i}",
            value=key
        )

        label = html.LABEL(
            f" {key}. {text}"
        )

        container = html.DIV(Class="option")

        container <= radio
        container <= label

        question_box <= container

    quiz_div <= question_box
    
    for i, q in enumerate(questions):
        selected = document.select(
            f'input[name="q{i}"]:checked'
        )

        if not selected:
            alert(f"Jawab soal nomor {i+1} dulu!")
            return

        answer = selected[0].value
        _, style_points = q["options"][answer]

        for style in style_points:
            styles[style] += 1

    highest_score = max(styles.values())

    results = [
        style
        for style, score in styles.items()
        if score == highest_score
    ]

    result_div = document["result"]

    if len(results) == 1:
        result_div.text = (
            f"Fashion style kamu adalah: "
            f"{results[0].title()}"
        )
    else:
        result_div.html = (
            "Fashion style kamu adalah kombinasi:<br>"
            + "<br>".join(
                f"• {style.title()}"
                for style in results
            )
        )


submit_btn.bind("click", calculate)
