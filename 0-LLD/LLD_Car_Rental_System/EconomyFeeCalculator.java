package LLD_Car_Rental_System;

public class EconomyFeeCalculator implements FeeCaculatorStrategy {

    @Override
    public double caculateFee(String startDate, String endDate, String vehicleType, Boolean premiumBoolean) {
        // Assuming a flat rate for economy vehicles
       double EcoFee = 100.0; // Example premium fee
       return EcoFee;
    }
}
