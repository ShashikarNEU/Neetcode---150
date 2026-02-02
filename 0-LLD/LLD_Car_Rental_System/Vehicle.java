package LLD_Car_Rental_System;

import java.util.List;

public class Vehicle {
  String vehicleType;
  String model;
  int licenseNo;
  int id;
  List<Booking> pastBookings;
  Booking currentBooking;
  Boolean isBooked;
  Boolean isPremium;

  public Vehicle(String vehicleType, int licenseNo, int id, List<Booking> pastBookings, Booking currentBooking, Boolean isPremium) {
    this.vehicleType = vehicleType;
    this.licenseNo = licenseNo;
    this.id = id;
    this.pastBookings = pastBookings;
    this.currentBooking = currentBooking;
    this.isPremium = isPremium;
  }
}
