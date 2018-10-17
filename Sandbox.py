"""class RaceCar:
    color = "Your Name"
    fuel_remaining = .5
    laps = 500

    def __init__(self, input_color, input_fuel_remaining, input_laps, **kwargs):
        self.color = input_color
        self.fuel_remaining = input_fuel_remaining
        self.laps = input_laps
        for key, value in kwargs.items():
            setattr(self, key, value)

    def run_lap(self, length):
        self.fuel_remaining -= (length * .125)
        self.laps += 1
red_car = RaceCar("red", "dude", 10, age="old")
RaceCar.laps = 10
print(red_car.laps)


class Inventory:
    def __init__(self):
        self.slots = []

    def add_item(self, item):
        self.slots.append(item)


class SortedInventory(Inventory):
    def add_item(self, item):
        self.slots.append(item)
        list.sort(self.slots)

sinv = SortedInventory
print(sinv)
def combiner(list_strings_numbers):
    strings1 = []
    numberstotal = 0
    for str_or_num in list_strings_numbers:
         if(isinstance (str_or_num, str)):
             strings1.append(str_or_num)
         else:
             numberstotal += str_or_num
    return "".join(strings1) + str(numberstotal)
print(combiner(["apple", 5.2, "dog", 8]))
class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern

    def __str__(self):
        returnString = ""
        for letter in self.pattern:
            if (letter=='.'):
                returnString += 'dot-'
            else:
                returnString += 'dash-'
        return returnString[:-1]
test =  Letter(['.', '.', '.'])
print(str(test))

class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern

    def __iter__(self):
        yield from self.pattern

    def __str__(self):
        output = []
        for blip in self:
            if blip == '.':
                output.append('dot')
            else:
                output.append('dash')
        return '-'.join(output)


    @classmethod
    def from_string(cls,inDotDash):
        temppattern = []
        for blip in inDotDash.split("-"):
            if blip == 'dot':
                temppattern.append('.')
            else:
                temppattern.append('_')
        pattern=temppattern
        return cls(pattern)


test =  Letter.from_string("dash-dot")
print(test)

class S(Letter):
    def __init__(self):
        pattern = ['.', '.', '.']
        super().__init__(pattern)

class NumString:
    def __init__(self, value):
        self.value = str(value)

    def __str__(self):
        return self.value

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __add__(self, other):
        if '.' in self.value:
            return float(self) + other
            return float(self) + other
        return int(self) + other

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.value = self + other
        return self.value

    def __mul__(self, other):
        if '.' in self.value:
            return float(self) * other
        return int(self) * other

    def __rmul__(self, other):
        return self * other

        class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    @property
    def area(self):
        return (self.width * self.length)

    @property
    def perimeter(self):
        return ((self.length * 2) + (self.width * 2))


newRect = Rectangle(5,2)
print(newRect.perimeter)

class Product:
    _price = 0.0
    tax_rate = 0.12

    def __init__(self, base_price):
        self._price = base_price

    @property
    def price(self):
        return self._price + (self._price * self.tax_rate)

    @price.setter
    def price(self,price):
        self._price = price

newP = Product(1)
print(newP.price)
newP.price = 5
print(newP.price)

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = []
        for y in range(self.height):
            for x in range(self.width):
                self.cells.append((x, y))
    def __iter__(self):
        yield from self.cells

class TicTacToe(Board):
    def __init__(self):
        super().__init__(width=3,height=3)
        class Song:
    def __init__(self, artist, title, length):
        self.artist = artist
        self.title = title
        self.length = length

    def __int__(self):
        return int(self.length)

    def __eq__(self, other):
        return int(self) == int(other)

    def __ne__(self, other):
        return int(self) != int(other)

    def __gt__(self, other):
        return int(self) > int(other)

    def __lt__(self, other):
        return int(self) < int(other)

    def __ge__(self, other):
        return int(self) > int(other) or int(self) == int(other)

    def __le__(self, other):
        return int(self) < int(other) or int(self) == int(other)

class YatzyScoresheet:
    def score_ones(self, hand):
        return sum(hand.ones)

    def _score_set(self, hand, set_size):
        scores = [0]
        for worth, count in hand._sets.items():
            if count == set_size:
                scores.append(worth * set_size)
        return max(scores)

    def score_one_pair(self, hand):
        return self._score_set(hand, 2)

    def score_chance(self, hand):
        scoreSum = 0
        for die in hand:
            scoreSum += die
        return scoreSum

    @classmethod
    def score_yatzy(self, hand):
        isYatzy = 0
        for dieFirst in hand:
            isYatzy = 0
            for dieSecond in hand:
                if dieFirst == dieSecond:
                    isYatzy += 1
                    if isYatzy == 5:
                        return 50
        return 0
y1 = YatzyScoresheet
print(y1.score_yatzy([3, 2, 3, 2, 3, 3]))


import re

names_file = open("names.txt", encoding="utf-8")
data = names_file.read()
names_file.close()
# print(data)
last_name = r'Love'
first_name = r'Kenneth'


# print(re.match(last_name,data))
# print(re.search(first_name,data))
# print(re.findall(r'\(?\d+\)?-?\s?\d+-\d+',data))
# print(re.findall(r'\w*, \w+',data))

def find_words(count, strToSearch):
    wordsToReturn = []
    searchTerm = r'\w{' + str(count) + ',}'
    return re.findall(searchTerm, strToSearch)


# print(find_words(4, "dog, cat, baby, balloon, me"))

# print(re.findall(r'[-\w\d+.]+@[-\w\d+.]+',data))
# print(re.findall(r'\b[trehous]{9}\b',data,re.I))

def find_email(strToSearch):
    return re.findall(r'[-\w\d+.]+@[-\w\d+.]+', strToSearch)

# print(find_email("kenneth.love@teamtreehouse.com, @support, ryan@teamtreehouse.com, test+case@example.co.uk"))
# ['kenneth@teamtreehouse.com', 'ryan@teamtreehouse.com', 'test@example.co.uk']
#print(re.findall(r'''
#    \b@[-\w\d+.]* # First a word boundary, an @, and then any number of characters
#    [^gov\t]+ # Ignore one or more instances of the letters g,o,v and a tab
#    \b # Match another word boundary
#''', data,re.VERBOSE|re.I))

#print(re.findall(r'''
#    \b[-\w]*, # Find a word boundary, one plus hyphens or characters, and a comma
#   \s # find 1 whitespace
# [-\w ]+ # 1+ hyphens and characters and explicit spaces
#[^\t\n] # Ignore tabs and newlines
#''', data,re.X))


line = re.search(r'''
   ^(?P<name>[\w ]*,\s[-\w ]+)\t # Last and first names
   (?P<email>[-\w\d.+]+@[-\w\d.]+)\t # Email
   (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t # Phone
   (?P<job>[\w\s]+,\s[\w\s.]+)\t? # Job and company
   (?P<twitter>@[\w\d]+)?$ # Twitter
''', data,re.X|re.MULTILINE)
#print(line)
#print(line.groupdict())

string = '''Love, Kenneth, kenneth+challenge@teamtreehouse.com, 555-555-5555, @kennethlove
Chalkley, Andrew, andrew@teamtreehouse.co.uk, 555-555-5556, @chalkers
McFarland, Dave, dave.mcfarland@teamtreehouse.com, 555-555-5557, @davemcfarland
Kesten, Joy, joy@teamtreehouse.com, 555-555-5558, @joykesten'''

contacts = re.search(r'''
   (?P<email>[-\w\d.+]+@[-\w\d.]+),\s # Email
   (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4}),\s # Phone
''', string,re.X|re.MULTILINE)
#print(contacts)
#print(contacts.groupdict())

twitters = re.search(r'''
   (?P<twitter>@[\w\d]+)$ # Twitter
''', string,re.X|re.MULTILINE)
#print(twitters)
#print(twitters.groupdict())

line = re.compile(r'''
   ^(?P<name>(?P<last>[\w ]*),\s(?P<first>[-\w ]+))\t # Last and first names
   (?P<email>[-\w\d.+]+@[-\w\d.]+)\t # Email
   (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t # Phone
   (?P<job>[\w\s]+,\s[\w\s.]+)\t? # Job and company
   (?P<twitter>@[\w\d]+)?$ # Twitter
''',re.X|re.MULTILINE)
#print(re.search(line,data).groupdict())
#print(line.search(data).groupdict())
#for match in line.finditer(data):
 #   print('{first} {last} <{email}>'.format(**match.groupdict()))

string = '''Love, Kenneth: 20'''

players = re.search(r'''
       (?P<last_name>[\w ]*),\s # Last
       (?P<first_name>[-\w ]+):\s # first
       (?P<score>[ \d]+) # score
    ''', string, re.X | re.MULTILINE)
print(players)
print(players.groupdict())

class Player:
    last_name =""
    first_name =""
    score=""
    def __init__(self,last_name,first_name,score):
        self.last_name =last_name
        self.first_name =first_name
        self.score=score
import datetime
#dir(datetime)
#print(datetime.datetime.now())
treehouse_start = datetime.datetime.now()
#print(treehouse_start)
treehouse_start.replace(hour=9,minute=0,second=0,microsecond=0)
th_start = datetime.datetime(2014,10,15,9,0)
#print(th_start)
time_worked = treehouse_start -th_start
#print(time_worked.seconds)
now = datetime.datetime.now()
#print(datetime.timedelta(minutes=5))
#print(now - datetime.timedelta(days=3))
hour = datetime.timedelta(hours=3) * 9
workday = hour * 9
tomorrow = datetime.datetime.now().replace(hour=9,minute=0) + datetime.timedelta(days=1)
#print(tomorrow + workday)

today = datetime.datetime.today()
#print(today.hour)
def minutes(d1,d2):
    return round(datetime.timedelta.total_seconds(d2 - d1)/60)
#print(minutes(datetime.datetime(2014,10,15,9,0),datetime.datetime(2014,10,17,9,0)))
#print(now.strftime('%m/%d/%y'))
#print(now.strptime('2015-04-02','%Y-%m-%d'))
#print(now.strptime('2015-04-02 12:00','%Y-%m-%d %H:%M'))

def to_string(dt):
    return dt.strftime('%d %B %Y')
def from_string(dt,dtFormat):
    return datetime.datetime.strptime(dt,dtFormat)
#print (to_string(datetime.datetime.now()))
#print (from_string("09/24/12 18:30", "%m/%d/%y %H:%M"))
answer_format = '%m/%d'
link_format = '%b_%d'
link = 'https://en.wikipedia.org/wiki/{}'

while True:
    answer = input("What date would you like? Please use the MM/DD format. Enter 'quit' to quit. ")
    if answer.upper() == 'QUIT':
        break
    try:
        date = datetime.datetime.strptime(answer, answer_format)
        output = link.format(date.strftime(link_format))
        print(output)
    except ValueError:
        print("That's not a valid date. Please try again.")

starter = datetime.datetime(2015, 10, 21, 16, 29)
def delorean(inNum):
    return starter + datetime.timedelta(hours=inNum)
#print(delorean(5))
def time_machine(inNum,stringTimeDelta):
    if (stringTimeDelta=="minutes"):
        return starter + datetime.timedelta(minutes=inNum)
    elif (stringTimeDelta=="hours"):
        return starter + datetime.timedelta(hours=inNum)
    elif (stringTimeDelta=="days"):
        return starter + datetime.timedelta(days=inNum)
    elif (stringTimeDelta=="years"):
        return starter + datetime.timedelta(days=inNum*365)
#print(time_machine(5,"minutes"))
def timestamp_oldest(*args):
    args_list = list(args)
    args_list.sort()
    return datetime.datetime.fromtimestamp(args_list[0])

import datetime
pacific = datetime.timezone(datetime.timedelta(hours=-8))
eastern = datetime.timezone(datetime.timedelta(hours=-5))
naive = datetime.datetime(2014,4,21,9)
aware = datetime.datetime(2014,4,21,9, tzinfo=pacific)
print(aware)
#print(naive.astimezone(pacific))
print(aware.astimezone(eastern))
auckland = datetime.timezone(datetime.timedelta(hours=13))
mumbai = datetime.timezone(datetime.timedelta(hours=5,minutes=30))
print(aware.astimezone(mumbai))

pacific = pytz.timezone('US/Pacific')
eastern = pytz.timezone('US/Eastern')
fmt = '%Y-%m-%d %H:%M:%S %Z%z'
utc = ptyz.utc
start = pacific.localize(datetime.datetime(2014,4,21,9))
start.strftime(fmt)
start_eastern = start.astimezone(eastern)
start_utc = datetime.datetime(2014,4,21,9,tzinfo=utc)

import datetime
print(datetime.datetime.now())
print(datetime.datetime.today())
"""

import re

names_file = open("names.txt", encoding="utf-8")
data = names_file.read()
names_file.close()
# print(data)
last_name = r'Ken'
first_name = r'Kenneth'


print(re.search("bob","test"))