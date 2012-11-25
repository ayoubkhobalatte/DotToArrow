#	HelloPHPCommand.py
#	
#	Copyright (c) 2009 Ayoub Khobalatte
#	Licensed under the MIT and GPL licenses.
#
#	https://github.com/Rorchackh/HelloPHP

import sublime
import sublime_plugin
import os

class HelloPHPCommand(sublime_plugin.EventListener):

	dotPattern = "\.([a-zA-Z_0-9]+?\(.*?\))"

	def isPHPFile(self, view):
		return "PHP" in os.path.basename(view.settings().get('syntax'))

	def isIgnoredCase(self, view):
		action = view.command_history(0, True)[0]
		if action == "left_delete" or action == "right_delete":
			return True
		return False

	def isReturnKey(self, view):
		# return view.command_history(0, True)[0] == "insert"
		return True

	def modifyLine(self, view):
		extracted = []

		dots = view.find_all(self.dotPattern, sublime.IGNORECASE, "$1", extracted)

		edit = view.begin_edit()
		for dot in dots:
			view.replace(edit, dot, "->" + extracted[0])
		view.end_edit(edit)

	def on_modified (self, view):
		if self.isPHPFile(view):
			if self.isIgnoredCase(view):
				return

			if not self.isReturnKey(view):
				return

			self.modifyLine(view)






