""" test for balance check after uploading csv file"""
from app import db
from app.db.models import User, Song

def test_user_balance(application):
    balance = 0.0
    with application.app_context():
        # create a record
        user = User('test@test.com', 'test1234')
        db.session.add(user)
        user = User.query.filter_by(email='test@test.com').first()
        # asserting that the user retrieved is correct

        assert user.email == 'test@test.com'
        # check balance before update
        #assert user.balance == 0

        user.songs = [Song(5000, "CREDIT"), Song(1000, "DEBIT")]
        db.session.commit()

        # check balance for credit transaction
        user_account1 = Song.query.filter_by(amount=5000).first()


        if user_account1.type == "CREDIT":
            balance = balance + user_account1.amount
        else:
            balance = balance - user_account1.amount

        user_account1.balance = balance

        assert user_account1.balance == 5000

        # check balance for credit transaction
        user_account2 = Song.query.filter_by(amount=1000).first()

        if user_account2.type == "CREDIT":
            balance = balance + user_account2.amount
        else:
            balance = balance - user_account2.amount

        user_account2.balance = balance

        assert user_account2.balance == 4000