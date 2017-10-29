#!/usr/bin/env python3

principal = 500000
payment = 2600.0
rate = 0.05
total_paid = 0 

# Extra Payment 
extra_payment = 1000
start_month = 1
end_month = 60
month = 0

f = open("schedule_out.txt", "w")

print("{:>10s} {:>10s} {:>10s} {:>10s}".format("Month", "Interest", "Remaining", "Principal"), file=f)

while principal > 0:
	
    month += 1
    if month >= start_month and month <= end_month:
        total_payment = payment + extra_payment
    else:
        total_payment = payment

    interest = principal * (rate/12)
    principal = principal + interest - total_payment
    total_paid += total_payment  

    print("{:>10d} {:>10.2f} {:>10.2f} {:>10.2f}".format(month, interest, total_payment - interest, principal), file=f)


print("Total Paid : ", total_paid, file=f)

f.close()
        
