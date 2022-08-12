# 1.Написать итератор, который принимает список списков, и возвращает их плоское представление, т.е последовательность
# состоящую из вложенных элементов.
nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]


class FlatIterator:

	def __init__(self, list_t):
		self.list_t = list_t
		self.end = len(list_t)
		self.pos_1 = 0
		self.pos_2 = -1

	def __iter__(self):
		return self

	def __next__(self):
		self.pos_2 += 1
		if self.pos_2 >= len(self.list_t[self.pos_1]):
			self.pos_2 = 0
			self.pos_1 += 1
		if self.pos_1 >= len(self.list_t):
			raise StopIteration
		return self.list_t[self.pos_1][self.pos_2]


# 2. Написать генератор, который принимает список списков, и возвращает их плоское представление
def flat_generator(list_t):
	for pos_1 in list_t:
		for pos_2 in pos_1:
			yield pos_2


# 3.* Написать итератор аналогичный итератору из задания 1, но обрабатывающий списки с любым уровнем вложенности
advance_nested_list = [
	['a', ['b', 'c']],
	['d', ['e'], [[['f']]], 'h', False],
	[1, 2, None],
	'2',
	[True],
]


class AdvanceFlatIterator:

	def __init__(self, list_t):
		self.list_t = self.open_list(list_t)
		self.end = len(list_t)
		self.pos_1 = -1

	def __iter__(self):
		return self

	def __next__(self):
		self.pos_1 += 1
		if self.pos_1 >= len(self.list_t):
			raise StopIteration
		return self.list_t[self.pos_1]

	def open_list(self, lst, res=[]):
		for el in lst:
			if isinstance(el, list):
				self.open_list(el)
			else:
				res.append(el)
		return res


# 4.* Написать генератор аналогичный генератор из задания 2, но обрабатывающий списки с любым уровнем вложенности
def advance_flat_generator(list_t):
	for pos_1 in list_t:
		if isinstance(pos_1, list):
			for pos_2 in advance_flat_generator(pos_1):
				yield pos_2
		else:
			yield pos_1


if __name__ == '__main__':
	print('--------- Задание 1. ---------')
	for item in FlatIterator(nested_list):
		print(item)
	flat_list = [item for item in FlatIterator(nested_list)]
	print(flat_list)

	print('--------- Задание 2. ---------')
	for item in flat_generator(nested_list):
		print(item)

	print('--------- Задание 3. ---------')
	for item in AdvanceFlatIterator(advance_nested_list):
		print(item)
	flat_list = [item for item in AdvanceFlatIterator(advance_nested_list)]
	print(flat_list)

	print('--------- Задание 4. ---------')
	for item in advance_flat_generator(advance_nested_list):
		print(item)
