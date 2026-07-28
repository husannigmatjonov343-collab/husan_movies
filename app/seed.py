"""
Ma'lumotlar bazasini namuna kinolar bilan to'ldirish.
Ishga tushirish: python -m app.seed
"""
from .database import Base, engine, SessionLocal
from .models import Movie, Genre

GENRES = [
    ("Fantastika", "fantastika"),
    ("Drama", "drama"),
    ("Aksiya", "aksiya"),
    ("Triller", "triller"),
    ("Animatsiya", "animatsiya"),
    ("Komediya", "komediya"),
    ("Jangari", "jangari"),
    ("Fantaziya", "fantaziya"),
    ("Qo'rqinchli", "qorqinchli"),
    ("Romantik", "romantik"),
    ("Jinoyat", "jinoyat"),
    ("Sarguzasht", "sarguzasht"),
]

MOVIES = [
    dict(title="Interstellar", year=2014, country="AQSh", duration_min=169, rating=8.6,
         description="Yer inqirozga uchraganda, bir guruh olim va uchuvchilar insoniyat uchun yangi uy topish maqsadida qurt uyasi orqali sayohat qiladi.",
         poster="https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg",
         backdrop="https://image.tmdb.org/t/p/w1280/xJHokMbljvjADYdit5fK5VQsXEG.jpg",
         youtube_id="zSWdZVtXT7E", director="Christopher Nolan", cast="Matthew McConaughey, Anne Hathaway",
         genres=["Fantastika", "Drama", "Sarguzasht"], featured=1, views=15420),
    dict(title="Inception", year=2010, country="AQSh", duration_min=148, rating=8.8,
         description="Tush ichida tush ko'rish orqali insonlarning ongiga kirib, fikrlarini o'g'irlaydigan mutaxassis haqida hikoya.",
         poster="https://image.tmdb.org/t/p/w500/9gk7adHYeDvHkCSEqAvQNLV5Uge.jpg",
         backdrop="https://image.tmdb.org/t/p/w1280/s3TBrRGB1iav7gFOCNx3H31MoES.jpg",
         youtube_id="YoHD9XEInc0", director="Christopher Nolan", cast="Leonardo DiCaprio, Joseph Gordon-Levitt",
         genres=["Fantastika", "Triller"], featured=1, views=21830),
    dict(title="The Dark Knight", year=2008, country="AQSh", duration_min=152, rating=9.0,
         description="Betmen Gotham shahrini Joker degan xavfli jinoyatchidan himoya qilish uchun kurashadi.",
         poster="https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
         backdrop="https://image.tmdb.org/t/p/w1280/hqkIcbrOHL86UncnHIsHVcVmzue.jpg",
         youtube_id="EXeTwQWrcwY", director="Christopher Nolan", cast="Christian Bale, Heath Ledger",
         genres=["Aksiya", "Jinoyat", "Triller"], featured=1, views=30250),
    dict(title="Parasite", year=2019, country="Janubiy Koreya", duration_min=132, rating=8.5,
         description="Kambag'al oila boy oilaning hayotiga sekin-asta kirib borishi haqidagi kutilmagan syujetli film.",
         poster="https://image.tmdb.org/t/p/w500/7IiTTgloJzvGI1TAYymCfbfl3vT.jpg",
         backdrop="https://image.tmdb.org/t/p/w1280/TU9NIjwzjoKPwQHoHshkFcQUCG.jpg",
         youtube_id="5xH0HfJHsaY", director="Bong Joon-ho", cast="Song Kang-ho, Lee Sun-kyun",
         genres=["Drama", "Triller"], featured=0, views=9840),
    dict(title="Spider-Man: Into the Spider-Verse", year=2018, country="AQSh", duration_min=117, rating=8.4,
         description="Turli olamlardan bo'lgan bir nechta o'rgimchak-odam multivselenniyni qutqarish uchun birlashadi.",
         poster="https://image.tmdb.org/t/p/w500/iiZZdoQBEYBv6id8su7ImL0oCbD.jpg",
         backdrop="https://image.tmdb.org/t/p/w1280/2rmK7mnchw9Xr3XdzGrF6nDh4wf.jpg",
         youtube_id="g4Hbz2jLxvQ", director="Bob Persichetti", cast="Shameik Moore, Jake Johnson",
         genres=["Animatsiya", "Aksiya", "Fantastika"], featured=1, views=18760),
    dict(title="La La Land", year=2016, country="AQSh", duration_min=128, rating=8.0,
         description="Los-Anjelesda orzu ortidan quvgan aktrisa va jaz musiqachisining sevgi va orzular haqidagi hikoyasi.",
         poster="https://image.tmdb.org/t/p/w500/uDO8zWDhfWwoFdKS4fzkUJt0Rf0.jpg",
         backdrop="https://image.tmdb.org/t/p/w1280/ftbTHhZmzcbXLYNhBTh0lS02Yh4.jpg",
         youtube_id="0pdqf4P9MB8", director="Damien Chazelle", cast="Ryan Gosling, Emma Stone",
         genres=["Romantik", "Drama"], featured=0, views=7650),
    dict(title="Mad Max: Fury Road", year=2015, country="Avstraliya", duration_min=120, rating=8.1,
         description="Cho'l bo'ylab davom etadigan ta'qib va portlashlarga to'la, chegara bilmas post-apokaliptik sarguzasht.",
         poster="https://image.tmdb.org/t/p/w500/hA2ple9q4qnwxp3hKVNhroipsir.jpg",
         backdrop="https://image.tmdb.org/t/p/w1280/gVJqoCkA1IUhCXAvpqzpqUqSXwZ.jpg",
         youtube_id="hEJnMQG9ev8", director="George Miller", cast="Tom Hardy, Charlize Theron",
         genres=["Aksiya", "Sarguzasht"], featured=0, views=13200),
    dict(title="Coco", year=2017, country="AQSh", duration_min=105, rating=8.4,
         description="Musiqaga oshiq bo'lgan bolakay ajdodlar dunyosiga sayohat qilib, oilaviy sirlarni ochadi.",
         poster="https://image.tmdb.org/t/p/w500/gGEsBPAijhVUFoiNpgZXqRVWJt2.jpg",
         backdrop="https://image.tmdb.org/t/p/w1280/askg3SMvhqEl4OL52YuvdtY40Yb.jpg",
         youtube_id="xlnPHQ3TLX8", director="Lee Unkrich", cast="Anthony Gonzalez, Gael García Bernal",
         genres=["Animatsiya", "Drama", "Sarguzasht"], featured=0, views=11400),
    dict(title="Get Out", year=2017, country="AQSh", duration_min=104, rating=7.7,
         description="Qiz do'stining oilasiga tashrif buyurgan yigit asta-sekin dahshatli sirni fosh etadi.",
         poster="https://image.tmdb.org/t/p/w500/tFXcEccSQMf3lfhfXKSU9iRBpa3.jpg",
         backdrop="https://image.tmdb.org/t/p/w1280/tYdpXG7Y1CTGz1U6MOhbLDo9nA6.jpg",
         youtube_id="DzfpyUB60YY", director="Jordan Peele", cast="Daniel Kaluuya, Allison Williams",
         genres=["Qo'rqinchli", "Triller"], featured=0, views=8930),
    dict(title="The Grand Budapest Hotel", year=2014, country="AQSh", duration_min=99, rating=8.1,
         description="Afsonaviy mehmonxona boshqaruvchisi va uning shogirdi haqidagi hazil-mutoyibaga to'la sarguzasht.",
         poster="https://image.tmdb.org/t/p/w500/eWdyYQreja6JGCzqHWXpWHDrrPo.jpg",
         backdrop="https://image.tmdb.org/t/p/w1280/nX5XiF7dU2po8pgpJgWQ0Vpg9v5.jpg",
         youtube_id="1Fg5iWmQjwk", director="Wes Anderson", cast="Ralph Fiennes, Tony Revolori",
         genres=["Komediya", "Drama"], featured=0, views=5210),
    dict(title="John Wick", year=2014, country="AQSh", duration_min=101, rating=7.4,
         description="Nafaqadagi qotil, o'ldirilgan kuchugi uchun o'ch olish maqsadida yana ishga qaytadi.",
         poster="https://image.tmdb.org/t/p/w500/fZPSd91yGE9fCcCe6OoQr6E3Bev.jpg",
         backdrop="https://image.tmdb.org/t/p/w1280/qqHQsStV6exqEw3jtVzZoCFXKtx.jpg",
         youtube_id="2AUmvWm5ZDQ", director="Chad Stahelski", cast="Keanu Reeves, Michael Nyqvist",
         genres=["Aksiya", "Jangari", "Jinoyat"], featured=0, views=16700),
    dict(title="Whiplash", year=2014, country="AQSh", duration_min=106, rating=8.5,
         description="Barabanchi shogird va uning shafqatsiz o'qituvchisi orasidagi mukammallikka intilish kurashi.",
         poster="https://image.tmdb.org/t/p/w500/6uSPcdGNsA09qkoOtxNfBl0Iz2y.jpg",
         backdrop="https://image.tmdb.org/t/p/w1280/fRGxZuo7jJUWQsVg9PREb98Aclp.jpg",
         youtube_id="7d_jQycdQGo", director="Damien Chazelle", cast="Miles Teller, J.K. Simmons",
         genres=["Drama"], featured=0, views=6540),
    dict(title="Your Name.", year=2016, country="Yaponiya", duration_min=106, rating=8.4,
         description="Bir-biridan uzoqda yashovchi ikki o'smirning tanalari almashib turishi haqidagi sehrli hikoya.",
         poster="https://image.tmdb.org/t/p/w500/q719jXXEzOoYaps6babgKnONONX.jpg",
         backdrop="https://image.tmdb.org/t/p/w1280/glnrpgTfLKmDVFXcDx0i9UwbaOD.jpg",
         youtube_id="xU47nhruN-Q", director="Makoto Shinkai", cast="Ryunosuke Kamiki, Mone Kamishiraishi",
         genres=["Animatsiya", "Romantik", "Fantaziya"], featured=1, views=19230),
    dict(title="Dune", year=2021, country="AQSh", duration_min=155, rating=8.0,
         description="Cho'l sayyorasida hokimiyat, dinlar va taqdir haqidagi ulkan ilmiy-fantastik doston.",
         poster="https://image.tmdb.org/t/p/w500/d5NXSklXo0qyIYkgV94XAgMIckC.jpg",
         backdrop="https://image.tmdb.org/t/p/w1280/jYEW5xZkZk2WTrdbMGAPFuBqbDc.jpg",
         youtube_id="8g18jFHCLXk", director="Denis Villeneuve", cast="Timothée Chalamet, Zendaya",
         genres=["Fantastika", "Sarguzasht"], featured=1, views=22110),
    dict(title="Knives Out", year=2019, country="AQSh", duration_min=130, rating=7.9,
         description="Boy yozuvchining o'limi ortidan sirli detektiv oilaning har bir a'zosini so'roq qiladi.",
         poster="https://image.tmdb.org/t/p/w500/pThyQovXQrw2m0s9x82twj48Jq4.jpg",
         backdrop="https://image.tmdb.org/t/p/w1280/oX0PhSBgYNStg2iwmvHkQFRWaW6.jpg",
         youtube_id="qGqiHJTsRkQ", director="Rian Johnson", cast="Daniel Craig, Chris Evans",
         genres=["Jinoyat", "Triller", "Komediya"], featured=0, views=10380),
    dict(title="Spirited Away", year=2001, country="Yaponiya", duration_min=125, rating=8.6,
         description="Ruhlar dunyosiga tushib qolgan qizning ota-onasini qutqarish uchun sehrli sayohati.",
         poster="https://image.tmdb.org/t/p/w500/39wmItIWsg5sZMyRUHLkWBcuVCM.jpg",
         backdrop="https://image.tmdb.org/t/p/w1280/Ab8mkHmkYADjU7wQiOkia9BzGvS.jpg",
         youtube_id="ByXuk9QqQkk", director="Hayao Miyazaki", cast="Rumi Hiiragi, Miyu Irino",
         genres=["Animatsiya", "Fantaziya", "Sarguzasht"], featured=1, views=17890),
    dict(title="The Social Network", year=2010, country="AQSh", duration_min=120, rating=7.7,
         description="Fейsbukning tashkil topishi va do'stlik, sotqinlik, muvaffaqiyat haqidagi haqiqiy voqealar asosidagi film.",
         poster="https://image.tmdb.org/t/p/w500/n0ybibhJtQ5icDqTp8eRytcIHJx.jpg",
         backdrop="https://image.tmdb.org/t/p/w1280/z5ADjejyBOaFHexbpNvOJ9y8QK.jpg",
         youtube_id="lB95KLmpLR4", director="David Fincher", cast="Jesse Eisenberg, Andrew Garfield",
         genres=["Drama", "Jinoyat"], featured=0, views=8120),
    dict(title="Avengers: Endgame", year=2019, country="AQSh", duration_min=181, rating=8.4,
         description="Qahramonlar guruhi butun koinotni qutqarish uchun so'nggi va eng katta jangga otlanadi.",
         poster="https://image.tmdb.org/t/p/w500/or06FN3Dka5tukK1e9sl16pB3iy.jpg",
         backdrop="https://image.tmdb.org/t/p/w1280/7RyHsO4yDXtBv1zUU3mTpHeQ0d5.jpg",
         youtube_id="TcMBFSGVi1c", director="Anthony Russo, Joe Russo", cast="Robert Downey Jr., Chris Evans",
         genres=["Aksiya", "Fantastika", "Sarguzasht"], featured=1, views=35400),
    dict(title="Joker", year=2019, country="AQSh", duration_min=122, rating=8.4,
         description="Jamiyat tomonidan rad etilgan komediyachining asta-sekin jinoyatchiga aylanish tarixi.",
         poster="https://image.tmdb.org/t/p/w500/udDclJoHjfjb8Ekgsd4FDteOkCU.jpg",
         backdrop="https://image.tmdb.org/t/p/w1280/n6bUvigpRFqSwmPp1m2YADdbRBc.jpg",
         youtube_id="zAGVQLHvwOY", director="Todd Phillips", cast="Joaquin Phoenix, Robert De Niro",
         genres=["Drama", "Jinoyat", "Triller"], featured=0, views=20130),
    dict(title="Toy Story", year=1995, country="AQSh", duration_min=81, rating=8.3,
         description="O'yinchoqlar bolakay uxlab qolganda jonlanib, o'z olamlarida sarguzashtlarni boshdan kechiradi.",
         poster="https://image.tmdb.org/t/p/w500/uXDfjJbdP4ijW5hWSBrPrlKpxab.jpg",
         backdrop="https://image.tmdb.org/t/p/w1280/tYtOM6WHTiwbtNvsxzWFULzHg1w.jpg",
         youtube_id="v-PjgYDrg70", director="John Lasseter", cast="Tom Hanks, Tim Allen",
         genres=["Animatsiya", "Komediya", "Sarguzasht"], featured=0, views=12900),
    dict(title="Gladiator", year=2000, country="AQSh", duration_min=155, rating=8.5,
         description="Xiyonatga uchragan Rim generali qullikka tushib, arenada o'ch olish yo'lini tanlaydi.",
         poster="https://image.tmdb.org/t/p/w500/ty8TGRuvJLPUmAR1H1nRIsgwvim.jpg",
         backdrop="https://image.tmdb.org/t/p/w1280/rmXbAxlhJb1zvj0ejEjcMkOnfWG.jpg",
         youtube_id="P1KEmpg-32c", director="Ridley Scott", cast="Russell Crowe, Joaquin Phoenix",
         genres=["Aksiya", "Drama", "Jangari"], featured=0, views=14200),
    dict(title="Everything Everywhere All at Once", year=2022, country="AQSh", duration_min=140, rating=8.0,
         description="Oddiy kir yuvish do'koni egasi ko'p olamlar orqali sayohat qilib, borliqni qutqarishi kerak.",
         poster="https://image.tmdb.org/t/p/w500/w3LxiVYdWWRvEVdn5RYq6jIqkb1.jpg",
         backdrop="https://image.tmdb.org/t/p/w1280/ss0Os3uWJfQAENGLQGoOgTVE1lI.jpg",
         youtube_id="wxN1T1uxQ2g", director="Daniel Kwan, Daniel Scheinert", cast="Michelle Yeoh, Ke Huy Quan",
         genres=["Fantastika", "Komediya", "Sarguzasht"], featured=1, views=13650),
    dict(title="The Shawshank Redemption", year=1994, country="AQSh", duration_min=142, rating=9.3,
         description="Noto'g'ri sudlangan bankir qamoqxonada umid va do'stlik orqali ozodlikka yo'l topadi.",
         poster="https://image.tmdb.org/t/p/w500/q6y0Go1tsGEsmtFryDOJo3dEmqu.jpg",
         backdrop="https://image.tmdb.org/t/p/w1280/kXfqcdQKsToO0OUXHcrrNCHDBzO.jpg",
         youtube_id="6hB3S9bIaco", director="Frank Darabont", cast="Tim Robbins, Morgan Freeman",
         genres=["Drama", "Jinoyat"], featured=1, views=27600),
]


def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        if db.query(Movie).count() > 0:
            print("Ma'lumotlar bazasi allaqachon to'ldirilgan, o'tkazib yuborildi.")
            return

        genre_map = {}
        for name, slug in GENRES:
            g = Genre(name=name, slug=slug)
            db.add(g)
            db.flush()
            genre_map[name] = g

        for m in MOVIES:
            movie = Movie(
                title=m["title"], year=m["year"], country=m["country"],
                duration_min=m["duration_min"], rating=m["rating"],
                description=m["description"], poster=m["poster"], backdrop=m["backdrop"],
                youtube_id=m["youtube_id"], director=m["director"], cast=m["cast"],
                is_featured=m["featured"], views=m["views"],
            )
            movie.genres = [genre_map[g] for g in m["genres"]]
            db.add(movie)

        db.commit()
        print(f"{len(MOVIES)} ta kino va {len(GENRES)} ta janr muvaffaqiyatli qo'shildi.")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
