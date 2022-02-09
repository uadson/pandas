import os

from settings import database
from settings import datalist


class Analysis:

	def __init__(self):
		self.dataset = dict()

	def get_data(self):
		objects = {num + 1: elem for num, elem in enumerate(datalist)}
		for key, value in objects.items():
			print(key, '-', value)
		option = int(input('\nSelect dataset: '))
		self.dataset = f'{os.path.join(database, objects.get(option))}'
		return self.dataset


if __name__ == '__main__':
	dataset = Analysis()
	print(dataset.get_data())