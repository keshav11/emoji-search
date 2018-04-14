# emoji-search
search emojis using command line

## install
### using pip
```
first clone the repository
$ cd emojisearch
$ pip install .
```

## Usage
#### show results where keyword exits anywhere in the emoji name
```
$ emojisearch grinning_cat_face

:grinning_cat_face:  😺
:grinning_cat_face_with_smiling_eyes:  😸
```
#### show results only if whole emoji name mathces with keyword
```
$ emojisearch -w grinning_cat_face

:grinning_cat_face:  😺
```

#### show results only if emoji name starts with search keyword
```
$ emojisearch -s cat

:cat:  🐈
:cat_face:  🐱
:cat_face_with_tears_of_joy:  😹
:cat_face_with_wry_smile:  😼
```
