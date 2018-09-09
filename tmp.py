# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import pandas as pd


df = pd.read_csv('./prefecture.csv')

name = "兵庫県"

df_row = df[df['prefecture'].str.contains(name)]
print(df_row.city.values[0])


#コマンド一覧
'''
echo $PATH
/Users/masaki/.rbenv/shims: #ruby, railsとか入ってる。
/Users/masaki/.rbenv/bin:
/usr/local/Cellar/pyenv-virtualenv/1.0.0/shims:
/Users/masaki/.pyenv/shims:  #conda, python, pipとか入ってる。
/usr/local/bin: #atom, vimとか入ってる。
/usr/bin: #phpとか入ってる。
/bin:
/usr/sbin:
/sbin:
/opt/X11/bin:
/Users/masaki/.pyenv/bin
'''
