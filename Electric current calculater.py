def calculate_current():
    print("Choose the formula to calculate electric current:")
    print("1. Using Voltage and Resistance (I = V / R)")
    print("2. Using Power and Voltage (I = P / V)")
    print("3. Using Charge and Time (I = Q / t)")
    
    choice = int(input("Enter your choice (1/2/3): "))
    
    if choice == 1:
        voltage = float(input("Enter Voltage (V) in volts: "))
        resistance = float(input("Enter Resistance (R) in ohms: "))
        if resistance == 0:
            print("Resistance cannot be zero.")
        else:
            current = voltage / resistance
            print(f"Electric Current (I) = {current:.2f} A")
    
    elif choice == 2:
        power = float(input("Enter Power (P) in watts: "))
        voltage = float(input("Enter Voltage (V) in volts: "))
        if voltage == 0:
            print("Voltage cannot be zero.")
        else:
            current = power / voltage
            print(f"Electric Current (I) = {current:.2f} A")
    
    elif choice == 3:
        charge = float(input("Enter Charge (Q) in coulombs: "))
        time = float(input("Enter Time (t) in seconds: "))
        if time == 0:
            print("Time cannot be zero.")
        else:
            current = charge / time
            print(f"Electric Current (I) = {current:.2f} A")
    
    else:
        print("Invalid choice. Please choose a valid option.")

# Run the program
calculate_current()
