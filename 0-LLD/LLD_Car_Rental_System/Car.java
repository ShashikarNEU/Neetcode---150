package LLD_Car_Rental_System;

import java.util.List;

public class Car extends Vehicle{
  
  public Car(String vehicleType, int licenseNo, int id, List<Booking> pastBookings, Booking currentBooking, Boolean isPremium) {
    super(vehicleType, licenseNo, id, pastBookings, currentBooking, isPremium);
  }

}
