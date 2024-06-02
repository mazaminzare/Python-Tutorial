
# raise IndexError('throw index error')
# raise ValueError('invalid value')


def colorsize(text,color):
    colors=('red','green','black')
    if type(text) is not str:
        raise TypeError("text must be string")
    elif color is not colors:
        raise ValueError(f"{color} is not in colors")
    else:
        print(f"printed {text} in {color}")

colorsize("hello","yellow")
