# 定义一个函数，用于计算两个数的和
def calculate_sum(a, b):
    return a + b

# 获取用户输入的两个数
num1 = float(input("请输入第一个数："))
num2 = float(input("请输入第二个数："))

# 调用函数计算和
sum = calculate_sum(num1, num2)

# 打印结果
print(f"{num1} 和 {num2} 的和是：{sum}")
