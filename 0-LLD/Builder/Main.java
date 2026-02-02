package Builder;

public class Main {
  public static void main(String[] args) {
    Car.CarBuilder builder = new Car.CarBuilder();
    Car car1 = builder.setEngine("V6")
            .setMake("2025")
            .setModel("E5")
            .build();
    
    Car car2 = builder.setEngine("V5")
        .setModel("E6")
        .build();
    
    System.out.println(car1);
    System.out.println(car2);
  }
}