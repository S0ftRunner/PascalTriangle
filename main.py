



row = int(input())
pascal_triangle = []

for i in range(row):
    temp_list = []
    for j in range(i+1):
        if j == 0 or j == i:
            temp_list.append(1)
        else:
            temp_list.append(pascal_triangle[i-1][j-1] + pascal_triangle[i-1][j])
    pascal_triangle.append(temp_list)



print(*pascal_triangle, sep='\n')