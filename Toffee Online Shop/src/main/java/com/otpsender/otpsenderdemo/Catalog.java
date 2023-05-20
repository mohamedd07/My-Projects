package com.otpsender.otpsenderdemo;

import java.util.ArrayList;
import java.util.List;

public class Catalog {

    private List<Category> categories;

    public Catalog() {
        this.categories = new ArrayList<>();
    }

    public void addCategory(Category category) {
        categories.add(category);
    }

    public Category getCategory(String i) {
        for(Category category : categories)
        {
            if(category.getName().equals(i))
                return category;
        }
        return null;
    }

    public List<Category> getCategory()
    {
        return categories;
    }



    public void display() {
        for (Category category : categories) {
            System.out.println("Category: " + category.getName());
        }
    }

    
}

