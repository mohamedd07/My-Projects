package com.otpsender.otpsenderdemo;

import java.io.*;
import java.util.Scanner;

public class JavaApplication1 {
        public static Catalog loadDataFromFile(String filePath) throws IOException {
         Catalog catalog = new Catalog();
         BufferedReader reader = new BufferedReader(new FileReader(filePath));

         String line;
         Category currentCategory = null;

         while ((line = reader.readLine()) != null) {
             String[] parts = line.split(",");
             String itemType = parts[0];

             if (itemType.equals("CATEGORY")) {
                 String categoryName = parts[1];
                 currentCategory = new Category(categoryName);
                 catalog.addCategory(currentCategory);
             } else if (itemType.equals("ITEM")) {
                 if (currentCategory != null) {
                     String itemName = parts[1];
                     double itemPrice = Double.parseDouble(parts[2]);
                     double itemMount = Double.parseDouble(parts[3]);
                     Double itemLimit = Double.parseDouble(parts[4]);
                     String itemDescription = parts[5];
                     Item item = new Item(itemName, itemPrice, itemMount, itemLimit, itemDescription);
                     currentCategory.addItem(item);
                 }
             }
         }

         //reader.close();

         return catalog;
     }

    public static void deleteDataFromFile(String filePath) throws IOException {
        BufferedWriter writer = new BufferedWriter(new FileWriter(filePath));
        writer.write("");
        writer.close();
    }

    public static void addDataToFile(String filePath, Catalog catalog) throws IOException {
        BufferedWriter writer = new BufferedWriter(new FileWriter(filePath, true));

        for (Category category : catalog.getCategory()) {
            writer.write("CATEGORY," + category.getName() + "\n");
            for (Item item : category.getItems()) {
                writer.write("ITEM," + item.getName() + "," + item.getPrice() + ","
                        + item.getMount() + "," + item.getLimit() + "," + item.getDescription() + "\n");
            }
        }

        writer.close();
    }
}