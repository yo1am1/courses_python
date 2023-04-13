import unittest


def parse(query: str) -> dict:
    if "?" in query:
        text = query[query.rfind("?") + 1:]
        for i in text:
            if i.isalnum():
                continue
            else:
                text = text.replace(i, " ")
        text = text.split(" ")
        res = dict(zip(text[::2], text[1::2]))
    else:
        res = {}
    return res


class TestParse(unittest.TestCase):
    def testName(self):
        const = parse('https://example.com/?name=Dima')
        self.assertEqual(const, {'name': 'Dima'})

    def testNameColor(self):
        const = parse('https://example.com/path/to/page?name=ferret&color=purple')
        self.assertEqual(const, {'name': 'ferret', 'color': 'purple'})

    def testNameColor1(self):
        const = parse('https://example.com/path/to/page?name=ferret&color=purple&')
        self.assertEqual(const, {'name': 'ferret', 'color': 'purple'})

    def testNameSex(self):
        const = parse('https://example.com/path/to/page?name=Давид&sex=male&')
        self.assertEqual(const, {'name': 'Давид', 'sex': 'male'})

    def testSex(self):
        const = parse('https://example.com/path/to/page?sex=male')
        self.assertEqual(const, {'sex': 'male'})

    def testEmpty(self):
        const = parse('https://example.com/')
        self.assertEqual(const, {})

    def testEmpty1(self):
        const = parse('http://example.com/?')
        self.assertEqual(const, {})

    def testAge(self):
        const = parse('http://example.com/?age=5')
        self.assertEqual(const, {'age': '5'})

    def testColor(self):
        const = parse('http://example.com/?color=white&')
        self.assertEqual(const, {'color': 'white'})

    def testSize(self):
        const = parse('http://example.com/?size=большой')
        self.assertEqual(const, {'size': 'большой'})

    def testAlph(self):
        const = parse('http://example.com/?а=б')
        self.assertEqual(const, {'а': 'б'})

    def testNum(self):
        const = parse('http://example.com/?5=6')
        self.assertEqual(const, {'5': '6'})


if __name__ == '__main__':
    unittest.main()
