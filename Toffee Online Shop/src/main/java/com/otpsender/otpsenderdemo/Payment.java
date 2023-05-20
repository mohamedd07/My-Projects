package com.otpsender.otpsenderdemo;

import java.util.Scanner;

public class Payment {
    private Order order;
    private String phoneNum;
    public Payment(Order order){
        this.order = order;
        this.phoneNum = phoneNum;
    }

    public void Cash(Order order) {
        double totalprice = order.getTotal();
//        System.out.println("Your total price is: " + totalprice);
        Scanner input = new Scanner(System.in);
        System.out.println("Enter your Phone number: ");
        phoneNum = input.nextLine();
        if (phoneNum. length() ==11 && phoneNum.charAt(0) == '0' && phoneNum.charAt(1) == '1') {
            System.out.println("1- Confirm\n" +
                    "2- Cancel");
            if (input.nextInt() == 1) {
                System.out.println("Your order has been confirmed");
            } else {
                System.out.println("Your order has been canceled");

            }        }
        else{
            System.out.println("Invalid phone number");
            Cash(order);
        }
    }
}
