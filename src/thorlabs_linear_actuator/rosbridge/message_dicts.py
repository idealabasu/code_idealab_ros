# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 16:38:27 2020

@author: danaukes
"""

class DictClass(object):
    def __init__(self, dict1):
        for key,value in dict1.items():
            setattr(self,key,value)


import message_sets as ms
#Introduction
msg_general = {}
msg_general['MOD_IDENTIFY'] =  0x0223
msg_general['MOD_SET_CHANENABLESTATE'] =  0x0210
msg_general['MOD_REQ_CHANENABLESTATE'] =  0x0211
msg_general['MOD_GET_CHANENABLESTATE'] =  0x0212
msg_general['HW_DISCONNECT'] =  0x0002
msg_general['HW_RESPONSE'] =  0x0080
msg_general['HW_RICHRESPONSE'] =  0x0081
msg_general['HW_START_UPDATEMSGS'] =  0x0011
msg_general['HW_STOP_UPDATEMSGS'] =  0x0012
msg_general['HW_REQ_INFO'] =  0x0005
msg_general['HW_GET_INFO'] =  0x0006
msg_general['RACK_REQ_BAYUSED'] =  0x0060
msg_general['RACK_GET_BAYUSED'] =  0x0061
msg_general['HUB_REQ_BAYUSED'] =  0x0065
msg_general['HUB_GET_BAYUSED'] =  0x0066
msg_general['RACK_REQ_STATUSBITS'] =  0x0226
msg_general['RACK_GET_STATUSBITS'] =  0x0227
msg_general['RACK_SET_DIGOUTPUTS'] =  0x0228
msg_general['RACK_REQ_DIGOUTPUTS'] =  0x0229
msg_general['RACK_GET_DIGOUTPUTS'] =  0x0230
msg_general['MOD_SET_DIGOUTPUTS'] =  0x0213
msg_general['MOD_REQ_DIGOUTPUTS'] =  0x0214
msg_general['MOD_GET_DIGOUTPUTS'] =  0x0215

#Motor Control Messages
msg_control = {}
msg_control['HW_YES_FLASH_PROGRAMMING'] =  0x0017
msg_control['HW_NO_FLASH_PROGRAMMING'] =  0x0018
msg_control['MOT_SET_POSCOUNTER'] =  0x0410
msg_control['MOT_REQ_POSCOUNTER'] =  0x0411
msg_control['MOT_GET_POSCOUNTER'] =  0x0412
msg_control['MOT_SET_ENCCOUNTER'] =  0x0409
msg_control['MOT_REQ_ENCCOUNTER'] =  0x040A
msg_control['MOT_GET_ENCCOUNTER'] =  0x040B
msg_control['MOT_SET_VELPARAMS'] =  0x0413
msg_control['MOT_REQ_VELPARAMS'] =  0x0414
msg_control['MOT_GET_VELPARAMS'] =  0x0415
msg_control['MOT_SET_JOGPARAMS'] =  0x0416
msg_control['MOT_REQ_JOGPARAMS'] =  0x0417
msg_control['MOT_GET_JOGPARAMS'] =  0x0418
msg_control['MOT_REQ_ADCINPUTS'] =  0x042B
msg_control['MOT_GET_ADCINPUTS'] =  0x042C
msg_control['MOT_SET_POWERPARAMS'] =  0x0426
msg_control['MOT_REQ_POWERPARAMS'] =  0x0427
msg_control['MOT_GET_POWERPARAMS'] =  0x0428
msg_control['MOT_SET_GENMOVEPARAMS'] =  0x043A
msg_control['MOT_REQ_GENMOVEPARAMS'] =  0x043B
msg_control['MOT_GET_GENMOVEPARAMS'] =  0x043C
msg_control['MOT_SET_MOVERELPARAMS'] =  0x0445
msg_control['MOT_REQ_MOVERELPARAMS'] =  0x0446
msg_control['MOT_GET_MOVERELPARAMS'] =  0x0447
msg_control['MOT_SET_MOVEABSPARAMS'] =  0x0450
msg_control['MOT_REQ_MOVEABSPARAMS'] =  0x0451
msg_control['MOT_GET_MOVEABSPARAMS'] =  0x0452
msg_control['MOT_SET_HOMEPARAMS'] =  0x0440
msg_control['MOT_REQ_HOMEPARAMS'] =  0x0441
msg_control['MOT_GET_HOMEPARAMS'] =  0x0442
msg_control['MOT_SET_LIMSWITCHPARAMS'] =  0x0423
msg_control['MOT_REQ_LIMSWITCHPARAMS'] =  0x0424
msg_control['MOT_GET_LIMSWITCHPARAMS'] =  0x0425
msg_control['MOT_MOVE_HOME'] =  0x0443
msg_control['MOT_MOVE_HOMED'] =  0x0444
msg_control['MOT_MOVE_RELATIVE'] =  0x0448
msg_control['MOT_MOVE_COMPLETED'] =  0x0464
msg_control['MOT_MOVE_ABSOLUTE'] =  0x0453
msg_control['MOT_MOVE_JOG'] =  0x046A
msg_control['MOT_MOVE_VELOCITY'] =  0x0457
msg_control['MOT_MOVE_STOP'] =  0x0465
msg_control['MOT_MOVE_STOPPED'] =  0x0466
msg_control['MOT_SET_BOWINDEX'] =  0x04F4
msg_control['MOT_REQ_BOWINDEX'] =  0x04F5
msg_control['MOT_GET_BOWINDEX'] =  0x04F6
msg_control['MOT_SET_DCPIDPARAMS'] =  0x04A0
msg_control['MOT_REQ_DCPIDPARAMS'] =  0x04A1
msg_control['MOT_GET_DCPIDPARAMS'] =  0x04A2
msg_control['MOT_SET_AVMODES'] =  0x04B3
msg_control['MOT_REQ_AVMODES'] =  0x04B4
msg_control['MOT_GET_AVMODES'] =  0x04B5
msg_control['MOT_SET_POTPARAMS'] =  0x04B0
msg_control['MOT_REQ_POTPARAMS'] =  0x04B1
msg_control['MOT_GET_POTPARAMS'] =  0x04B2
msg_control['MOT_SET_BUTTONPARAMS'] =  0x04B6
msg_control['MOT_REQ_BUTTONPARAMS'] =  0x04B7
msg_control['MOT_GET_BUTTONPARAMS'] =  0x04B8
msg_control['MOT_SET_EEPROMPARAMS'] =  0x04B9
msg_control['MOT_SET_PMDPOSITIONLOOPPARAMS'] =  0x04D7
msg_control['MOT_REQ_PMDPOSITIONLOOPPARAMS'] =  0x04D8
msg_control['MOT_GET_PMDPOSITIONLOOPPARAMS'] =  0x04D9
msg_control['MOT_SET_PMDMOTOROUTPUTPARAMS'] =  0x04DA
msg_control['MOT_REQ_PMDMOTOROUTPUTPARAMS'] =  0x04DB
msg_control['MOT_GET_PMDMOTOROUTPUTPARAMS'] =  0x04DC
msg_control['MOT_SET_PMDTRACKSETTLEPARAMS'] =  0x04E0
msg_control['MOT_REQ_PMDTRACKSETTLEPARAMS'] =  0x04E1
msg_control['MOT_GET_PMDTRACKSETTLEPARAMS'] =  0x04E2
msg_control['MOT_SET_PMDPROFILEMODEPARAMS'] =  0x04E3
msg_control['MOT_REQ_PMDPROFILEMODEPARAMS'] =  0x04E4
msg_control['MOT_GET_PMDPROFILEMODEPARAMS'] =  0x04E5
msg_control['MOT_SET_PMDJOYSTICKPARAMS'] =  0x04E6
msg_control['MOT_REQ_PMDJOYSTICKPARAMS'] =  0x04E7
msg_control['MOT_GET_PMDJOYSTICKPARAMS'] =  0x04E8
msg_control['MOT_SET_PMDCURRENTLOOPPARAMS'] =  0x04D4
msg_control['MOT_REQ_PMDCURRENTLOOPPARAMS'] =  0x04D5
msg_control['MOT_GET_PMDCURRENTLOOPPARAMS'] =  0x04D6
msg_control['MOT_SET_PMDSETTLEDCURRENTLOOPPARAMS'] =  0x04E9
msg_control['MOT_REQ_PMDSETTLEDCURRENTLOOPPARAMS'] =  0x04EA
msg_control['MOT_GET_PMDSETTLEDCURRENTLOOPPARAMS'] =  0x04EB
msg_control['MOT_SET_PMDSTAGEAXISPARAMS'] =  0x04F0
msg_control['MOT_REQ_PMDSTAGEAXISPARAMS'] =  0x04F1
msg_control['MOT_GET_PMDSTAGEAXISPARAMS'] =  0x04F2
msg_control['MOT_SET_TSTACTUATORTYPE'] =  0x04FE
msg_control['MOT_GET_STATUSUPDATE'] =  0x0481
msg_control['MOT_REQ_STATUSUPDATE'] =  0x0480
msg_control['MOT_GET_DCSTATUSUPDATE'] =  0x0491
msg_control['MOT_REQ_DCSTATUSUPDATE'] =  0x0490
msg_control['MOT_ACK_DCSTATUSUPDATE'] =  0x0492
msg_control['MOT_REQ_STATUSBITS'] =  0x0429
msg_control['MOT_GET_STATUSBITS'] =  0x042A
msg_control['MOT_SUSPEND_ENDOFMOVEMSGS'] =  0x046B
msg_control['MOT_RESUME_ENDOFMOVEMSGS'] =  0x046C
msg_control['MOT_SET_TRIGGER'] =  0x0500
msg_control['MOT_REQ_TRIGGER'] =  0x0501
msg_control['MOT_GET_TRIGGER'] =  0x0502
msg_control['MOT_SET_KCUBEMMIPARAMS'] =  0x0520
msg_control['MOT_REQ_KCUBEMMIPARAMS'] =  0x0521
msg_control['MOT_GET_KCUBEMMIPARAMS'] =  0x0522
msg_control['MOT_SET_KCUBETRIGIOCONFIG'] =  0x0523
msg_control['MOT_REQ_KCUBETRIGCONFIG'] =  0x0524
msg_control['MOT_GET_KCUBETRIGCONFIG'] =  0x0525
msg_control['MOT_SET_KCUBEPOSTRIGPARAMS'] =  0x0526
msg_control['MOT_REQ_KCUBEPOSTRIGPARAMS'] =  0x0527
msg_control['MOT_GET_KCUBEPOSTRIGPARAMS'] =  0x0528


#Filter Flipper Control Messages
msg_filter_flipper = {}
msg_filter_flipper['MOT_SET_MFF_OPERPARAMS'] =  0x0510
msg_filter_flipper['MOT_REQ_MFF_OPERPARAMS'] =  0x0511
msg_filter_flipper['MOT_GET_MFF_OPERPARAMS'] =  0x0512

#Solenoid Control Messages
msg_solenoid = {}
msg_solenoid['MOT_SET_SOL_OPERATINGMODE'] =  0x04C0
msg_solenoid['MOT_REQ_SOL_OPERATINGMODE'] =  0x04C1
msg_solenoid['MOT_GET_SOL_OPERATINGMODE'] =  0x04C2
msg_solenoid['MOT_SET_SOL_CYCLEPARAMS'] =  0x04C3
msg_solenoid['MOT_REQ_SOL_CYCLEPARAMS'] =  0x04C4
msg_solenoid['MOT_GET_SOL_CYCLEPARAMS'] =  0x04C5
msg_solenoid['MOT_SET_SOL_INTERLOCKMODE'] =  0x04C6
msg_solenoid['MOT_REQ_SOL_INTERLOCKMODE'] =  0x04C7
msg_solenoid['MOT_GET_SOL_INTERLOCKMODE'] =  0x04C8
msg_solenoid['MOT_SET_SOL_STATE'] =  0x04CB
msg_solenoid['MOT_REQ_SOL_STATE'] =  0x04CC
msg_solenoid['MOT_GET_SOL_STATE'] =  0x04CD


#Piezo Control Messages
msg_piezo = {}
msg_piezo['PZ_SET_POSCONTROLMODE'] =  0x0640
msg_piezo['PZ_REQ_POSCONTROLMODE'] =  0x0641
msg_piezo['PZ_GET_POSCONTROLMODE'] =  0x0642
msg_piezo['PZ_SET_OUTPUTVOLTS'] =  0x0643
msg_piezo['PZ_REQ_OUTPUTVOLTS'] =  0x0644
msg_piezo['PZ_GET_OUTPUTVOLTS'] =  0x0645
msg_piezo['PZ_SET_OUTPUTPOS'] =  0x0646
msg_piezo['PZ_REQ_OUTPUTPOS'] =  0x0647
msg_piezo['PZ_GET_OUTPUTPOS'] =  0x0648
msg_piezo['PZ_SET_INPUTVOLTSSRC'] =  0x0652
msg_piezo['PZ_REQ_INPUTVOLTSSRC'] =  0x0653
msg_piezo['PZ_GET_INPUTVOLTSSRC'] =  0x0654
msg_piezo['PZ_SET_PICONSTS'] =  0x0655
msg_piezo['PZ_REQ_PICONSTS'] =  0x0656
msg_piezo['PZ_GET_PICONSTS'] =  0x0657
msg_piezo['PZ_REQ_PZSTATUSBITS'] =  0x065B
msg_piezo['PZ_GET_PZSTATUSBITS'] =  0x065C
msg_piezo['PZ_GET_PZSTATUSUPDATE'] =  0x0661
msg_piezo['PZ_ACK_PZSTATUSUPDATE'] =  0x0662
msg_piezo['PZ_SET_OUTPUTLUT'] =  0x0700
msg_piezo['PZ_REQ_OUTPUTLUT'] =  0x0701
msg_piezo['PZ_GET_OUTPUTLUT'] =  0x0702
msg_piezo['PZ_SET_OUTPUTLUTPARAMS'] =  0x0703
msg_piezo['PZ_REQ_OUTPUTLUTPARAMS'] =  0x0704
msg_piezo['PZ_GET_OUTPUTLUTPARAMS'] =  0x0705
msg_piezo['PZ_START_LUTOUTPUT'] =  0x0706
msg_piezo['PZ_STOP_LUTOUTPUT'] =  0x0707
msg_piezo['PZ_SET_EEPROMPARAMS'] =  0x07D0
msg_piezo['PZ_SET_TPZ_DISPSETTINGS'] =  0x07D1
msg_piezo['PZ_REQ_TPZ_DISPSETTINGS'] =  0x07D2
msg_piezo['PZ_GET_TPZ_DISPSETTINGS'] =  0x07D3
msg_piezo['PZ_SET_TPZ_IOSETTINGS'] =  0x07D4
msg_piezo['PZ_REQ_TPZ_IOSETTINGS'] =  0x07D5
msg_piezo['PZ_GET_TPZ_IOSETTINGS'] =  0x07D6
msg_piezo['PZ_SET_ZERO'] =  0x0658
msg_piezo['PZ_REQ_MAXTRAVEL'] =  0x0650
msg_piezo['PZ_GET_MAXTRAVEL'] =  0x0651
msg_piezo['PZ_SET_IOSETTINGS'] =  0x0670
msg_piezo['PZ_REQ_IOSETTINGS'] =  0x0671
msg_piezo['PZ_GET_IOSETTINGS'] =  0x0672
msg_piezo['PZ_SET_OUTPUTMAXVOLTS'] =  0x0680
msg_piezo['PZ_REQ_OUTPUTMAXVOLTS'] =  0x0681
msg_piezo['PZ_GET_OUTPUTMAXVOLTS'] =  0x0682
msg_piezo['PZ_SET_TPZ_SLEWRATES'] =  0x0683
msg_piezo['PZ_REQ_TPZ_SLEWRATES'] =  0x0684
msg_piezo['PZ_GET_TPZ_SLEWRATES'] =  0x0685
msg_piezo['MOT_SET_PZSTAGEPARAMDEFAULTS'] =  0x0686
msg_piezo['PZ_SET_LUTVALUETYPE'] =  0x0708
msg_piezo['KPZ_SET_KCUBEMMIPARAMS'] =  0x07F0
msg_piezo['KPZ_REQ_KCUBEMMIPARAMS'] =  0x07F1
msg_piezo['KPZ_GET_KCUBEMMIPARAMS'] =  0x07F2
msg_piezo['KPZ_SET_KCUBETRIGIOCONFIG'] =  0x07F3
msg_piezo['KPZ_REQ_KCUBETRIGIOCONFIG'] =  0x07F4
msg_piezo['KPZ_GET_KCUBETRIGIOCONFIG'] =  0x07F5
msg_piezo['PZ_SET_TSG_IOSETTINGS'] =  0x07DA
msg_piezo['PZ_REQ_TSG_IOSETTINGS'] =  0x07DB
msg_piezo['PZ_GET_TSG_IOSETTINGS'] =  0x07DC
msg_piezo['PZ_REQ_TSG_READING'] =  0x07DD
msg_piezo['PZ_GET_TSG_READING'] =  0x07DE
msg_piezo['KSG_SET_KCUBEMMIPARAMS'] =  0x07F6
msg_piezo['KSG_REQ_KCUBEMMIPARAMS'] =  0x07F7
msg_piezo['KSG_GET_KCUBEMMIPARAMS'] =  0x07F8
msg_piezo['KSG_SET_KCUBETRIGIOCONFIG'] =  0x07F9
msg_piezo['KSG_REQ_KCUBETRIGIOCONFIG'] =  0x07FA
msg_piezo['KSG_GET_KCUBETRIGIOCONFIG'] =  0x07FB



#NanoTrak Control Messages
msg_nano_trak = {}
msg_nano_trak['PZ_SET_NTMODE'] =  0x0603
msg_nano_trak['PZ_REQ_NTMODE'] =  0x0604
msg_nano_trak['PZ_GET_NTMODE'] =  0x0605
msg_nano_trak['PZ_SET_NTTRACKTHRESHOLD'] =  0x0606
msg_nano_trak['PZ_REQ_NTTRACKTHRESHOLD'] =  0x0607
msg_nano_trak['PZ_GET_NTTRACKTHRESHOLD'] =  0x0608
msg_nano_trak['PZ_SET_NTCIRCHOMEPOS'] =  0x0609
msg_nano_trak['PZ_REQ_NTCIRCHOMEPOS'] =  0x0610
msg_nano_trak['PZ_GET_NTCIRCHOMEPOS'] =  0x0611
msg_nano_trak['PZ_MOVE_NTCIRCTOHOMEPOS'] =  0x0612
msg_nano_trak['PZ_REQ_NTCIRCCENTREPOS'] =  0x0613
msg_nano_trak['PZ_GET_NTCIRCCENTREPOS'] =  0x0614
msg_nano_trak['PZ_SET_NTCIRCPARAMS'] =  0x0618
msg_nano_trak['PZ_REQ_NTCIRCPARAMS'] =  0x0619
msg_nano_trak['PZ_GET_NTCIRCPARAMS'] =  0x0620
msg_nano_trak['PZ_SET_NTCIRCDIA'] =  0x061A
msg_nano_trak['PZ_SET_NTCIRCDIALUT'] =  0x0621
msg_nano_trak['PZ_REQ_NTCIRCDIALUT'] =  0x0622
msg_nano_trak['PZ_GET_NTCIRCDIALUT'] =  0x0623
msg_nano_trak['PZ_SET_NTPHASECOMPPARAMS'] =  0x0626
msg_nano_trak['PZ_REQ_NTPHASECOMPPARAMS'] =  0x0627
msg_nano_trak['PZ_GET_NTPHASECOMPPARAMS'] =  0x0628
msg_nano_trak['PZ_SET_NTTIARANGEPARAMS'] =  0x0630
msg_nano_trak['PZ_REQ_NTTIARANGEPARAMS'] =  0x0631
msg_nano_trak['PZ_GET_NTTIARANGEPARAMS'] =  0x0632
msg_nano_trak['PZ_SET_NTGAINPARAMS'] =  0x0633
msg_nano_trak['PZ_REQ_NTGAINPARAMS'] =  0x0634
msg_nano_trak['PZ_GET_NTGAINPARAMS'] =  0x0635
msg_nano_trak['PZ_SET_NTTIALPFILTERPARAMS'] =  0x0636
msg_nano_trak['PZ_REQ_NTTIALPFILTERPARAMS'] =  0x0637
msg_nano_trak['PZ_GET_NTTIALPFILTERPARAMS'] =  0x0638
msg_nano_trak['PZ_REQ_NTTIAREADING'] =  0x0639
msg_nano_trak['PZ_GET_NTTIAREADING'] =  0x063A
msg_nano_trak['PZ_SET_NTFEEDBACKSRC'] =  0x063B
msg_nano_trak['PZ_REQ_NTFEEDBACKSRC'] =  0x063C
msg_nano_trak['PZ_GET_NTFEEDBACKSRC'] =  0x063D
msg_nano_trak['PZ_REQ_NTSTATUSBITS'] =  0x063E
msg_nano_trak['PZ_GET_NTSTATUSBITS'] =  0x063F
msg_nano_trak['PZ_REQ_NTSTATUSUPDATE'] =  0x0664
msg_nano_trak['PZ_GET_NTSTATUSUPDATE'] =  0x0665
msg_nano_trak['PZ_ACK_NTSTATUSUPDATE'] =  0x0666
msg_nano_trak['KNA_SET_NTTIALPFILTERCOEFFS'] =  0x0687
msg_nano_trak['KNA_REQ_NTTIALPFILTERCOEFFS'] =  0x0688
msg_nano_trak['KNA_GET_NTTIALPFILTERCOEFFS'] =  0x0689
msg_nano_trak['KNA_SET_KCUBEMMIPARAMS'] =  0x068A
msg_nano_trak['KNA_REQ_KCUBEMMIPARAMS'] =  0x068B
msg_nano_trak['KNA_GET_KCUBEMMIPARAMS'] =  0x068C
msg_nano_trak['KNA_SET_KCUBETRIGIOCONFIG'] =  0x068D
msg_nano_trak['KNA_REQ_KCUBETRIGIOCONFIG'] =  0x068E
msg_nano_trak['KNA_GET_KCUBETRIGIOCONFIG'] =  0x068F
msg_nano_trak['KNA_REQ_XYSCAN'] =  0x06A0
msg_nano_trak['KNA_GET_XYSCAN'] =  0x06A1
msg_nano_trak['KNA_STOP_XYSCAN'] =  0x06A2
msg_nano_trak['NT_SET_EEPROMPARAMS'] =  0x07E7
msg_nano_trak['NT_SET_TNA_DISPSETTINGS'] =  0x07E8
msg_nano_trak['NT_REQ_TNA_DISPSETTINGS'] =  0x07E9
msg_nano_trak['NT_GET_TNA_DISPSETTINGS'] =  0x07EA
msg_nano_trak['NT_SET_TNAIOSETTINGS'] =  0x07EB
msg_nano_trak['NT_REQ_TNAIOSETTINGS'] =  0x07EC
msg_nano_trak['NT_GET_TNAIOSETTINGS'] =  0x07ED


#Laser Control Messages
msg_laser = {}
msg_laser['LA_SET_PARAMS'] =  0x0800
msg_laser['LA_REQ_PARAMS'] =  0x0801
msg_laser['LA_GET_PARAMS'] =  0x0802
msg_laser['LA_SET_EEPROMPARAMS'] =  0x0810
msg_laser['LA_ENABLEOUTPUT'] =  0x0811
msg_laser['LA_DISABLEOUTPUT'] =  0x0812
msg_laser['LD_OPENLOOP'] =  0x0813
msg_laser['LD_CLOSEDLOOP'] =  0x0814
msg_laser['LD_POTROTATING'] =  0x0815
msg_laser['LD_MAXCURRENTADJUST'] =  0x0816
msg_laser['LD_SET_MAXCURRENTDIGPOT'] =  0x0817
msg_laser['LD_REQ_MAXCURRENTDIGPOT'] =  0x0818
msg_laser['LD_GET_MAXCURRENTDIGPOT'] =  0x0819
msg_laser['LD_FINDTIAGAIN'] =  0x081A
msg_laser['LD_TIAGAINADJUST'] =  0x081B
msg_laser['LA_REQ_STATUSUPDATE'] =  0x0820
msg_laser['LA_GET_STATUSUPDATE'] =  0x0821
msg_laser['LA_ACK_STATUSUPDATE'] =  0x0822
msg_laser['LD_REQ_STATUSUPDATE'] =  0x0825
msg_laser['LD_GET_STATUSUPDATE'] =  0x0826
msg_laser['LD_ACK_STATUSUPDATE'] =  0x0827
msg_laser['LA_SET_KCUBETRIGIOCONFIG'] =  0x082A
msg_laser['LA_REQ_KCUBETRIGCONFIG'] =  0x082B
msg_laser['LA_GET_KCUBETRIGCONFIG'] =  0x082C



#Quad Control Messages
msg_quad = {}
msg_quad['QUAD_SET_PARAMS'] =  0x0870
msg_quad['QUAD_REQ_PARAMS'] =  0x0871
msg_quad['QUAD_GET_PARAMS'] =  0x0872
msg_quad['QUAD_REQ_STATUSUPDATE'] =  0x0880
msg_quad['QUAD_GET_STATUSUPDATE'] =  0x0881
msg_quad['QUAD_ACK_STATUSUPDATE'] =  0x0882
msg_quad['QUAD_SET_EEPROMPARAMS'] =  0x0875


#TEC Control Messages
msg_tec={}
msg_tec['TEC_SET_PARAMS'] =  0x0840
msg_tec['TEC_REQ_PARAMS'] =  0x0841
msg_tec['TEC_GET_PARAMS'] =  0x0842
msg_tec['TEC_SET_EEPROMPARAMS'] =  0x0850
msg_tec['TEC_REQ_STATUSUPDATE'] =  0x0860
msg_tec['TEC_GET_STATUSUPDATE'] =  0x0861
msg_tec['TEC_ACK_STATUSUPDATE'] =  0x0862



#TIM and KIM Control Messages
msg_tim_kim={}
msg_tim_kim['PZMOT_SET_PARAMS'] =  0x08C0
msg_tim_kim['PZMOT_REQ_PARAMS'] =  0x08C1
msg_tim_kim['PZMOT_GET_PARAMS'] =  0x08C2
msg_tim_kim['PZMOT_MOVE_ABSOLUTE'] =  0x04D8
msg_tim_kim['PZMOT_MOVE_COMPLETED'] =  0x08D6
msg_tim_kim['PZMOT_MOVE_JOG'] =  0x08D9
msg_tim_kim['PZMOT_REQ_STATUSUPDATE'] =  0x08E0
msg_tim_kim['PZMOT_GET_STATUSUPDATE'] =  0x08E1

msg = {}
msg.update(msg_general)
msg.update(msg_control)
msg.update(msg_filter_flipper)
msg.update(msg_solenoid)
msg.update(msg_piezo)
msg.update(msg_nano_trak)
msg.update(msg_laser)
msg.update(msg_quad)
msg.update(msg_tec)
msg.update(msg_tim_kim)

message_general = DictClass(msg_general)
message_control = DictClass(msg_control)
message_filter_flipper = DictClass(msg_filter_flipper)
message_solenoid = DictClass(msg_solenoid)
message_piezo = DictClass(msg_piezo)
message_nano_trak = DictClass(msg_nano_trak)
message_laser = DictClass(msg_laser)
message_quad = DictClass(msg_quad)
message_tec = DictClass(msg_tec)
message_tim_kim = DictClass(msg_tim_kim)
message = DictClass(msg)

msg_bbd_10x = dict([(key,msg[key]) for key in ms.BBD10x])
message_bbd_10x = DictClass(msg_bbd_10x)