try:
    print('try....')
    r=10/int('a')
    print('result:',r)
except ValueError as e:
    print('except:',e)
except ZeroDivisionError as e:
    print('except:',e)
else:
    print('no error')
finally:
    print('finally...')
print('END')
# 跨层调用 我们不需要关注每一个被调用的底层方法，为最顶层的调用方法进行try...except就可以了
def foo(s):
    return 10/int(s)
def bar(s):
    return foo(s)*2
def main():
    try:
        bar('0')
    except Exception as e:
        print('except:',e)
    finally:
        print('finally....')
main()
print('END')