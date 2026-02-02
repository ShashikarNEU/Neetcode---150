package LLD_Car_Rental_System;

import java.util.ArrayList;
import java.util.List;

public class Main {
  public static void main(String[] args) {
    VehicleFactory vehicleFactory = new VehicleFactory();
    ArrayList<Booking> pastBookings = new ArrayList<>();
    Booking currentBooking = new Booking(); // Assuming Booking class has a default constructor
    // Add model also based on that, put premuim = True or False
    vehicleFactory.createVehicle("Car", 123, 1, pastBookings, currentBooking, null);

    // Assuming CarRentalSingleton is a singleton class that provides access to the CarRentalSystem instance
    CarRentalSystem carRentalSystem = CarRentalSingleton.getInstance();


    List<Vehicle> premiumVehicles = carRentalSystem.getPremiumVehicles("Car");

    // Select vehicles from here (Print)

    for (Vehicle vehicle : premiumVehicles) {
      System.out.println("Vehicle ID: " + vehicle.id + ", License No: " + vehicle.licenseNo + ", Is Premium: " + vehicle.isPremium);
    }
    // Assuming he chooses index 0 for booking
    FeeCaculatorStrategy feeCaculatorStrategy = new PremuimFeeCaculator();
    Booking booking = carRentalSystem.bookVehicle(premiumVehicles.get(0), "2023-10-01", "2023-10-05", feeCaculatorStrategy);
    System.out.println("Booked Vehicle ID: " + premiumVehicles.get(0).id + ", Start Date: " + premiumVehicles.get(0).currentBooking.startDate + ", End Date: " + premiumVehicles.get(0).currentBooking.endDate);

    // On Return Day
    
    if (booking.isActive && booking.isPremium) {
      double fee = booking.caculateFee(booking.startDate, booking.endDate, booking.vehicle.vehicleType, true);
      booking.isActive = false; // Mark booking as inactive after fee calculation
      booking.vehicle.isBooked = false; // Mark vehicle as not booked
      booking.vehicle.currentBooking = null; // Clear current booking for the vehicle
      booking.vehicle.pastBookings.add(booking); // Add booking to past bookings
      // Print the total fee for the booking
      System.out.println("Total Fee for Booking ID " + booking.bookingId + ": " + fee);
    }
  }
}
