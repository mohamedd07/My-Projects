package com.otpsender.otpsenderdemo;

public class Item {
    private String name;
    private double price;
    private double limit;
    private String description;
    private double mount;
    private double mountTOBuy = 0;

    public Item(String name, double price,double mount, double limit, String description) {
        this.name = name;
        this.price = price;
        this.limit = limit;
        this.description = description;
        this.mount = mount;
    }

    // Getters and setters

    public String getName() {
        return name;
    }

    public double getPrice() {
        return price;
    }

    public double getLimit() {
        return limit;
    }


    public String getDescription() {
        return description;
    }

    public double getMount() {
        return mount;
    }

    public void setMount(double mount) {
        this.mount = mount;
    }

    public double getMountToBuy() {
        return mountTOBuy;
    }

    public void setMountToBuy(double num ) {
        mountTOBuy = num;
    }

    public void updateMount(double mount) {
        this.mount -= mount;
    }
}
