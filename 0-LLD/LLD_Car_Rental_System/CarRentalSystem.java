package LLD_Car_Rental_System;

import java.util.ArrayList;
import java.util.List;

public class CarRentalSystem {
  List<Vehicle> vehicles;

  public List<Vehicle> getPremiumVehicles(String vehicleType){
    List<Vehicle> premiumVehicles = new ArrayList<>();
    for (Vehicle vehicle: vehicles)
    {
      if (vehicle.isPremium && vehicle.vehicleType.equals(vehicleType))
      {
        premiumVehicles.add(vehicle);
      }
    }
    return premiumVehicles;
  }
  
  public Booking bookVehicle(Vehicle vehicle, String startDate, String endDate, FeeCaculatorStrategy feeCaculatorStrategy)
  {
    Booking booking = new Booking(vehicle, startDate, endDate, endDate, false, vehicle.isPremium, feeCaculatorStrategy);
    vehicle.currentBooking = booking;
    vehicle.isBooked = true;
    return booking;
  }
  
}
