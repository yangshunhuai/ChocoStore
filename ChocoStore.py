#!/usr/bin/env python
# ChocoStore UI


from PySimpleGUI import *
import win32con
import win32clipboard as clipbrd
import os
import webbrowser as wb

choco_url = "https://chocolatey.org/packages?q="

chocotest = Button('Test Chocolatey', key='testchoco')
search_lbl = Text('Search')
search_input = InputText(key='keyword')
search_btn = Button('Search Chocolatey website', key='search')
get_clipboard = Button('Get package name from clipboard', key='getpkgname')
pkg_lbl = Text('Package name')
pkg = InputText()
install_btn = Button('Install', key='install')

layout = [[chocotest],
          [search_lbl, search_input, search_btn],
          [get_clipboard],
          [pkg_lbl, pkg, install_btn]]

root = Window('ChocoStore', layout)

while True:
    event, values = root.read()
    if event == 'testchoco':
        ver = os.popen('choco -v')
        Print('Chocolatey version: ' + ver.read())
        pass

    if event == 'getpkgname':
        clipbrd.OpenClipboard()
        cmd = clipbrd.GetClipboardData(win32con.CF_UNICODETEXT)
        clipbrd.CloseClipboard()
        pkg = cmd[14:]
        Print('Package name      : ' + pkg)
        pass

    if event == 'search':
        keyword = values['keyword']
        search_url = choco_url + keyword.replace(' ', '+')
        wb.open(search_url)
        pass

    if event == 'install':
    	os.system('choco install ' + pkg)

    if event == WIN_CLOSED:
        break
        pass


root.Close()
