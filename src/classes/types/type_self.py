from typing import Optional


class User:
    def __init__(self, user_id: int):
        self.id = user_id

    def is_same(self, other: "User") -> bool:
        return self.id == other.id


def get_user_by_id(user_id: int) -> Optional[User]:
    return User(user_id)


if __name__ == "__main__":
    u1 = User(1)
    u2 = User(2)

    print(f"Are u1 and u2 the same? {u1.is_same(u2)}")
