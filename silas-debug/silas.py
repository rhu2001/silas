#!/usr/bin/env python3

import argparse
import var_list
import strings
from classes import augmented_matrix as am

def m_create(args):
	pass

def am_defaults(args):
	if args.create:
		temp_am = am.AugmentedMatrix()
		temp_am.build(human_row_nums = True)
		var_list.store_var(args.create, temp_am)
		del temp_am
	elif args.build:
		temp_am = var_list.get_var(args.build)
		temp_am.build()
		var_list.store_var(args.build, temp_am)
		del temp_am

def main():
	main_parser = argparse.ArgumentParser()
	main_parser.add_argument("-ls", "--listvars", help = "lists names of all stored variables", action ='store_true')
	main_parser.add_argument("--clear", help = "clears all variables", action ='store_true')
	main_parser.add_argument("-s", "--show", metavar = "<var-name>", type = str, help = "displays variable stored at <var-name>")
	subparsers = main_parser.add_subparsers(help='<sub-command> help')

	m_parser = subparsers.add_parser('matrix', aliases = ["m"])
	m_parser.add_argument("-c", "--create", metavar = "<var-name>", type = str, help = "creates a matrix with variable name as <var-name>")
	m_parser.add_argument("-b", "--build", metavar = "<var-name>", type = str, help = "builds a matrix stored at <var_name>")

	am_parser = subparsers.add_parser('augmentedmatrix', aliases = ["am"])
	am_parser.add_argument("-c", "--create", metavar = "<var-name>", type = str, help = "creates and builds an augmented matrix with variable name as <var-name>")
	am_parser.add_argument("-b", "--build", metavar = "<var-name>", type = str, help = "builds augmented matrix stored at <var_name>")
	#am_parser.add_argument("--elim", nargs = 2, metavar = ("<var-name>", "<algorithm>"), type = str, help = "row-reduces augmented matrix stored at <var-name> using either Gaussian [g] or Gauss-Jordan [gj] elimination")
	am_parser.set_defaults(func = am_defaults)

	args = main_parser.parse_args()
	if args.listvars:
		var_list.print_all()
	elif args.clear:
		var_list.clear()
	elif args.show:
		temp_var = var_list.get_var(args.show)
		if temp_var:
			print(temp_var)
		del temp_var
	else:
		args.func(args)

if __name__ == "__main__":
    main()
