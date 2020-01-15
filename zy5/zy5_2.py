# 循环和递实现公共最长子序列动态规划
# 递归
# def lcs1(A, B):
#     # 普通递归
#     if not(A and B):
#         return ''
#     elif A[-1] == B[-1]:
#         return lcs1(A[:-1], B[:-1]) + A[-1]
#     else:
#         if len(lcs1(A[:-1], B)) > len(lcs1(A, B[:-1])):
#             return lcs1(A[:-1], B)
#         else:
#             return lcs1(A, B[:-1])

chart = {}
def lcs2(A, B):
    # 动态规划版
    global chart
    if (A, B) in chart.keys():
        return chart.get((A, B))
    else:
        if not(A and B):
            return ''
        elif A[-1] == B[-1]:
            return lcs2(A[:-1], B[:-1]) + A[-1]
        else:
            if len(lcs2(A[:-1], B)) > len(lcs2(A, B[:-1])):
                chart.update({(A[:-1], B): lcs2(A[:-1], B)})
                return lcs2(A[:-1], B)
            else:
                chart.update({(A,B[:-1]): lcs2(A, B[:-1])})
                return lcs2(A, B[:-1])

print(lcs2('educatiSDWonal', 'advSDWantage'))
print(chart)
