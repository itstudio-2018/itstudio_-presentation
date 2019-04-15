# 爱特展示网 需求文档



## 1. 首页

​	展现爱特的形象

​	简洁、大方、

​	( 静态页面 内容基本不变 )

##### 设计

​	UI：

- 良好的设计布局
- 精美的视图
- 注意设计好页面头

​	前端：

- 严格按照 UI 设计的稿子，画HTML
- 设计炫酷的动画效果
- 网页内容直接写在 HTML 里

​	后端：

- 根据 url 返回 HTML 及 相关内容

  

## 2. 部门介绍页

​	放置 每个部门的部门介绍

​	现在的部门有 程序、前端、UI、APP、游戏

​	考虑到 部门可能会有变动 ( 部门名称、部门数量 ) 需要设计成 可变动的动态页面

​	( 后台添加、改动、删除数据 )

##### 设计

​	UI：

- 良好的设计布局
- 精美的视图
- 设计多个部门 ( 不少于6个 ) 的 显示样式
- 设计部门的介绍显示栏

​	前端：

- 严格按照 UI 设计的稿子，画HTML
- 设计动画效果
- 使用接口请求 部门的相关信息
- 部门数量变化时，页面也相应改变

​	后端：

- 根据 url 返回 HTML 及 相关内容

- 设计接口 返回 部门的相关信息

  

## 3. 作品展示页

​	放置 爱特参与设计的作品

​	含有作品名称、作品快照、作品链接

​	考虑到 作品的数量会有变化 需要设计成 可变动的动态页面

​	( 后台添加、改动、删除数据 )

##### 设计

​	UI：

- 良好的设计布局
- 精美的视图
- 合理设计作品的摆放方式，注意作品数量变化

​	前端：

- 严格按照 UI 设计的稿子，画HTML
- 设计动画效果
- 使用接口请求 作品的相关信息
- 作品数量变化时，页面也相应改变

​	后端：

- 根据 url 返回 HTML 及 相关内容
- 设计接口 返回 作品的相关信息



## 4. 爱特大事记页

​	放置 爱特发生的大事件 并有 相关的介绍

​	按照年份放置

​	考虑到 大事记的数量、内容会有变化 需要设计成 可变动的动态页面

​	( 后台添加、改动、删除数据 )

##### 设计

​	UI：

- 良好的设计布局
- 精美的视图
- 大事记按年分摆放，设计摆放方式，注意数量的变化
- 大事记的详情显示

​	前端：

- 严格按照 UI 设计的稿子，画HTML
- 设计动画效果
- 使用接口请求 大事记的相关信息
- 大事记数量变化时，页面也相应改变

​	后端：

- 根据 url 返回 HTML 及 相关内容
- 设计接口 返回 大事记的相关信息



## 5. 成员展示页

​	放置 爱特每届的成员 含有照片 和 相关介绍

​	按照年份放置

​	考虑到成员会有变化 需要设计成 可变动的动态页面

​	( 后台添加、改动、删除数据 )

##### 设计

​	UI：

- 良好的设计布局
- 精美的视图
- 成员介绍按年分摆放
- 不可一次显示全部，设计分页
- 设计成员介绍的 图片 和 文字 的显示形式
- 注意成员介绍数量的变化

​	前端：

- 严格按照 UI 设计的稿子，画HTML
- 设计动画效果
- 成员介绍不可一次显示全部，设计分页
- 使用接口请求 成员介绍的相关信息
- 成员介绍数量变化时，页面也相应改变

​	后端：

- 根据 url 返回 HTML 及 相关内容
- 设计接口 返回 成员的相关信息



## 6. 留言页

​	放置所有的留言

​	留言

​		昵称留言，不设计登陆功能

​		设计默认可选头像

​		昵称不超过10个字 ( 含有敏感词过滤 )

​		留言内容不超过100个字 ( 含有敏感词过滤 )

​		有图片验证码( 或者滑动验证码 )

​		留言可在后台回复 为管理员回复

​		留言设计滚动分页，第一次访问获取 2 页留言，显示第 1 页， 当滚动到第 2 页时，请求第3页，以此类推，直至最后一页

​		留言按新到就排序

##### 设计

​	UI：

- 良好的设计布局
- 精美的视图
- 留言的摆放形式
- 留言的显示形式分为 有回复的留言 和 没有回复的留言 考虑回复防止的位置
- 留言不可一次显示全部，设计分页
- 注意留意数量的变化
- 设计可选默认头像 或 其他方式区别留言
- 设计图片验证码 ( 或 滑动验证码 ) 的放置部位

​	前端：

- 严格按照 UI 设计的稿子，画HTML
- 设计动画效果
- 留言不可一次显示全部，设计分页
- 使用接口请求 留言的相关信息
- 留言请求的方式为 第一次访问获取 2 页留言，显示第 1 页， 当滚动到第 2 页时，请求第3页，以此类推，直至最后一页
- 注意有回复的留言的显示
- 留言数量变化时，页面也相应改变
- 验证 昵称 不超过 10 个字，留言内容 不超过 100 个字
- 注意对文字的转义，预防攻击
- 使用接口 提交留言

​	后端：

- 根据 url 返回 HTML 及 相关内容
- 设计接口 返回 留言的相关信息
- 设计接口 接受留言 进行发表
- 验证 昵称 留言内容 的 合法性 并 返回状态
- 对于 昵称 留言内容 设计敏感词过滤
- 图片验证码的请求频率



## 7. 申请加入页

​	需要填写  姓名、手机号、邮箱、年级、学院、专业

​	( 可设计备注栏 )

​	验证 姓名、手机号、邮箱 的合法性、不可缺少

​	有图片验证码( 或者滑动验证码 )

​	发送邮件进行激活 ( 链接激活 )

​	后台可导出申请人的信息

##### 设计

​	UI：

- 良好的设计布局
- 精美的视图
- 设计姓名、手机号、邮箱、年级、学院、专业的填写框
- 设计图片验证码 ( 或 滑动验证码 ) 的放置部位

​	前端：

- 严格按照 UI 设计的稿子，画HTML
- 验证 姓名、手机号、邮箱 的合法性 所有内容不可为空
- 使用接口 提交申请

​	后端：

- 根据 url 返回 HTML 及 相关内容
- 设计接口 接受申请
- 验证 所有内容 并 返回状态
- 图片验证码的请求频率



## 8. 状态查看页

​	此页查看申请人的状态，分为 未激活、待初审、待面试、待笔试、已选中 

​	( 

​		以上为只显示状态 

​		或者 设计为 流程图

​	)

​	需要输入邮箱，进行查看

​	验证邮箱的合法性

​	后台对状态进行修改

##### 设计

​	UI：

- 良好的设计布局
- 精美的视图
- 邮箱的填写框
- 状态栏设计 或者为 流程图

​	前端：

- 严格按照 UI 设计的稿子，画HTML
- 验证邮箱的合法性
- 使用接口 请求状态 

​	后端：

- 根据 url 返回 HTML 及 相关内容
- 设计接口 接受查看请求
- 验证邮箱 并 返回 相关内容

​	

## 9. 激活成功页

​	申请人的激活形式为 邮箱链接激活

​	需要有一个页面显示激活成功

##### 设计

​	UI：

- 良好的设计布局
- 精美的视图
- 设计显示状态的部位

​	前端：

- 严格按照 UI 设计的稿子，画HTML

​	后端：

- 根据 url 判断 合法性 并进行激活

## 10. 404页

​	此页为了优化用户体验

##### 设计

​	UI：

- 良好的设计布局
- 精美的视图
- 提示内容

​	前端：

- 严格按照 UI 设计的稿子，画HTML
- ( 可设计 HTML 小游戏 )

​	后端：

- 根据 url 返回 HTML 及 相关内容



## 11. 后台

##### 设计

​	后端：

- 对 部门、大事记、成员介绍、作品介绍 能进行 添加、修改、删除
- 能够回复留言
- 查看申请人的状态 并 进行修改
- 导出申请人信息 为 Excel