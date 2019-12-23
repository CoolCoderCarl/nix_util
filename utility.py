import methods


if __name__ == '__main__':

    if methods.namespace.request == "get":
        methods.getRequest()
    elif methods.namespace.request == "post":
        methods.postRequest()