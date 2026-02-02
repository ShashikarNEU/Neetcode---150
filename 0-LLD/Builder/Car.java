package Builder;
public class Car {
    private String make = "2001";
    private String model = "E21";
    private String engine = "V3";

    public Car(CarBuilder builder)
    {
      this.make = builder.make;
      this.model = builder.model;
      this.engine = builder.engine;
    }

    public String getMake() {
      return make;
    }

    public String getModel() {
      return model;
    }
    public String getEngine() {
      return engine;
    }

    @Override
    public String toString() {
      return "Car{" +
              "make='" + make + '\'' +
              ", model='" + model + '\'' +
              ", engine='" + engine + '\'' +
              '}';
    }

    public static class CarBuilder {
      private String make = "2001";
      private String model = "E21";
      private String engine = "V3";

      public CarBuilder setMake(String make){
        this.make = make;
        return this;
      }

      public CarBuilder setModel(String model){
        this.model = model;
        return this;
      }

      public CarBuilder setEngine(String engine){
        this.engine = engine;
        return this;
      }

      public Car build() {
        return new Car(this);
      }
    }
}