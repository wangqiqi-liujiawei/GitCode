# if __name__ == '__main__':
#     languages = [
#         'Regional Assembly Language', "COBOL", "ML", "PHP", "REBOL", "D", "C#",
#         "Visual Basic .NET", "F#", "Scala", "Factor", "Windows PowerShell",
#         "Rust", "Clojure", "Go"
#     ]
#     years = [
#         1951, 1952, 1954, 1954, 1955, 1957, 1958, 1958, 1959, 1959, 1962, 1962,
#         1962, 1963, 1964, 1964, 1985, 1986, 1986, 1987, 1988, 1989, 1990, 1991,
#         1991, 1991, 1995
#     ]
#     [print(languages[i], ':', years[i]) for i in range(0, len(languages))]
#     for i in years:
#         print(i)

# import helpers
# helpers.display('Sample message', True)

# from helpers import display
# display('Sample message')
import os
from dotenv import load_dotenv
load_dotenv()


password = os.getenv('PASSWORD')
print(password)
