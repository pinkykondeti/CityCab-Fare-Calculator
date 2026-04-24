CityCab Fare Calculator

A Python-based backend script that calculates ride fares for a ride-sharing service CityCab. The fare dynamically changes based on distance, vehicle type, and peak-hour surge pricing.

--Features

1. Supports multiple vehicle types (Economy, Premium, SUV)
2. Dynamic pricing based on distance (per km rate)
3. Surge pricing applied during peak hours (5 PM – 8 PM)
4. Error handling for invalid inputs
5. Generates a formatted ride receipt

--Tech Stack

1. Python 3.x
2. No external libraries required (pure Python)

-- Project Structure

CityCab-Fare-Calculator/

│
├── Farecalc.py    

└── README.md     

--How It Works

1. User inputs:

   1. Distance (in km)
   2. Vehicle type (Economy / Premium / SUV)
   3. Hour of the ride (0–23)

2. The system:

   1. Calculates base fare using a dictionary mapping
   2. Applies 1.5x surge pricing if time is between 17–20 hours
   3. Returns final fare

--How to Run

Step 1: Clone the repository

     git clone https://github.com/your-username/CityCab-Fare-Calculator.git
     
     cd CityCab-Fare-Calculator

Step 2: Run the script

       python Farecalc.py

--Example Usage

1.Normal Pricing (No Surge)

Enter distance (km): 10

Enter vehicle type (Economy/Premium/SUV): Economy

Enter hour (0-23): 14

Final Fare: 100.0
 
2.Surge Pricing Applied (Peak Hours)

Enter distance (km): 10

Enter vehicle type (Economy/Premium/SUV): Premium

Enter hour (0-23): 18

** Surge Pricing Applied (1.5x)

Final Fare: 270.0

-- Pricing Details

| Vehicle Type | Rate per km (₹) |
| ------------ | --------------- |
| Economy      | 10              |
| Premium      | 18              |
| SUV          | 25              |

--Surge Pricing

* Applied during: 17:00 – 20:00
* Multiplier: 1.5x

--Error Handling

1. Invalid vehicle type → "Service Not Available"
2. Invalid input → Exception handled gracefully

--Future Enhancements

1. GUI version using Tkinter
2. Web app using Flask / React
3. Database integration for ride history
4. API-based backend service

👨‍💻 Author

Developed this project as part of my learning
