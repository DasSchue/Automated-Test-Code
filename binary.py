import ATV #decodes ATV LCD
import Snow
import Sling
import os

def getStringVal(s):   #Miller's code to auto determine int base (2, 10, 16)
    if s.startswith("0x"):
        return int(s[2:],base=16)
    elif s.startswith("0b"):
        try:
            return int(s[2:],base=2)
        except:
            return (0)
    else:
        return int(s,base=10)
 
lcd_type_selected=0

while lcd_type_selected==0:
    print ("Enter LCD type: ATV, Snow, Sling")
    lcd_select= input()
    lcd_select=lcd_select.lower()
    if lcd_select[0:2] == "at":
        lcd_type="ATV"
        lcd_type_selected=1
        print ("ATV Selected")
    elif lcd_select[0:2]== "sn":
        lcd_type="Snow"
        lcd_type_selected=1
        print ("Snow Selected")
    elif lcd_select[0:2]== "sl":
        lcd_type="Sling"
        lcd_type_selected=1
        print ("Sling Selected")

x=0
y=0
prev_raw_number=""

while x<1000000000000000:
    f=open("E:\i2c_code_python\Python\LCDData.txt","r+") #location of LCD Reader program output file
    new_raw_number=f.read()
    f.close

    if new_raw_number=="000000000000000000000000000000000000000000000000000000000": #default when there is no LCD output
        if y==3000:  #timer to gloss over short interuptions
            os.system('cls')
            print ("\n\n\n\n\n\nUNIT IS OFF")
            file=open("display.txt","w")
            file.write ("UNIT IS OFF\n")
            file.close()
            y=0
        else:
            y=y+1
    elif new_raw_number==prev_raw_number: #does nothing if the data has not changed, saves refresh
        x=x+1
        y=0
        continue
    else:
        raw_number=new_raw_number.replace(" ", "") #remove spaces
        y=0
        if len(raw_number) >20: #selects only LCD i2c traffic, converts to base 10 then binary
            raw_number=(raw_number[6:]) 
            raw_number='0x' + raw_number 
            dec_number=getStringVal(raw_number)
            bin_number=(bin(dec_number))
            the_binary_list=list(bin_number)
            bin_list=the_binary_list[2:]

            while len(bin_list)<216:  #not sure why I did this......
                bin_list.insert(0,"0")

            segment=0

            if lcd_type=="ATV":
                segment=ATV.cATV(bin_list)
                characters=ATV.ATV(segment)
                icons=ATV.iATV(bin_list)
            elif lcd_type=="SNO":
                segment=SNO.cSNO(bin_list)
                characters=SNO.SNO(segment)
            elif lcd_type=="SLG":
                segment=SLG.cSLG(bin_list)
                characters=SLG.SLG(segment)

            os.system('cls')

            phone_row= ("  "+icons[0]+icons[3]+icons[4]+icons[5])
            upper_icon_row= (icons[6]+icons[7]+icons[8]+icons[9]+icons[10]+icons[11])

            #phone_row= ("  ")
            upper_row= (characters[0]+characters[1]+characters[2]+characters[16]+icons[11]+icons[9]+icons[6]+icons[7]+icons[8]+icons[10])
            middle_row= (characters[3]+characters[4]+characters[5]+characters[6]+icons[13]+characters[7]+characters[8]+icons[14]+characters[9]+icons[12]+characters[10]+icons[15]+icons[16]+icons[17]+icons[18]+icons[19]+icons[20]+icons[21]+icons[22]+icons[23])
            lower_row= (characters[11]+" "+icons[24]+" "+characters[12]+characters[13]+icons[28]+characters[14]+icons[29]+characters[15]+" "+icons[31]+" "+icons[30])
            fuel_row= (icons[32]+icons[33]+icons[34]+icons[35]+icons[36]+icons[37]+icons[38]+icons[39]+icons[40])
           
            print (phone_row)
            #print ("")
            print (upper_icon_row)
            print (upper_row)
            print (middle_row)
            print (lower_row)
            print (fuel_row)
            #print (segment[9])
            #print (icons)

            file=open("display.txt","w")
            file.write (phone_row+"\n")
            file.write (upper_row+"\n")
            file.write (middle_row+"\n")
            file.write (lower_row+"\n")
            file.write (fuel_row)
            file.close()
            
            prev_raw_number=new_raw_number
            x=x+1    
            if x==250:
                os.system('cls')
                x=0






        



