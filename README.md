# zentao_sqli_poc-exp
禅道cms多线程sql注入脚本,
python poc/exp脚本为单线程,
使用py poc 检测发现漏洞可以直接用 go 版本exp跑，高并发不到十秒出结果

## exp.go

tips:修改第13行全局变量 url 为你要测试的地址，

默认显示第一条记录的password字段，也就是admin的密码，

可修改 sqli 函数中 poc 变量修改sql语句     注：account为用户名字段



