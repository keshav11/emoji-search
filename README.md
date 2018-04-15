# emoji-search

[![PyPI](https://img.shields.io/pypi/v/emojisearch.svg)](https://pypi.python.org/pypi/emojisearch)

search emojis using command line

## Install
### using pip

```
pip install emojisearch
```
### using source

```
$ git clone https://github.com/keshav11/emoji-search.git
$ cd emojisearch
$ pip install .
```

## Usage

### show results where keyword exits anywhere in the emoji name

```
$ emojisearch grinning_cat_face
:grinning_cat_face:  😺
:grinning_cat_face_with_smiling_eyes:  😸
```
### show results only if whole emoji name matches with keyword

```
$ emojisearch -w grinning_cat_face
:grinning_cat_face:  😺
```

### show results only if emoji name starts with search keyword

```
$ emojisearch -s cat
:cat:  🐈
:cat_face:  🐱
:cat_face_with_tears_of_joy:  😹
:cat_face_with_wry_smile:  😼
```
