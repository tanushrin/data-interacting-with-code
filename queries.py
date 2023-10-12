# pylint: disable=missing-docstring, C0103

def directors_count(db):
    # return the number of directors contained in the database
    query = "SELECT COUNT(*) from directors d"
    db.execute(query)
    result = db.fetchone()
    return result[0]


def directors_list(db):
    # return the list of all the directors sorted in alphabetical order
    query = "select d.name  from directors d order by d.name"
    db.execute(query)
    results = db.fetchall()
    return [each_director[0] for each_director in results]


def love_movies(db):
    # return the list of all movies which contain the exact word "love"
    # in their title, sorted in alphabetical order
    query = "select m.title  from movies m WHERE UPPER(m.title) LIKE '%LOVE%'"
    db.execute(query)
    results = db.fetchall()
    return [each_movie[0] for each_movie in results]


def directors_named_like_count(db, name):
    # return the number of directors which contain a given word in their name
    query = f"SELECT COUNT(d.name) \
    FROM directors d \
    WHERE UPPER(d.name) LIKE '%{name}%'"
    db.execute(query)
    result = db.fetchone()
    return result[0]

def movies_longer_than(db, min_length):
    # return this list of all movies which are longer than a given duration,
    # sorted in the alphabetical order
    query = f"SELECT m.title FROM movies m \
        WHERE m.minutes  > {min_length}  \
        ORDER BY m.title "
    db.execute(query)
    results = db.fetchall()
    return [each_movie[0] for each_movie in results]
