class DB:
    def get_users(self):
        return ['Kasia', 'Ania', 'Tomek']


class BusinessLogic:
    def __init__(self, db):
        self._db = db

    def get_user_ended_with(self, letter):
        if type(letter) != str:
            raise ValueError('letter must be str')

        users = self._db.get_users()

        result = []

        for user in users:
            if user.endswith(letter):
                result.append(user)

        return result


if __name__ == '__main__':
    db = DB()
    b = BusinessLogic(db)

    result = b.get_user_ended_with('a')

    print(result)
