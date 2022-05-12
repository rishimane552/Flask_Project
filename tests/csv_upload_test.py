"""csv file upload test"""
import io
import csv
from app.db.models import User, Song


def test_csv_upload(client):
    file_name = "csvtest.csv"
    data = {
        'image': (io.BytesIO(b" text data"), file_name)
    }
    response = client.post('/songs/upload', data=data)
    assert response.status_code == 400