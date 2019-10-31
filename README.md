该Project为Flask的入门Demo

backend为主程序的文件夹

    backend文件夹里：
    
        apis：flask的api层
            one.py：调用one_helloworld.py里的函数
            two.py：调用two_helloworld.py里的函数
            
        config：用来配置一些文件的路径和配置其他的一些默认信息
        
        core:apis里调用的函数
            one_helloworld.py：被one.py调用
            two_helloworld.py：被two.py调用
            
        util:用来存储静态文件和模板
        
        __init__.py：有关日志的文件
        
        __main__.py：初始化和启动app
        
    scripts文件夹：
        里面存放的是要运行的脚本文件，可有可无
        
    .gitignore：是上传到git上忽略的文件
    
    LICENSE：默认文件
    
    requirements.txt：是安装这个项目时要安装的一些python包
    
    setup.py：用来描述这个项目
    
    wegi.py：用来启动整个项目
