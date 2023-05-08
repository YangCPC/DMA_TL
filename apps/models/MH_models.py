from apps.models import BaseModel
from exts import db

class MHSecureCommunicationWithCEParams(BaseModel):
    __tablename__ = 'mh_ce_param'

    r1 = db.Column(db.Integer, nullable=False)
    t2 = db.Column(db.String(20), nullable=False)
    DMi = db.Column(db.Integer, nullable=False)
    H2 = db.Column(db.String(200), nullable=False)
    m2 = db.Column(db.String(200), nullable=False)
    c2 = db.Column(db.BLOB, nullable=False)
