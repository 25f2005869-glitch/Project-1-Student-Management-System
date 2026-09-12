from extensions import db


class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    roll_no = db.Column(
        db.String(20),
        unique=True,
        nullable=False
    )

    department = db.Column(
        db.String(100),
        nullable=False
    )

    year = db.Column(
        db.Integer,
        nullable=False
    )

    phone = db.Column(
        db.String(15)
    )

    email = db.Column(
        db.String(120),
        unique=True
    )

    address = db.Column(
        db.Text
    )

    def __repr__(self):
        return f"<Student {self.name}>"