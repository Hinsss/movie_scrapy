def test():
	lt = []
	for x in range(1, 1001):
		lt.append(x)
	return lt

# 生成器，不是保存的数据，而是保存的这个数据生成的方式，用到的时候，直接调用，再给你生成
def demo():
	for x in range(1, 11):
		yield x
		# print('嘿嘿嘿')
	yield '哈哈哈'
	yield '嘻嘻嘻'

a = demo()

# for x in a:
# 	print(x)

print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))