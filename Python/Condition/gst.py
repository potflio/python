# Get salary input from the user
salary = float(input("Enter your salary: "))

# Determine GST rate based on salary
if salary < 20000:
    gst_rate = 0.03
else:
    gst_rate = 0.05

# Calculate GST amount
gst = salary * gst_rate

# Print GST
print("Applicable GST rate:", gst_rate * 100, "%")
print("GST amount on salary is:", gst)
