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
    "goth": 0
}

questions = [
    {
        "question": "Gimana kamu menilai kepribadianmu?",
        "options": {
            "a": ("Simpel, anti ribet, dan seadanya", ["casual", "minimalist"]),
            "b": ("Aku seorang yang gampang berempati, sedikit sensitif, dan menyukai hal yang indah", ["vintage", "academia"]),
            "c": ("Aku orang yang gampang bergaul, humoris, dan petualang", ["streetwear", "y2k", "downtown"]),
            "d": ("Aku orang yang pede, mandiri, blak-blakan", ["emo", "goth"])
        }
    },
    {
        "question": "Prioritas utamamu saat mencari baju adalah…",
        "options": {
            "a": ("Yang penting simple", ["minimalist"]),
            "b": ("Yang penting cool", ["vintage", "academia"]),
            "c": ("Yang penting nyaman", ["casual", "streetwear", "downtown"]),
            "d": ("Yang penting 'ini aku banget!'", ["goth", "emo", "y2k"])
        }
    },
    {
        "question": "Berapa lama kamu memilih baju?",
        "options": {
            "a": ("10 menit-an", ["casual", "streetwear", "downtown"]),
            "b": ("1 jam lebih", ["academia", "vintage"]),
            "c": ("Kurang dari 5 menit", ["minimalist", "casual"]),
            "d": ("Berjam-jam", ["goth", "y2k", "emo"])
        }
    },
    {
        "question": "Desain sepatu apa yang paling kamu suka?",
        "options": {
            "a": ("Sneakers yang eye-catching", ["streetwear"]),
            "b": ("Sepatu kulit", ["academia", "downtown"]),
            "c": ("Sandal/sepatu slip-on", ["casual", "minimalist"]),
            "d": ("Boots second", ["vintage", "y2k", "goth"])
        }
    },
    {
        "question": "Apa warna utama dari koleksi pakaianmu?",
        "options": {
            "a": ("Warna-warna ceria dan mencolok", ["y2k", "casual"]),
            "b": ("Warna-warna yang aman", ["minimalist", "streetwear", "emo", "goth"]),
            "c": ("Warna-warna yang hangat", ["vintage", "downtown"])
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
