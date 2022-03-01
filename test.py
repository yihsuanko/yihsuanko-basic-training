def yield_test(n):
    print("start n =", n)
    for i in range(n):
        yield i*i
        print("i =", i)

    print("end")

tests = yield_test(3)
for test in tests:
    print("test =", test)
    print("--------")