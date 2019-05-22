from io import StringIO
from unittest import main, TestCase
from unittest.mock import patch


def stdout(string):
    print(string)


class Test_stdout(TestCase):
    def test_stdout(self):
        resultado_esperado = 'Rapidinha de Python\n'

        with patch('sys.stdout', new=StringIO()) as fake_out:
            stdout('Rapidinha de Python')
            self.assertEqual(fake_out.getvalue(), resultado_esperado)


if __name__ == '__main__':
    main()
