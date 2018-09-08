# vscode 设置自定义 .vimrc
<pre>
    "vim.insertModeKeyBindings": [
        {
            "before": ["j", "k"],
            "after": ["<ESC>"]
        }
    ]
</pre>
# Modules使用
## 模块的引入 
1. 模块定义好后，我们可以使用 `import` 语句来引入模块，当解释器遇到 `import` 语句，如果模块在当前的搜索路径就会被导入。
2. 搜索路径是一个解释器会先进行搜索的所有目录的列表。
3. 在模块中，可以通过变量 `__name__` 来引用。
4. 一个模块只会被导入一次，不管你执行了多少次 `import` ,这样可以防止导入模块被一遍一遍地执行。
5. `from ... import` 语句让你从模块中导入一个指定的部分到当前命名空间中。
5. 全局符号表：

## 搜索路径执行顺序
当你导入一个模块， Python 解析器对模块位置的搜索顺序是：
0. 内置模块,如果内置模块中不存在，则搜索变量 `sys.path` 中的目录列表，下面几项为目录列表的组成部分。
1. 当前目录
2. 如果不在当前目录，Python 则搜索在 shell 变量 PYTHONPATH 下的每个目录。
3. 如果都找不到， Python 会查看默认路径。 Unix下，默认路径一般为 `/usr/local/lib/python/。
> 模块搜索路径存储在 system 模块的 sys.path 变量中。变量里包含当前目录， PYTHONPATH 和由安装过程决定的默认目录。

# 命名空间和作用域 
https://www.programiz.com/python-programming/namespace

## python 中的包(Packages)
You can think of packages as the directories on a file system and modules as files within directories, but don't take this analogy too literally since packages and modules need not originate from the file system. Like file system directories, packages are organized hierarchically, and packages may themselves contain subpackages, as well as regular modules.

### [package机制](https://juejin.im/post/5a2cfc4f6fb9a044ff316588)
简单来说，一个目录下如果包含 `__init__.py`，则 Python 视作一个 Python package。其中：
1. `__init__.py` 中的东西，在初始化这个包时，会首先被加载
2. package 中还可以定义 sub package。

### 初衷
最开始时，utils 可能仅仅是一个 `utils.py` 就可以了，然后调用者 `from utils import XXUtils` 就完事了。

然而大部分情况不是这样的，所有 Utils 都放到一个文件里面是 stupid 的（一个源码文件最多400-500行）。所以我们的目录结构会是这样的：

<pre>
utils/
    __init__.py
    a_util.py
    b_util.py
    ......
</pre>
调用者怎么使用呢？ `from utiles.a_util import Autils`

这种方式有一个假定：调用者要很清楚他所需要的 Utils 位于哪个 py 文件中。但是这种假设并不总是成立，大家对于同一概念的理解，极有可能是千差万别的。比如 utils,你觉得叫做 utils 合适，别人还觉得叫 tools 合适呢，其实都是一个东西。

### HOW
合理利用 package 机制，就能马上优化这一体验。

我们只要在 `__init__.py` 中这么写即可：
<pre>
__init__.py

from .a_util import AUtils
from .b_util import BUtils
</pre>

即： 调用者根本不关心你的实现在哪里，你只要给我一个utils的命名空间即可，而且确保所有的 Utils 都在这个命名空间里面。

为了更加符合 PEP8 的规范，作为库作者，我们的目录结构可能变成这样：

<pre>
utils/
    __init__.py
    _a_util.py               # 不对外界公开, 仅限本package的其他模块使用
    _b_util.py
</pre>

> 在许多开源库中，大年们经常使用这一手法来优化我们的体验。
## venv


## virtualenv使用
<pre>
pip3 install virtualenv
cd my_project_dir
virtualenv venv   # venv为虚拟环境目录名，目录名自定义
# ls
bin  include  lib  lib64  pip-selfcheck.json
source venv/bin/activate   # 激活
pip3 install requests
. venv/bin/deactivate
rm -rf venv
</pre>


## Python 中的模块、库、包有什么区别？
<pre>
module: 一个 .py 文件就是个 module
lib: 抽象概念，和另外两个不是一类，只要你喜欢，什么都是 lib, 就算只有个 hello world
package: 就是个带 __init__.py 的文件夹，并不在乎里面有什么，不过一般来讲会包含一些 packages/modules
python(库): 是参考其它编程语言的说法，就是指 python 中的完成一定功能的代码集合，供用户使用的代码组合。在 python 中是包和模块的形式。
framework(框架): 是一个基本概念上的结构，用于去解决或者处理复杂的问题。
</pre>
 

# [PEP 8](https://juejin.im/post/5afe94845188254267264da1)
## 注释
总体原则，错误的注释不如没有注释。所以当一段代码发生变化时，第一件事就是要修改注释！注释必须使用英文，最好是完整的句子，首字母大写，句后要有结束符，结束符后跟两个空格，开始下一句。如果是短语，可以省略结束符。

1. 块注释，在一段代码前增加的注释。在 # 后加一空格。段落之间以只有 # 的行间隔。比如：
<pre>
# Description : Module config.
# 
# Input : None
#
# Output : None
</pre>
2. 行注释，在一句代码后加注释。（这种方式尽量少用）
<pre>
x = x + 1               # Increment x
</pre>
3. 避免无谓的注释。

## 文档编排
1. 模块说明 --> docstring --> import --> globals & constants --> 其他定义
2. import: 标准 --> 三方 --> 自己编写; 之间空一行
## 文档描述
1. 为所有的共有模块、函数、类、方法写 docstrings; 非共有的没有必要，但是可以写注释(在 def 的下一行)。
2. 如果 docstring 要换行，参考如下例子，详见 PEP 257
<pre>
"""
Return a foobang
Optional plotz says to frobnicate the bizbaz first.
"""
</pre>

## 命名规范
1. class, function 严格照着 PEP 8 执行
2. 全局变量（全局变量，一般是常量），应该始终使用全大写

### 所有的命名类型
类型 | 例子
---- | ----
单个小写字母 | b
单个大写字母 | B
纯小写单词 | lowercase
纯大写单词 | UPPERCASE
小写加下滑线 | lower_case_with_underscopes
大写加下滑线 | UPPER_CASE_WITH_UNDERSCOPES
驼峰 | CapitalizedWords
驼峰加下滑线 | Capitalized_Words_With_Underscores
内部使用标识符(from M import * 不会导入此类对象) | _single_leading_underscore
词尾加单下滑线(避免与 python 关键字冲突) | single_trailing_underscore_
词首加双下滑线()|__double_leading_underscore
词首词尾加双下滑线 | \_\_double_leading_and_trailing_underscore__

*一般的命名规范*
Identifier | Convention
---- | ----
Module | lowercase
Class | CapWords
Functions | lowercase
Methods | lowercase
Type variables | CapWords
Constants | UPPERCASE
Packages | lowercase

> 可以通过 `pep8` 模块或者 `coala` 包来辅助检查代码

<pre>
pip install pep8
</pre>


# pep8 模块
<pre>
pep8 --show-source --show-pep8 testsuite/E40.py
pep8 --first optparse.py
pep8 --statistics -qq Python-2.5/Lib
</pre>

# Need
1. Pylint
2. Flake8
3. pytest
4. UT
5. pep8
