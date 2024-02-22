def is_triangle_valid(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return "Yes"
    else:
        return "No"

a, b, c =input("Enter three Vlues").split()

result = is_triangle_valid(a, b, c)

print(result)
