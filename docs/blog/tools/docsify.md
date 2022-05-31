# Docsify 
[Docsify](https://docsify.js.org)是一个文档类网站生成器，不同于其他网站生成器，如Hugo,该生成器的特点在于动态渲染HTML文件，即我们的网站repo只需要存储markdown文件和简单的index.html文件即可。更直白地说就是“网站外观归它，写内容归我们”。同时，使用该生成器的流程也很简单。主要直接为如下方面：

1. 安装预设
- Nodejs, npm (12.22.9)

```bash
sudo apt install nodejs npm
node -v
```
2. 安装docsify (4.12.2)

```bash
sudo npm i docsify-cli -g
```
3. 克隆sunniejs blog主题

```bash 
cd ~/Workplace/web
git clone https://github.com/sunniejs/blog.git
```
4. 本地实时预览

```bash
cd blog
docsify serve docs
```
4. 修改主题配置(index.html)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Kyrie's World</title>
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
  <meta name="description" content="Description">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
  <link rel="stylesheet" href="//cdn.jsdelivr.net/npm/docsify@4/lib/themes/vue.css">
  <link rel="stylesheet" href="./_media/custom.css">
  <link href="https://fonts.googleapis.com/css?family=Lobster"rel="stylesheet">
</head>
<body>
  <div id="app"></div>
  <script>
    window.$docsify = {
      name: 'Kyrie’s World',
      repo: 'https://github.com/kyrie1218/kyrieecon',
      coverpage:true,
      themeColor: '#25798A',
      loadSidebar: true,
    }
  </script>
  <!-- Docsify v4 -->
  <script src="//cdn.jsdelivr.net/npm/docsify@4"></script>
  <!--复制代码插件-->
  <script src="https://unpkg.com/docsify-copy-code@2"></script>
  <!--katex数学公式插件-->
  <script src="//cdn.jsdelivr.net/gh/upupming/docsify-katex@latest/dist/docsify-katex.js"></script>
  <link rel="stylesheet" href="//cdn.jsdelivr.net/npm/katex@latest/dist/katex.min.css"/>
  <!--重点内容提醒插件-->
  <script src="https://unpkg.com/docsify-plugin-flexible-alerts"></script>
  <!--暗黑模式插件-->
  <script src="//cdn.jsdelivr.net/npm/docsify-dark-mode@latest/dist/index.min.js"></script>
  <link rel="stylesheet" href="//cdn.jsdelivr.net/npm/docsify-dark-mode@latest/dist/style.min.css"/>
  <!--图片标题插件-->
  <script src="https://unpkg.com/@h-hg/docsify-image-caption/dist/docsify-image-caption.min.js"></script>
  <!--语法高亮插件-->
  <script src="//cdn.jsdelivr.net/npm/prismjs@1/components/prism-bash.min.js"></script>
  <!--全文搜索插件-->
  <script src="//cdn.jsdelivr.net/npm/docsify/lib/plugins/search.min.js"></script>
  <!--图片缩放插件-->
  <script src="//cdn.jsdelivr.net/npm/docsify/lib/plugins/zoom-image.min.js"></script>
  <!--上下翻页插件-->
  <script src="//cdn.jsdelivr.net/npm/docsify-pagination/dist/docsify-pagination.min.js"></script>
</body>
</html>
```
