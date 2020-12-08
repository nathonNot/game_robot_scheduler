

func_dc = {}


def hand(func_name):
    def decorator(func):
        def wrapper(*args,**kwargs):
            global func_dc
            func_dc[func_name] = func
            return func(*args)
        return wrapper
    return decorator


@hand(func_name = "hand_test")
async def hand_test(user_id,msg):
    print(msg)