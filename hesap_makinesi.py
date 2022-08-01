a = int(input("ilk sayıyı giriniz"))
b = int(input("ikinci sayıyı giriniz"))
islem =int(input("işlem türü"))
if islem == 1:
    print("{} ile {} toplamı {}'na eşittir".format(a, b, a + b))
elif islem == 2:
    print("{} ile {} çıkarma {}'na eşittir".format(a, b, a - b))
elif islem == 3:
    print("{} ile {} çarpma {}'na eşittir".format(a, b, a * b))
elif islem == 4:
    print("{} ile {} bölme {}'na eşittir".format(a, b, a / b))
else:
    print("geçersiz işlem")
