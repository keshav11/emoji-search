import emoji
import sys

if __name__ == '__main__':
    search_key = sys.argv[1]
    results = {key: emoji.EMOJI_UNICODE[key] for key in emoji.EMOJI_UNICODE.keys()
               if search_key.lower() in key.lower()}
    for key, val in results.items():
        print(key + "  " + val)



