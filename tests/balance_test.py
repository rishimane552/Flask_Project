""" test for balance check after uploading csv file"""

def test_balance(client, application):
    """ checks balance after upload"""
    with application.app_context():
        email = 'test@test.com'
        password = 'test1234'
        csv_test_file = 'tests/csvtest.csv'
        response = client.post("/register", data=dict(email=email, password=password, confirm=password),
                               follow_redirects=True)
        response = client.post("/login", data=dict(email=email, password=password, confirm=password),
                               follow_redirects=True)
        response = client.post("/songs/upload", data=dict(file=open(csv_test_file, 'rb')), follow_redirects=True)
        assert response.status_code == 200
        response = client.get("/songs")
        assert b'Total Balance:' in response.data