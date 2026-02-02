package LLD_Car_Rental_System;

public class PremuimFeeCaculator implements FeeCaculatorStrategy{

  @Override
  public double caculateFee(String startDate, String endDate, String vehicleType, Boolean premiumBoolean) {
    // Assuming a fixed premium fee for simplicity
    double premiumFee = 100.0; // Example premium fee
    return premiumFee;
  }
  
}
