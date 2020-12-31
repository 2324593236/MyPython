#项目二：个人所得税计算器
#
before=float(input("请输入您的税前工资："))
shb=float(input("请输入社保扣除金额："))
shsh=0#纳税金额
ynsh=before-shb-5000#应纳税所得额
if ynsh<=3000 and ynsh>0:
    shsh=ynsh*0.03-0
elif ynsh<=12000:
    shsh=ynsh*0.1-210
elif ynsh<=25000:
    shsh=ynsh*0.2-1410
elif ynsh<=35000:
    shsh=ynsh*0.25-2660
elif ynsh<=55000:
    shsh=ynsh*0.3-4410
elif ynsh<=80000:
    shsh=ynsh*0.35-7160
elif ynsh>80000:
    shsh=ynsh*0.45-15160
print("应纳税金额：",shsh,"元","/n","到手工资：",before-shb-shsh,"元")
