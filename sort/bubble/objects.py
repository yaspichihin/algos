import random

from faker import Faker
from pydantic import BaseModel, Field


class User(BaseModel):
        name: str = Field(..., min_length=2, max_length=50)
        age: int = Field(..., ge=0, le=150)

def bubble_sort(users: list[User]) -> None:
    """Мутирует переданный список"""

    for i in range(len(users), 0, -1):
        for j in range(i - 1):
            if users[j].age > users[j + 1].age:
                users[j], users[j + 1] = users[j + 1], users[j]


if __name__ == "__main__":
    users = [User(name=Faker().name(), age=random.randint(0, 150)) for _ in range(100)]
    bubble_sort(users)
    assert users == sorted(users, key=lambda x: x.age), "Ошибка сортировки"
