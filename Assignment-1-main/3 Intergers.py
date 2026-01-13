a, b, c= map(int, input("nhập 3 số nguyên:").split())
sum = a + b + c
product = a * b * c
average = sum/3
print ("tổng các số là: "+ str(sum), "tích các số là: "+str(product), "trung bình cộng các số là: "+str(average), sep="\n")