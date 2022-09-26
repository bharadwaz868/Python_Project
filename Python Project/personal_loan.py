# Collect the necessary inputs: Principal P,  Rate of interest applicable R/r , Tenure in years N/n
# Calculate EMI repayable E ,Monthly Interest Mi, Amount of Months a
# Display to the User

def main():
    print("This is a EMI Calculator ")
    print("")


    P = float(input("Enter the loan amount: "))
    r = float(input("Enter the rate of interest applicable: "))
    n = int(input("Enter Tenure in years: "))
    r = r/12/100
    n= n *12


    # mi = r / 1200
    # a = n * 12
    # emi = P * mi / (1 - (1 + mi) ** (-a))
    E = (P * r * (1+r)**n) / ((1+r)**n -1)
    TI = (E*n)-P
    TA = E*n

    print("Emi payable is %.2f" %E)
    print("Total Interest  payable is %.2f" %TI)
    print("Total Amount  payable is %.2f" %TA)
    
    exit()

main()

