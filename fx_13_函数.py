def circle(father, mother = 'Ning', uncle = 'Chao' ):
    print(f'我的爸爸是{father}，妈妈是{mother}，叔叔是{uncle}')

circle('Kun','Ning')


def circle1(*a):
    """
    不定长位置参数
    :param a:
    :return:
    """
    print(a)

circle1()

# 不定长关键字参数
def circle2(**a):
    print(a)

circle2( c = 'a', b = 'b')

def circles(father, mother, grandma, grandpa, *args , wife = 'what', **ps ):
    print(f'爸爸是{father},妈妈是{mother}，媳妇是{wife}， 奶奶是{grandma}, 爷爷是{grandpa},args,ps')

circles('Kun', 'Ning',
        'love', 'everyone',
        grandma='Pen', grandpa='Wen',
        a = 'a', b = 'b'
        )