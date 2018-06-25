import random


def ran(word, dict_):
	list_ = dict_.get(word)
	rand = random.randint(0, len(list_) - 1)
	oword = list_[rand]
	return oword


a = {
    'собака': ['туда-ка', 'собака', 'сюда-ка'],
    'изучает': ['обучает', 'тренирует', 'развивает', 'изучает'],
    'дзю-до': ['дзю-до', 'дзю-после', 'мяу тай', 'самбо', 'несамобо']
}
b = 'собака изучает дзю-до'
print(b)
c = b.split()
d = ''
for i in range(0, len(c)):
	d = d + ran(c[i], a) + ' '
print(d)
