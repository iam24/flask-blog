# coding=utf8
from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views


# 转换成程序工厂函数的操作让定义路由变复杂了。在单脚本程序中,程序实例存在于全 局作用域中,路由可以直接使用 app.route 修饰器定义。但现在程序在运行时创建,只 有调用 create_app() 之后才能使用 app.route 修饰器,这时定义路由就太晚了。和路由 一样,自定义的错误页面处理程序也面临相同的困难,因为错误页面处理程序使用 app. errorhandler 修饰器定义。

# 幸好 Flask 使用蓝本提供了更好的解决方法。蓝本和程序类似,也可以定义路由。不同的 是,在蓝本中定义的路由处于休眠状态,直到蓝本注册到程序上后,路由才真正成为程序 的一部分。使用位于全局作用域中的蓝本时,定义路由的方法几乎和单脚本程序一样。