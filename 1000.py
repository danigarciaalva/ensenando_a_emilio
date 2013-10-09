#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
	l = []
	for i in sys.stdin:
		l = i.split(" ")
		a,b=int(l[0]),int(l[1])
		print a+b
