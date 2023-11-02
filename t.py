#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author : loolewliu
# @date : 2023/11/3
# @file : t.py
# @use : XXX

import argparse


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('module_name', metavar='STR', type=str,
                        help='module names of ')
    parser.add_argument('-i', '--infile', dest='infile', metavar='FILE', type=str, required=True,
                        help="input file")
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    print(args.infile)
    print(args.module_name)


if __name__ == "__main__":
    main()



