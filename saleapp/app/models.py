from app import db, app
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey,Enum
from sqlalchemy.orm import relationship
from  enum import Enum as RoleEnum

class UserRole(RoleEnum):
    Admin = 1
    User = 2

class User(db.Model):
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(50))
    username = Column(String(50),nullable=False)
    password = Column(String(50), nullable=False)
    user_role = Column(Enum(UserRole), default = UserRole.User)

class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True)
    products = relationship('Product', backref='category', lazy=True)


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    description = Column(String(255), nullable=True)
    price = Column(Float, default=0)
    image = Column(String(100), nullable=True)
    active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


if __name__ == '__main__':
    with app.app_context():
        #db.create_all()
        import hashlib

        u = User(name='admin', username='admin', password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()),
                 user_role = UserRole.Admin)
        db.session.add(u)
        db.session.commit()
        # db.create_all()
        # c1 = Category(name="Mobile")
        # c2 = Category(name="Table")
        # c3 = Category(name="Laptop")
        # db.session.add_all([c1, c2, c3])
        # db.session.commit()
        products = [{
            "name": "iPhone 7 Plus",
            "description": "Apple, 32GB, RAM: 3GB, iOS13",
            "price": 17000000,
            "image":
                "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
            "category_id": 1
        }, {
            "name": "iPad Pro 2020",
            "description": "Apple, 128GB, RAM: 6GB",
            "price": 37000000,
            "image":
                "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
            "category_id": 2
        }, {
            "name": "Galaxy Note 10 Plus",
            "description": "Samsung, 64GB, RAML: 6GB",
            "price": 24000000,
            "image":
                "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
            "category_id": 1
        }, {
            "name": "iPhone 7 Plus",
            "description": "Apple, 32GB, RAM: 3GB, iOS13",
            "price": 17000000,
            "image":
                "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
            "category_id": 1
        }, {
            "name": "iPad Pro 2020",
            "description": "Apple, 128GB, RAM: 6GB",
            "price": 37000000,
            "image":
                "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
            "category_id": 2
        }, {
            "name": "Galaxy Note 10 Plus",
            "description": "Samsung, 64GB, RAML: 6GB",
            "price": 24000000,
            "image":
                "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
            "category_id": 1
        },
            {
                "name": "iPhone 7 Plus",
                "description": "Apple, 32GB, RAM: 3GB, iOS13",
                "price": 17000000,
                "image":
                    "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
                "category_id": 1
            }, {
                "name": "iPad Pro 2020",
                "description": "Apple, 128GB, RAM: 6GB",
                "price": 37000000,
                "image":
                    "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
                "category_id": 2
            }, {
                "name": "Galaxy Note 10 Plus",
                "description": "Samsung, 64GB, RAML: 6GB",
                "price": 24000000,
                "image":
                    "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
                "category_id": 1
            }, {
                "name": "iPhone 7 Plus",
                "description": "Apple, 32GB, RAM: 3GB, iOS13",
                "price": 17000000,
                "image":
                    "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
                "category_id": 1
            }, {
                "name": "iPad Pro 2020",
                "description": "Apple, 128GB, RAM: 6GB",
                "price": 37000000,
                "image":
                    "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
                "category_id": 2
            }, {
                "name": "Galaxy Note 10 Plus",
                "description": "Samsung, 64GB, RAML: 6GB",
                "price": 24000000,
                "image":
                    "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
                "category_id": 1
            }]
        # for p in products:
        #     prod = Product(**p)
        #     db.session.add(prod)
        #
        # db.session.commit()
