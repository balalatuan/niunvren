# 输入的总组数

t = int(input().strip())

# 遍历每组数据
for _ in range(t):
    # 读取每组数据：首先是整数的个数 n，然后是 n 个整数
    data = list(map(int, input().strip().split()))
    # 计算这些整数的和
    total_sum = sum(data[1:])  # data[0] 是整数的个数，所以从 data[1] 开始求和
    # 输出结果
    print(total_sum)