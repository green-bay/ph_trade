from app.db import db, CRUDMixin, TimestampMixin


class ClassifiedAd(db.Model, CRUDMixin, TimestampMixin):
    __tablename__='classified_ad'

    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    publisher = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(80))
    email = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    image = db.Column(db.LargeBinary)
    categories = db.relationship('ClassifiedTags',secondary='ads_tags_rel', lazy='subquery', backref=db.backref('ads', lazy=True))


class ClassifiedTags(db.Model, CRUDMixin):
    __tablename__='classified_tags'

    name = db.Column(db.String(255), nullable=False)


adds_tags_rel = db.Table('ads_tags_rel', db.Model.metadata,
        db.Column('ad_id', db.Integer, db.ForeignKey('classified_ad.id')),
        db.Column('tag_id', db.Integer, db.ForeignKey('classified_tags.id'))
            )
