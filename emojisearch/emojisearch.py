import emoji
import sys
import getopt


def print_usage():
    """print usage of the utility"""
    print('emojisearch -[swh] search_keyword')


def main():
    # parse and validate options and argument
    try:
        options, arguments = getopt.getopt(sys.argv[1:], "swh")
    except getopt.GetoptError as exp:
        print(exp)
        print_usage()
        sys.exit(-2)

    starts_with = False
    whole_word = False
    help = False

    for opt, ars in options:
        if opt == '-s':
            starts_with = True
        if opt == '-w':
            whole_word = True
        if opt == '-h':
            help = True

    if help:
        print_usage()
        sys.exit(0)


    if len(arguments) == 0:
        print('search keyword not provided')
        print_usage()
        sys.exit(-2)

    search_key = arguments[0]
    # search for emoji
    if whole_word:
        results = {key: emoji.EMOJI_UNICODE[key] for key in emoji.EMOJI_UNICODE.keys() if
                   ":"+search_key.lower()+":" == key.lower()}
    elif starts_with:
        results = {key: emoji.EMOJI_UNICODE[key] for key in emoji.EMOJI_UNICODE.keys() if
                   key.lower().startswith(':' + search_key)}
    else:
        results = {key: emoji.EMOJI_UNICODE[key] for key in emoji.EMOJI_UNICODE.keys() if
                   search_key.lower() in key.lower()}

    # print out results
    for key, val in results.items():
        print(key + "  " + val)


if __name__ == '__main__':
    main()
