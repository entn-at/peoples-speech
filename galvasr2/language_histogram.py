from pyspark.sql import Row

# language_counts =  [Row(language='en', count=16871),
#  Row(language='nb', count=4),
#  Row(language='ro', count=28),
#  Row(language='sl', count=1),
#  Row(language='pl', count=8),
#  Row(language='sk', count=2),
#  Row(language='pt', count=56),
#  Row(language='ko', count=5),
#  Row(language='ms', count=20),
#  Row(language='cs', count=6),
#  Row(language='qu', count=10),
#  Row(language='tr', count=9),
#  Row(language='de', count=17),
#  Row(language='is', count=1),
#  Row(language='br', count=2),
#  Row(language='es', count=80),
#  Row(language='hr', count=4),
#  Row(language='eu', count=4),
#  Row(language='el', count=3),
#  Row(language='af', count=18),
#  Row(language='it', count=29),
#  Row(language='ku', count=11),
#  Row(language='kn', count=2),
#  Row(language='ar', count=5),
#  Row(language='sv', count=3),
#  Row(language='nl', count=11),
#  Row(language='rw', count=2),
#  Row(language='bn', count=3),
#  Row(language='hu', count=2),
#  Row(language='ca', count=5),
#  Row(language='gu', count=6),
#  Row(language='ru', count=299),
#  Row(language='mt', count=10),
#  Row(language='th', count=3),
#  Row(language='lt', count=4),
#  Row(language='no', count=243),
#  Row(language='bg', count=2),
#  Row(language='cy', count=5),
#  Row(language='fo', count=5),
#  Row(language='hi', count=2),
#  Row(language='ta', count=2),
#  Row(language='et', count=3),
#  Row(language='zh', count=13),
#  Row(language='', count=16),
#  Row(language='se', count=21),
#  Row(language='fr', count=50),
#  Row(language='ja', count=6),
#  Row(language='id', count=3),
#  Row(language='la', count=6),
#  Row(language='da', count=4),
#  Row(language='fi', count=5),
#  Row(language='he', count=4)
# ]

language_counts = [
    Row(language="en", count=16871),
    Row(language="ru", count=299),
    Row(language="no", count=243),
    Row(language="es", count=80),
    Row(language="pt", count=56),
    Row(language="fr", count=50),
    Row(language="it", count=29),
    Row(language="ro", count=28),
    Row(language="se", count=21),
    Row(language="ms", count=20),
    Row(language="af", count=18),
    Row(language="de", count=17),
    Row(language="", count=16),
    Row(language="zh", count=13),
    Row(language="ku", count=11),
    Row(language="nl", count=11),
    Row(language="qu", count=10),
    Row(language="mt", count=10),
    Row(language="tr", count=9),
    Row(language="pl", count=8),
    Row(language="cs", count=6),
    Row(language="gu", count=6),
    Row(language="ja", count=6),
    Row(language="la", count=6),
    Row(language="ko", count=5),
    Row(language="ar", count=5),
    Row(language="ca", count=5),
    Row(language="cy", count=5),
    Row(language="fo", count=5),
    Row(language="fi", count=5),
    Row(language="nb", count=4),
    Row(language="hr", count=4),
    Row(language="eu", count=4),
    Row(language="lt", count=4),
    Row(language="da", count=4),
    Row(language="he", count=4),
    Row(language="el", count=3),
    Row(language="sv", count=3),
    Row(language="bn", count=3),
    Row(language="th", count=3),
    Row(language="et", count=3),
    Row(language="id", count=3),
    Row(language="sk", count=2),
    Row(language="br", count=2),
    Row(language="kn", count=2),
    Row(language="rw", count=2),
    Row(language="hu", count=2),
    Row(language="bg", count=2),
    Row(language="hi", count=2),
    Row(language="ta", count=2),
    Row(language="sl", count=1),
    Row(language="is", count=1),
]

from collections import OrderedDict

iso_639_choices = OrderedDict(
    [
        ("ab", "Abkhaz"),
        ("aa", "Afar"),
        ("af", "Afrikaans"),
        ("ak", "Akan"),
        ("sq", "Albanian"),
        ("am", "Amharic"),
        ("ar", "Arabic"),
        ("an", "Aragonese"),
        ("hy", "Armenian"),
        ("as", "Assamese"),
        ("av", "Avaric"),
        ("ae", "Avestan"),
        ("ay", "Aymara"),
        ("az", "Azerbaijani"),
        ("bm", "Bambara"),
        ("ba", "Bashkir"),
        ("eu", "Basque"),
        ("be", "Belarusian"),
        ("bn", "Bengali"),
        ("bh", "Bihari"),
        ("bi", "Bislama"),
        ("bs", "Bosnian"),
        ("br", "Breton"),
        ("bg", "Bulgarian"),
        ("my", "Burmese"),
        ("ca", "Catalan; Valencian"),
        ("ch", "Chamorro"),
        ("ce", "Chechen"),
        ("ny", "Chichewa; Chewa; Nyanja"),
        ("zh", "Chinese"),
        ("cv", "Chuvash"),
        ("kw", "Cornish"),
        ("co", "Corsican"),
        ("cr", "Cree"),
        ("hr", "Croatian"),
        ("cs", "Czech"),
        ("da", "Danish"),
        ("dv", "Divehi; Maldivian;"),
        ("nl", "Dutch"),
        ("dz", "Dzongkha"),
        ("en", "English"),
        ("eo", "Esperanto"),
        ("et", "Estonian"),
        ("ee", "Ewe"),
        ("fo", "Faroese"),
        ("fj", "Fijian"),
        ("fi", "Finnish"),
        ("fr", "French"),
        ("ff", "Fula"),
        ("gl", "Galician"),
        ("ka", "Georgian"),
        ("de", "German"),
        ("el", "Greek, Modern"),
        ("gn", "Guaraní"),
        ("gu", "Gujarati"),
        ("ht", "Haitian"),
        ("ha", "Hausa"),
        ("he", "Hebrew (modern)"),
        ("hz", "Herero"),
        ("hi", "Hindi"),
        ("ho", "Hiri Motu"),
        ("hu", "Hungarian"),
        ("ia", "Interlingua"),
        ("id", "Indonesian"),
        ("ie", "Interlingue"),
        ("ga", "Irish"),
        ("ig", "Igbo"),
        ("ik", "Inupiaq"),
        ("io", "Ido"),
        ("is", "Icelandic"),
        ("it", "Italian"),
        ("iu", "Inuktitut"),
        ("ja", "Japanese"),
        ("jv", "Javanese"),
        ("kl", "Kalaallisut"),
        ("kn", "Kannada"),
        ("kr", "Kanuri"),
        ("ks", "Kashmiri"),
        ("kk", "Kazakh"),
        ("km", "Khmer"),
        ("ki", "Kikuyu, Gikuyu"),
        ("rw", "Kinyarwanda"),
        ("ky", "Kirghiz, Kyrgyz"),
        ("kv", "Komi"),
        ("kg", "Kongo"),
        ("ko", "Korean"),
        ("ku", "Kurdish"),
        ("kj", "Kwanyama, Kuanyama"),
        ("la", "Latin"),
        ("lb", "Luxembourgish"),
        ("lg", "Luganda"),
        ("li", "Limburgish"),
        ("ln", "Lingala"),
        ("lo", "Lao"),
        ("lt", "Lithuanian"),
        ("lu", "Luba-Katanga"),
        ("lv", "Latvian"),
        ("gv", "Manx"),
        ("mk", "Macedonian"),
        ("mg", "Malagasy"),
        ("ms", "Malay"),
        ("ml", "Malayalam"),
        ("mt", "Maltese"),
        ("mi", "Māori"),
        ("mr", "Marathi (Marāṭhī)"),
        ("mh", "Marshallese"),
        ("mn", "Mongolian"),
        ("na", "Nauru"),
        ("nv", "Navajo, Navaho"),
        ("nb", "Norwegian Bokmål"),
        ("nd", "North Ndebele"),
        ("ne", "Nepali"),
        ("ng", "Ndonga"),
        ("nn", "Norwegian Nynorsk"),
        ("no", "Norwegian"),
        ("ii", "Nuosu"),
        ("nr", "South Ndebele"),
        ("oc", "Occitan"),
        ("oj", "Ojibwe, Ojibwa"),
        ("cu", "Old Church Slavonic"),
        ("om", "Oromo"),
        ("or", "Oriya"),
        ("os", "Ossetian, Ossetic"),
        ("pa", "Panjabi, Punjabi"),
        ("pi", "Pāli"),
        ("fa", "Persian"),
        ("pl", "Polish"),
        ("ps", "Pashto, Pushto"),
        ("pt", "Portuguese"),
        ("qu", "Quechua"),
        ("rm", "Romansh"),
        ("rn", "Kirundi"),
        ("ro", "Romanian, Moldavan"),
        ("ru", "Russian"),
        ("sa", "Sanskrit (Saṁskṛta)"),
        ("sc", "Sardinian"),
        ("sd", "Sindhi"),
        ("se", "Northern Sami"),
        ("sm", "Samoan"),
        ("sg", "Sango"),
        ("sr", "Serbian"),
        ("gd", "Scottish Gaelic"),
        ("sn", "Shona"),
        ("si", "Sinhala, Sinhalese"),
        ("sk", "Slovak"),
        ("sl", "Slovene"),
        ("so", "Somali"),
        ("st", "Southern Sotho"),
        ("es", "Spanish; Castilian"),
        ("su", "Sundanese"),
        ("sw", "Swahili"),
        ("ss", "Swati"),
        ("sv", "Swedish"),
        ("ta", "Tamil"),
        ("te", "Telugu"),
        ("tg", "Tajik"),
        ("th", "Thai"),
        ("ti", "Tigrinya"),
        ("bo", "Tibetan"),
        ("tk", "Turkmen"),
        ("tl", "Tagalog"),
        ("tn", "Tswana"),
        ("to", "Tonga"),
        ("tr", "Turkish"),
        ("ts", "Tsonga"),
        ("tt", "Tatar"),
        ("tw", "Twi"),
        ("ty", "Tahitian"),
        ("ug", "Uighur, Uyghur"),
        ("uk", "Ukrainian"),
        ("ur", "Urdu"),
        ("uz", "Uzbek"),
        ("ve", "Venda"),
        ("vi", "Vietnamese"),
        ("vo", "Volapük"),
        ("wa", "Walloon"),
        ("cy", "Welsh"),
        ("wo", "Wolof"),
        ("fy", "Western Frisian"),
        ("xh", "Xhosa"),
        ("yi", "Yiddish"),
        ("yo", "Yoruba"),
        ("za", "Zhuang, Chuang"),
        ("zu", "Zulu"),
    ]
)


# language_counts = sorted(language_counts, key=lambda x: -x["count"])
# print(language_counts)

import matplotlib.pyplot as plt
import numpy as np

language_counts = [l for l in language_counts if l["language"] != ""]

language_counts = language_counts[:20]

languages = [row["language"] for row in language_counts]
# languages = [iso_639_choices[l] if l != ""  else "Unknown" for l in languages]
counts = [row["count"] for row in language_counts]
pos = np.arange(len(languages))

plt.bar(pos, counts, align="center", alpha=0.5)
plt.xticks(pos, languages)
plt.ylabel("Number of Items (Logarithmic)")
plt.title("Languages of Appropriately-Licensed Items in archive.org")
plt.yscale("log")

plt.savefig("blahblah.png")
