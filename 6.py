weight_pounds = float(input())
height_inches = float(input())
weight_kg = weight_pounds * 0.453592
height_meters = height_inches * 0.0254
# print(round(weight_kg / height_meters**2, 2))
print(round(weight_pounds * 703 / height_inches**2, 2))