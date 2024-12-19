
print('тест 1')


A = "число {} текст {} и снова число {}"
txt = A.format(123,         456, 321)
print(txt)

txt = "число {0} - это {1} или {2}".format(42, 43, 44)
print(txt)

txt = "код: {0:05d}, символ: {0:*^5c}".format(65)
print(txt)

txt = "число: {:_>+20.3E}".format(123.458)
print(txt)

B = "{0:_{2}{1}s}"
num = 6
for k in range(1, num + 1):
    print(B.format("*", k, ">"), end="")
    print(" " * (2 * (num - k)), end="")
    print(B.format("*", k, "<"))