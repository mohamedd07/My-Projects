package com.otpsender.otpsenderdemo;
// import Cart.*;
//import Cart.Cart;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;
import java.io.File;


public class Order {
    private Cart cart;
    private static int Orderid = 1;
    private Double Total;

    public Order(Cart cart){
        this.Total = cart.getPrice();
        this.cart = cart;
    }
    public int getOrderid() {
        return Orderid;
    }
    public Double getTotal() {
        return cart.getPrice();
    }
    public Order(int Orderid,Double Total){
        this.Orderid = Orderid;
        this.Total = Total;
    }
    public void Save(Order order){
        File file = new File("order.txt");
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(file,true))){
            writer.write("Order id :");
            writer.newLine();
            writer.write(String.valueOf(order.getOrderid()));
            writer.newLine();
            writer.write("Total Price : ");
            writer.newLine();
            writer.write(String.valueOf(order.getTotal()));
            writer.newLine();
        }
        catch (IOException e){
            e.printStackTrace();
        }
    }
    public void makeOrder(){
        Order order = new Order(cart);
        if(cart == null){
            System.out.println("your cart is empty");
        }
        else{
            System.out.println("Your cart is :");
            cart.displayItems();
            System.out.println("Do you want to make an order with your current cart ?(y/n)");
            Scanner input = new Scanner(System.in);
            char choice = input.next().charAt(0);
            if(choice == 'y'){
                Save(this);
                Orderid++;
            }
            else{
                System.out.println("Your order has been canceled");
            }
        }
    }
}
