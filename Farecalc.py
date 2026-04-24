# CityCab Fare Calculator

def calculate_fare(km, vehicle_type, hour):
    # Step 1: Dictionary Mapping
    rates = {
        'Economy': 10,
        'Premium': 18,
        'SUV': 25
    }

    # Step 4: Error Handling
    if vehicle_type not in rates:
        return None

    base_rate = rates[vehicle_type]
    total = km * base_rate

    # Step 2: Surge Logic
    surge_multiplier = 1
    if 17 <= hour <= 20:
        surge_multiplier = 1.5

    final_price = total * surge_multiplier
    return final_price


# ====== USER INPUT ======
try:
    km = float(input("Enter distance (in km): "))
    vehicle_type = input("Enter vehicle type (Economy / Premium / SUV): ")
    hour = int(input("Enter hour of ride (0-23): "))

    # Function call
    fare = calculate_fare(km, vehicle_type, hour)

    # Step 4: Handle invalid vehicle type
    if fare is None:
        print("\n❌ Service Not Available for selected vehicle type.")
    else:
        # ====== RECEIPT ======
        print("\n========= CityCab Ride Receipt =========")
        print(f"Distance: {km} km")
        print(f"Vehicle Type: {vehicle_type}")
        print(f"Hour: {hour}:00")

        if 17 <= hour <= 20:
            print("Surge Pricing Applied: YES (1.5x)")
        else:
            print("Surge Pricing Applied: NO")

        print(f"Final Fare: ₹{fare:.2f}")
        print("========================================")

except ValueError:
    print("\n❌ Invalid input! Please enter correct numeric values.")