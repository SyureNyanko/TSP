#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import time
import sys


def length(v1, v2):
	'''Measure length or cost'''
	#t = (x1 - x2) * 100
	#return t
	#print(str(v1) + " , " + str(v2))
	dv = (v1[0] - v2[0], v1[1] - v2[1])
	d2 = dv[0] * dv[0] + dv[1] * dv[1]
	d = math.sqrt(d2)
	return d


def route_swap(s, a, b):
	'''Generate new route s is old route, a and b are indexes'''
	new_route = s[0:a+1]
	mid = s[a+1:b+1]
	new_route = new_route + mid[::-1]
	new_route = new_route + s[b+1:]
	return new_route

def calc_two_point_length(s, i, j):
	return length(s[i], s[j])

def calc_route_length(route):
	ret = 0
	for i in range(len(route)):
		ret += length(route[i], route[(i+1)%len(route)])
	return ret


def two_opt(bestroute):
	'''Peforms 2-opt search to improve route'''
	l = len(bestroute)
	#len_best_route = calc_route_length(bestroute)

	while(True):
		flag = True
		for i in range(l-2):
			i_next = (i + 1)%l
			for j in range(i + 2, l):
				j_next = (j + 1)%l
				if i == 0 and j_next == 0:
					continue
				Li_i_next = length(bestroute[i], bestroute[i_next])
				Lj_j_next = length(bestroute[j], bestroute[j_next])
				Li_j = length(bestroute[i], bestroute[j])
				Li_next_j_next = length(bestroute[i_next], bestroute[j_next])
				L_now = Li_i_next + Lj_j_next
				L_new = Li_j + Li_next_j_next
				if L_now > L_new:
					print(str(i) + "," + str(j) + "," + str(bestroute))
					bestroute = route_swap(bestroute, i, j)
					#len_best_route = len_best_route - L_new + L_new
					flag = False

		if flag:
			break

	return bestroute

if __name__ == '__main__':
	'''point_tables is example case'''
	point_table = [(0,0),(1,2),(10,0),(4,5),(2,0)]
	point_size = len(point_table)
	print("initial :" + str(point_table))
	bestroute = two_opt(point_table)
	print("result  :" + str(bestroute))

