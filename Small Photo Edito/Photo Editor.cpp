/*
This a Photo Editor that has some filters to edit bmp 256*256 images.
Last modified 20/4/2022
*/

#include <iostream>
#include <fstream>
#include <cstring>
#include <cmath>
#include "bmplib.cpp"

using namespace std;
unsigned char image[SIZE][SIZE] , newimage[SIZE][SIZE];

void loadImage ();
void saveImage ();
void Shuffle_Image(int a, int b, int c, int d);
void Invert_Image();
void Rotate_Image(int A);
void flip_filter();
void BW_filter();
void mirror_filter();

int main()
{
  cout<<"Ahlan ya user ya habibi"<<endl;
  loadImage();
  char n;
cout<<"\nplease, choose:\n(1)Bw filter\n(2)Invert filter\n(4)flip filter\n(5)Rotate filter\n(a)Mirror filter\n(b)Shuffle filter\n(s)save image\n(0)Exit"<<endl;
  cin>>n;
if (n == 's'){
saveImage ();
goto s;}

else if (n == '1')
BW_filter();

else if (n == '2')
Invert_Image();

else if (n == '4')
flip_filter();

else if (n == '5'){
int A;
cout<<"What is the amount of rotation you want?"<<endl;
cout<<"1-Rotate (90)degrees"<<endl;
cout<<"2-Rotate (180)degrees"<<endl;
cout<<"3-Rotate (270)degrees"<<endl;;
cin>>A;  
Rotate_Image(A);}

else if (n == 'a')
mirror_filter();

else if (n == 'b'){
int a,b,c,d;
cout<<"What is the order of the new quadrants that you want?"<<endl;
cin>>a>>b>>c>>d;
Shuffle_Image(a,b,c,d);}

else if (n == '0')
goto s;

else{
cout<<"wrong choice!"<<endl;
goto s;}

saveImage();
s:return 0;
}

//_______________________________________________________________________________________
void loadImage () {
   char imageFileName[100];

   // Get gray scale image file name
   cout << "Please enter file name of the image to process: ";
   cin >> imageFileName;
   // Add to it .bmp extension and load image
   strcat (imageFileName, ".bmp");
   readGSBMP(imageFileName, image);
   readGSBMP(imageFileName, newimage);
}

//_______________________________________________________________________________________
void saveImage () {
   char imageFileName[100];

   // Get gray scale image target file name
   cout << "Enter the target image file name: ";
   cin >> imageFileName;

   // Add to it .bmp extension and load image
   strcat (imageFileName, ".bmp");
   writeGSBMP(imageFileName, image);
   //writeGSBMP(imageFileName, newimage);
}

// ___________________________________________________________________________________________________________________________________
void Shuffle_Image(int a, int b, int c, int d) {
if ( a == 1){
  for (int i =0, x =0;i <SIZE/2;++i,++x){
    for(int j =0, y =0;j< SIZE/2; ++j, ++y){
      image[x][y] = newimage[i][j];
    }
  } 
}
else if (a == 2){
  for(int i=0,x =0;i < SIZE/2;++i,++x){
    for(int j = SIZE / 2,y =0;j< SIZE ;++j,++y){
      image[x][y] = newimage[i][j];
    }
  }  
}
else if ( a == 3){
 for(int i =SIZE/2, x =0;i < SIZE;++i,++x){
   for (int j = 0, y=0;j < SIZE/2;++j,++y){
     image[x][y] = newimage[i][j];
    }
  }  
}
else if (a == 4){
  for(int i =SIZE/2,x=0;i< SIZE;++i,++x){
    for(int j =SIZE/2,y=0;j<SIZE;++j,++y){
      image[x][y] = newimage[i][j];
    }
  }
}
// ______________________________________________
if (b == 1){
  for(int i =0,x=0; i < SIZE/2;++i){
    for(int j = 0,y=SIZE/2; j < SIZE/2;++j){
      image[x][y] = newimage[i][j];
     ++y;}
   ++x;  }
}
else if (b == 2){
  for(int i =0,x=0; i < SIZE/2;++i){
    for(int j = SIZE / 2,y =SIZE/2; j < SIZE;++j){
      image[x][y] = newimage[i][j];
     ++y;}
   ++x;  }
}
else if ( b == 3){
  for(int i =SIZE/2,x=0; i < SIZE;++i){
    for(int j = 0,y= SIZE/2; j < SIZE/2;++j){
      image[x][y] = newimage[i][j];
     ++y;}
   ++x;  }
}
else if (b == 4){
  for(int i =SIZE/2,x=0; i < SIZE;++i){
    for(int j = SIZE/2,y=SIZE/2; j < SIZE;++j){
      image[x][y] = newimage[i][j];
     ++y;}
   ++x;  }
}

// ______________________________________________

if (c == 1){
  for(int i =0,x =SIZE/2; i <SIZE/2;++i){
    for(int j =0,y=0; j <SIZE/2;++j){
      image[x][y] = newimage[i][j];
     ++y;}
   ++x;}
}
if (c == 2){
  for(int i =0,x=SIZE/2; i <SIZE/2;++i){
    for(int j =SIZE/2,y=0; j <SIZE;++j){
      image[x][y] = newimage[i][j];
     ++y;}
   ++x;}
}
if (c == 3){
  for(int i =SIZE/2,x=SIZE/2; i <SIZE;++i){
    for(int j =0,y=0; j <SIZE/2;++j){
      image[x][y] = newimage[i][j];
     ++y;}
   ++x;}
}
if (c == 4){
  for(int i =SIZE/2,x=SIZE/2; i <SIZE;++i){
    for(int j =SIZE/2,y=0; j <SIZE;++j){
      image[x][y] = newimage[i][j];
     ++y;}
   ++x;}
}
// ______________________________________________
if (d == 1){
  for(int i =0, x=SIZE/2; i <SIZE/2;++i){
    for(int j =0,y=SIZE/2; j <SIZE/2;++j){
      image[x][y] = newimage[i][j];
     ++y;}
   ++x;}
}
if (d == 2){
  for(int i =0,x=SIZE/2; i <SIZE/2;++i){
    for(int j =SIZE/2,y=SIZE/2; j <SIZE;++j){
      image[x][y] = newimage[i][j];
     ++y;}
   ++x;}
}
if (d == 3){
  for(int i =SIZE/2,x=SIZE/2; i <SIZE;++i){
    for(int j =0,y=SIZE/2; j <SIZE/2;++j){
      image[x][y] = newimage[i][j];
     ++y;}
   ++x;}
}
if (d == 4){
  for(int i =SIZE/2,x=SIZE/2; i <SIZE;++i){
    for(int j =SIZE/2,y=SIZE/2; j <SIZE;++j){
      image[x][y] = newimage[i][j];
     ++y;}
   ++x;}
}
}
// ___________________________________________________________________________________________________________________________________
void Invert_Image() {
  for (int i = 0; i < SIZE; i++) {
    for (int j = 0; j< SIZE; j++) {

if (image[i][j] == 0)
            image[i][j] = 255;
        else if (image[i][j] == 255)
            image[i][j] = 0;
        else
            image[i][j] = 255-image[i][j];
    }
  }
}
// ___________________________________________________________________________________________________________________________________
void Rotate_Image(int A){
if (A == 1){
 for (int i = 0; i < SIZE; i++) {
    for (int j = 0; j< SIZE; j++) {
      image[i][j]=newimage[255-j][i];
    }
  }
}
else if (A == 2){
  for (int i = 0; i < SIZE; i++) {
    for (int j = 0; j< SIZE; j++) {
      swap(image[i][j],image[255-i][255-j]);
    }
   if ( i > 127)
   break;
  }
}

else if (A == 3){
 for (int i = 0; i < SIZE; i++) {
    for (int j = 0; j< SIZE; j++) {
      image[i][j]=newimage[255-j][i];
    }
  }
  for (int i = 0; i < SIZE; i++) {
    for (int j = 0; j< SIZE; j++) {
      swap(image[i][j],image[255-i][255-j]);
    }
   if ( i > 127)
   break;
  }
}
}
// ___________________________________________________________________________________________________________________________________
void flip_filter()
{
    int fliping_directoin;
    cout<<"please, choose (1)vertically fliping or (2)horizontally fliping: ";
    cin>>fliping_directoin;

    switch (fliping_directoin)
    {
    case (1):
        for (int i = 0; i < (SIZE)/2; i++) 
        {
            for (int j = 0; j< (SIZE); j++)
            {
                int tmp = image[SIZE - i][j] + image[i][j];
                image[i][j] = tmp - image[i][j];
                image[SIZE - i][j] = tmp - image[i][j];
            }
        }   
        break;

    case (2):
        for (int i = 0; i < SIZE; i++)
        {
            for (int j = 0; j < (SIZE)/2; j++)
            {
                int tmp = image[i][SIZE - j] + image[i][j];
                image[i][j] = tmp - image[i][j] ;
                image[i][SIZE - j] = tmp - image[i][j] ;

            }            
        }
        break;

    default: cout<<"wrong choice!"<<endl;
        break;
    }
}

// ___________________________________________________________________________________________________________________________________
void BW_filter()
{
    long average = 0;
    for (int i = 0; i < SIZE; i++) 
        {
            for (int j = 0; j< SIZE; j++)
                average += image[i][j];
        }
        
average /= (SIZE * SIZE);


    for (int i = 0; i < SIZE; i++) 
        {
            for (int j = 0; j< SIZE; j++)
            {
                if (image[i][j] > average)
                {
                    image[i][j] = 200;
                }

                else
                    image[i][j] = 0;
                
            }
        }   
}

// _____________________________________________________________________________________________________________________________________
void mirror_filter()
{
   int mirror_direction;
   cout<<"please, enter (1)Right 1/2 (2)Lift 1/2 (3)Upper 1/2 (4)Lower 1/2: ";
   cin>>mirror_direction;

   switch (mirror_direction)
   {
   case (1):
         for (int i = 0; i < SIZE; i++)
         {
            for (int j = 0; j < SIZE; j++)
            {
               image[i][j] = image[i][SIZE - 1 - j];
            }
         }   
      break;

   case (2):
         for (int i = 0; i < SIZE; i++)
         {
            for (int j = 0; j < SIZE; j++)
            {
               image[i][SIZE-1-j] = image[i][j];
            }
         }
      break;

   case (3):
         for (int i = 0; i < SIZE; i++)
         {
            for (int j = 0; j < SIZE; j++)
            {
               image[SIZE-1-i][j] = image[i][j];
            }      
         }
      break;

   case (4):
         for (int i = 0; i < SIZE; i++)
         {
            for (int j = 0; j < SIZE; j++)
            {
               image[i][j] = image[SIZE-1-i][j];
            }
         }
      break;

default: cout<<"wrong choice!"<<endl;
      break;
}
}
