package com.otpsender.otpsenderdemo;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

//import static Cart.JavaApplication1.loadDataFromFile;

public class Cart {
    private double totalPrice = 0;
    private ArrayList<Item> items;
    private Cart cart;

    public Cart() {
        this.items = new ArrayList<>();
    }

    public void setPrice(double num)
    {
        this.totalPrice += num;
    }

    public double getPrice()
    {
        return totalPrice;
    }

    public void addItem(Item item , double mount) {
        if (mount <= item.getLimit() && mount <= item.getMount()) {
            item.updateMount(mount);
            item.setMountToBuy(mount);
            items.add(item);
            setPrice((item.getMountToBuy() * item.getPrice()));
            System.out.println("Item added to cart: " + item.getName());
        } else {
            System.out.println("Item cannot be added to cart. Limit reached: " + item.getLimit());
        }
    }
    public void removeItem(String i)
    {
        Item item = null;
        for(int j = 0 ; j < items.size() ; ++j)
        {
            item = items.get(j);
            if(item.getName().equals(i))
            {
                item.updateMount(-1*item.getMountToBuy());
                setPrice(-1*(item.getMountToBuy() * item.getPrice()));
                item.setMountToBuy(0);
                items.remove(item);
                --j;
                System.out.println("Item removed from cart: " + item.getName());
            }
        }
    }

    public void displayItems() {
        if(items.isEmpty())
        {
            System.out.println("Cart is empty ");
            return;
        }
        for (Item item : items) {
            System.out.println("Item: " + item.getName());
            System.out.println("Mount: " + item.getMountToBuy());
            System.out.println("Price: " + (item.getPrice()* item.getMountToBuy()));

        }
        System.out.println("---------------------------");
        System.out.println("totalPrice: " + getPrice());
        System.out.println("---------------------------");
    }


    }


