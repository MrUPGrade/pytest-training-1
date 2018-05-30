class A:
    def __init__(self, message):
        self.message = message

    def print(self):
        print(self.message)


def fake():
    print("FAKE")


if __name__ == '__main__':
    a = A('dupa')

    a.print = fake

    a.print()
