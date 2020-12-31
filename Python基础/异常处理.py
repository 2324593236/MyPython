###异常处理
##try...except
try:#测试
    value1#异常代码
except [ExceptionName [as alias]]:#ExceptionName异常类型，as alias异常别名
    value2#异常反馈内容

##try...except...else
try:#测试
    value1#异常代码
except [ExceptionName [as alias]]:#ExceptionName异常类型，as alias异常别名
    value2#异常反馈内容
else:#不抛出异常时
    value3#非异常反馈内容

##try...except...finally
try:#测试
    value1#异常代码
except [ExceptionName [as alias]]:#ExceptionName异常类型，as alias异常别名
    value2#异常反馈内容
finally:#无论是否异常
    value3#结束反馈内容

##raise语句抛出异常
raise [ExceptionName[(reason)]]#ExceptionName异常类型，reason异常描述
