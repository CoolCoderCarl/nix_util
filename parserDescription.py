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
    post_parser.add_argument('--delay', dest='delay', help='A delayed response. 10 sec max')



    put_parser = requests_parser.add_parser('put', help='The request’s PUT parameters')
    put_parser.add_argument('--status', dest='status', help='''100 Informational responses\n
                                                               200 Success\n
                                                               300 Redirection\n
                                                               400 Client Errors\n
                                                               500 Server Errors\n''')
    put_parser.add_argument('--anything', dest='anything', help='Anything passed in request', action='store_true' ,default=False)



    delete_parser = requests_parser.add_parser('delete', help='The request’s DELETE parameters')
    delete_parser.add_argument('--delete')


    return root_parser