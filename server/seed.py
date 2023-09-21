#!/usr/bin/env python3

from random import randint, choice as rc
from faker import Faker
from app import app
from models import db, Bakery, BakedGood

fake = Faker()

with app.app_context():

    BakedGood.query.delete()
    Bakery.query.delete()
    
    bakeries_data = [
        {
            "baked_goods": [
                {
                    "bakery_id": 1,
                    "id": 8,
                    "name": "Veronica",
                    "price": 7,
                },
                {
                    "bakery_id": 1,
                    "id": 15,
                    "name": "Sean",
                    "price": 9,
                },
                {
                    "bakery_id": 1,
                    "id": 25,
                    "name": "Robin",
                    "price": 3,
                },
                {
                    "bakery_id": 1,
                    "id": 27,
                    "name": "Derek",
                    "price": 7,
                },
                {
                    "bakery_id": 1,
                    "id": 105,
                    "name": "Holly",
                    "price": 10,
                },
                {
                    "bakery_id": 1,
                    "id": 173,
                    "name": "Maureen",
                    "price": 8,
                },
                {
                    "bakery_id": 1,
                    "id": 187,
                    "name": "Jennifer",
                    "price": 5,
                }
            ],
            "name": "Jones-Erickson",
        },
        {
            "baked_goods": [
                {
                    "bakery_id": 2,
                    "id": 76,
                    "name": "Samantha",
                    "price": 7,
                },
                {
                    "bakery_id": 2,
                    "id": 95,
                    "name": "Jeffrey",
                    "price": 5,
                },
                {
                    "bakery_id": 2,
                    "id": 125,
                    "name": "Pamela",
                    "price": 5,
                },
                {
                    "bakery_id": 2,
                    "id": 149,
                    "name": "Brandy",
                    "price": 7,
                },
                {
                    "bakery_id": 2,
                    "id": 175,
                    "name": "Kendra",
                    "price": 8,
                }
            ],
            "name": "Cook-Cunningham",
        },
    ]

    bakeries = []
    for bakery_data in bakeries_data:
        bakery = Bakery(
            name=bakery_data["name"],
        )
        bakeries.append(bakery)

    db.session.add_all(bakeries)
    db.session.commit()

    baked_goods = []
    for bakery_data in bakeries_data:
        for baked_good_data in bakery_data["baked_goods"]:
            baked_good = BakedGood(
                name=baked_good_data["name"],
                price=baked_good_data["price"],
                bakery=rc(bakeries),  
            )
            baked_goods.append(baked_good)

    db.session.add_all(baked_goods)
    db.session.commit()

    most_expensive_baked_good = rc(baked_goods)
    most_expensive_baked_good.price = 100
    db.session.add(most_expensive_baked_good)
    db.session.commit()
