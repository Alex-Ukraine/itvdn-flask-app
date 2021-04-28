"""
SELECT QUERIES
"""
from sqlalchemy import and_

from src import db
from src.database import models

films = db.session.query(models.Film).order_by(models.Film.rating.desc()).all()
hp = db.session.query(models.Film).filter(
    models.Film.title == 'Harry Potter and Chamber of Secrets'
).first()
hp1 = db.session.query(models.Film).filter_by(title='Harry Potter and Chamber of Secrets'
).first()

hp2 = db.session.query(models.Film).filter(
    models.Film.title != 'Harry Potter and Chamber of Secrets',
    models.Film.rating >= 8
).all()
hp3 = db.session.query(models.Film).filter(
    models.Film.title != 'Harry Potter and Chamber of Secrets'
).filter(models.Film.rating >= 7.5).all()
hp4 = db.session.query(models.Film).filter(
    and_(
        models.Film.title != 'Harry Potter and Chamber of Secrets',
        models.Film.rating >= 7.5
    )
).all()
hp5 = db.session.query(models.Film).filter(
    models.Film.title.like('%Deathly Hallows%')
).all()
hp6 = db.session.query(models.Film).filter(
    models.Film.title.ilike('%deathly hallows%')
).all()
hp7 = db.session.query(models.Film).filter(
    models.Film.length.in_([146, 161])).all()
hp8 = db.session.query(models.Film).filter(
    ~models.Film.length.in_([146, 161])).all()
hp9 = db.session.query(models.Film).filter(
    ~models.Film.length.in_([146, 161]))[:2]
films_with_actors = db.session.query(models.Film).join(models.Film.actors).all()
# print(hp9)
print(films_with_actors)