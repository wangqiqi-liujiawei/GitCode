# -*- coding: UTF-8 -*-
def parse_ide_trend(top_ide_trend):
    top_ides = []
    top_ide_lines = top_ide_trend.split('\n')[1:]
    head = top_ide_lines[0]
    columns = head.split('\t')
    for row in top_ide_lines[1:]:
        row = row.strip()
        if row:
            cells = row.split('\t')
            top_ide = {}
            for i in range(0, len(columns)):
                column = columns[i]
                cell = cells[i]
                top_ide[column] = cell
            top_ides.append(top_ide)
    return top_ides


def parse_py_ide(py_ide_infos):
    py_ides = []
    for row in py_ide_infos:
        name_end = row.find('(')
        name = row[0:name_end]

        link_end = row.find(')')
        link = row[name_end + 1:link_end]

        desc = row[link_end + 2:]
        py_ides.append({'name': name, 'link': link, 'desc': desc})

    return py_ides


def dump_join_result(py_ide, top_ide):
    py_ide_name = py_ide['name']

    print(f'Python IDE：{py_ide_name}')
    print('----------')

    print('* 基本信息')
    for key in py_ide:
        value = py_ide[key]
        print(f'  * {key}: {value}')

    print('* 排行信息')
    if top_ide:
        for key in top_ide:
            if key != 'IDE' and key != 'Change':
                value = top_ide[key]
                print(f'  * {key}: {value}')
    else:
        print('  * 无')

    print('')


if __name__ == '__main__':
    top_ide_trend = '''
Rank	Change	IDE	Share	Trend
1		Visual Studio	29.24 %	+3.5 %
2		Eclipse	13.91 %	-2.9 %
3		Visual Studio Code	12.07 %	+3.3 %
4		Android Studio	9.13 %	-2.5 %
5		pyCharm	8.43 %	+0.7 %
6		IntelliJ	6.7 %	+0.8 %
7		NetBeans	4.82 %	-0.3 %
8		Sublime Text	3.49 %	-0.2 %
9		Xcode	3.37 %	-1.2 %
10		Atom	3.25 %	-0.5 %
11		Code::Blocks	2.16 %	+0.2 %
12		Vim	0.79 %	-0.1 %
13		Xamarin	0.48 %	-0.1 %
14		PhpStorm	0.46 %	-0.2 %
15		geany	0.39 %	+0.2 %
16		Komodo	0.31 %	-0.2 %
17		Qt Creator	0.26 %	-0.0 %
18		Emacs	0.18 %	-0.1 %
19		JDeveloper	0.13 %	-0.0 %
20		RAD Studio	0.08 %	-0.0 %
21		JCreator	0.07 %	-0.0 %
22		Light Table	0.07 %	-0.0 %
23		MonoDevelop	0.06 %	-0.0 %
24		SharpDevelop	0.03 %	-0.0 %
25		Eric Python	0.03 %	-0.0 %
26		Aptana	0.02 %	-0.0 %
27		RubyMine	0.02 %	-0.0 %
28		Coda 2	0.02 %	+0.0 %
29		Monkey Studio	0.01 %	-0.0 %
30		DrJava	0.01 %	-0.0 %
'''
    py_ide_infos = ["IDEL(https://docs.python.org/3/library/idle.html), Python 内置的IDE，功能比较一般。", "VIM(http://www.vim.org/),如果你是个VIM爱好者，可以用VIM编写Python，但是Python的缩进处理会比较麻烦。当然，你在 Linux 服务器上的时候有时候就只能用VI/VIM了。", "Visual Studio Code(https://code.visualstudio.com/)，VSCode 对Python的支持非常友好，配合几个插件后几乎是对 Python 开发最友好的IDE了。", "PyCharm(https://www.jetbrains.com/pycharm/)，jetbrains 出品的 PyCharm 也是 Python 开发者常用的IDE。"]
    top_ides = parse_ide_trend(top_ide_trend)
    py_ides = parse_py_ide(py_ide_infos)
    # print(top_ides)
    # top_ide_dict={}

    top_ide_dict = {}
    for top_ide in top_ides:
        top_ide_dict[top_ide['IDE'].lower()] = top_ide
    for py_ide in py_ides:
        find_top_ide = top_ide_dict.get(py_ide['name'].lower())
        dump_join_result(py_ide, find_top_ide)
    # dump_join_result(py_ides, top_ides)
