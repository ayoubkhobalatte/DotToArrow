## Description

Old habits die hard hard. I understand that. If you're coming to the PHP world from the your favourite programming language (say Java or C++), you might experience a few syntax differences that might annoy you. Namely, the arrow notation instead of the dot.

DotToArrow is a small [Sublime Text 2](http://www.sublimetext.com/2) plugin made to help people who are new or not used to PHP syntax 

This plugin transforms the dot (.) sign to the arrow sign (->) for method and class variable calls.

## How to install
Installing this plugin is easy. You can do it in two possible ways.

<h3> Using Package Control (Recommended) </h3>

<b>WARNING:</b> This is not yet supported.

Simply install the awesome [Package Control](http://wbond.net/sublime_packages/package_control) plugin by Will Bond. Then open the command palette (usually by hitting the Command+Shift+P or CTRL+Shift+P) and type <i>Install package: DotToArrow</i>

<h3> Manual Install </h3>

<p>
	Clone this repo or download a zip archive and copy it to your user packages. 
	You will need to restart Sublime Text 2.
</p>

# How to use
Once this plugin is installed, it is automatically run when you have PHP files opened. 
This plugin looks for function calls as you type and change dots to arrow as you write them.

<h3>Customize Behavior</h3>

You can choose whether the plugin adds semicolons for you when it detects a function call. This is default behavior. 
However, if you would like to switch this off, Please open DotToArrow.sublime-settings and change 

	{
	   "add_semi_colon": true
	}

to 
	
	{
	   "add_semi_colon": false
	}

## Licence
Copyright 2013 Ayoub Khobalatte.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this work except in compliance with the License. You may obtain a copy of the License in the LICENSE file, or at:

  [http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

## How to contribute

Found a bug in this plugin or have an idea? Please feel free to open a ticket here or send me a private message. You can also follow me on [Twitter](https://twitter.com/rorchackh) or  [Github](https://github.com/rorchackh) for the latest news and development.
