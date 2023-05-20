package com.otpsender.otpsenderdemo;
import java.io.*;
import java.util.*;

import static com.otpsender.otpsenderdemo.JavaApplication1.loadDataFromFile;
// import Cart.*;
// import Ordering.*;

class User {
    private String gmail;
    private String password;
    public User(String gmail, String password) {
        this.gmail = gmail;
        this.password = password;
    }
    public User(){};
    
    
    public String getGmail() {
        return this.gmail;
    }
    
    public void setGmail(String gmail) {
        this.gmail = gmail;
    }
    
    public String getPassword() {
        return this.password;
    }
    
    public void setPassword(String password) {
        this.password = password;
    }

    public void APP() throws NumberFormatException, IOException{
        String s;
        Cart cart = new Cart();


        while(true){
            Scanner input4 = new Scanner(System.in);
            System.out.println("Do you want to:\n" +
                    "1-Add items to your cart\n" +
                    "2-Remove items from your cart\n" +
                    "3-Display your cart\n" +
                    "4-Make an order\n" +
                    "5-Exit\n");
            int choice = input4.nextInt();
            if(choice == 1){
                Catalog catalog = loadDataFromFile("data.txt");
                catalog.display();
                Scanner in = new Scanner(System.in);
                System.out.println("Enter name of category to show it's items ");
                s = in.nextLine();
                Category category = catalog.getCategory(s);
                category.disPlay();

                System.out.println("Enter item to add it to cart ");
                Scanner input2 = new Scanner(System.in);
                s = input2.nextLine();
                Item item = category.getItems(s);

                System.out.println("Enter Mount of item u want to buy ");
                Scanner input3 = new Scanner(System.in);
                double num = input3.nextDouble();
                cart.addItem(item, num);
            } else if (choice == 2) {
                Scanner in = new Scanner(System.in);
                System.out.println("Enter name of item to remove it from cart ");
                s = in.nextLine();
                cart.removeItem(s);
                cart.displayItems();
            } else if (choice == 3) {
                System.out.println("Your cart contains :");
                cart.displayItems();
            } else if (choice == 4) {
                Order order = new Order(cart);
                order.makeOrder();
                Payment payment = new Payment(order);
                payment.Cash(order);
                cart = new Cart();
            } else if (choice == 5) {
                System.exit(0);
            } else {
                System.out.println("Invalid choice");
            }
            continue;
        }
    }
    
    public void login(String gmail,String password) {
        try {
            File file = new File("users.txt");
            Scanner scanner = new Scanner(file);
            boolean success=true;
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                String[] fields = line.split(",");
                
                if (fields[0].equals(gmail) && fields[1].equals(password)) {
                    System.out.println("Logedin Successfully");
                    success=false;
                    APP();
                
                } 
            }
            if(success){System.out.println("Wrong email or password");}
            scanner.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

    }






    /**
     * @param args
     */
//    public static void main(String[] args) {
//
//    }
}

