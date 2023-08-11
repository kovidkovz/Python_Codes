# Calculate income tax for the given income by adhering to the below rules
# Taxable Income	Rate (in %)
# First $10,000	        0
# Next $10,000	       10
# The remaining	       20
income=int(input("Enter your income in $:" ))
print("The income is: ","$",income)
if income<20000:
    tax_payable=0
elif income==20000:
    tax_payable=10000*10/100
else:
    tax_payable=10000*10/100
    x=income-20000
    tax_payable+=x*20/100
print("Tax to be paid","$",tax_payable)
