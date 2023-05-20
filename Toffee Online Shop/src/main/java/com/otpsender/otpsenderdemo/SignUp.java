package com.otpsender.otpsenderdemo;
import java.io.*;
import java.util.*;




class SignUp {
    private String address;
    private int OTP;
    // @Autowired
    private EmailSenderService em;
    public SignUp(String address , EmailSenderService em) {
        this.address = address;
        this.em=em;
    }
public SignUp(){};
    public void signUp(String gmail, String password, String address, int OTP) {
        User user = new User(gmail, password);
        try {
            FileWriter writer = new FileWriter("users.txt", true);
            writer.write(user.getGmail() + "," + user.getPassword() + "," + address + "\n");
            writer.close();
            System.out.println("Signed up Succesfully");
            User app=new User();
            app.APP();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }


    public int OTP() {
        Random rand = new Random();
        int otp = rand.nextInt(9000) + 999;
        OTP = otp;
        return OTP;
    }

    public int getOTP() {
        return OTP;
    }

    public String getAddress() {
        return address;
    }
}
