import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:

    # Secret Key
    SECRET_KEY = "student-management-system-secret-key"

    # SQLite Database
    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///" +
        os.path.join(BASE_DIR, "database", "student.db")
    )

    # Disable Track Modifications
    SQLALCHEMY_TRACK_MODIFICATIONS = False