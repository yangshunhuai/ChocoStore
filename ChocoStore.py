#!/usr/bin/env python
# ChocoStore UI
from PySimpleGUI import *
import win32con
import win32clipboard as clipbrd
import os
import webbrowser as wb

choco_url = "https://chocolatey.org/packages?q="

chocotest = Button('测试Chocolatey', key='testchoco')
search_lbl = Text('搜索软件')
search_input = InputText(key='keyword')
search_btn = Button('搜索Chocolatey官网', key='search')
get_clipboard = Button('读取剪贴板', key='getpkgname')
pkg_lbl = Text('软件包名称')
pkg = InputText()
install_btn = Button('安装', key='install')

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
    if event == 'getpkgname':
        clipbrd.OpenClipboard()
        cmd = clipbrd.GetClipboardData(win32con.CF_UNICODETEXT)
        clipbrd.CloseClipboard()
        pkg = cmd[14:]
        Print('Package name      : ' + pkg)
    if event == 'search':
        keyword = values['keyword']
        search_url = choco_url + keyword.replace(' ', '+')
        wb.open(search_url)
    if event == WIN_CLOSED:
        break

root.Close()