import argparse


def createParser():
    root_parser = argparse.ArgumentParser(
        prog='utility',
        description='''Simple swagger program''',
        epilog='''(c) CoolCoderCarl'''
    )
    requests_parser = root_parser.add_subparsers(dest='request')

    get_parser = requests_parser.add_parser('get', help='The request’s query parameters')
    get_parser.add_argument('--header', dest='header', help='The request’s headers', action='store_true', default=False)
    get_parser.add_argument('--ip', dest='ip', help='The Requester’s IP Address', action='store_true', default=False)
    get_parser.add_argument('--useragent', dest='useragent', help='The request’s User-Agent header', action='store_true' ,default=False)


    post_parser = requests_parser.add_parser('post', help='The request’s POST parameters')
    post_parser.add_argument('--header', dest='header', help='Response headers')



    put_parser = requests_parser.add_parser('put', help='The request’s PUT parameters')
    put_parser.add_argument('--put')



    delete_parser = requests_parser.add_parser('delete', help='The request’s DELETE parameters')
    delete_parser.add_argument('--delete')


    return root_parser