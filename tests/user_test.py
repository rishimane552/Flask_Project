import logging

from app import db
from app.db.models import User, Song


def test_adding_user(application):
    log = logging.getLogger("myApp")
    with application.app_context():
        assert db.session.query(User).count() == 0
        assert db.session.query(Song).count() == 0
        # showing how to add a record
        # create a record
        user = User('test@test.com', 'test1234')
        db.session.add(user)
        user = User.query.filter_by(email='test@test.com').first()
        log.info(user)
        # asserting that the user retrieved is correct
        assert user.email == 'test@test.com'
        # this is how you get a related record ready for insert
        user.songs = [Song(1000, "CREDIT"), Song(2000, "DEBIT")]
        # commit is what saves the songs
        db.session.commit()
        assert db.session.query(Song).count() == 2
        song1 = Song.query.filter_by(amount='1000').first()
        assert song1.amount == 1000
        # changing the title of the song
        song1.title = 500
        # saving the new title of the song
        db.session.commit()
        song2 = Song.query.filter_by(amount='2000').first()
        assert song2.amount == 2000

        db.session.delete(user)
        assert db.session.query(User).count() == 0
        assert db.session.query(Song).count() == 0
