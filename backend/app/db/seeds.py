from app.db.repositories.items import ItemsRepository
from app.db.repositories.users import UsersRepository
from app.db.repositories.comments import CommentsRepository
from app.api.dependencies.database import get_repository

from random import choice, randint

item_names = ["fish", "percolator", "handbag", "gavel", "radiator"]
user_names = ["steve", "skullboy", "oldmama", "ed", "USER01"]
comment_strings = ["Meh", "Alright, I guess...", "AMAZING!!1"]

items = get_repository(ItemsRepository)()
users = get_repository(UsersRepository)()
comments = get_repository(CommentsRepository)()

created = {"users": [], "items": [], "comments": []}


async def seed():
    for _ in range(100):
        user_name = f"{choice(user_names)}{randint(100,10000)}"
        created["users"].append(
            await users.create_user(
                username=user_name, email="example@test.com", password="password"
            )
        )

    for _ in range(100):
        print(choice(created["users"]))
        user = choice(created["users"])
        item_name = choice(item_names)
        slug = f"{item_name}{randint(1, 1000000)}"
        created["items"].append(
            await items.create_item(
                slug=slug, title=item_name, description="", seller=user
            )
        )
        await comments.create_comment_for_item(
            body=choice(comment_strings),
            item=choice(created["items"]),
            user=choice(created["users"]),
        )

seed()