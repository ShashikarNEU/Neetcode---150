package LLD_Car_Rental_System;

import java.util.List;

public class VehicleFactory {
  public Vehicle createVehicle(String vehicleType, int licenseNo, int id, List<Booking> pastBookings, Booking currentBooking, Boolean isPremium)
  {
    if (vehicleType.equals("Car"))
    {
      // Based on model, put isPremium True or False, take model in argument also
      return new Car(vehicleType, licenseNo, id, pastBookings, currentBooking, isPremium);
    }
    // Add more vehicle types here as needed
    // For now, we will just return a generic Vehicle
    // You can also throw an exception if the vehicle type is not supported
    // For simplicity, we will return a Vehicle object directly
    // You can also create a Vehicle subclass for each vehicle type
    // and return that instead
    // For example, if you have a Truck class, you can do:
    // if (vehicleType.equals("Truck")) {
    //   return new Truck(vehicleType, licenseNo, id, pastBookings, currentBooking, isPremium);
    // }
    // For now, we will just return a generic Vehicle object
    return new Vehicle(vehicleType, licenseNo, id, pastBookings, currentBooking, isPremium);
  }
}
