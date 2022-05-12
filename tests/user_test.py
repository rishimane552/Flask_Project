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
        # add it to get ready to be committed
        db.session.add(user)
        # call the commit
        # db.session.commit()
        # assert that we now have a new user
        # assert db.session.query(User).count() == 1
        # finding one user record by email
        user = User.query.filter_by(email='test@test.com').first()
        log.info(user)
        # asserting that the user retrieved is correct
        assert user.email == 'test@test.com'
        # this is how you get a related record ready for insert
        user.songs = [Song(1000, "CREDIT"), Song("2000", "DEBIT")]
        # commit is what saves the songs
        db.session.commit()
        assert db.session.query(Song).count() == 2
        song1 = Song.query.filter_by(AMOUNT=1000).first()
        assert song1.AMOUNT == 1000
        # changing the title of the song
        song1.title = 500
        # saving the new title of the song
        db.session.commit()
        song2 = Song.query.filter_by(amount=500).first()
        assert song2.title == 500

        db.session.delete(user)
        assert db.session.query(User).count() == 0
        assert db.session.query(Song).count() == 0
