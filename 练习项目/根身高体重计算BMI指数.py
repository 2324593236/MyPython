# _*_ coding utf-8 _*_
# 开发团队：HS黄舍
# 开发人员：Administrator
# 开发项目：Python Study
# 开发时间：日期:2020/11/24 时间:13:07
# 文件名称：根身高体重计算BMI指数.py
# 开发工具：PyCharm

sg = float(input("请输入您的身高（单位：米）："))
tz = float(input("请输入您的体重（单位：千克）："))
bmi = tz/(sg*sg)
if bmi < 18.5:
    print("您的BMI值为:",bmi,"您的体重偏轻或您的身高偏高")
if bmi >= 18.5 and bmi < 24.9:
    print("您的BMI值为:",bmi,"正常范围~~请注意保持~~~")
if bmi > 24.9:
    print("您的BMI值为:",bmi,"您的体重偏重或您的身高偏低")