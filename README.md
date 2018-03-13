#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <string.h>
#include <windows.h>
#include "conio2.h"
#include <ctype.h>
#include "LabjackUD.h"
#include "LJUD_DynamicLinking.h"


void CONSOLECOLORS(int ForgC, int BackC);
void GoToXY(int column, int line)
{
    COORD coord;
    coord.X = column;
    coord.Y = line;
    HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);

    if (!SetConsoleCursorPosition(hConsole, coord))
		printf ("ERROR IN XY!");
}



void ErrorHandler (LJ_ERROR ljError, long lngLineNumber)
{
    char  err[255];
    if  (ljError  !=  LJE_NOERROR)
    {
        ErrorToString(ljError,  err);
        printf("Error  #  %ld:  %s\n",  ljError,  err);
        printf("Source  line  number  =  %ld\n",lngLineNumber);
        if(ljError  >  LJE_MIN_GROUP_ERROR)
        {
            getchar();
            exit(0);    //  Quit  if  serious  error
        }
    }
}



//void CONSOLECOLORS(int ForgC, int BackC);
//void GOTOXY( int x, int y );


int main()
{
LJ_ERROR ljError; // LabJack error code
LJ_HANDLE ljHandle = 0; // ID# assigned to the opened LabJack
LoadLabJackUD(); // Load the LabJack DLL
// Open the first found LabJack U3
ljError = OpenLabJack (LJ_dtU3, LJ_ctUSB, "1", 1, &ljHandle);
ErrorHandler(ljError, __LINE__);
// Set all pin assignments to the factory default condition
ljError = ePut(ljHandle, LJ_ioPIN_CONFIGURATION_RESET, 0, 0, 0);
ErrorHandler(ljError, __LINE__);
//int ReadVal; // FIO values
double ReadVal; // FIO values

ljError = ePut(ljHandle, LJ_ioPUT_ANALOG_ENABLE_PORT, 0, 65535, 16);
ErrorHandler(ljError, __LINE__);




	{
    int asd=1;
    while (asd>0)

    {
    FILE *fp;
    char buff[255];

    fp = fopen("LCDData.txt", "r");
    fgets(buff, 255, (FILE*)fp);
    //printf("2: %s\n", buff );
    fclose(fp);






        //char lcdinput[]="80 00 08 00 40 A1 8F 91 42 10 00 B0 DE 83 05 00 70 BE 50 05 07 60 A1 1A 84 10 10 10 35";
        char lcdinput[255];
        strcpy (lcdinput, buff);


        if (lcdinput[6]>47)
          {




        int c[256];
        int lcdbinaryit=0;
        int lcdinputit=9;
        int repeatcount=0;
        while (repeatcount<27)

        {
            int internalrepeat=0;

            while (internalrepeat<2)
            {
               // printf("Xx= %d \n", lcdbinaryit);
              //  printf("Zz= %d \n", lcdinputit );
              //  printf("Yy= %d \n", internalrepeat );
              //  printf ("lcdin= %d\n\n", lcdinput[lcdinputit]);


               // printf("lcdinput= %d\n", lcdinput[lcdinputit] );


                if (lcdinput[lcdinputit]==48)
                    {c[lcdbinaryit+0]=0;
                    c[lcdbinaryit+1]=0;
                    c[lcdbinaryit+2]=0;
                    c[lcdbinaryit+3]=0;}

                if (lcdinput[lcdinputit]==49)
                    {c[lcdbinaryit+0]=0;
                    c[lcdbinaryit+1]=0;
                    c[lcdbinaryit+2]=0;
                    c[lcdbinaryit+3]=1;}

                if (lcdinput[lcdinputit]==50)
                    {c[lcdbinaryit+0]=0;
                    c[lcdbinaryit+1]=0;
                    c[lcdbinaryit+2]=1;
                    c[lcdbinaryit+3]=0;}

                if (lcdinput[lcdinputit]==51)
                    {c[lcdbinaryit+0]=0;
                    c[lcdbinaryit+1]=0;
                    c[lcdbinaryit+2]=1;
                    c[lcdbinaryit+3]=1;}

                if (lcdinput[lcdinputit]==52)


                    {c[lcdbinaryit+0]=0;
                    c[lcdbinaryit+1]=1;
                    c[lcdbinaryit+2]=0;
                    c[lcdbinaryit+3]=0;}

                if (lcdinput[lcdinputit]==53)
                    {c[lcdbinaryit+0]=0;
                    c[lcdbinaryit+1]=1;
                    c[lcdbinaryit+2]=0;
                    c[lcdbinaryit+3]=1;}


                if (lcdinput[lcdinputit]==54)
                    {c[lcdbinaryit+0]=0;
                    c[lcdbinaryit+1]=1;
                    c[lcdbinaryit+2]=1;
                    c[lcdbinaryit+3]=0;}

                if (lcdinput[lcdinputit]==55)
                    {c[lcdbinaryit+0]=0;
                    c[lcdbinaryit+1]=1;
                    c[lcdbinaryit+2]=1;
                    c[lcdbinaryit+3]=1;}

                if (lcdinput[lcdinputit]==56)
                    {c[lcdbinaryit+0]=1;
                    c[lcdbinaryit+1]=0;
                    c[lcdbinaryit+2]=0;
                    c[lcdbinaryit+3]=0;}

                if (lcdinput[lcdinputit]==57)
                    {c[lcdbinaryit+0]=1;
                    c[lcdbinaryit+1]=0;
                    c[lcdbinaryit+2]=0;
                    c[lcdbinaryit+3]=1;}

                if (lcdinput[lcdinputit]==65 || lcdinput[lcdinputit]==97)
                    {c[lcdbinaryit+0]=1;
                    c[lcdbinaryit+1]=0;
                    c[lcdbinaryit+2]=1;
                    c[lcdbinaryit+3]=0;}

                if (lcdinput[lcdinputit]==66 || lcdinput[lcdinputit]==98)
                    {c[lcdbinaryit+0]=1;
                    c[lcdbinaryit+1]=0;
                    c[lcdbinaryit+2]=1;
                    c[lcdbinaryit+3]=1;}

                if (lcdinput[lcdinputit]==67 || lcdinput[lcdinputit]==99)
                    {c[lcdbinaryit+0]=1;
                    c[lcdbinaryit+1]=1;
                    c[lcdbinaryit+2]=0;
                    c[lcdbinaryit+3]=0;}

                if (lcdinput[lcdinputit]==68 || lcdinput[lcdinputit]==100)
                    {c[lcdbinaryit+0]=1;
                    c[lcdbinaryit+1]=1;
                    c[lcdbinaryit+2]=0;
                    c[lcdbinaryit+3]=1;}

                if (lcdinput[lcdinputit]==69 || lcdinput[lcdinputit]==101)
                    {c[lcdbinaryit+0]=1;
                    c[lcdbinaryit+1]=1;
                    c[lcdbinaryit+2]=1;
                    c[lcdbinaryit+3]=0;}

                if (lcdinput[lcdinputit]==70 || lcdinput[lcdinputit]==102)
                    {c[lcdbinaryit+0]=1;
                    c[lcdbinaryit+1]=1;
                    c[lcdbinaryit+2]=1;
                    c[lcdbinaryit+3]=1;}

              //  printf("LCD=%d", c[lcdbinaryit+0]);
              //  printf("%d", c[lcdbinaryit+1]);
              //  printf("%d", c[lcdbinaryit+2]);
               // printf("%d", c[lcdbinaryit+3]);
                //printf("\n");


                lcdbinaryit=lcdbinaryit+4;
                lcdinputit++;
                internalrepeat++;

               // printf("X= %d \n", lcdbinaryit);
               // printf("z= %d \n", lcdinputit );
                //printf("y= %d \n", internalrepeat );

                //printf("\n");

            }
            internalrepeat=0;
            lcdinputit++;
            repeatcount++;
        }

    int new[17];
    new[1]=(c[204]+(c[205]*2)+(c[206]*4)+(c[207]*8)+(c[202]*16)+(c[200]*32)+(c[201]*64));
    new[2]=(c[196]+(c[197]*2)+(c[198]*4)+(c[199]*8)+(c[194]*16)+(c[192]*32)+(c[193]*64));
    new[3]=(c[188]+(c[189]*2)+(c[190]*4)+(c[191]*8)+(c[186]*16)+(c[184]*32)+(c[185]*64));
    new[4]=(c[35]+(c[39]*2)+(c[37]*4)+(c[44]*8)+(c[40]*16)+(c[43]*32)+(c[42]*64)+(c[47]*128)+(c[46]*256)+(c[34]*512)+(c[33]*1024)+(c[32]*2048)+(c[45]*4096)+(c[41]*8192));
    new[5]=(c[31]+(c[18]*2)+(c[16]*4)+(c[24]*8)+(c[36]*16)+(c[38]*32)+(c[26]*64)+(c[27]*128)+(c[30]*256)+(c[19]*512)+(c[17]*1024)+(c[28]*2048)+(c[29]*4096)+(c[25]*8192));
    new[6]=(c[15]+(c[3]*2)+(c[1]*4)+(c[8]*8)+(c[20]*16)+(c[23]*32)+(c[22]*64)+(c[11]*128)+(c[10]*256)+(c[14]*512)+(c[13]*1024)+(c[12]*2048)+(c[9]*4096)+(c[21]*8192));
    new[7]=(c[115]+(c[126]*2)+(c[124]*4)+(c[4]*8)+(c[0]*16)+(c[2]*32)+(c[6]*64)+(c[7]*128)+(c[114]*256)+(c[127]*512)+(c[125]*1024)+(c[112]*2048)+(c[113]*4096)+(c[5]*8192));
    new[8]=(c[131]+(c[143]*2)+(c[141]*4)+(c[132]*8)+(c[120]*16)+(c[123]*32)+(c[122]*64)+(c[135]*128)+(c[134]*256)+(c[130]*512)+(c[129]*1024)+(c[128]*2048)+(c[133]*4096)+(c[121]*8192));
    new[9]=(c[151]+(c[146]*2)+(c[144]*4)+(c[136]*8)+(c[140]*16)+(c[142]*32)+(c[138]*64)+(c[139]*128)+(c[150]*256)+(c[147]*512)+(c[145]*1024)+(c[148]*2048)+(c[149]*4096)+(c[137]*8192));
    new[10]=(c[167]+(c[163]*2)+(c[161]*4)+(c[152]*8)+(c[156]*16)+(c[159]*32)+(c[158]*64)+(c[155]*128)+(c[154]*256)+(c[166]*512)+(c[165]*1024)+(c[164]*2048)+(c[153]*4096)+(c[157]*8192));
    new[11]=(c[171]+(c[182]*2)+(c[180]*4)+(c[172]*8)+(c[160]*16)+(c[162]*32)+(c[174]*64)+(c[175]*128)+(c[170]*256)+(c[183]*512)+(c[181]*1024)+(c[168]*2048)+(c[169]*4096)+(c[173]*8192));
    new[12]=(c[48]+(c[61]*2)+(c[62]*4)+(c[51]*8)+(c[55]*16)+(c[52]*32)+(c[54]*64)+(c[49]*128)+(c[53]*256)+(c[50]*512));
    new[13]=(c[64]+(c[77]*2)+(c[79]*4)+(c[67]*8)+(c[66]*16)+(c[65]*32)+(c[78]*64));
    new[14]=(c[72]+(c[85]*2)+(c[87]*4)+(c[75]*8)+(c[74]*16)+(c[73]*32)+(c[86]*64));
    new[15]=(c[80]+(c[93]*2)+(c[95]*4)+(c[83]*8)+(c[82]*16)+(c[81]*32)+(c[94]*64));
    new[16]=(c[88]+(c[101]*2)+(c[103]*4)+(c[91]*8)+(c[90]*16)+(c[89]*32)+(c[102]*64));
    new[17]=(c[187]+(c[176]*2)+(c[195]*4)+(c[177]*8));




    char alpha[35];

    //printf("3 bin=  %d%d%d%d%d%d%d\n",c[188],c[189],c[190],c[191],c[186],c[184],c[185]);

    //printf("1= %d\n",new[1]);
    //printf("2= %d\n",new[2]);
    //printf("3= %d\n",new[3]);
    //printf("4= %d\n",new[4]);
    //printf("4 bin=  %d%d%d%d%d%d%d%d%d%d%d%d%d%d\n",c[35],c[39],c[37],c[44],c[40],c[43],c[42],c[47],c[46],c[34],c[33],c[32],c[45],c[41]);
    //printf("5= %d\n",new[5]);
    //printf("6= %d\n",new[6]);
    //printf("7= %d\n",new[7]);
    //printf("8= %d\n",new[8]);
    //printf("9= %d\n",new[9]);
    //printf("10= %d\n",new[10]);
    //printf("11= %d\n",new[11]);
    //printf("12= %d\n",new[12]);
    //printf("12 bin=  %d%d%d%d%d%d%d%d%d%d\n",c[48],c[61],c[62],c[51],c[55],c[52],c[54],c[49],c[53],c[50]);
    //printf("13= %d\n",new[13]);
    //printf("14= %d\n",new[14]);
    //printf("15= %d\n",new[15]);
    //printf("16= %d\n",new[16]);
    //printf("17= %d\n",new[17]);

    int zed=1;
    while (zed<=17)
    {
        //printf ("new%d %d   ",zed, new[zed]);
        if (new[zed]==6)
            alpha[zed]='1';
        else if (new[zed]==7)
            alpha[zed]='7';
        else if (new[zed]==30)
            alpha[zed]='J';
        else if (new[zed]==56)
            alpha[zed]='L';
        else if (new[zed]==57)
            alpha[zed]='C';
        else if (new[zed]==62)
            alpha[zed]='U';
        else if (new[zed]==63)
            alpha[zed]='0';//IS ALSO O
        else if (new[zed]==192)
            alpha[zed]='-';
        //else if (new[zed]==8752)
            //alpha[zed]='V';
        else if (new[zed]==694)
            alpha[zed]='M';
        else if (new[zed]==1085)
            alpha[zed]='G';
        else if ((new[zed]==1103) || (new[zed]==79) || (new[zed]==207))
            alpha[zed]='3';
        else if ((new[zed]==1115) || (new[zed]==91)  || (new[zed]==219))
            alpha[zed]='2';
        else if ((new[zed]==1123) || (new[zed]==99))
            alpha[zed]='d';//Degrees
        else if ((new[zed]==1126) || (new[zed]==102) || (new[zed]==230))
            alpha[zed]='4';
        else if ((new[zed]==1135) || (new[zed]==111)) //1127
            alpha[zed]='9';
        else if ((new[zed]==1133) || (new[zed]==109) || (new[zed]==237))
            alpha[zed]='5';// IS ALSO S
        else if ((new[zed]==1137) || (new[zed]==113))
            alpha[zed]='F';
        else if ((new[zed]==1139) || (new[zed]==115) || (new[zed]==243))
            alpha[zed]='P';
        else if ((new[zed]==1142) || (new[zed]==118) || (new[zed]==246))
            alpha[zed]='H';
        else if ((new[zed]==1143) || (new[zed]==119))
            alpha[zed]='A';
        else if ((new[zed]==1145) || (new[zed]==121))
            alpha[zed]='E';
        else if ((new[zed]==1149) || (new[zed]==125) || (new[zed]==253))
            alpha[zed]='6';
        else if ((new[zed]==1151) || (new[zed]==127) || (new[zed]==15))
            alpha[zed]='8';
        else if (new[zed]==2111)
            alpha[zed]='Q';
        else if ((new[zed]==3187) || (new[zed]==755))
            alpha[zed]='R';
        else if ((new[zed]==2230) || (new[zed]==822))
            alpha[zed]='N';
        else if (new[zed]==2672)
            alpha[zed]='K';
        else if (new[zed]==4353)
            alpha[zed]='T';
        else if (new[zed]==4361)
            alpha[zed]='I';
        else if (new[zed]==4367)
            alpha[zed]='D';
        else if (new[zed]==4736)
            alpha[zed]='Y';
        else if (new[zed]==7951)
            alpha[zed]='B';
        else if (new[zed]==8713)
            alpha[zed]='Z';
        else if (new[zed]==8752)
            alpha[zed]='V';
        else if ((new[zed]==10294) || (new[zed]==566))
            alpha[zed]='W';
        else if (new[zed]==10880)
            alpha[zed]='X';
        else if (new[zed]==0)
            alpha[zed]=' ';
        else
            alpha[zed]= new[zed];

        //printf ("%c    ",alpha[zed]);
        zed++;
    }

        if (new[17]==7)
            alpha[17]='0';
        if (new[17]==9)
            alpha[17]='F';
        if (new[17]==5)
            alpha[17]='C';
    //int VV=256;//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    c[256]=0;//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    //****************************************************************
    printf("\n\n    ");//phone data block
    if (c[203]==1)
        printf("S0 ");
    else
        printf("   ");
    if (c[215]==1)
        printf("S1 ");
    else
        printf("   ");
    if (c[211]==1)
        printf("S2 ");
    else
        printf("   ");
    if (c[210]==1)
        printf("BT ");
    else
        printf("   ");
    if (c[209]==1)
        printf("MG ");
    else
        printf("   ");
    if (c[214]==1)
        printf("PH \n\n");
    else
        printf("   \n\n");
    //********************************************************************
    if (c[208]==1)
        printf("    KMH");
    else
        printf("       ");
    if (c[212]==1)
        printf(" MPH");
    else
        printf("    ");
    if (c[213]==1)
        printf(" RPM");
    else
        printf("    ");
    printf (" %c",alpha[1]);//1
    printf ("%c",alpha[2]);//2
    printf ("%c",alpha[3]);//3
    printf ("%c",alpha[17]);//17
    if (c[178]==1)
        printf(" AM");
    else
        printf("   ");
    if (c[179]==1)
        printf(" ET");
    else
        printf("   ");
    if (c[116]==1)
        printf(" DG");
    else
        printf("   ");
    printf("\n\n");

    //******************************************************************

    printf ("    %c",alpha[4]);//4
    printf ("%c",alpha[5]);//5
    printf ("%c",alpha[6]);//6
    printf ("%c",alpha[7]);//7
    printf ("%c",alpha[8]);//8
    printf ("%c",alpha[9]);//9
    printf ("%c",alpha[10]);//10
    printf ("%c",alpha[11]);//11

    if (c[117]==1)
        printf(" D.1");
    else
        printf("    ");
    if (c[57]==1)
        printf(" C:1");
    else
        printf("    ");
    if (c[56]==1)
        printf(" C:2");
    else
        printf("    ");

    printf("\n\n");
    //********************************************************************

    printf("    ");
    if (c[60]==1)
        printf("RPM ");
    else
        printf("    ");
    if (c[70]==1)
        printf("SPD ");
    else
        printf("    ");
    if (c[69]==1)
        printf("TIM ");
    else
        printf("    ");
    if (c[68]==1)
        printf("RNG ");
    else
        printf("    ");
    if (c[76]==1)
        printf("L/1 ");
    else
        printf("    ");
    if (c[100]==1)
        printf("KM ");
    else
        printf("   ");
    if (c[96]==1)
        printf("MI ");
    else
        printf("   ");
    if (c[97]==1)
        printf("/H ");
    else
        printf("   ");
    if (c[119]==1)
        printf("GAL ");
    else
        printf("    ");
    printf("\n\n");
    //********************************************************************

    printf ("    %c ",alpha[12]);//12
    if (c[59]==1)
        printf("DR1 ");
    else
        printf("    ");
    if (c[63]==1)
        printf("DR2 ");
    else
        printf("    ");
    if (c[58]==1)
        printf("DR3 ");
    else
        printf("    ");
    if (c[71]==1)
        printf("HL ");
    else
        printf("   ");
    printf ("%c",alpha[13]);//13
    printf ("%c",alpha[14]);//14
    printf ("%c",alpha[15]);//15
    printf ("%c ",alpha[16]);//16
    if (c[84]==1)
        printf("C:3 ");
    else if (c[92]==1)
        printf("D:0  ");
    else
        printf("    ");
    if (c[98]==1)
        printf("WRN ");
    else
        printf("    ");
    if (c[99]==1)
        printf("TMR ");
    else
        printf("    ");
    printf("\n\n");
    //****************************************************
    if (c[118]==1)
        printf("    FUEL ");
    else
        printf("         ");
    if (c[111]==1)
        printf("T8 ");
    else
        printf("   ");
    if (c[107]==1)
        printf("T7 ");
    else
        printf("   ");
    if (c[110]==1)
        printf("T6 ");
    else
        printf("   ");
    if (c[106]==1)
        printf("T5 ");
    else
        printf("   ");
    if (c[108]==1)
        printf("T4 ");
    else
        printf("   ");
    if (c[104]==1)
        printf("T3 ");
    else
        printf("   ");
    if (c[109]==1)
        printf("T2 ");
    else
        printf("   ");
    if (c[105]==1)
        printf("T1 ");
    else
        printf("   ");

	printf("\n\n");

    ReadVal=0;
    ljError = eGet (ljHandle, LJ_ioGET_AIN, 0, &ReadVal, 0);
    //printf ("1= %g ",ReadVal);

    if (ReadVal<1)
        printf("  1= OFF  \n");
    else if
        (ReadVal<1)
        printf("  1= LOW  \n");
    else
        printf("  1= HIGH \n");


	ljError = eGet (ljHandle, LJ_ioGET_AIN, 1, &ReadVal, 0);
	//printf ("2= %g ",ReadVal);
	if (ReadVal<1)
        printf("  2= OFF \n");
    else if
        (ReadVal<1)
        printf("2= LOW  \n");
    else
        printf("  2= HIGH \n");
	ljError = eGet (ljHandle, LJ_ioGET_AIN, 2, &ReadVal, 0);
	//printf ("3= %g ",ReadVal);
	if (ReadVal<1)
        printf("  3= OFF  \n");
    else if
        (ReadVal<1)
        printf("3= LOW  \n");
    else
        printf("  3= HIGH \n");
	ljError = eGet (ljHandle, LJ_ioGET_AIN, 3, &ReadVal, 0);
	//printf ("4= %g ",ReadVal);
	if (ReadVal<1)
        printf("  4= OFF  \n");
    else if
        (ReadVal<1)
        printf("4= LOW  \n");
    else
        printf("  4= HIGH \n");
	ljError = eGet (ljHandle, LJ_ioGET_AIN, 4, &ReadVal, 0);
	//printf ("5= %g ",ReadVal);
	if (ReadVal<1)
        printf("  5= OFF  \n");
    else if
        (ReadVal<1)
        printf("5= LOW  \n");
    else
        printf("  5= HIGH \n");

	ljError = eGet (ljHandle, LJ_ioGET_AIN, 5, &ReadVal, 0);
	//printf ("6= %g ",ReadVal);
	if (ReadVal<1)
        printf("  6= OFF \n");
    else if
        (ReadVal<1)
        printf("6= LOW  \n");
    else
        printf("  6= HIGH \n");

	ljError = eGet (ljHandle, LJ_ioGET_AIN, 6, &ReadVal, 0);
	//printf ("7= %g ",ReadVal);
	if (ReadVal<1)
        printf("  7= OFF \n");
    else if
        (ReadVal<1)
        printf("7= LOW  \n");
    else
        printf("  7= HIGH \n");
	ljError = eGet (ljHandle, LJ_ioGET_AIN, 7, &ReadVal, 0);
	//printf ("8= %g ",ReadVal);
	if (ReadVal<1)
        printf("  8= OFF \n");
    else if
        (ReadVal<1)
        printf("8= LOW  \n");
    else
        printf("  8= HIGH \n");
	ljError = eGet (ljHandle, LJ_ioGET_AIN, 8, &ReadVal, 0);
	//printf ("9= %g ",ReadVal);
	if (ReadVal<1)
        printf("  9= OFF \n");
    else if
        (ReadVal<1)
        printf("9= LOW  \n");
    else
        printf("  9= HIGH \n");
	ljError = eGet (ljHandle, LJ_ioGET_AIN, 9, &ReadVal, 0);
	//printf ("10= %g ",ReadVal);
	if (ReadVal<1)
        printf("  10= OFF \n");
    else if
        (ReadVal<1)
        printf("10= LOW  \n");
    else
        printf("  10= HIGH \n");

    printf("\n\n\n\n");


          }
    asd++;
    Sleep(50);   //300
    //printf ("ASD====== %d\n",asd);
    //system("cls");
    GoToXY(0, 130);
    }
    return 0;
}
}
