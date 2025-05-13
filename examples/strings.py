temp = 15
message = f"Temperature is {temp:.2f} degrees Celsius"
print(message)

total_minutes = 122
hour = total_minutes // 60
minute = total_minutes % 60
print(f"{hour:02}:{minute:02}")

print(str(hour).rjust(2, "0"))
