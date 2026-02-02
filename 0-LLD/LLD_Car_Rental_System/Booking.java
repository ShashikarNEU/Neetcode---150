package LLD_Car_Rental_System;

public class Booking {
  int bookingId;
  Vehicle vehicle;
  String startDate;
  String endDate;
  String customerName;
  boolean isActive;
  Boolean isPremium;

  FeeCaculatorStrategy feeCaculatorStrategy;

  
  public void setFeeCaculatorStrategy(FeeCaculatorStrategy feeCaculatorStrategy) {
    this.feeCaculatorStrategy = feeCaculatorStrategy;
  }

  public Booking(Vehicle vehicle, String startDate, String endDate, String customerName, boolean isActive, Boolean isPremium, FeeCaculatorStrategy feeCaculatorStrategy) {
    this.bookingId = (int) (Math.random() * 10000); // Random booking ID for simplicity
    this.vehicle = vehicle;
    this.startDate = startDate;
    this.endDate = endDate;
    this.customerName = customerName;
    this.isActive = isActive;
    this.isPremium = isPremium;
    this.feeCaculatorStrategy = feeCaculatorStrategy;
  }

  public Booking() {
    //TODO Auto-generated constructor stub
  }

  public double caculateFee(String startDate, String endDate, String vehicleType, Boolean premiumBoolean) {
    return feeCaculatorStrategy.caculateFee(startDate, endDate, vehicleType, premiumBoolean);
  }
  
}
