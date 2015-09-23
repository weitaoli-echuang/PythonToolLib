__author__ = 'VDTConstructor'

import math


def main():
	for m in xrange(1, 10, 1):
		for delta in xrange(1, 2):
			low = math.ceil((m + 1) / math.pow(2, delta) - 1)
			high = math.floor(m / math.pow(2, delta))
			if low != high:
				print 'wrong'
			else:
				print 'low %d,high %d' % (low, high)
	print 'here'


if __name__ == '__main__':
	main()