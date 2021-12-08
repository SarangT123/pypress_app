import pip
packages = ["Flask",
            "Flask-Admin",
            "Flask-Bcrypt",
            "Flask-Login",
            "Flask-SQLAlchemy",
            "Flask-WTF",
            "Click",
            "WTForms",
            ]
for package in packages:
    failed = pip.main(["install", package])
