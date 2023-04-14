import unittest


def parse_cookie(query: str) -> dict:
    res, query = {}, query.replace(";", " ").split()
    for k in query:
        k = k.replace("=", " ", 1).split()
        res[k[0]] = k[-1]
    return res


class TestParse(unittest.TestCase):

    def testCookies(self):
        const = parse_cookie('name=Dima;age=28;')
        self.assertEqual(const, {'name': 'Dima', 'age': '28'})

    def testCookies1(self):
        const = parse_cookie('name=Dima;')
        self.assertEqual(const, {'name': 'Dima'})

    def testCookies2(self):
        const = parse_cookie('name=Dima;age=28;')
        self.assertEqual(const, {'name': 'Dima', 'age': '28'})

    def testCookies3(self):
        const = parse_cookie('')
        self.assertEqual(const, {})

    def testCookies4(self):
        const = parse_cookie('name=Dima=User;age=28;')
        self.assertEqual(const, {'name': 'Dima=User', 'age': '28'})

    def testCookies5(self):
        const = parse_cookie('name=Dima=User=God;age=28;')
        self.assertEqual(const, {'name': 'Dima=User=God', 'age': '28'})

    def testCookies5(self):
        const = parse_cookie(';age=28;')
        self.assertEqual(const, {'age': '28'})

    def testCookies6(self):
        const = parse_cookie('name=Dima;age=28;sex=male;married=False')
        self.assertEqual(const, {'name': 'Dima', 'age': '28', 'sex': 'male', 'married': 'False'})

    def testCookies7(self):
        const = parse_cookie(';')
        self.assertEqual(const, {})

    def testCookies8(self):
        const = parse_cookie('имя=Егор; возраст=18')
        self.assertEqual(const, {'имя': 'Егор', 'возраст': '18'})

    def testCookies9(self):
        const = parse_cookie('name=Dima;age=28;')
        self.assertEqual(const, {'name': 'Dima', 'age': '28'})

    def testCookies10(self):
        const = parse_cookie('name=Dima;age=28;')
        self.assertEqual(const, {'name': 'Dima', 'age': '28'})


if __name__ == '__main__':
    unittest.main()
