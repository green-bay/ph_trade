from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask import current_app
import datetime

db = SQLAlchemy()
bcrypt = Bcrypt()

class CRUDMixin(object):

    id = db.Column(db.Integer, primary_key=True)

    @classmethod
    def validate_args(cls, **kwargs):
        invalid = []
        for attr in kwargs:
            try:
                getattr(cls, attr)
            except AttributeError:
                current_app.logger.debug('In create of {} invalid column given {}'.format(str(cls), attr))
                invalid.append(attr)
        for i in invalid:
            kwargs.pop(i)
        return kwargs

    @classmethod
    def create(cls, commit=True, **kwargs):
        kwargs = cls.validate_args(**kwargs)
        instance = cls(**kwargs)
        return instance.save(commit=commit)

    @classmethod
    def get(cls, id):
        return cls.query.get(id)

    @classmethod
    def get_or_404(cls, id):
        return cls.query.get_or_404(id)

    @classmethod
    def get_all(cls):
        res = cls.query.all()
        return [r.as_dict() for r in res]

    def write(self, commit=True, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        db.session.delete(self)
        return commit and db.session.commit()

    def as_dict(self):
        def normalize_dates(input):
            if type(input) in (datetime.datetime, datetime.date):
                return input.strftime('%d-%B-%Y')
            else:
                return input
        return {c.name: normalize_dates(getattr(self, c.name)) for c in self.__table__.columns}


class TimestampMixin(object):
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)
