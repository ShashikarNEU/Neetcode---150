package LLD_Car_Rental_System;

public interface FeeCaculatorStrategy {
    double caculateFee(String startDate, String endDate, String vehicleType, Boolean premiumBoolean);
}
