from app import db


class DonorModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    contact_no = db.Column(db.String, nullable=False)
    blood_group = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)


