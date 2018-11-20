def cATV(bin_list):
    def getStringVal(s):
        if s.startswith("0x"):
            return int(s[2:],base=16)
        elif s.startswith("0b"):
            return int(s[2:],base=2)
        else:
            return int(s,base=10)
    
    seg1=("0b"+bin_list[204]+bin_list[205]+bin_list[206]+bin_list[207]+bin_list[202]+bin_list[200]+bin_list[201])
    seg1=(str(getStringVal(seg1)))
    seg2=("0b"+bin_list[196]+bin_list[197]+bin_list[198]+bin_list[199]+bin_list[194]+bin_list[192]+bin_list[193])
    seg2=(str(getStringVal(seg2)))
    seg3=("0b"+bin_list[188]+bin_list[189]+bin_list[190]+bin_list[191]+bin_list[186]+bin_list[184]+bin_list[185])
    seg3=(str(getStringVal(seg3)))
    seg4=("0b"+bin_list[35]+bin_list[39]+bin_list[37]+bin_list[44]+bin_list[40]+bin_list[43]+bin_list[42]+bin_list[47]+bin_list[46]+bin_list[34]+bin_list[33]+bin_list[32]+bin_list[45]+bin_list[41])
    seg4=(str(getStringVal(seg4)))
    seg5=("0b"+bin_list[31]+bin_list[18]+bin_list[16]+bin_list[24]+bin_list[36]+bin_list[38]+bin_list[26]+bin_list[27]+bin_list[30]+bin_list[19]+bin_list[17]+bin_list[28]+bin_list[29]+bin_list[25])
    seg5=(str(getStringVal(seg5)))
    seg6=("0b"+bin_list[15]+bin_list[3]+bin_list[1]+bin_list[8]+bin_list[20]+bin_list[23]+bin_list[22]+bin_list[11]+bin_list[10]+bin_list[14]+bin_list[13]+bin_list[12]+bin_list[9]+bin_list[21])
    seg6=(str(getStringVal(seg6)))
    seg7=("0b"+bin_list[115]+bin_list[126]+bin_list[124]+bin_list[4]+bin_list[0]+bin_list[2]+bin_list[6]+bin_list[7]+bin_list[114]+bin_list[127]+bin_list[125]+bin_list[112]+bin_list[113]+bin_list[5])
    seg7=(str(getStringVal(seg7)))
    seg8=("0b"+bin_list[131]+bin_list[143]+bin_list[141]+bin_list[132]+bin_list[120]+bin_list[123]+bin_list[122]+bin_list[135]+bin_list[134]+bin_list[130]+bin_list[129]+bin_list[128]+bin_list[133]+bin_list[121])
    seg8=(str(getStringVal(seg8)))
    seg9=("0b"+bin_list[151]+bin_list[146]+bin_list[144]+bin_list[136]+bin_list[140]+bin_list[142]+bin_list[138]+bin_list[139]+bin_list[150]+bin_list[147]+bin_list[145]+bin_list[148]+bin_list[149]+bin_list[137])
    seg9=(str(getStringVal(seg9)))
    seg10=("0b"+bin_list[167]+bin_list[163]+bin_list[161]+bin_list[152]+bin_list[156]+bin_list[159]+bin_list[158]+bin_list[155]+bin_list[154]+bin_list[166]+bin_list[165]+bin_list[164]+bin_list[153]+bin_list[157])
    seg10=(str(getStringVal(seg10)))
    seg11=("0b"+bin_list[171]+bin_list[182]+bin_list[180]+bin_list[172]+bin_list[160]+bin_list[162]+bin_list[174]+bin_list[175]+bin_list[170]+bin_list[183]+bin_list[181]+bin_list[168]+bin_list[169]+bin_list[173])
    seg11=(str(getStringVal(seg11)))
    seg12=("0b"+bin_list[48]+bin_list[61]+bin_list[62]+bin_list[51]+bin_list[55]+bin_list[52]+bin_list[54]+bin_list[49]+bin_list[53]+bin_list[50])
    seg12=(str(getStringVal(seg12)+1)) #+1 ADDED TO MAKE ALL NUMBERS UNIQUE.
    seg13=("0b"+bin_list[64]+bin_list[77]+bin_list[79]+bin_list[67]+bin_list[66]+bin_list[65]+bin_list[78])
    seg13=(str(getStringVal(seg13)))
    seg14=("0b"+bin_list[72]+bin_list[85]+bin_list[87]+bin_list[75]+bin_list[74]+bin_list[73]+bin_list[86])
    seg14=(str(getStringVal(seg14)))
    seg15=("0b"+bin_list[80]+bin_list[93]+bin_list[95]+bin_list[83]+bin_list[82]+bin_list[81]+bin_list[94])
    seg15=(str(getStringVal(seg15)))
    seg16=("0b"+bin_list[88]+bin_list[101]+bin_list[103]+bin_list[91]+bin_list[90]+bin_list[89]+bin_list[102])
    seg16=(str(getStringVal(seg16)))
    seg17=("0b"+bin_list[187]+bin_list[176]+bin_list[195]+bin_list[177])
    seg17=(str(getStringVal(seg17)))
    csegment=(seg1,seg2,seg3,seg4,seg5,seg6,seg7,seg8,seg9,seg10,seg11,seg12,seg13,seg14,seg15,seg16,seg17)
    return csegment
def ATV(segment):
    
    segmentx=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
    iteration=0

    while iteration <17:
        #print (segment[iteration])
        if segment[iteration]== "126" or segment[iteration]=="16128":
            segmentx[iteration]= "0" #ALSO IS USED AS "O"
        elif segment[iteration]=="48" or segment[iteration]=="385" or segment[iteration]=="6144":
            segmentx[iteration]="1"
        elif segment[iteration]=="109" or segment[iteration]=="377" or segment[iteration]=="13960":
            segmentx[iteration]="2"
        elif segment[iteration]=="121" or segment[iteration]=="973" or segment[iteration]=="15496":
            segmentx[iteration]="3"
        elif segment[iteration]=="51" or segment[iteration]=="431" or segment[iteration]=="6536":
            segmentx[iteration]="4"
        elif segment[iteration]=="91" or segment[iteration]=="733" or segment[iteration]=="11656":
            segmentx[iteration]="5" #ALSO IS USED AS "S"
        elif segment[iteration]=="95" or segment[iteration]=="765" or segment[iteration]=="12168":
            segmentx[iteration]="6"
        elif segment[iteration]=="112" or segment[iteration]=="14336": 
            segmentx[iteration]="7"
        elif segment[iteration]=="127" or segment[iteration]=="16264": 
            segmentx[iteration]="8"
        elif segment[iteration]=="123" or segment[iteration]=="15752": 
            segmentx[iteration]="9"
        elif segment[iteration]=="13": 
            segmentx[iteration]="-"
        elif segment[iteration]=="16383": 
            segmentx[iteration]="#" #=ALL SEGMENTS ON
        elif segment[iteration]=="15240": 
            segmentx[iteration]="A" 
        elif segment[iteration]=="15402": 
            segmentx[iteration]="B" 
        elif segment[iteration]=="9984": 
            segmentx[iteration]="C"
        elif segment[iteration]=="15394": 
            segmentx[iteration]="D"
        elif segment[iteration]=="10120": 
            segmentx[iteration]="E"
        elif segment[iteration]=="9096": 
            segmentx[iteration]="F"
        elif segment[iteration]=="12040": 
            segmentx[iteration]="G"
        elif segment[iteration]=="445" or segment[iteration]=="7048": 
            segmentx[iteration]="H"
        elif segment[iteration]=="9250": 
            segmentx[iteration]="I"
        elif segment[iteration]=="7808": 
            segmentx[iteration]="J"
        elif segment[iteration]=="916": 
            segmentx[iteration]="K"
        elif segment[iteration]=="113" or segment[iteration]=="1792": 
            segmentx[iteration]="L"
        elif segment[iteration]=="6992": 
            segmentx[iteration]="M"
        elif segment[iteration]=="436" or segment[iteration]=="6980": 
            segmentx[iteration]="N"
        elif segment[iteration]=="829" or segment[iteration]=="13192": 
            segmentx[iteration]="P"
        elif segment[iteration]=="16132": 
            segmentx[iteration]="Q"
        elif segment[iteration]=="830" or segment[iteration]=="13196": 
            segmentx[iteration]="R"
        elif segment[iteration]=="8226": 
            segmentx[iteration]="T"
        elif segment[iteration]=="7936": 
            segmentx[iteration]="U"
        elif segment[iteration]=="785": 
            segmentx[iteration]="V"
        elif segment[iteration]=="434" or segment[iteration]=="6917": 
            segmentx[iteration]="W"
        elif segment[iteration]=="85": 
            segmentx[iteration]="X"
        elif segment[iteration]=="82": 
            segmentx[iteration]="Y"
        elif segment[iteration]=="9233": 
            segmentx[iteration]="Z"
        else:
            segmentx[iteration]=" "
        iteration=iteration+1
    #print (segmentx)
    return segmentx
def iATV(bin_list):    
    ind_segments=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8,8,8,8,8,8,8]
    ind_segments[0]=bin_list[203] #Phn Sig #1
    ind_segments[1]=bin_list[215] #Phn Sig #2
    ind_segments[2]=bin_list[211] #Phn Sig #3
    ind_segments[3]=bin_list[210] #Phn BT
    ind_segments[4]=bin_list[209] #Phn Message
    ind_segments[5]=bin_list[214] #Phn Call

    ind_segments[6]=bin_list[208] #Upper kmh
    ind_segments[7]=bin_list[212] #Upper mph
    ind_segments[8]=bin_list[213] #Upper rpm
    ind_segments[9]=bin_list[178] #Upper ambient sym
    ind_segments[10]=bin_list[179] #Upper engine temp sym
    ind_segments[11]=bin_list[116] #Upper degree sym

    ind_segments[12]=bin_list[117] #mid "."
    ind_segments[13]=bin_list[57] #mid ":" #1
    ind_segments[14]=bin_list[56] #mid ":" #2

    ind_segments[15]=bin_list[60] #mid rpm
    ind_segments[16]=bin_list[70] #mid speed
    ind_segments[17]=bin_list[69] #mid time
    ind_segments[18]=bin_list[68] #mid range
    ind_segments[19]=bin_list[76] #mid L/100
    ind_segments[20]=bin_list[100] #mid km
    ind_segments[21]=bin_list[96] #mid mi
    ind_segments[22]=bin_list[97] #mid /h
    ind_segments[23]=bin_list[119] #mid /gal

    ind_segments[24]=bin_list[59] #drive 1
    ind_segments[25]=bin_list[63] #drive 2
    ind_segments[26]=bin_list[58] #drive 4
    ind_segments[27]=bin_list[59] #hill

    ind_segments[28]=bin_list[84] # lower ":"
    ind_segments[29]=bin_list[92] # lower "."
    ind_segments[30]=bin_list[98] # wrench
    ind_segments[31]=bin_list[99] # timer

    ind_segments[32]=bin_list[118] #Fuel main
    ind_segments[33]=bin_list[111] #Fuel 1/8
    ind_segments[34]=bin_list[107] #Fuel 2/8
    ind_segments[35]=bin_list[110] #Fuel 3/8
    ind_segments[36]=bin_list[106] #Fuel 4/8
    ind_segments[37]=bin_list[108] #Fuel 5/8
    ind_segments[38]=bin_list[104] #Fuel 6/8
    ind_segments[39]=bin_list[109] #Fuel 7/8
    ind_segments[40]=bin_list[105] #Fuel 8/8
    
    return ind_segments








































    

    
        
