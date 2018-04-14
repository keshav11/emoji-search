# emoji-search
search emojis using command line

## Usage
### show results where keyword exits anywhere in the emoji name
```
$ python emoji_search.py grinning_cat_face

:grinning_cat_face:  😺
:grinning_cat_face_with_smiling_eyes:  😸
```
### show results only if whole emoji name mathces with keyword
```
$ python emoji_search.py -w grinning_cat_face

:grinning_cat_face:  😺
```

### search and show results ony if full emoji name starts with search keyword
```
$ python emoji_search.py -s cat

:cat:  🐈
:cat_face:  🐱
:cat_face_with_tears_of_joy:  😹
:cat_face_with_wry_smile:  😼
```
