#	DotToArrowCommand.py
#	
#	Copyright (c) 2013 Ayoub Khobalatte
# 	Licensed under the Apache License, Version 2.0
#
#	https://github.com/Rorchackh/DotToArrow

import sublime
import sublime_plugin
import os

class DotToArrowCommand(sublime_plugin.EventListener):

	def __init__(self):
		self.dotPattern = "\.([a-zA-Z_0-9]+?\(.*?\))"
		self.addSemicolon = sublime.load_settings('DotToArrow.sublime-settings').get('add_semi_colon')

	def isPHPFile(self, view):
		return "PHP" in os.path.basename(view.settings().get('syntax'))

	def isIgnoredCase(self, view):
		action = view.command_history(0, True)[0]
		if action == "left_delete" or action == "right_delete":
			return True
		return False

	def modifyLine(self, view):
		extracted = []

		dots = view.find_all(self.dotPattern, sublime.IGNORECASE, "$1", extracted)

		edit = view.begin_edit()
		for dot in dots:
			# replacing the dot by arrow notation here
			view.replace(edit, dot, "->" + extracted[0])

			print self.addSemicolon

			# adding a semicolon at the end of line
			pos = view.sel()[0].begin()
			if self.addSemicolon:
				view.insert(edit, pos, ';')

			# Moving the cursor back inside parentheses
			repos = pos - 1
			view.sel().clear()
			view.sel().add(sublime.Region(repos, repos))

		view.end_edit(edit)

	def on_modified (self, view):
		if self.isPHPFile(view):
			if self.isIgnoredCase(view):
				return

			self.modifyLine(view)
		# else:
		# 	sublime.message_dialog("This file doesn't seem to be a PHP file (Check syntax chosen)");
        