# WaitYiYan

通过命令在QQ对话框查询您在`文心一言`等待列表排在第几位, 这是一个[QChatGPT项目](https://github.com/RockChinQ/QChatGPT)的插件

![image](https://user-images.githubusercontent.com/45992437/226093800-8909e961-dbec-400c-8821-e7b3ba8a924a.png)

## 使用方式

1. 部署[QChatGPT项目](https://github.com/RockChinQ/QChatGPT)，完成后使用管理员账号私聊机器人号发送`!plugin https://github.com/RockChinQ/WaitYiYan`安装此插件
2. 安装适用于[Chrome/Edge](https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm) 或 [Firefox](https://addons.mozilla.org/en-US/firefox/addon/cookie-editor/) 的Cookies编辑器插件
3. 访问[文心一言官网](https://yiyan.baidu.com/welcome)，登录您的百度账号，加入等待列表
4. 打开第二步安装的插件，点击 `Export` 按钮, 复制JSON格式的Cookies
5. 前往QChatGPT主程序的`config.py`所在目录，新建文件`yiyancookies.json`，将刚刚复制的cookie粘贴进去
6. 重启主程序

此时即可私聊向机器人发送`!wyy`查看您目前的排位
