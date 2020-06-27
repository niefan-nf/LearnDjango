# Python 课程设计

----

## 准备

内容来自：博客园

 [削微寒的教程HelloDjango](https://www.cnblogs.com/xueweihan/category/1511653.html)

---

### 开发环境

----

`Windows 10（64位）`

`Python版本：3.8.3（64位）`

`Pycharm 2020.1`

`Django版本：2.2.3`



---

### 安装Python

官网：https://www.python.org/downloads/windows/

根据自己的系统选择下载，下载后双击安装即可。

```markdown
tip: 安装的时候注意勾选添加到环境变量中去
```



安装完成后检测`Python`是否可以正常运行。在命令行输入：`python`或`python -V`，如果出现`Python`的版本号，说明`Python`已经安装成功！

![image-20200622143509532](D:%5CLearn%5Cpython%5Cnotes%5Cimage-20200622143509532.png)

---

### 使用虚拟环境

---

#### virtualenv 创建和管理虚拟环境

---

因为`Pycharm`在创建项目的时候可以顺便创建虚拟环境，所以这里不使用`virtualenv `创建虚拟环境了。



---

#### pipenv 创建和管理虚拟环境

---

首先通过`pip install pipenv`安装`pipenv`

![image-20200622140741761](D:%5CLearn%5Cpython%5Cnotes%5Cimage-20200622140741761.png)



---

### 安装Django

使用` pipenv install django==2.3`

测试是否安装成功：

可以输入 `pipenv run python` 进入`python`解释器的交互界面，然后输入：

```python
> pipenv run python

>>> import django 
>>> print(django.get_version())
```

![image-20200622141513632](D:%5CLearn%5Cpython%5Cnotes%5Cimage-20200622141513632.png)

或者可以在`Python Console`中输入

![image-20200622141620227](D:%5CLearn%5Cpython%5Cnotes%5Cimage-20200622141620227.png)

---

### 建立Django工程

---

在我们的终端中输入:

```python
pipenv run django-amdin startproject blogproject
```

`django-admin startproject`命令用来初始化一个django项目，它接收两个参数第一个是项目名（这里是`blogproject`），第二个是指定项目生成的位置（这里我没有指定位置，他会默认在我们根目录下生成）。

![image-20200622142225267](D:%5CLearn%5Cpython%5Cnotes%5Cimage-20200622142225267.png)

```python
整个项目的目录结构

blogproject\
	blogproject\
		__init__.py
		setting.py
		urls.py
		wsgi.py
	db.sqlite3
	manage.py
	venv\
	Pipfile
```



---

### Hello Django

---

进入我们新建的`Django`项目`blogproject`下 :

`cd blogproect`

运行命令：

`pipenv run python manage.py runserver`

就可以在本机上开启一个 Web 服务器：

![image-20200622142854409](D:%5CLearn%5Cpython%5Cnotes%5Cimage-20200622142854409.png)



点击这里

![image-20200622142931551](D:%5CLearn%5Cpython%5Cnotes%5Cimage-20200622142931551.png)

或者输入 http://127.0.0.1:8000/，就可以看到`django`工作成功的界面了：

![image-20200622143435112](D:%5CLearn%5Cpython%5Cnotes%5Cimage-20200622143435112.png)



`django `默认的语言是英语，所以显示给我们的欢迎页面是英文的。我们在 `django `的配置文件里稍作修改，让它支持中文。

![image-20200622144231805](D:%5CLearn%5Cpython%5Cnotes%5Cimage-20200622144231805.png)

```python
# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'
```

把`LANGUAGE_CODE`的值改为`zh-hans`，`TIME_ZONE`的值改为`Asia/Shanghai`:

```python
# 把英文改为中文
LANGUAGE_CODE = 'zh-hans'

# 把国际时区改为中国时区（东八区）
TIME_ZONE = 'Asia/Shanghai'
```

**保存更改后**关闭 `settings.py` 文件。

再次运行开发服务器，并在浏览器中打开 http://127.0.0.1:8000/，可以看到`django`已经支持中文了。

![image-20200622144129572](D:%5CLearn%5Cpython%5Cnotes%5Cimage-20200622144129572.png)



---

## 博客应用

---

### 建立博客应用

----

创建我们的`django`博客应用，这里我做的是博客，所以命名为`blog`。进入到`manage.py`文件所在的目录（即项目根目录）下，运行：

`pipenv run python manage.py startapp blog`

命令创建一个`blog`应用：

```shell
> pipenv run python manage.py startapp blog
```

![image-20200622145529163](D:%5CLearn%5Cpython%5Cnotes%5Cimage-20200622145529163.png)

`manage.py`是我们的工程管理助手，上面使用了它的`runserver`命令开启了一个本地开发服务器，在这里使用`manage.py`的`startapp`命令创建了一个`blog`应用

---

### 应用的目录结构

---

```python
blog\
	migrations\
		__init__.py
	__init__.py
	admin.py
	apps.py
	models.py
	tests.py
	views.py
```

这个应用的文件夹结构`django`已经为我们建立好了，但它还只是包含各种文件的一个文件夹而已，`django`目前还不知道这是一个应用。所以我们得告诉`django`这是我们建立的应用，即我们还需要在`django `中的配置文件中注册这个应用。

打开项目`blogproject`下的`setting.p`y文件，它是一个设置文件，找到`INSTALLED_APPS`设置项，将`blog`应用添加进去。

```python
blogproject/blogproject/settings.py

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog', # 注册blog应用
]
```

![image-20200622151527628](D:%5CLearn%5Cpython%5Cnotes%5Cimage-20200622151527628.png)

这里我们可以看到`django`已经为我们提供了一些内置的应用，这些应用提供了各种各样的功能，这就是`django`强大的地方，通用的功能`django`已经为我们写好了，我们只需要编写与自身相关的功能代码即可。

---



## 创建Django博客的数据库模型

---



### 设计博客的数据库表结构

---

博客最主要的功能就是展示我们所写的文章，它需要从某个地方获取博客文章数据才能把文章展示出来，通常来说这个地方就是**数据库**。我们把我们写好的文章永久地保存在数据库里，当用户访问我们的博客的时候，`django`就去数据库里把这些数据拉取出来展现给用户。

博客的文章应该含有标题、正文、作者、发表时间，以及它的分类、标签、评论等数据。为了更好的存储这额数据，我们需要合理地组织数据库的表结构。

博客的初级版本主要包括博客文章，文章会有分类以及标签。一篇文章只能有一个分类，但可以有多个标签。

数据库存储的数据其实就是表格的形式，例如存储博客文章的数据库：

| 文章id |  标题   |    正文    | 发表时间 |  分类  |    标签     |
| :----: | :-----: | :--------: | :------: | :----: | :---------: |
|   1    | title 1 | content  1 | 2020-6-1 | python | python 学习 |
|   2    | title 2 | content 2  | 2020-6-2 | python | python 学习 |
|   3    | title 3 | content 3  | 2020-6-3 | django | django 学习 |
|   4    | title 4 | content 4  | 2020-6-4 |  java  |  java 学习  |

我们稍微分析一下就会发现一个问题前三篇文章的分类和标签都是相同的，这样会产生很多的重复数据，浪费存储空间。

不同的文章可能他们对应的分类或者标签都是相同的，我们把分类和标签都提取出来，分成两个单独的数据库表：

分类：

| 分类id | 分类名 |
| :----: | :----: |
|   1    | Django |
|   2    | Python |

标签：

| 标签id |   标签名    |
| :----: | :---------: |
|   1    | Django 学习 |
|   2    | Python 学习 |

---

### 编写博客模型代码

---

`django`我们提供了一套`ORM`（`Object Relational Mapping` 对象关系映射）系统

对于我们的分类数据库表，`django`只要求我么这样写：

```python
blog/models.py

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
```

`Category`就是一个标准的`Python`类，它继承了`models.Model`类，类名为`Category`。`Category`类有一个属性`name`，它是`models.CharField`的一个实例。

这样，`django `就可以把这个类翻译成数据库的操作语言，在数据库里创建一个名为 `category `的表格，这个表格的一个列名为 `name`。还有一个列 `id`，虽然没有显示定义，但 `django `会为我们自动创建。可以看出从 `Python `代码翻译成数据库语言时其规则就是一个 `Python `类对应一个数据库表格，类名即表名，类的属性对应着表格的列，属性名即列名。

我们需要 3 个表格：文章（`Post`）、分类（`Category`）以及标签（`Tag`），下面就来分别编写它们对应的 `Python `类。模型的代码通常写在相关应用的 `models.py `文件里。

```python
blog/models.py

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    """
    django模型必须继承models.Model类
    Category 只需要一个简单的分类名 name 就行了
    CharField 指定分类名 name 的数据类型，CharField 是字符型
    CharField 的 max_length 参数指定其最大长度，超过这个长度的分类名就不能被存入数据库
    django 还为我们提供了多种其它的数据类型，如日期时间类型 DateTimeField、整数类型 IntegerField 等等。
    django 内置的全部类型可查看文档：
    """

    name = models.CharField(max_length=100)


class Tag(models.Model):
    """
    标签Tag和Category一样，继承models.Model类
    """

    name = models.CharField(max_length=100)

class Post(models.Model):
    """
    文章的数据库表稍微复杂
    """
    # 文章的标题
    title = models.CharField(max_length=70)

    # 文章正文，使用了TextField
    # 存储比较短的字符串可以使用 CharField，但对于文章的正文来说可能会是一大段文本，因此使用 TextField 来存储大     段文本。
    body = models.TextField()

    # 文章的创建时间和最后一次修改时间，存储时间的字段用DateTimeField类型
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    # 文章摘要，可以没有文章摘要，但默认情况下 CharField要求我们必须存入数据，否则就会报错。
    # 指定 CharField 的 blank=True 参数值后就可以允许空值了
    excerpt = models.CharField(max_length=200, blank=True)

    """
    这是分类与标签
    我们在这里把文章对应的数据库表和分类、标签对应的数据库表关联了起来，但是关联形式稍微有点不同。
    我们规定一篇文章只能对应一个分类，但是一个分类下可以有多篇文章，所以我们使用的是 ForeignKey，即一
    对多的关联关系。且自 django 2.0 以后，ForeignKey 必须传入一个 on_delete 参数用来指定当关联的
    数据被删除时，被关联的数据的行为，我们这里假定当某个分类被删除时，该分类下全部文章也同时被删除，因此
    使用 models.CASCADE 参数，意为级联删除。
    而对于标签来说，一篇文章可以有多个标签，同一个标签下也可能有多篇文章，所以我们使用 
    ManyToManyField，表明这是多对多的关联关系。
    同时我们规定文章可以没有标签，因此为标签 tags 指定了 blank=True。
    """
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    
    """
    文章作者，这里User是从 django.contrib.auth.models 导入的
    django.contrib.auth 是 django 内置的应用，专门用于处理网站用户的注册，登录流程，User是 django
    为我们写好的用户模型
    这里我们通过ForeignKey 把文章和 User 关联了起来。
    因为我们规定一篇文章只能有一个作者，而一个作者可能会写很多篇文章，因此这是一对多的关联关系，和Category 类似
    """
    
    author = models.ForeignKey(User, on_delete=models.CASCADE) 


```

---

### 博客模型代码详解

---

首先是 `Category` 和 `Tag` 类，它们均继承自 `models.Model` 类，这是 django 规定的。`Category` 和 `Tag` 类均有一个`name` 属性，用来存储它们的名称。由于分类名和标签名一般都是用字符串表示，因此我们使用了 `CharField` 来指定 `name` 的数据类型，同时 `max_length` 参数则指定 `name` 允许的最大长度，超过该长度的字符串将不允许存入数据库。除了 `CharField` ，django 还为我们提供了更多内置的数据类型，比如时间类型 `DateTimeField`、整数类型 `IntegerField` 等等。

`Post` 类也一样，必须继承自 `models.Model` 类。文章的数据库表稍微复杂一点，主要是列更多，我们指定了这些列：

- `title`：文章的标题，数据类型是 `CharField`，允许的最大长度 `max_length = 70`。

- `body`：文章正文，我们使用了 `TextField`。比较短的字符串存储可以使用 `CharField`，但对于文章的正文来说可能会是一大段文本，因此使用 `TextField` 来存储大段文本。

- `created_time` 和 `modified_time`：这两个列分别表示文章的创建时间和最后一次修改时间，存储时间的列用 `DateTimeField` 数据类型。

- `excerpt`：文章摘要，可以没有文章摘要，但默认情况下 `CharField` 要求我们必须存入数据，否则就会报错。指定 `CharField` 的 `blank=True` 参数值后就可以允许空值了。

- `category` 和 `tags`：分类与标签，分类与标签的模型我们已经定义在上面。我们把文章对应的数据库表和分类、标签对应的数据库表关联了起来，但是关联形式稍微有点不同。我们规定一篇文章只能对应一个分类，但是一个分类下可以有多篇文章，所以我们使用的是 `ForeignKey`，即一对多的关联关系。且自 `django 2.0` 以后，`ForeignKey `必须传入一个 `on_delete `参数用来指定当关联的数据被删除时，被关联的数据的行为，我们这里假定当某个分类被删除时，该分类下全部文章也同时被删除，因此使用 `models.CASCADE` 参数，意为级联删除。

  而对于标签来说，一篇文章可以有多个标签，同一个标签下也可能有多篇文章，所以我们使用 `ManyToManyField`，表明这是多对多的关联关系。同时我们规定文章可以没有标签，因此为标签 tags 指定了 `blank=True`。

- `author`：文章作者，这里 `User` 是从 `django.contrib.auth.models` 导入的。`django.contrib.auth` 是 `django `内置的应用，专门用于处理网站用户的注册、登录等流程。其中 `User` 是 `django `为我们已经写好的用户模型，和我们自己编写的 `Category` 等类是一样的。这里我们通过 `ForeignKey` 把文章和 `User`关联了起来，因为我们规定一篇文章只能有一个作者，而一个作者可能会写多篇文章，因此这是一对多的关联关系，和 `Category` 类似。



---



### 多对一和多对多两种关联关系

---

前面使用了两种关联数据库表的形式：`ForeignKey`和`ManyToManyField`。

---



#### ForeignKey

---

`ForeignKey`表明一种一对多的关联关系。比如我们这里的文章和分类的关系，一篇文章只能对应一个分类，而一个分类下可以有多篇文章。

在数据库表中，它们的实际存储情况如下：

| 文章ID |  标题   |  正文  | 分类ID |
| :----: | :-----: | :----: | :----: |
|   1    | title 1 | body 1 |   1    |
|   2    | title 2 | body 2 |   2    |
|   3    | title 3 | body 3 |   1    |
|   4    | title 4 | body 4 |   2    |

| 分类ID | 分类名 |
| :----: | :----: |
|   1    | Django |
|   2    | Python |

可以看到文章和分类实际上是通过文章数据库表中 `分类 ID` 这一列关联的。当要查询文章属于哪一个分类时，只需要查看其对应的分类 ID 是多少，然后根据这个分类 ID 就可以从分类数据库表中找到该分类的数据。例如这里文章 1、3对应的分类 ID 均为 1，而分类 ID 为 1 的分类名为 `django`，所以文章 1、3 属于分类 `django`。同理文章 2、4 属于分类 `Python`。

反之，要查询某个分类下有哪些文章，只需要查看对应该分类 ID 的文章有哪些即可。例如这里 `django `的分类 ID 为 1，而对应分类 ID 为 1 的文章有文章 1、3，所以分类 `django `下有 2 篇文章。

---



#### ManyToManyField

---

`ManyToManyField` 表明一种多对多的关联关系，比如这里的文章和标签，一篇文章可以有多个标签，而一个标签下也可以有多篇文章。反应到数据库表格中，它们的实际存储情况是这样的：

| 文章 ID |  标题   |  正文  |
| :-----: | :-----: | :----: |
|    1    | title 1 | body 1 |
|    2    | title 2 | body 2 |
|    3    | title 3 | body 3 |
|    4    | title 4 | body 4 |

| 标签 ID |   标签名    |
| :-----: | :---------: |
|    1    | Django 学习 |
|    2    | Python 学习 |

| 文章 ID | 标签 ID |
| :-----: | :-----: |
|    1    |    1    |
|    1    |    2    |
|    2    |    1    |
|    3    |    2    |

多对多的关系无法再像一对多的关系中的例子一样在文章数据库表加一列 **分类 ID** 来关联了，因此需要额外建一张表来记录文章和标签之间的关联。例如**文章 ID** 为 1 的文章，既对应着 **标签 ID** 为 1 的标签，也对应着 **标签 ID** 为 2 的标签，即文章 1 既属于标签 1：`django `学习，也属于标签 2：`Python `学习。

反之，**标签 ID** 为 1 的标签，既对应着 **文章 ID** 为 1 的文章，也对应着 **文章 ID** 为 2 的文章，即标签 1：`django `学习下有两篇文章。



---



## Django 迁移、操作数据库

---

前面编写好了数据库模型的代码，但仅仅只是`Python`代码，`django`还没有把它翻译成数据库语言，因此实际上这些数据库表还没有真正的在数据库中创建。

---

### 迁移数据库

---

为了让`django`完成翻译，创建好这些数据库表，我们可以再一次使用我们的工程管理助手 — `manage.py`。切换到`manage.py` 文件所在的目录（项目根目录）下，分别运行 `pipenv run python manage.py makemigrations` 和`pipenv run python manage.py migrate`命令：

```python
> pipenv run python manage.py makemigrations
Migrations for 'blog':
  blog\migrations\0001_initial.py
    - Create model Category
    - Create model Tag
    - Create model Post

> pipenv run python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, blog, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying blog.0001_initial... OK
  Applying sessions.0001_initial... OK

```

当我们执行了 `python manage.py makemigrations` 后，`django `在 `blog `应用的 `migrations\` 目录下生成了一个 `0001_initial.py `文件，这个文件是 `django `用来记录我们对模型做了哪些修改的文件。目前来说，我们在 `models.py `文件里创建了 3 个模型类，`django `把这些变化记录在了 `0001_initial.py` 里。

不过此时还只是告诉了 `django `我们做了哪些改变，为了让 `django `真正地为我们创建数据库表，接下来又执行了 `python manage.py migrate` 命令。`django `通过检测应用中 `migrations\ `目录下的文件，得知我们对数据库做了哪些操作，然后它把这些操作翻译成数据库操作语言，从而把这些操作作用于真正的数据库。

运行以下的命令可以看看django究竟为我们做了什么：

```python
> pipenv run python manage.py sqlmigrate blog 0001

BEGIN;
--
-- Create model Category
--
CREATE TABLE "blog_category" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL);
--
-- Create model Tag
--
CREATE TABLE "blog_tag" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL);
--
-- Create model Post
--
CREATE TABLE "blog_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(70) NOT NULL, "body" text NOT NULL, "cr
eated_time" datetime NOT NULL, "modified_time" datetime NOT NULL, "excerpt" varchar(200) NOT NULL, "author_id" integer NOT NULL RE
FERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "category_id" integer NOT NULL REFERENCES "blog_category" ("id") DEFERR
ABLE INITIALLY DEFERRED);
CREATE TABLE "blog_post_tags" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "post_id" integer NOT NULL REFERENCES "blog_post"
("id") DEFERRABLE INITIALLY DEFERRED, "tag_id" integer NOT NULL REFERENCES "blog_tag" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "blog_post_author_id_dd7a8485" ON "blog_post" ("author_id");
CREATE INDEX "blog_post_category_id_c326dbf8" ON "blog_post" ("category_id");
CREATE UNIQUE INDEX "blog_post_tags_post_id_tag_id_4925ec37_uniq" ON "blog_post_tags" ("post_id", "tag_id");
CREATE INDEX "blog_post_tags_post_id_a1c71c8a" ON "blog_post_tags" ("post_id");
CREATE INDEX "blog_post_tags_tag_id_0875c551" ON "blog_post_tags" ("tag_id");
COMMIT;

```

我们可以看到经`django`翻译后的数据库表创建语句。

---

### 选择数据库版本

---

这里我们并没有安装任何的数据库软件，`django`就帮我们迁移了数据库。这是因为我们使用了`Python`内置的`SQLite3`数据库。

`SQLite3 `是一个十分轻巧的数据库，它仅有一个文件。你可以看一到项目根目录下多出了一个 `db.sqlite3` 的文件，这就是 `SQLite3 `数据库文件，`django `博客的数据都会保存在这个数据库文件里。

`django `在 `settings.py` 里为我们做了一些默认的数据库配置：

```python
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

```

可以看到默认的数据库引擎就是使用的`SQLite3`。

---

### 用Django的方式操作数据库

---

数据库最主要的操作就是往里面存入数据、从中取出数据、修改已保存的数据和删除不再需要的数据（合称 `CURD`）。和创建数据库表一样，`django `为这些操作提供了一整套方法，从而把我们从数据库语言中解放出来。我们不用学习如何利用数据库语言去完成这些操作，只要简单地调用几个 `Python `函数就可以满足我们的需求。

---

#### 存数据

---

先在命令行中来探索一下这些函数，感受一下如何用 `django `的方式来操作数据库。在 `manage.py` 所在目录下运行 `pipenv run python manage.py shell` 命令：

```python
> pipenv run python manage.py shell
Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>>
```

首先我们来创建一个分类和标签：

```python
>>> from blog.models import Category, Tag, Post
>>> c = Category(name='category test')
>>> c.save()
>>> t = Tag(name='tag test')
>>> t.save()
```

我们首先导入 3 个之前写好的模型类，然后实例化了一个 `Category` 类和一个 `Tag` 类，为他们的属性 `name` 赋了值。为了让 `django `把这些数据保存进数据库，调用实例的 `save` 方法即可。

再创建一篇文章试试，但创建文章之前，我们需要先创建一个 `User`，用于指定文章的作者。创建 `User `的命令 `django `已经帮我们写好了，依然是通过 `manage.py` 来运行。首先按住` Ctrl + c` 退出命令交互栏（一次退不出就连续多按几次），运行 `pipenv run python manage.py createsuperuser` 命令并根据提示创建用户：

```python
> pipenv run python manage.py createsuperuser
用户名 (leave blank to use 'fan'): fan
电子邮件地址: 1528023125@qq.com
Password:
Password (again):
Superuser created successfully.
```

运行 `python manage.py createsuperuser` 开始创建用户，之后会提示你输入用户名、邮箱、密码和确认密码，按照提示输入即可。**注意一点的是密码输入过程中不会有任何字符显示，不要误以为你的键盘出问题了，正常输入即可。**最后出现` Superuser created successfully.` 说明用户创建成功了。

再次运行 `python manage.py shell` 进入 Python 命令交互栏，开始创建文章：

```python
>>> from blog.models import Category, Tag, Post
>>> from django.utils import timezone
>>> from django.contrib.auth.models import User

>>> user = User.objects.get(username='fan')
>>> c = Category.objects.get(name='category test')

>>> p = Post(title='title test', body='body test', created_time=timezone.now(), modified_time=timezone.now(), category=c, author=user)
>>> p.save()
```

由于我们重启了 `shell`，因此需要重新导入了 `Category`、`Tag`、`Post` 以及 `User`。我们还导入了一个 `django `提供的辅助模块 `timezone`，这是因为我们需要调用它的 `now()` 方法为 `created_time` 和 `modified_time` 指定时间，容易理解 `now` 方法返回当前时间。然后我们根据用户名和分类名，通过 `get` 方法取出了存在数据库中的 `User` 和 `Category`（取数据的方法将在下面介绍）。接着我们为文章指定了 `title`、`body` 、`created_time`、`modified_time`值，并把它和前面创建的 `Category `以及 `User `关联了起来。允许为空 `excerpt`、`tags` 我们就没有为它们指定值了。

---

#### 取数据

---

数据已经存入数据库了，现在要把它们取出来看看：

```python
>>> Category.objects.all()
<QuerySet [<Category: Category object>]>
>>> Tag.objects.all()
<QuerySet [<Tag: Tag object>]>
>>> Post.objects.all()
<QuerySet [<Post: Post object>]>
>>>
```

`objects` 是我们的模型管理器，它为我们提供一系列从数据库中取数据方法，这里我们使用了 `all` 方法，表示我们要把对应的数据全部取出来。可以看到 `all` 方法都返回了数据，这些数据应该是我们之前存进去的，但是显示的字符串有点奇怪，无法看出究竟是不是我们之前存入的数据。为了让显示出来的数据更加人性化一点，我们为 3 个模型分别增加一个 `__str__` 方法：

```python
blog/models.py

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    """
    django模型必须继承models.Model类
    Category 只需要一个简单的分类名 name 就行了
    CharField 指定分类名 name 的数据类型，CharField 是字符型
    CharField 的 max_length 参数指定其最大长度，超过这个长度的分类名就不能被存入数据库
    django 还为我们提供了多种其它的数据类型，如日期时间类型 DateTimeField、整数类型 IntegerField 等等。
    django 内置的全部类型可查看文档：
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Tag(models.Model):
    """
    标签Tag和Category一样，继承models.Model类
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    文章的数据库表稍微复杂
    """
    # 文章的标题
    title = models.CharField(max_length=70)

    # 文章正文，使用了TextField
    # 存储比较短的字符串可以使用 CharField，但对于文章的正文来说可能会是一大段文本，因此使用 TextField 来存储大段文本。
    body = models.TextField()

    # 文章的创建时间和最后一次修改时间，存储时间的字段用DateTimeField类型
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    # 文章摘要，可以没有文章摘要，但默认情况下 CharField要求我们必须存入数据，否则就会报错。
    # 指定 CharField 的 blank=True 参数值后就可以允许空值了
    excerpt = models.CharField(max_length=200, blank=True)

    """
    这是分类与标签
    我们在这里把文章对应的数据库表和分类、标签对应的数据库表关联了起来，但是关联形式稍微有点不同。
    我们规定一篇文章只能对应一个分类，但是一个分类下可以有多篇文章，所以我们使用的是 ForeignKey，即一
    对多的关联关系。且自 django 2.0 以后，ForeignKey 必须传入一个 on_delete 参数用来指定当关联的
    数据被删除时，被关联的数据的行为，我们这里假定当某个分类被删除时，该分类下全部文章也同时被删除，因此
    使用 models.CASCADE 参数，意为级联删除。
    而对于标签来说，一篇文章可以有多个标签，同一个标签下也可能有多篇文章，所以我们使用 
    ManyToManyField，表明这是多对多的关联关系。
    同时我们规定文章可以没有标签，因此为标签 tags 指定了 blank=True。
    """
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    """
    文章作者，这里User是从 django.contrib.auth.models 导入的
    django.contrib.auth 是 django 内置的应用，专门用于处理网站用户的注册，登录流程，User是 django
    为我们写好的用户模型
    这里我们通过ForeignKey 把文章和 User 关联了起来。
    因为我们规定一篇文章只能有一个作者，而一个作者可能会写很多篇文章，因此这是一对多的关联关系，和Category 类似
    """

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

```

定义好 `__str__` 方法后，解释器显示的内容将会是 `__str__` 方法返回的内容。这里 `Category` 返回分类名 `name` ，`Tag` 返回标签名，而 `Post` 返回它的 `title`。

先按 `Ctrl + c `退出 `Shell`，再重新运行 `python manage.py shell` 进入 `Shell`。

```python
>>> from blog.models import Category, Tag, Post
>>> Category.objects.all()
<QuerySet [<Category: category test>]>

>>> Tag.objects.all()
<QuerySet [<Tag: tag test>]>

>>> Post.objects.all()
<QuerySet [<Post: title test>]>

>>> Post.objects.get(title='title test')
<Post: title test>
```

可以看到返回的是我们之前存入的数据。

此外我们在创建文章时提到了通过 `get` 方法来获取数据，这里 `all` 方法和 `get` 方法的区别是：`all` 方法返回全部数据，是一个类似于列表的数据结构（`QuerySet`）；而 `get` 返回一条记录数据，如有多条记录或者没有记录，`get` 方法均会抛出相应异常。

---

#### 改数据

---

尝试修改数据：

```python
>>> c = Category.objects.get(name='category test')
>>> c.name = 'category test new'
>>> c.save()
>>> Category.objects.all()
<QuerySet [<Category: test category new>]>
```

首先通过 `get` 方法根据分类名 `name` 获取值为 category test 到分类，修改它的 `name` 属性为新的值 category test new，然后调用 `save` 方法把修改保存到数据库，之后可以看到数据库返回的数据已经是修改后的值了。`Tag`、`Post` 的修改也一样。

----

#### 删数据

---

删除掉数据：

```python
>>> p = Post.objects.get(title='title test')
>>> p
<Post: title test>
>>> p.delete()
(1, {'blog.Post_tags': 0, 'blog.Post': 1})
>>> Post.objects.all()
<QuerySet []>
```

先根据标题 `title` 的值从数据库中取出 `Post`，保存在变量 `p` 中，然后调用它的`delete` 方法，最后看到 `Post.objects.all()` 返回了一个空的 QuerySet（类似于一个列表），表明数据库中已经没有 Post，Post 已经被删除了。



---



## Django的视图函数

---

### Django处理HTTP请求

---

Web应用的交互过程其实就是HTTP请求与响应的过程。无论是在PC端还是在移动端，我们通常使用浏览器来上网，上网流程大致是这样的：

1. 打开浏览器，在地址栏输入我们想访问的网址，比如 https://www.baidu.com/
2. 浏览器知道我们想要访问那个网址后，它在后台帮我们做了很多的事情。主要就是把我们的访问意图包装成一个`HTTP`请求，发送给我们想要访问的网址对应的服务器。通俗点说就是浏览器帮我们通知网站的服务器：有人来看你了啦，访问的请求都写在`HTTP`报文里了，你安装要求处理好告诉我，我在帮你回应他。
3. 服务器处理了`HTTP`请求，然后生成一段`HTTP`响应给浏览器。浏览器解读这个响应，把相关的内容在浏览器里显示出来，于是我们就看到了网站的内容。比如你访问了博客园主页：https://cnblogs.com/，服务器接收到这个请求后就知道用户访问的是首页，首页显示的是全部文章列表，于是它从数据库里把文章数据取出来，生成一个写着这些数据的 `HTML `文档，包装到 `HTTP `响应里发给浏览器，浏览器解读这个响应，把 `HTML `文档显示出来，我们就看到了文章列表的内容。

因此，`django `作为一个 `Web `框架，它的使命就是处理流程中的第二步。即接收浏览器发来的 `HTTP `请求，返回相应的 `HTTP `响应。于是引出这么几个问题：

1. `django `如何接收 `HTTP `请求？
2. `django `如何处理这个 `HTTP `请求？
3. `django `如何生成 `HTTP `响应？

对于如何处理这些问题，`django `有其一套规定的机制。我们按照 `django `的规定，就能开发出所需的功能。

---

### Hello 视图函数

---

这里先以一个简单的`Hello World` 为例来看看 `django` 处理上述问题的机制是怎么样的。

---

#### 绑定 URL 与视图函数

---

首先 `django `需要知道当用户访问不同的网址时，应该如何处理这些不同的网址（即所说的路由）。`django `的做法是把不同的网址对应的处理函数写在一个` urls.py `文件里，当用户访问某个网址时，`django `就去会这个文件里找，如果找到这个网址，就会调用和它绑定在一起的处理函数（叫做视图函数）。

下面是具体的做法，**首先在 blog 应用的目录下创建一个 urls.py 文件**，这是我们的目录结构如下:

```python
blog\
	migrations\
    	0001_initial.py
        __init__.py
	__init__.py
    admin.py
    apps.py
    models.py
    tests.py
    urls.py
    views.py
```

然后在`urls.py`中写入：

```python 
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

我们首先从` django.urls` 导入了 `path` 函数，又从当前目录下导入了 views 模块。然后我们把网址和处理函数的关系写在了 `urlpatterns` 列表里。

绑定关系的写法是把网址和对应的处理函数作为参数传给 `path` 函数（第一个参数是网址，第二个参数是处理函数），另外我们还传递了另外一个参数 `name`，这个参数的值将作为处理函数 `index` 的别名，这在以后会用到。

注意这里我们的网址实际上是一个规则，`django `会用这个规则去匹配用户实际输入的网址，如果匹配成功，就会调用其后面的视图函数做相应的处理。

比如说我们本地开发服务器的域名是 [http://127.0.0.1:8000](http://127.0.0.1:8000/) ，那么当用户输入网址 [http://127.0.0.1:8000](http://127.0.0.1:8000/) 后，`django `首先会把协议 `http`、域名 `127.0.0.1` 和端口号 `8000 `去掉，此时只剩下一个空字符串，而 `''` 的模式正是匹配一个空字符串，于是二者匹配，`django `便会调用其对应的 `views.index` 函数。

<h5 style="color:red">在这里需要注意的是</h5>

```
在 blogproject\ 目录下（即 settings.py 所在的目录），原本就有一个 urls.py 文件，这是整个工程项目的 URL 配置文件。而我们这里新建了一个 urls.py 文件，且位于 blog 应用下。这个文件将用于 blog 应用相关的 URL 配置，这样便于模块化管理。不要把两个文件搞混了。
```

---

#### 编写视图函数

---

编写我们的`views.index`视图函数了，视图函数的定义在`views.py`文件里：

```python
blog/views.py

from django.http import HttpResponse

def index(request):
    return HttpResponse("欢迎访问我的博客首页！")
```

前面说过，`Web `服务器的作用就是接收来自用户的 `HTTP `请求，根据请求内容作出相应的处理，并把处理结果包装成 `HTTP `响应返回给用户。

这个两行的函数体现了这个过程。它首先接受了一个名为 `request` 的参数，这个 `request` 就是 `django `为我们封装好的 `HTTP `请求，它是类 `HttpRequest` 的一个实例。然后我们便直接返回了一个 `HTTP `响应给用户，这个 `HTTP `响应也是 `django `帮我们封装好的，它是类 `HttpResponse` 的一个实例，只是我们给它传了一个自定义的字符串参数。

浏览器接收到这个响应后就会在页面上显示出我们传递的内容 ：欢迎访问我的博客首页！

---

#### 配置项目的 URL

---

前面我们建立了一个 `urls.py` 文件，并且绑定了 `URL `和视图函数 `index`，但是 `django `并不知道。`django `匹配 `URL `模式是在` blogproject\ `目录（即 `settings.py` 文件所在的目录）的 `urls.py` 下的，所以我们要把 `blog `应用下的 `urls.py `文件包含到 `blogproject\urls.py` 里去：

`blogproject\urls.py`：

```python
blogproject/urls.py

"""
一大段注释
"""

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
```

修改为：

```python
from django.contrib import admin
from django.urls import path, include

urlspatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls'))
]
```

我们这里导入了一个 `include` 函数，然后利用这个函数把 `blog `应用下的 `urls.py` 文件包含了进来。此外` include `前还有一个 `''`，这是一个空字符串。这里也可以写其它字符串，`django `会把这个字符串和后面 `include `的 `urls.py `文件中的 `URL `拼接。比如说如果我们这里把 `''` 改成 `'blog/'`，而我们在 `blog\urls.py` 中写的 `URL `是 `''`，即一个空字符串。那么 `django `最终匹配的就是 `blog/` 加上一个空字符串，即 `blog/`。

---

#### 运行结果

---

运行 `pipenv run python manage.py runserver` 打开开发服务器，在浏览器中输入本机服务器地址：http://127.0.0.1:8000/，可以看到`django`返回的内容：

![image-20200622215208031](D:%5CLearn%5Cpython%5Cnotes%5Cimage-20200622215208031.png)

---



### 使用 django 模板系统

---

这基本上就是 `django `的开发流程了，写好处理 `HTTP `请求和返回 `HTTP `响应的视图函数，然后把视图函数绑定到相应的 `URL `上。

我们看到在视图函数里返回的是一个 `HttpResponse` 类的实例，我们给它传入了一个希望显示在用户浏览器上的字符串。但是我们的博客不可能只显示这么一句话，它有可能会显示很长很长的内容。比如我们发布的博客文章列表，或者一大段的博客文章。我们不能每次都把这些大段大段的内容传给 `HttpResponse`。

`django `对这个问题给我们提供了一个很好的解决方案，叫做模板系统。django 要我们把大段的文本写到一个文件里，然后 `django `自己会去读取这个文件，再把读取到的内容传给 `HttpResponse`。让我们用模板系统来改造一下上面的例子。

首先在我们的项目**根目录**（即 `manage.py` 文件所在目录）下建立一个名为 `templates `的文件夹，用来存放我们的模板。然后在 `templates\` 目录下建立一个名为 `blog `的文件夹，用来存放和 `blog `应用相关的模板。

当然模板存放在哪里是无关紧要的，只要 `django `能够找到的就好。但是我们建立这样的文件夹结构的目的是把不同应用用到的模板隔离开来，这样方便以后维护。我们在 `templates\blog `目录下建立一个名为` index.html` 的文件，此时你的目录结构应该是这样的：

```python
blogproject\
    manage.py
 	...
    templates\
    	blog\
    		index.html
```

> <h5 style="color:red">注意：</h5>
>
> 再一次强调 `templates\` 目录位于项目根目录，而 `index.html` 位于 `templates\blog` 目录下，而不是 `blog `应用下，如果弄错了你可能会得到一个 `TemplateDoesNotExist` 异常。如果遇到这个异常，请回来检查一下模板目录结构是否正确。

在 `templates\blog\index.html `文件里写入下面的代码：

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{{ title }}</title>
</head>
<body>
<h1>{{ welcome }}</h1>
</body>
</html>
```

这是一个标准的 HTML 文档，只是里面有两个比较奇怪的地方：`{{ title }}`，`{{ welcome }}`。这是 `django `规定的语法。用 `{{ }}` 包起来的变量叫做模板变量。`django` 在渲染这个模板的时候会根据我们传递给模板的变量替换掉这些变量。最终在模板中显示的将会是我们传递的值。

> 
>
> `index.html` 必须以 `UTF-8` 的编码格式保存，且小心不要往里面添加一些特殊字符，否则极有可能得到一个 `UnicodeDecodeError` 这样的错误。

模板写好了，还得告诉 `django `去哪里找模板，在 `settings.py` 文件里设置一下模板文件所在的路径。在 `settings.py` 找到 `TEMPLATES` 选项，它的内容是这样的：

```python
blogproject/settings.py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.djangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

其中 `DIRS` 就是设置模板的路径，在 `[]` 中写入 `os.path.join(BASE_DIR, 'templates')`，即像下面这样：

```python
blogproject/settings.py

TEMPLATES = [
    {
        ...
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
     	...
    },
]
```

这里 `BASE_DIR` 是` settings.py` 在配置开头前面定义的变量，记录的是工程根目录 `blogproject\ `的值。在这个目录下有模板文件所在的目录 `templates\`，于是利用`os.path.join` 把这两个路径连起来，构成完整的模板路径，`django `就知道去这个路径下面找我们的模板了。

视图函数可以改一下了：

```python
blog/views.py

from django.shortcuts import render


def index(request):
    return render(request, 'blog/index.html', context={
        'title': '我的博客首页',
        'welcome': '欢迎访问我的博客首页'
    })
```

这里我们不再是直接把字符串传给 `HttpResponse` 了，而是调用 `django `提供的 `render` 函数。这个函数根据我们传入的参数来构造 `HttpResponse`。

我们首先把 `HTTP `请求传了进去，然后 `render` 根据第二个参数的值 `blog/index.html `找到这个模板文件并读取模板中的内容。之后 `render` 根据我们传入的 `context` 参数的值把模板中的变量替换为我们传递的变量的值，`{{ title }}` 被替换成了 `context` 字典中 `title` 对应的值，同理 `{{ welcome }}` 也被替换成相应的值。

最终，我们的 `HTML `模板中的内容字符串被传递给 `HttpResponse` 对象并返回给浏览器（`django `在 `render` 函数里隐式地帮我们完成了这个过程），这样用户的浏览器上便显示出了我们写的 `HTML `模板的内容了。

![image-20200622221435248](D:%5CLearn%5Cpython%5Cnotes%5Cimage-20200622221435248.png)

----



## 为博客添加皮肤

---

### 首页视图函数

---

前面说明了`django`的开发流程，即先配置`URL`，把`URL`和相应的视图函数绑定，一般写在`urls.py`文件里，然后在工程的`urls.py`文件引入。其次是编写视图函数，视图中需要渲染模板，这里也在`settings.py`中进行了模板相关的配置，让`django`能够找到需要渲染的模板。最后把渲染完成的`HTTP`响应完成返回就可以了。

首页的视图函数：

```python
blog/views.py

from django.shortcuts import render
from .models import Post

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
```

这里是`objects`的`all()`方法从数据库里获取了全部的文章，存到了`post_list`变量里。all()方法返回的是一个`QuerySet`（类似于列表的数据结构），通常来说博客文章列表是按照文章发表时间倒序排列的，即最新的文章排在最前面。所以这里我们调用了`order_by()`方法对这个返回的`queryset`进行排序。排序的字段是`created_time()`，即文章的创建时间。`-`表示逆序，如果不加`-`则是正序。

我们渲染了 `blog\index.html`模板文件，并且把包含文章列表的数据的`post_list`变量传给了模板。

---



### 处理静态文件

---

我们需要都`django`做一些必要的配置，才能让`django`知道如何在开发服务器中引入这些`CSS`和`JavaScript`文件，这样才能让博客页面的`CSS`样式生效。

我们需要把`CSS`和`JavaScript`文件放在`blog`应用的`static\`目录下。因此，先在`blog`应用下建立一个`static`文件夹。同时，为了避免和其他应用中的`CSS`和`JavaScript`文件命令冲突，我们在`static\`目录下再新建一个`blog`文件夹，把博客模板中的`css`和`js`文件，以及同文件夹里面的全部文件一同拷入这个目录。最终我们的目录结构如下：

```python
blog\
    __init__.py
    static\
    	blog\
    		css\
    			.css 文件...
    		js\
    			.js 文件...
    admin.py
    apps.py
    migrations\
        __init__.py
    models.py
    tests.py
    views.py
```

用下载的博客模板中的 `index.html `文件替换掉之前我们自己写的 `index.html` 文件。

开启服务器，看看效果：

![image-20200623161911539](D:%5CLearn%5Cpython%5Cnotes%5Cimage-20200623161911539.png)

看到首页显示的样式非常混乱，原因是浏览器无法正确加载 `CSS `等样式文件。需要以 `django `的方式来正确地处理 `CSS `和 `JavaScript `等静态文件的加载路径。`CSS `样式文件通常在 `HTML `文档的 `head `标签里引入，打开` index.html `文件，在文件的开始处找到 `head `标签包裹的内容。

```html
templates/blog/index.html

<!DOCTYPE html>
<html>
  <head>
      <title>Black &amp; White</title>

      <!-- meta -->
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">

      <!-- css -->
      <link rel="stylesheet" href="css/bootstrap.min.css">
      <link rel="stylesheet" href="http://code.ionicframework.com/ionicons/2.0.1/css/ionicons.min.css">
      <link rel="stylesheet" href="css/pace.css">
      <link rel="stylesheet" href="css/custom.css">

      <!-- js -->
      <script src="js/jquery-2.1.3.min.js"></script>
      <script src="js/bootstrap.min.js"></script>
      <script src="js/pace.min.js"></script>
      <script src="js/modernizr.custom.js"></script>
  </head>
  <body>
      <!-- 其它内容 -->
      <script src="js/script.js"></script>
  </body>
</html>
```

`CSS `样式文件的路径在 `link `标签的 `href `属性里，而 `JavaScript `文件的路径在 `script `标签的 `src `属性里。可以看到诸如 `href="css/bootstrap.min.css"` 或者` src="js/jquery-2.1.3.min.js"` 这样的引用，由于引用文件的路径不对，所以浏览器引入这些文件失败。我们需要把它们改成正确的路径。把代码改成下面样子，正确地引入 `static `文件下的 `CSS `和 `JavaScript `文件：

```html
templates/blog/index.html

{% load static %}
<!DOCTYPE html>
<html>
  <head>
      <title>Black &amp; White</title>

      <!-- meta -->
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">

      <!-- css -->
      <link rel="stylesheet" href="http://code.ionicframework.com/ionicons/2.0.1/css/ionicons.min.css">
      <link rel="stylesheet" href="{% static 'blog/css/bootstrap.min.css' %}">
      <link rel="stylesheet" href="{% static 'blog/css/pace.css' %}">
      <link rel="stylesheet" href="{% static 'blog/css/custom.css' %}">

      <!-- js -->
      <script src="{% static 'blog/js/jquery-2.1.3.min.js' %}"></script>
      <script src="{% static 'blog/js/bootstrap.min.js' %}"></script>
      <script src="{% static 'blog/js/pace.min.js' %}"></script>
      <script src="{% static 'blog/js/modernizr.custom.js' %}"></script>
  </head>
  <body>
      <!-- 其它内容 -->
      <script src="{% static 'blog/js/script.js' %}"></script>
  </body>
</html>
```

但是当我们重新启动服务器后可以看到，服务器还是没有找到我们的静态资源：

![image-20200623161911539](D:%5CLearn%5Cpython%5Cnotes%5Cimage-20200623161911539.png)

还需要再我们的`settings.py`中加上：

```python
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'templates/blog/static')
]
```

最后可以看到我们的静态资源已经被引入了，首页的样式也没有乱了：

![image-20200623164811103](D:%5CLearn%5Cpython%5Cnotes%5Cimage-20200623164811103.png)

---



### 修改模板

---

目前我们看到的只是模板中预先填充的一些数据，我们得让它显示从数据库中获取的文章数据。下面来稍微改造一下模板：

在模板 `index.html` 中你会找到一系列 `article `标签：

```html
templates/blog/index.html

...
<article class="post post-1">
  ...
</article>

<article class="post post-2">
  ...
</article>

<article class="post post-3">
  ...
</article>
...
```

这里面包裹的内容显示的就是文章数据了。我们前面在视图函数 `index `里给模板传了一个 `post_list` 变量，它里面包含着从数据库中取出的文章列表数据。就像 `Python `一样，我们可以在模板中循环这个列表，把文章一篇篇循环出来，然后一篇篇显示文章的数据。要在模板中使用循环，需要使用到前面提到的模板标签，这次使用 `{% for %} `模板标签。将 `index.html` 中多余的 `article `标签删掉，只留下一个 `article `标签，然后写上下列代码：

```html
templates/blog/index.html

...
{% for post in post_list %}
  <article class="post post-{{ post.pk }}">
    ...
  </article>
{% empty %}
  <div class="no-post">暂时还没有发布的文章！</div>
{% endfor %}
...
```

可以看到语法和 `Python `的 `for `循环类似，只是被 `{% %}` 这样一个模板标签符号包裹着。`{% empty %}` 的作用是当 `post_list` 为空，即数据库里没有文章时显示 `{% empty %}` 下面的内容，最后我们用 `{% endfor %}` 告诉 `django `循环在这里结束了。

现在我们可以在循环体内通过 `post` 变量访问单篇文章的数据了。分析 `article `标签里面的 `HTML `内容，`h1 `显示的是文章的标题，

```html
<h1 class="entry-title">
	<a href="single.html">Adaptive Vs. Responsive Layouts And Optimal Text Readability</a>
</h1>
```

我们把标题替换成 `post` 的 `title` 属性值。注意要把它包裹在模板变量里，因为它最终要被替换成实际的 `title `值。

```html
<h1 class="entry-title">
	<a href="single.html">{{ post.title }}</a>
</h1>
```

下面这 5 个 `span `标签里分别显示了分类（`category`）、文章发布时间、文章作者、评论数、阅读量。

```html
<div class="entry-meta">
  <span class="post-category"><a href="#">django 博客教程</a></span>
  <span class="post-date"><a href="#"><time class="entry-date"
                                            datetime="2012-11-09T23:15:57+00:00">2017年5月11日</time></a></span>
  <span class="post-author"><a href="#">追梦人物</a></span>
  <span class="comments-link"><a href="#">4 评论</a></span>
  <span class="views-count"><a href="#">588 阅读</a></span>
</div>
```

再次替换掉一些数据，由于评论数和阅读量暂时没法替换，因此先留着，我们在之后实现了这些功能后再来修改它，目前只替换分类、文章发布时间、文章作者：

```html
<div class="entry-meta">
  <span class="post-category"><a href="#">{{ post.category.name }}</a></span>
  <span class="post-date"><a href="#"><time class="entry-date"
                                            datetime="{{ post.created_time }}">{{ post.created_time }}</time></a></span>
  <span class="post-author"><a href="#">{{ post.author }}</a></span>
  <span class="comments-link"><a href="#">4 评论</a></span>
  <span class="views-count"><a href="#">588 阅读</a></span>
</div>
```

这里 `p` 标签里显示的是摘要

```html
<div class="entry-content clearfix">
  <p>免费、中文、零基础，完整的项目，基于最新版 django 1.10 和 Python 3.5。带你从零开始一步步开发属于自己的博客网站，帮助你以最快的速度掌握 django
    开发的技巧...</p>
  <div class="read-more cl-effect-14">
    <a href="#" class="more-link">继续阅读 <span class="meta-nav">→</span></a>
  </div>
</div>
```

替换成 `post` 的摘要：

```html
<div class="entry-content clearfix">
  <p>{{ post.excerpt }}</p>
  <div class="read-more cl-effect-14">
    <a href="#" class="more-link">继续阅读 <span class="meta-nav">→</span></a>
  </div>
</div>
```

再次访问首页，它显示：暂时还没有发布的文章！

![image-20200623170137135](D:%5CLearn%5Cpython%5Cnotes%5Cimage-20200623170137135.png)

数据库中其实还没有任何数据。

---



## 创作后台

---



### 创建admin 后台管理员账户

---

要想进入`django admin` 后台，首先需要创建一个超级管理员账户。我们在` Django 迁移、操作数据库` 中已经创建了一个后台账户。

```python
> pipenv run python manage.py createsuperuser
用户名 (leave blank to use 'fan'): fan
电子邮件地址: 1528023125@qq.com
Password:
Password (again):
Superuser created successfully.
```

---



### 在 admin 后台注册模型

---

要在后台注册我们自己创建的模型，这样 `django admin` 才能知道它们的存在：

```python
blog/admin.py

from django.contrib import admin
from .models import Post, Category, Tag

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
```

运行开发服务器，访问 http://127.0.0.1:8000/admin/ ，就进入了到了django admin 后台登录页面：

![image-20200623170936348](D:%5CLearn%5Cpython%5Cnotes%5Cimage-20200623170936348.png)

![image-20200623171021926](D:%5CLearn%5Cpython%5Cnotes%5Cimage-20200623171021926.png)

可以看到我们刚才注册的三个模型了，点击 `Posts` 后面的**增加**按钮，将进入添加 `Post `的页面，也就是新增博客文章。然后在相关的地方输入一些测试用的内容，增加完后点击保存，这样文章就添加完毕了。

![image-20200623171258235](D:%5CLearn%5Cpython%5Cnotes%5Cimage-20200623171258235.png)

注意每篇文章必须有一个分类，在添加文章时可以选择已有分类。如果数据库中还没有分类，在选择分类时点击 `Category` 后面的 + 按钮新增一个分类即可。

访问 http://127.0.0.1:8000/ 首页，可以看到添加的文章列表了，效果图：

![image-20200623171420889](D:%5CLearn%5Cpython%5Cnotes%5Cimage-20200623171420889.png)

---



### 定制 admin 后台

---

使用 `admin`后台的时候，我们发现了下面的一些体验相关的问题：

- `admin `后台本身的页面元素是已经汉化了的，但是我们自己的 `blog `应用，以及 `Post`、`Category`、`Tag `在页面中显示却是英文的，以及发布文章的时候，表单各字段的 `label `也是英文的。
- 在 `admin` 后台的 `post `列表页面，我们只看到了文章的标题，但是我们希望它显示更加详细的信息，例如作者、发布时间、修改时间等。
- 新增文章时，所有数据都要自己手动填写。但是，有些数据应该是自动生成。例如文章发布时间 `created_time `和修改时间 `modified_time`，应该在创建或者修改文章时自动生成，而不是手动控制。同时我们的博客是单人博客系统，发布者肯定是文章作者，这个也应该自动设定为 `admin `后台的登录账户。

---



#### 汉化 blog 应用

---

首先来看一下需要汉化的地方，`admin `首页每个版块代表一个 `app`，比如 `BLOG `版块表示 blog 应用，版块标题默认显示的就是应用名。应用版块下包含了该应用全部已经注册到 `admin `后台的 `model`，之前我们注册了 `Post`、`Category `和 `Tag`，所以显示的是这三个 `model`，显示的名字就是 `model `的名字。如下图所示：

![img](D:%5CLearn%5Cpython%5Cnotes%5C759200-20190813231722039-757546151.png)

其次是新增 `post `页面的表单，各个字段的 `label `由定义在 `Post `类的 `Field `名转换而来，比如 `Post `模型中定义了 title 字段，则对应表单的 `label `就是 `Title`。

首先是 `BLOG `版块的标题 `BLOG`，一个版块代表一个应用，显然这个标题使用应用名转换而来，在 `blog `应用下有一个 `app.py` 模块，其代码如下：

```python
from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'
```

这些是我们在运行 `startapp `创建 `blog `应用时自动生成的代码，可以看到有一个 `BlogConfig` 类，其继承自 `AppConfig` 类，看名字就知道这是和应用配置有关的类。我们可以通过设置这个类中的一些属性的值来配置这个应用的一些特性的。比如这里的 `name `是用来定义 `app `的名字，需要和应用名保持一致，不要改。要修改 `app `在 `admin `后台的显示名字，添加 `verbose_name `属性。

```python
class BlogConfig(AppConfig):
    name = 'blog'
    verbose_name = '博客'
```

同时，我们此前在 `settings `中注册应用时，是直接注册的 `app `名字 `blog`，现在在 `BlogConfig `类中对 `app `做了一些配置，所以应该将这个类注册进去：

```python
INSTALLED_APPS = [
    'django.contrib.admin',
	...

    'blog.apps.BlogConfig',  # 注册 blog 应用
]
```

再次登录后台，就可以看到 `BLOG `版块的标题已经显示为**博客**了。

接下来是让应用下注册的 `model `显示为中文，既然应用是在` apps.py` 中配置，那么和 `model `有关的配置应该去找相对应的 `model `。配置 `model `的一些特性是通过 `model `的内部类 `Meta` 中来定义。比如对于 `Post `模型，要让他在 `admin `后台显示为中文，如下：

```python
class Post(models.Model):
	...
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
```

同样的可以把 `Tag `和 `Category `也设置一下：

```python
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
```

在 `admin `就可以看到汉化后的效果了。

![image-20200623173129936](D:%5CLearn%5Cpython%5Cnotes%5Cimage-20200623173129936.png)

然后就是修改 `post `的表单的 `label`，`label `由定义在 `model `中的 `Field `名转换二来，所以在 `Field `中修改。

```python
class Post(models.Model):
    title = models.CharField('标题', max_length=70)
    body = models.TextField('正文')
    created_time = models.DateTimeField('创建时间')
    modified_time = models.DateTimeField('修改时间')
    excerpt = models.CharField('摘要', max_length=200, blank=True)
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)
```

---



#### 文章列表显示更加详细的信息

---

在 `admin `后台的文章列表页面，我们只看到了文章的标题，但是我们希望它显示更加详细的信息，这需要我们来定制 `admin `了，在 `admin.py` 添加如下代码：

```python
blog/admin.py

from django.contrib import admin
from .models import Post, Category, Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']

# 把新增的 Postadmin 也注册进来
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
```

刷新 `admin Post `列表页面，可以看到显示的效果好多了。

![image-20200623173935938](D:%5CLearn%5Cpython%5Cnotes%5Cimage-20200623173935938.png)

---



#### 简化新增文章的表单

---

接下来优化新增文章时，填写表单数据的不合理的地方。文章的创建时间和修改时间应该根据当前时间自动生成，而现在是由人工填写，还有就是文章的作者应该自动填充为后台管理员用户，那么这些自动填充数据的字段就不需要在新增文章的表单中出现了。

此前我们在 `blog/admin.py`中定义了一个 `PostAdmin` 来配置 `Post `在 `admin `后台的一些展现形式。`list_display `属性控制 `Post `列表页展示的字段。此外还有一个 `fields `属性，则用来控制表单展现的字段，正好符合我们的需求：

```python
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
    fields = ['title', 'body', 'excerpt', 'category', 'tags']
```

这里 `fields` 中定义的字段就是表单中展现的字段。

填充创建时间，修改时间和文章作者的值。

`Postadmin `继承自 `ModelAdmin`，它有一个 `save_model `方法，这个方法只有一行代码：`obj.save()`。它的作用就是将此 `Modeladmin `关联注册的 `model `实例（这里 `Modeladmin `关联注册的是 `Post`）保存到数据库。这个方法接收四个参数，其中前两个，一个是 `request`，即此次的 `HTTP `请求对象，第二个是 `obj`，即此次创建的关联对象的实例，于是通过复写此方法，就可以将 `request.user` 关联到创建的 `Post `实例上，然后将 `Post `数据再保存到数据库：

```python
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
    fields = ['title', 'body', 'excerpt', 'category', 'tags']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)
```

创建时间和修改时间可以通过 `default `关键字参数指定：

```python
from django.utils import timezone

class Post(models.Model):
	...
    created_time = models.DateTimeField('创建时间', default=timezone.now)
    ...
```

修改时间 代码如下：

```python
from django.utils import timezone

class Post(models.Model):
	...
    
    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        super().save(*args, **kwargs)
```

要注意在指定完 `modified_time `的值后，要调用父类的 `save `以执行数据保存回数据库的逻辑。

---



## 博客文章详情页

---



### 设计文章详情页的 URL

---

在这之前我们的首页视图的`URL`， 在`blog/urls.py`文件里：

```python
blog/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

绑定 `URL `和视图：

```python
blog/urls.py

from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:pk>/', views.detail, name='detail'),
]
```

为了方便地生成上述的 `URL`，我们在 `Post` 类里定义一个 `get_absolute_url` 方法，注意 `Post` 本身是一个 `Python `类，在类中我们是可以定义任何方法的。

```python
blog/models.py

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone

class Post(models.Model):
    ...

    def __str__(self):
        return self.title
    
    # 自定义 get_absolute_url 方法
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
```

---

### 编写 detail 视图函数

---

实现`detail`视图函数：

```python
blog/views.py

from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    # ...

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html', context={'post': post})
```

---



### 编写详情页模板

----

把 `single.html` 拷贝到 `templates\blog `目录下（和 `index.html` 在同一级目录），然后改名为 `detail.html`，测试我们的目录结构为：

```python
blogproject\
    manage.py
    blogproject\
        __init__.py
        settings.py
        ...
    blog/
    	__init__.py
    	models.py
    	,,,
    templates\
    	blog\
    		index.html
    		detail.html
```

在 `index `页面博客文章列表的**标题**和**继续阅读按钮**写上超链接跳转的链接，即文章 `post` 对应的详情页的 `URL`，让用户点击后可以跳转到 `detail `页面：

```html
templates/blog/index.html

<article class="post post-{{ post.pk }}">
  <header class="entry-header">
    <h1 class="entry-title">
      <a href="{{ post.get_absolute_url }}">{{ post.title }}</a>
    </h1>
    ...
  </header>
  <div class="entry-content clearfix">
    ...
    <div class="read-more cl-effect-14">
      <a href="{{ post.get_absolute_url }}" class="more-link">继续阅读 <span class="meta-nav">→</span></a>
    </div>
  </div>
</article>
{% empty %}
  <div class="no-post">暂时还没有发布的文章！</div>
{% endfor %}
```



---

### 模板继承

---

我们看到 `index.html` 文件和 `detail.html `文件除了 `main` 标签包裹的部分不同外，其它地方都是相同的，我们可以把相同的部分抽取出来，放到 `base.html` 里。首先在 `templates\` 目录下新建一个 `base.html` 文件，这时候我们的目录结构：

```python
blogproject\
    manage.py
    blogproject\
        __init__.py
        settings.py
        ...
    blog\
    	__init__.py
    	models.py
    	,,,
    templates\
    	base.html
    	blog\
    		index.html
    		detail.html
```

把 `index.html `的内容全部拷贝到 `base.html` 文件里，然后删掉 `main `标签包裹的内容，替换成如下的内容:

```html
templates/base.html

...
<main class="col-md-8">
	{% block main %}
    {% endblock main %}
</main>
<aside class="col-md-4">
  {% block toc %}
  {% endblock toc %}
  ...
</aside>
...
```

在 index.html 里，我们在文件**最顶部**使用 `{% extends 'base.html' %}` 继承 base.html，这样就把 base.html 里的代码继承了过来，另外在 {% block main %}{% endblock main %} 包裹的地方填上 index 页面应该显示的内容：

```html
templates/blog/index.html

{% extends 'base.html' %}

{% block main %}
	{% for post in post_list %}
        <article class="post post-1">
          ...
        </article>
    {% empty %}
        <div class="no-post">暂时还没有发布的文章！</div>
    {% endfor %}
	<!-- 简单分页效果
    <div class="pagination-simple">
        <a href="#">上一页</a>
        <span class="current">第 6 页 / 共 11 页</span>
        <a href="#">下一页</a>
    </div>
    -->
    <div class="pagination">
      ...
    </div>
{% endblock main %}
```

自动摘取目录

```html
templates/blog/detail.html

{% extends 'base.html' %}

{% block main %}
    <article class="post post-1">
      ...
    </article>
	<section class="comment-area">
      ...
    </section>
{% endblock main %}
{% block toc %}
	<div class="widget widget-content">
        <h3 class="widget-title">文章目录</h3>
        <ul>
            <li>
                <a href="#">教程特点</a>
            </li>
            <li>
                <a href="#">谁适合这个教程</a>
            </li>
            <li>
                <a href="#">在线预览</a>
            </li>
            <li>
                <a href="#">资源列表</a>
            </li>
            <li>
                <a href="#">获取帮助</a>
            </li>
        </ul>
    </div>
{% endblock toc %}
```

修改 article 标签下的一些内容，让其显示文章的实际数据：

```html
<article class="post post-{{ post.pk }}">
  <header class="entry-header">
    <h1 class="entry-title">{{ post.title }}</h1>
    <div class="entry-meta">
      <span class="post-category"><a href="#">{{ post.category.name }}</a></span>
      <span class="post-date"><a href="#"><time class="entry-date"
                                                datetime="{{ post.created_time }}">{{ post.created_time }}</time></a></span>
      <span class="post-author"><a href="#">{{ post.author }}</a></span>
      <span class="comments-link"><a href="#">4 评论</a></span>
      <span class="views-count"><a href="#">588 阅读</a></span>
    </div>
  </header>
  <div class="entry-content clearfix">
    {{ post.body }}
  </div>
</article>
```

再次从首页点击一篇文章的标题或者继续阅读按钮跳转到详情页面，可以看到预期效果了！

![image-20200624194547703](D:%5CLearn%5Cpython%5Cnotes%5Cimage-20200624194547703.png)

---



## 让博客支持MarkDown语法和代码高亮

---

### 安装Python MarkDown

---

命令：`pipenv install markdown`

```python
Installing markdown…
Adding markdown to Pipfile's [packages]…
Installation Succeeded
Pipfile.lock not found, creating…
Locking [dev-packages] dependencies…
Locking [packages] dependencies…
           Building requirements...
Resolving dependencies...
Success!
Updated Pipfile.lock (3afd2d)!
Installing dependencies from Pipfile.lock (3afd2d)…
  ================================ 0/0 - 00:00:00
```

---

### 在detail视图中使用markdown

---

将 Markdown 格式的文本解析成 HTML 文本非常简单，只需调用这个库的 `markdown` 方法。我们书写的博客文章内容存在 `Post` 的 `body` 属性里，回到我们的详情页视图函数，对 `post` 的 `body` 的值做一下解析，把 Markdown 文本转为 HTML 文本再传递给模板：

```python
blog/views.py

import markdown
from django.shortcuts import get_object_or_404, render

from .models import Post

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request, 'blog/detail.html', context={'post': post})
```

 toc 允许自动生成目录。

```markdown
# 一级标题

## 二级标题

### 三级标题

- 列表项1
- 列表项2
- 列表项3

> 这是一段引用

​```python
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request, 'blog/detail.html', context={'post': post})
```

---

### safe 标签

---

我们在发布的文章详情页没有看到预期的效果，而是类似于一堆乱码一样的 HTML 标签，这些标签本应该在浏览器显示它自身的格式，但是 django 出于安全方面的考虑，任何的 HTML 代码在 django 的模板中都会被转义（即显示原始的 HTML 代码，而不是经浏览器渲染后的格式）。为了解除转义，只需在模板变量后使用 `safe` 过滤器即可，告诉 django，这段文本是安全的，你什么也不用做。在模板中找到展示博客文章内容的 `{{ post.body }}` 部分，为其加上 safe 过滤器：`{{ post.body|safe }}`，大功告成，这下看到预期效果了。	

![image-20200624201044813](D:%5CLearn%5Cpython%5Cnotes%5Cimage-20200624201044813.png)

---

### 代码高亮

---

首先在 base.html 的 head 标签里引入代码高亮的样式，有多种样式供你选择，这里我们选择 GitHub 主题的样式。样式文件直接通过 CDN 引入，同时在 style 标签里自定义了一点元素样式，使得代码块的显示效果更加完美。

```html
<head>
  ...
  <link href="https://cdn.bootcss.com/highlight.js/9.15.8/styles/github.min.css" rel="stylesheet">

  <style>
    .codehilite {
      padding: 0;
    }

    /* for block of numbers */
    .hljs-ln-numbers {
      -webkit-touch-callout: none;
      -webkit-user-select: none;
      -khtml-user-select: none;
      -moz-user-select: none;
      -ms-user-select: none;
      user-select: none;

      text-align: center;
      color: #ccc;
      border-right: 1px solid #CCC;
      vertical-align: top;
      padding-right: 5px;
    }

    .hljs-ln-n {
      width: 30px;
    }

    /* for block of code */
    .hljs-ln .hljs-ln-code {
      padding-left: 10px;
      white-space: pre;
    }
  </style>
</head>
```

然后是引入 js 文件，因为应该等整个页面加载完，插件再去解析代码块，所以把 js 文件的引入放在 body 底部：

```html
<body>
  <script src="https://cdn.bootcss.com/highlight.js/9.15.8/highlight.min.js"></script>
  <script src="https://cdn.bootcss.com/highlightjs-line-numbers.js/2.7.0/highlightjs-line-numbers.min.js"></script>
  <script>
    hljs.initHighlightingOnLoad();
    hljs.initLineNumbersOnLoad();
  </script>
</body>
```



---

## Markdown 文章自动生成目录，提升阅读体验

---

### 在文中插入目录

---

在渲染 Markdown 文本时加入了 toc 拓展后，就可以在文中插入目录了。方法是在书写 Markdown 文本时，在你想生成目录的地方插入 `[TOC]` 标记即可。例如新写一篇 Markdown 博文，其 Markdown 文本内容如下：

```markdown
[TOC]

## 我是标题一

这是标题一下的正文

## 我是标题二

这是标题二下的正文

### 我是标题二下的子标题
这是标题二下的子标题的正文

## 我是标题三
这是标题三下的正文
```

![image-20200624201912676](D:%5CLearn%5Cpython%5Cnotes%5Cimage-20200624201912676.png)

原本 `[TOC]` 标记的地方被内容的目录替换了。

---

### 在页面的任何地方插入目录

---

上述方式的一个局限性就是只能通过 `[TOC]` 标记在文章内容中插入目录。如果我想在页面的其它地方，比如侧边栏插入一个目录该怎么做呢？方法其实也很简单，只需要稍微改动一下解析 Markdown 文本内容的方式即可，具体代码就像这样：

```python
blog/views.py

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    post.body = md.convert(post.body)
		post.toc = md.toc

    return render(request, 'blog/detail.html', context={'post': post})
```

接下来就在博客文章详情页的文章目录侧边栏渲染文章的目录。删掉占位用的目录内容，替换成如下代码：

```python
{% block toc %}
    <div class="widget widget-content">
        <h3 class="widget-title">文章目录</h3>
        {{ post.toc|safe }}
    </div>
{% endblock toc %}
```

即使用模板变量标签 {{ post.toc }} 显示模板变量的值，注意 post.toc 实际是一段 HTML 代码，我们知道 django 会对模板中的 HTML 代码进行转义，所以要使用 safe 标签防止 django 对其转义。其最终渲染后的效果就是：

![image-20200624202747202](D:%5CLearn%5Cpython%5Cnotes%5Cimage-20200624202747202.png)

---

### 处理空目录

---

现在目录已经可以完美生成了，不过还有一个异常情况，当文章没有任何标题元素时，Markdown 就提取不出目录结构，post.toc 就是一个空的 div 标签，如下：

```python
<div class="toc">...............................
  <ul></ul>
</div>
```

对于这种没有目录结构的文章，在侧边栏显示一个目录是没有意义的，所以我们希望只有在文章存在目录结构时，才显示侧边栏的目录。那么应该怎么做呢？

分析 toc 的内容，如果有目录结构，ul 标签中就有值，否则就没有值。我们可以使用正则表达式来测试 ul 标签中是否包裹有元素来确定是否存在目录。

```python
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    post.body = md.convert(post.body)
    
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''
    
    return render(request, 'blog/detail.html', context={'post': post})
```

这里我们正则表达式去匹配生成的目录中包裹在 ul 标签中的内容，如果不为空，说明目录，就把 ul 标签中的值提取出来（目的是只要包含目录内容的最核心部分，多余的 HTML 标签结构丢掉）赋值给 `post.toc`；否则，将 post 的 toc 置为空字符串，然后我们就可以在模板中通过判断 post.toc 是否为空，来决定是否显示侧栏目录：

```python
{% block toc %}
  {% if post.toc %}
    <div class="widget widget-content">
      <h3 class="widget-title">文章目录</h3>
      <div class="toc">
        <ul>
          {{ post.toc|safe }}
        </ul>
      </div>
    </div>
  {% endif %}
{% endblock toc %}
```

这里我们看到了一个新的模板标签 `{% if %}`，这个标签用来做条件判断，和 Python 中的 if 条件判断是类似的。

---

### 美化标题的锚点 URL

---

文章内容的标题被设置了锚点，点击目录中的某个标题，页面就会跳到该文章内容中标题所在的位置，这时候浏览器的 URL 显示的值可能不太美观，比如像下面的样子：

> http://127.0.0.1:8000/posts/8/#_1
>
> http://127.0.0.1:8000/posts/8/#_3

`#_1` 就是锚点，Markdown 在设置锚点时利用的是标题的值，由于通常我们的标题都是中文，Markdown 没法处理，所以它就忽略的标题的值，而是简单地在后面加了个 _1 这样的锚点值。为了解决这一个问题，需要修改一下传给 `extentions` 的参数，其具体做法如下：

```python
blog/views.py

from django.utils.text import slugify
from markdown.extensions.toc import TocExtension

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        # 记得在顶部引入 TocExtension 和 slugify
        TocExtension(slugify=slugify),
    ])
    post.body = md.convert(post.body)
    
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''
    
    return render(request, 'blog/detail.html', context={'post': post})
```

这时候标题的锚点 URL 变得好看多了。

> http://127.0.0.1:8000/posts/8/#我是标题一
>
> http://127.0.0.1:8000/posts/8/#我是标题二下的子标题

---



## 自动生成文章摘要

---

博客文章的模型有一个 `excerpt` 字段，这个字段用于存储文章的摘要。目前为止，还只能在 django admin 后台手动为文章输入摘要。每次手动输入摘要比较麻烦，对有些文章来说，只要摘取正文的前 N 个字符作为摘要，以便提供文章预览就可以了。因此我们来实现如果文章没有输入摘要，则自动摘取正文的前 N 个字符作为摘要，这有两种实现方法。

---

### 覆写save方法

---

第一种方法是通过覆写模型的 `save` 方法，从正文字段摘取前 N 个字符保存到摘要字段。

我们之前的博客文章模型代码：

```python
blog/models.py

class Post(models.Model):
    # 其它字段...
    body = models.TextField()
    excerpt = models.CharField(max_length=200, blank=True)
    
    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        super().save(*args, **kwargs)
```

其中 `body` 字段存储的是正文，`excerpt` 字段用于存储摘要。通过覆写模型的 save 方法，在数据被保存到数据库前，先从 `body` 字段摘取 N 个字符保存到 `excerpt` 字段中，从而实现自动摘要的目的。具体代码如下：

```python
blog/models.py

import markdown
from django.utils.html import strip_tags

class Post(models.Model):
    # 其它字段...
    body = models.TextField()
    excerpt = models.CharField(max_length=200, blank=True)
    
    # 其它方法...
    
    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()

        # 首先实例化一个 Markdown 类，用于渲染 body 的文本。
        # 由于摘要并不需要生成文章目录，所以去掉了目录拓展。
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])

        # 先将 Markdown 文本渲染成 HTML 文本
        # strip_tags 去掉 HTML 文本的全部 HTML 标签
        # 从文本摘取前 54 个字符赋给 excerpt
        self.excerpt = strip_tags(md.convert(self.body))[:54]

        super().save(*args, **kwargs)
```

然后在模板中适当的地方使用模板标签引用 `{{ post.excerpt }}` 显示摘要的值即可：

```html
templates/blog/index.html

<article class="post post-{{ post.pk }}">
  ...
  <div class="entry-content clearfix">
      <p>{{ post.excerpt }}...</p>
      <div class="read-more cl-effect-14">
          <a href="{{ post.get_absolute_url }}" class="more-link">继续阅读 <span class="meta-nav">→</span></a>
      </div>
  </div>
</article>
```

新添加一篇文章（这样才能触发 save 方法，此前添加的文章不会自动生成摘要，要手动保存一下触发 save 方法），可以看到摘要效果了。

---

### 使用 truncatechars 模板过滤器

---

第二种方法是使用 `truncatechars` 模板过滤器（Filter）。在 django 的模板系统中，模板过滤器的使用语法为 `{{ var | filter: arg }}`。可以将模板过滤看做一个函数，它会作用于被它过滤的模板变量，从而改变模板变量的值。例如这里的 `truncatechars` 过滤器可以截取模板变量值的前 N 个字符显示。关于模板过滤器，我们之前使用过 `safe` 过滤器，可以参考 [让博客支持 Markdown 语法和代码高亮](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/67/) 这篇文章中对模板过滤器的说明。

例如摘要效果，需要显示 `post.body` 的前 54 的字符，那么可以在模板中使用 `{{ post.body | truncatechars:54 }}`。

```html
templates/blog/index.html

<article class="post post-{{ post.pk }}">
  ...
  <div class="entry-content clearfix">
      <p>{{ post.body|truncatechars:54 }}</p>
      <div class="read-more cl-effect-14">
          <a href="{{ post.get_absolute_url }}" class="more-link">继续阅读 <span class="meta-nav">→</span></a>
      </div>
  </div>
</article>
```

不过这种方法的一个缺点就是如果前 54 个字符含有块级 HTML 元素标签的话（比如一段代码块），会使摘要比较难看。所以推荐使用第一种方法。

----



## 博客侧边栏

---

我们的博客侧边栏有四项内容：最新文章、归档、分类和标签云。

---



### 使用模板标签的解决思路

----

### 模板标签目录结构

---

首先在我们的 **blog 应用**下创建一个 templatetags 文件夹。然后在这个文件夹下创建一个 __init__.py 文件，使这个文件夹成为一个 Python 包，之后在 templatetags\ 目录下创建一个 blog_extras.py 文件，这个文件存放自定义的模板标签代码。

此时你的目录结构应该是这样的：

```
blog\
    __init__.py
    admin.py
    apps.py
    migrations\
        __init__.py
    models.py
    static\
    templatetags\
    	__init__.py
    	blog_extras.py
    tests.py
    views.py
```

---

### 编写模板标签代码

---

接下来就是编写各个模板标签的代码了，自定义模板标签代码写在 blog_extras.py 文件中。其实模板标签本质上就是一个 Python 函数，因此按照 Python 函数的思路来编写模板标签的代码就可以了，并没有任何新奇的东西或者需要新学习的知识在里面。

---

#### 最新文章模板标签

---

打开 blog_extras.py 文件，开始写我们的最新文章模板标签。

```python
from django import template

from ..models import Post, Category, Tag

register = template.Library()


@register.inclusion_tag('blog/inclusions/_recent_posts.html', takes_context=True)
def show_recent_posts(context, num=5):
    return {
        'recent_post_list': Post.objects.all().order_by('-created_time')[:num],
    }
```

接下来就是定义模板 _recent_posts.html 的内容。在 templates\blogs 目录下创建一个 inclusions 文件夹，然后创建一个 _recent_posts.html 文件，内容如下：

```html
<div class="widget widget-recent-posts">
  <h3 class="widget-title">最新文章</h3>
  <ul>
    {% for post in recent_post_list %}
      <li>
        <a href="{{ post.get_absolute_url }}">{{ post.title }}</a>
      </li>
    {% empty %}
      暂无文章！
    {% endfor %}
  </ul>
</div>
```

很简单，循环由 `show_recent_posts` 传递的模板变量 `recent_post_list` 即可，和 index.html 中循环显示文章列表是一样的。

---

### 归档模板标签

---

和最新文章模板标签一样，先写好函数，然后将函数注册为模板标签即可。

```python
@register.inclusion_tag('blog/inclusions/_archives.html', takes_context=True)
def show_archives(context):
    return {
        'date_list': Post.objects.dates('created_time', 'month', order='DESC'),
    }
```

然后是渲染的模板 _archives.html 的内容：

```html
<div class="widget widget-archives">
  <h3 class="widget-title">归档</h3>
  <ul>
    {% for date in date_list %}
      <li>
        <a href="#">{{ date.year }} 年 {{ date.month }} 月</a>
      </li>
    {% empty %}
      暂无归档！
    {% endfor %}
  </ul>
</div>
```

由于 `date_list` 中的每个元素都是 Python 的 `date` 对象，所以可以引用 `year` 和 `month` 属性来获取年份和月份。

---

### 分类模板标签

---

过程还是一样，先写好函数，然后将函数注册为模板标签。注意分类模板标签函数中使用到了 `Category` 类，其定义在 blog.models.py 文件中，使用前记得先导入它，否则会报错。

```python
@register.inclusion_tag('blog/inclusions/_categories.html', takes_context=True)
def show_categories(context):
    return {
        'category_list': Category.objects.all(),
    }
```

_categories.html 的内容：

```html
<div class="widget widget-category">
  <h3 class="widget-title">分类</h3>
  <ul>
    {% for category in category_list %}
      <li>
        <a href="#">{{ category.name }} <span class="post-count">(13)</span></a>
      </li>
    {% empty %}
      暂无分类！
    {% endfor %}
  </ul>
</div>
```

`<span class="post-count">(13)</span>` 显示的是该分类下的文章数目，这个特性会在接下来的教程中讲解如何实现，目前暂时用占位数据代替吧。

---



#### 标签云模板标签

---

标签和分类其实是很类似的，模板标签：

```python
@register.inclusion_tag('blog/inclusions/_tags.html', takes_context=True)
def show_tags(context):
    return {
        'tag_list': Tag.objects.all(),
    }
```

_tags.html：

```html
<div class="widget widget-tag-cloud">
  <h3 class="widget-title">标签云</h3>
  <ul>
    {% for tag in tag_list %}
      <li>
        <a href="#">{{ tag.name }}</a>
      </li>
    {% empty %}
      暂无标签！
    {% endfor %}
  </ul>
</div>
```

---



### 使用自定义的模板标签

---

打开 base.html，为了使用刚才定义的模板标签，我们首先需要在模板中导入存放这些模板标签的模块，这里是 blog_extras.py 模块。当时我们为了使用 static 模板标签时曾经导入过 `{% load static %}`，这次在 `{% load static %}` 下再导入 blog_extras：

```html
templates/base.html

{% load static %}
{% load blog_extras %}
<!DOCTYPE html>
<html>
...
</html>
```

然后找到侧边栏各项，将他们都替换成对应的模板标签：

```html
templates/base.html

<aside class="col-md-4">
  {% block toc %}
  {% endblock toc %}

  {% show_recent_posts %}
  {% show_archives %}
  {% show_categories %}
  {% show_tags %}

  <div class="rss">
     <a href=""><span class="ion-social-rss-outline"></span> RSS 订阅</a>
  </div>
</aside>
```



现在运行开发服务器，可以看到侧边栏显示的数据已经不再是之前的占位数据，而是我们保存在数据库中的数据了。

---



## 分类、归档和标签页

---

侧边栏已经正确地显示了最新文章列表、归档、分类、标签等信息。现在来完善归档、分类和标签功能，当用户点击归档下的某个日期、分类栏目下的某个分类或者标签栏目下的某个标签时，跳转到文章列表页面，显示该日期、分类或者标签下的全部文章。

---



### 归档页面

---

要显示某个归档日期下的文章列表，思路和显示主页文章列表是一样的，主页视图的代码：

```python
blog/views.py

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
```

主页视图函数中通过 `Post.objects.all()` 获取全部文章，而在归档和分类视图中，我们不再使用 `all` 方法获取全部文章，而是使用 `filter` 来根据条件过滤。

归档视图：

```python
blog/views.py

def archive(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
```

写好视图函数后就是配置好 URL：

```python
blog/urls.py

from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:pk>/', views.detail, name='detail'),
    path('archives/<int:year>/<int:month>/', views.archive, name='archive'),
]
```

接下来在 inclusions 文件夹下找到 archives 的模板，修改超链接的 `href` 属性，让用户点击超链接后跳转到文章归档页面：

```html
inclusions/_archives.html

...
{% for date in date_list %}
<li>
  <a href="{% url 'blog:archive' date.year date.month %}">
    {{ date.year }} 年 {{ date.month }} 月
  </a>
</li>
{% endfor %}
...
```

测试一下，点击侧边栏归档的日期，跳转到归档页面，发现显示的就是归档下的文章列表。

---



### 分类页面

---

同样的写好分类页面的视图函数：

```python
blog/views.py

import markdown

from django.shortcuts import render, get_object_or_404

# 引入 Category 类
from .models import Post, Category

def category(request, pk):
    # 记得在开始部分导入 Category 类
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
```

URL 配置如下：

```python
blog/urls.py

urlpatterns = [
    path('archives/<int:year>/<int:month>/', views.archive, name='archive'),
    path('categories/<int:pk>/', views.category, name='category'),
]
```

这个分类页面对应的 URL 模式和文章详情页面对应的 URL 模式十分类似，你可以自己分析分析它是如何工作的，在此就不赘述了。

修改相应模板：

```html
inclusions/_categories.html

...
{% for category in category_list %}
<li>
  <a href="{% url 'blog:category' category.pk %}">{{ category.name }}</a>
</li>
{% endfor %}
...
```

同样，{% url %} 模板标签的用法和写归档页面时的用法是一样的。现在尝试点击相应的链接，就可以跳转到归档或者分类页面了。

---

#### 标签页面

---

标签页和分类是完全一样的步骤，因此稍微修改一下分类相关的代码就可以用于标签了。

```python
blog/views.py

from .models import Category, Post, Tag

def tag(request, pk):
    # 记得在开始部分导入 Tag 类
    t = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tags=t).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
```

可以看到和 `category` 几乎一样，只是这里根据 tag 来筛选文章。

然后是配置 url：

```python
from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    ...
    path('categories/<int:pk>/', views.category, name='category'),
    path('tags/<int:pk>/', views.tag, name='tag'),
]
```

再修改一下 inclusions\_tags.html 模板中的跳转链接：

```html
...
{% for tag in tag_list %}
  <li>
    <a href="{% url 'blog:tag' tag.pk %}">{{ tag.name }}</a>
  </li>
{% empty %}
    暂无标签！
{% endfor %}
...
```

侧边栏的功能这里差不多就都做完了。

---



## 评论功能

---

### 创建评论应用

---

首先**进入到项目根目录**，然后输入如下命令创建一个新的应用：

```python
> pipenv run python manage.py startapp comments
```

在 settings.py 里注册这个应用，django 才知道这是一个应用。

```python
blogproject/settings.py 
... 
INSTALLED_APPS = [    
    ...    'blog.apps.BlogConfig',  # 注册 blog 应用    
    'comments.apps.CommentsConfig',  # 注册 comments 应用 
] 
...
```

让 blog 应用在 django 的 admin 后台显示中文名字。这里也对评论应用做类似的配置：

```python
comments/app.py

from django.apps import AppConfig


class CommentsConfig(AppConfig):
    name = 'comments'
    verbose_name = '评论'
```

---

### 设计评论的数据库模型

---

评论模型的代码写在 comments\models.py 里：

```python
comments/models.py

from django.db import models
from django.utils import timezone


class Comment(models.Model):
    name = models.CharField('名字', max_length=50)
    email = models.EmailField('邮箱')
    url = models.URLField('网址', blank=True)
    text = models.TextField('内容')
    created_time = models.DateTimeField('创建时间', default=timezone.now)
    post = models.ForeignKey('blog.Post', verbose_name='文章', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}: {}'.format(self.name, self.text[:20])
```

创建了数据库模型就要迁移数据库，在**项目根目录**下分别运行下面两条命令：

```shell
> pipenv run python manage.py makemigrations
> pipenv run python manage.py migrate
```

---

### 注册评论模型到 admin

---

```python
comments/admin.py

from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'url', 'post', 'created_time']
    fields = ['name', 'email', 'url', 'text', 'post']


admin.site.register(Comment, CommentAdmin)
```

---

### 设计评论表单

---

在 comments\ 目录下（和 models.py 同级）新建一个 forms.py 文件，用来存放表单代码，我们的表单代码如下：

```python
comments/forms.py

from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']
```

---

### 展示评论表单

---

和 blog 应用中定义模板标签的老套路一样，首先建立评论应用模板标签的文件结构，在 comments\ 文件夹下新建一个 templatetags 文件夹，然后创建 __init__.py 文件使其成为一个包，再创建一个 comments_extras.py 文件用于存放模板标签的代码，文件结构如下：

```python
...
blog\
comments\
	templatetags\
		__init__.py
		comments_extras.py
...
```

然后定义一个 `inclusion_tag` 类型的模板标签，用于渲染评论表单，

```python
from django import template
from ..forms import CommentForm

register = template.Library()


@register.inclusion_tag('comments/inclusions/_form.html', takes_context=True)
def show_comment_form(context, post, form=None):
    if form is None:
        form = CommentForm()
    return {
        'form': form,
        'post': post,
    }
```

然后在 templates/comments/inclusions 目录下（没有就新建）新建一个 _form.html 模板，写上代码：

```html
<form action="{% url 'comments:comment' post.pk %}" method="post" class="comment-form">
  {% csrf_token %}
  <div class="row">
    <div class="col-md-4">
      <label for="{{ form.name.id_for_label }}">{{ form.name.label }}：</label>
      {{ form.name }}
      {{ form.name.errors }}
    </div>
    <div class="col-md-4">
      <label for="{{ form.email.id_for_label }}">{{ form.email.label }}：</label>
      {{ form.email }}
      {{ form.email.errors }}
    </div>
    <div class="col-md-4">
      <label for="{{ form.url.id_for_label }}">{{ form.url.label }}：</label>
      {{ form.url }}
      {{ form.url.errors }}
    </div>
    <div class="col-md-12">
      <label for="{{ form.text.id_for_label }}">{{ form.text.label }}：</label>
      {{ form.text }}
      {{ form.text.errors }}
      <button type="submit" class="comment-btn">发表</button>
    </div>
  </div>    <!-- row -->
</form>
```

然后我们就可以在 detail.html 中使用这个模板标签来渲染表单了，注意在使用前记得先 `{% load comment_extras %}` 这个模块。

```html
{% extends 'base.html' %}
{% load comment_extras %}
...

<h3>发表评论</h3>
{% show_comment_form post %}
```

---

### 评论视图函数

---

当用户提交表单中的数据后，django 需要调用相应的视图函数来处理这些数据，下面开始写我们视图函数处理逻辑：

```python
from blog.models import Post
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import CommentForm


@require_POST
def comment(request, post_pk):
    # 先获取被评论的文章，因为后面需要把评论和被评论的文章关联起来。
    # 这里我们使用了 django 提供的一个快捷函数 get_object_or_404，
    # 这个函数的作用是当获取的文章（Post）存在时，则获取；否则返回 404 页面给用户。
    post = get_object_or_404(Post, pk=post_pk)

    # django 将用户提交的数据封装在 request.POST 中，这是一个类字典对象。
    # 我们利用这些数据构造了 CommentForm 的实例，这样就生成了一个绑定了用户提交数据的表单。
    form = CommentForm(request.POST)

    # 当调用 form.is_valid() 方法时，django 自动帮我们检查表单的数据是否符合格式要求。
    if form.is_valid():
        # 检查到数据是合法的，调用表单的 save 方法保存数据到数据库，
        # commit=False 的作用是仅仅利用表单的数据生成 Comment 模型类的实例，但还不保存评论数据到数据库。
        comment = form.save(commit=False)

        # 将评论和被评论的文章关联起来。
        comment.post = post

        # 最终将评论数据保存进数据库，调用模型实例的 save 方法
        comment.save()

        # 重定向到 post 的详情页，实际上当 redirect 函数接收一个模型的实例时，它会调用这个模型实例的 get_absolute_url 方法，
        # 然后重定向到 get_absolute_url 方法返回的 URL。
        return redirect(post)

    # 检查到数据不合法，我们渲染一个预览页面，用于展示表单的错误。
    # 注意这里被评论的文章 post 也传给了模板，因为我们需要根据 post 来生成表单的提交地址。
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'comments/preview.html', context=context)
```

如果用户提交的数据合法，我们就将评论数据保存到数据库，否则说明用户提交的表单包含错误，我们将渲染一个 preview.html 页面，来展示表单中的错误，以便用户修改后重新提交。preview.html 的代码如下：

```html
{% extends 'base.html' %}
{% load comment_extras %}

{% block main %}
  {% show_comment_form post form %}
{% endblock main %}
```

---

### 绑定URL

---

视图函数需要和 URL 绑定，这里我们在 comment 应用中再建一个 urls.py 文件，写上 URL 模式：

```python
from django.urls import path

from . import views

app_name = 'comments'
urlpatterns = [
    path('comment/<int:post_pk>', views.comment, name='comment'),
]
```

别忘了给这个评论的 URL 模式规定命名空间，即 `app_name = 'comments'`。

最后要在项目的 blogproject\ 目录的 urls.py 里包含 comments\urls.py 这个文件：

```python
blogproject/urls.py

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    url(r'', include('comments.urls')),
]
```

---

### 发送评论消息

---

django 默认已经为我们做好了 messages 的相关配置，直接用即可。

两个地方需要发送消息，第一个是当评论成功，即评论数据成功保存到数据库后，因此在 comment 视图中加一句。

```python
from django.contrib import messages

if form.is_valid():
    ...
    # 最终将评论数据保存进数据库，调用模型实例的 save 方法
    comment.save()

    messages.add_message(request, messages.SUCCESS, '评论发表成功！', extra_tags='success')
    return redirect(post)
```

同样的，如果评论失败了，也发送一条消息：

```python
# 检查到数据不合法，我们渲染一个预览页面，用于展示表单的错误。
# 注意这里被评论的文章 post 也传给了模板，因为我们需要根据 post 来生成表单的提交地址。
context = {
    'post': post,
    'form': form,
}
messages.add_message(request, messages.ERROR, '评论发表失败！请修改表单中的错误后重新提交。', extra_tags='danger')
```

发送的消息被缓存在 cookie 中，然后我们在模板中获取显示即可。显示消息比较好的地方是在导航条的下面，我们在模板 base.html 的导航条代码下增加如下代码：

```html
<header>
  ...
</header>
{% if messages %}
    {% for message in messages %}
      <div class="alert alert-{{ message.tags }} alert-dismissible" role="alert">
        <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span
                aria-hidden="true">&times;</span></button>
        {{ message }}
      </div>
    {% endfor %}
{% endif %}
```

评论发布成功和失败的消息效果如下图：

![img](D:%5CLearn%5Cpython%5Cnotes%5C759200-20190908152131823-697789163.png)

![img](D:%5CLearn%5Cpython%5Cnotes%5C759200-20190908152416979-212563362.png)

---

### 显示评论内容

---

为了不改动已有的视图函数的代码，评论数据我们也使用自定义的模板标签来实现。模板标签代码如下：

```python
@register.inclusion_tag('comments/inclusions/_list.html', takes_context=True)
def show_comments(context, post):
    comment_list = post.comment_set.all().order_by('-created_time')
    comment_count = comment_list.count()
    return {
        'comment_count': comment_count,
        'comment_list': comment_list,
    }
```

模板 _list.html 代码如下：

```html
<h3>评论列表，共 <span>{{ comment_count }}</span> 条评论</h3>
<ul class="comment-list list-unstyled">
  {% for comment in comment_list %}
    <li class="comment-item">
      <span class="nickname">{{ comment.name }}</span>
      <time class="submit-date" datetime="{{ comment.created_time }}">{{ comment.created_time }}</time>
      <div class="text">
        {{ comment.text|linebreaks }}
      </div>
    </li>
  {% empty %}
    暂无评论
  {% endfor %}
</ul>
```

然后将 detail.html 中此前占位用的评论模板替换为模板标签渲染的内容：

```html
<h3>发表评论</h3>
{% show_comment_form post %}
<div class="comment-list-panel">
    {% show_comments post %}
</div>
```

访问文章详情页，可以看到已经发表的评论列表了：

![image-20200625152448197](D:%5CLearn%5Cpython%5Cnotes%5Cimage-20200625152448197.png)