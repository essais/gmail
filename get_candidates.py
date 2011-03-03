#!/usr/bin/env python
# encoding: utf-8
"""
get_candidates.py
"""

import sys, os
from gmail import Gmail

if __name__ == '__main__':
	g = Gmail("lucyhacks@gmail.com", "montaigne")

	folder_name = 'candidates'
	msgs = g.get_all_messages_from_folder(folder_name)

	for msg in msgs:
		print "message: %s" % (msg)

