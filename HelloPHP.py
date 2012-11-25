import sublime
import sublime_plugin
import os


class HelloPHPCommand(sublime_plugin.EventListener):

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
		for region in view.sel():

			originalLine = view.full_line(region)
			print "current line is: " + originalLine

			if "." in line:
				print 'detected the .'
				line_contents = line + ' ==> hell yeah'
				self.view.insert(edit, line.begin(), line_contents)

	def on_modified (self, view):

		if self.isPHPFile(view):

			if self.isIgnoredCase(view):
				return

				print 'emoty...'
			
			# print "Not an ignored case, now start detection"

			if not self.isReturnKey(view):
				return

			self.modifyLine(view)






