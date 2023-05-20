package com.otpsender.otpsenderdemo;
import java.util.Scanner;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.context.event.ApplicationReadyEvent;
import org.springframework.context.event.EventListener;

import static com.otpsender.otpsenderdemo.JavaApplication1.loadDataFromFile;

@SpringBootApplication
public class ToffeeApp {
	@Autowired
	private EmailSenderService senderService;
	public static void main(String[] args) {
		SpringApplication.run(ToffeeApp.class, args);
		
	}

    @EventListener(ApplicationReadyEvent.class)
	public void sendEmail() throws NumberFormatException, IOException {
		Scanner input=new Scanner(System.in);

        Scanner input1=new Scanner(System.in);
        System.out.println("WElcome to our online shop:)");
        System.out.println("1-Login");
        System.out.println("2-Signup");
        System.out.println("Enter your chiose: ");
        int x=input1.nextInt();
        String email,password,address;
		if(x==1){
            // Log in with an existing user
            System.out.println("Enter your email:");
            email=input.nextLine();
            System.out.println("Enter your password:");
            password=input.nextLine();
            User user = new User();
            user.login(email, password);
        }
		else{
            //Sign up a new user
            SignUp user = new SignUp();
            System.out.println("Enter your email:");
            email=input.nextLine();
            System.out.println("Enter your password:");
            password=input.nextLine();
            System.out.println("Enter your address:");
            address=input.nextLine();
			user.OTP();
        
			int Otp = user.getOTP();
			String s_Otp=String.valueOf(Otp);
		
			senderService.sendEmail(email,s_Otp , "OTP");
            System.out.println("Enter the OTP code:");
            int OTP=input1.nextInt();

            if(OTP==user.getOTP()){
            user.signUp(email, password, address,OTP);
				
			}
            else{System.out.println("The OTP code is uncorrect:(");}
        }  

	}
}


	// String onum="";
			// int q=0;
			
			// while(Otp!=0)
			// {
			// 	q=Otp%10;
			// 	Otp/=10;
				
			// 	if(q==1)
			// 	{
			// 		onum+="1";
			// 	}
			// 	else if(q==2)
			// 	{
			// 		onum+="2";
			// 	}
				
			// 	else if(q==3)
			// 	{
			// 		onum+="3";
			// 	}
				
			// 	else if(q==4)
			// 	{
			// 		onum+="4";
			// 	}
				
			// 	else if(q==5)
			// 	{
			// 		onum+="5";
			// 	}
				
			// 	else if(q==6)
			// 	{
			// 		onum+="6";
			// 	}
				
			// 	else if(q==7)
			// 	{
			// 		onum+="7";
			// 	}
				
			// 	else if(q==8)
			// 	{
			// 		onum+="8";
			// 	}
				
			// 	else if(q==9)
			// 	{
			// 		onum+="9";
			// 	}
			// 	else if(q==0)
			// 	{
			// 		onum+="0";
			// 	}
				
			// }
			// String s= "";
			// for(int i = onum.length()-1 ; i>-1;i--)
			// {
			// 	char w=onum.charAt(i);
			// 	s+=w;
			// }
			