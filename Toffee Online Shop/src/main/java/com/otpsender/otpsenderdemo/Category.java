package com.otpsender.otpsenderdemo;

import java.util.ArrayList;
import java.util.List;

public class Category {
    private String name;
    private List<Item> items;

    public Category(String name) {
        this.name = name;
        this.items = new ArrayList<>();
    }

    public void addItem(Item item) {
        items.add(item);
    }

    public Item getItems(String i) {
        for(Item item :items)
        {
            if(item.getName().equals(i))
                return item;
        }
        return null;
    }

    public List<Item> getItems()
    {
        return items;
    }

    public String getName()
    {
        return name;
    }

    public void disPlay(){
        for (Item item : items) {
            System.out.println("Item: " + item.getName());
            System.out.println("Price: " + item.getPrice());
            System.out.println("Mount: " + item.getMount());
            System.out.println("Description: " + item.getDescription());
            System.out.println("---------------------------");
        }
    }
}
