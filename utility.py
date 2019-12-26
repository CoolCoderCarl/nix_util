import methods


if __name__ == '__main__':

    if methods.namespace.request == "get":
        methods.getRequest()
    elif methods.namespace.request == "post":
        methods.postRequest()
    elif methods.namespace.request == "put":
        methods.putRequest()
    elif methods.namespace.request == "delete":
        methods.deleteRequest()