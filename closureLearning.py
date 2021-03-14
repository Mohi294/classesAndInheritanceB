def print_msg(msg):
    # This is the outer enclosing function

    def printer():
        # This is the nested function
        print( msg )

    return printer


# We execute the function
# Output: Hello
hi_func = print_msg("hi")
hi_func()

