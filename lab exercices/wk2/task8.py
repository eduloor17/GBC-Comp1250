#Task 8-Using the round() method, round the following float values
#1.235 to two decimal places, 2.45 to one decimal place
#3.97531 to four decimal places - Using a comment, state your observations
print('Task 8')
float1 = 1.235
float2 = 2.45
float3 = 3.97531
print(f"Original values: {float1}, {float2}, {float3}")
float1 = round(float1, 2)
float2 = round(float2, 1)
float3 = round(float3, 4)
print(f"Round values: {float1} (2 Decimal places), {float2} (1 Decimal place), {float3} (4 Decimal places)")
"""
I have 3 different float values, I use round(float, #), where float is the name of my variable 
and # is how many decimal round will do.
"""