import methods

if __name__ == "__main__":

    if methods.namespace.request == "get":
        methods.get_request()
    elif methods.namespace.request == "post":
        methods.post_request()
    elif methods.namespace.request == "put":
        methods.put_request()
    elif methods.namespace.request == "delete":
        methods.delete_request()
