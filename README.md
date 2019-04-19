#大众点评模拟登录checkRisk接口_token破解
思路和解决步骤：
（1）checkRisk接口请求拦截：
![输入接口关键词checkRisk回车](https://upload-images.jianshu.io/upload_images/10203810-2b8716e49c97968f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
（2）确定发起该请求会用到哪些js文件和js函数：
![调用的js函数](https://upload-images.jianshu.io/upload_images/10203810-19fd99cf3967a837.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
（3）所有的函数都点击进去，看看该函数里都写了啥有什么参数，方法是什么，这些参数都是什么value
![参数value](https://upload-images.jianshu.io/upload_images/10203810-be2ae2c0ae892571.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
(4)在js文件中搜索关键字_token找到可疑关键字Rohr_Opt
![关键字Rohr_Opt](https://upload-images.jianshu.io/upload_images/10203810-419ad2ff4097c948.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
（5）继续全局搜索Rohr_Opt，发现存在这两个文件中
![确定了加密算法的位置](https://upload-images.jianshu.io/upload_images/10203810-36e0868f8f46d64d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
该js文件的路径是https://s0.meituan.net/mx/rohr/rohr.min.js
（6）提取该文件内的js源码，格式化，好好研究是怎么算的
![整理js找到算法需求参数和函数间的调用关系](https://upload-images.jianshu.io/upload_images/10203810-7ac6f2b8cde3bd1a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
（7）根据常识知道token是base64的，但是b64解码后还是看不懂，在b64前又经过了一层加密，该加密方式是压缩字符串，
![deflate方法是js对string的压缩方法](https://upload-images.jianshu.io/upload_images/10203810-f684a6bf2c33211c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
（8）整理几千行，js代码间复杂的传参和调用关系，这里iP是源头，以此为核心展开
![解决该ip的生成](https://upload-images.jianshu.io/upload_images/10203810-50d3ceaf01ca9e7e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
（9）整理ip生成算法
```
var rohrdata = "";
var Rohr_Opt = new Object;
Rohr_Opt.Flag = "100049";
Rohr_Opt.LogVal = "rohrdata";
var _$_543c = ["\x75\x6E\x64\x65\x66\x69\x6E\x65\x64", "\x66\x75\x6E\x63\x74\x69\x6F\x6E", "\x6F\x62\x6A\x65\x63\x74", "\x67\x6C\x6F\x62\x61\x6C", "\x77\x69\x6E\x64\x6F\x77", "\x73\x65\x6C\x66", "\x4F\x62\x6A\x65\x63\x74", "\x4E\x75\x6D\x62\x65\x72", "\x53\x74\x72\x69\x6E\x67", "\x44\x61\x74\x65", "\x53\x79\x6E\x74\x61\x78\x45\x72\x72\x6F\x72", "\x54\x79\x70\x65\x45\x72\x72\x6F\x72", "\x4D\x61\x74\x68", "\x4A\x53\x4F\x4E", "\x62\x75\x67\x2D\x73\x74\x72\x69\x6E\x67\x2D\x63\x68\x61\x72\x2D\x69\x6E\x64\x65\x78", "\x61", "\x6A\x73\x6F\x6E", "\x6A\x73\x6F\x6E\x2D\x73\x74\x72\x69\x6E\x67\x69\x66\x79", "\x6A\x73\x6F\x6E\x2D\x70\x61\x72\x73\x65", "\x7B\x22\x61\x22\x3A\x5B\x31\x2C\x74\x72\x75\x65\x2C\x66\x61\x6C\x73\x65\x2C\x6E\x75\x6C\x6C\x2C\x22\x5C\x75\x30\x30\x30\x30\x5C\x62\x5C\x6E\x5C\x66\x5C\x72\x5C\x74\x22\x5D\x7D", "\x30", "\x22\x22", "\x31", "\x5B\x31\x5D", "\x5B\x6E\x75\x6C\x6C\x5D", "\x6E\x75\x6C\x6C", "\x5B\x6E\x75\x6C\x6C\x2C\x6E\x75\x6C\x6C\x2C\x6E\x75\x6C\x6C\x5D", "\x00\x08\x0A\x0C\x0D\x09", "\x5B\x0A\x20\x31\x2C\x0A\x20\x32\x0A\x5D", "\x22\x2D\x32\x37\x31\x38\x32\x31\x2D\x30\x34\x2D\x32\x30\x54\x30\x30\x3A\x30\x30\x3A\x30\x30\x2E\x30\x30\x30\x5A\x22", "\x22\x2B\x32\x37\x35\x37\x36\x30\x2D\x30\x39\x2D\x31\x33\x54\x30\x30\x3A\x30\x30\x3A\x30\x30\x2E\x30\x30\x30\x5A\x22", "\x22\x2D\x30\x30\x30\x30\x30\x31\x2D\x30\x31\x2D\x30\x31\x54\x30\x30\x3A\x30\x30\x3A\x30\x30\x2E\x30\x30\x30\x5A\x22", "\x22\x31\x39\x36\x39\x2D\x31\x32\x2D\x33\x31\x54\x32\x33\x3A\x35\x39\x3A\x35\x39\x2E\x39\x39\x39\x5A\x22", "\x22\x09\x22", "\x30\x31", "\x31\x2E", "\x5B\x6F\x62\x6A\x65\x63\x74\x20\x46\x75\x6E\x63\x74\x69\x6F\x6E\x5D", "\x5B\x6F\x62\x6A\x65\x63\x74\x20\x44\x61\x74\x65\x5D", "\x5B\x6F\x62\x6A\x65\x63\x74\x20\x4E\x75\x6D\x62\x65\x72\x5D", "\x5B\x6F\x62\x6A\x65\x63\x74\x20\x53\x74\x72\x69\x6E\x67\x5D", "\x5B\x6F\x62\x6A\x65\x63\x74\x20\x41\x72\x72\x61\x79\x5D", "\x5B\x6F\x62\x6A\x65\x63\x74\x20\x42\x6F\x6F\x6C\x65\x61\x6E\x5D", "\x76\x61\x6C\x75\x65\x4F\x66", "\x74\x6F\x53\x74\x72\x69\x6E\x67", "\x74\x6F\x4C\x6F\x63\x61\x6C\x65\x53\x74\x72\x69\x6E\x67", "\x70\x72\x6F\x70\x65\x72\x74\x79\x49\x73\x45\x6E\x75\x6D\x65\x72\x61\x62\x6C\x65", "\x69\x73\x50\x72\x6F\x74\x6F\x74\x79\x70\x65\x4F\x66", "\x68\x61\x73\x4F\x77\x6E\x50\x72\x6F\x70\x65\x72\x74\x79", "\x63\x6F\x6E\x73\x74\x72\x75\x63\x74\x6F\x72", "\x70\x72\x6F\x74\x6F\x74\x79\x70\x65", "\x5C\x5C", "\x5C\x22", "\x5C\x62", "\x5C\x66", "\x5C\x6E", "\x5C\x72", "\x5C\x74", "\x30\x30\x30\x30\x30\x30", "\x5C\x75\x30\x30", "\x22", "", "\x74\x6F\x4A\x53\x4F\x4E", "\x2D", "\x2B", "\x54", "\x3A", "\x2E", "\x5A", "\x5B\x0A", "\x2C\x0A", "\x0A", "\x5D", "\x5B", "\x2C", "\x5B\x5D", "\x20", "\x7B\x0A", "\x7D", "\x7B", "\x7B\x7D", "\x5C", "\x2F", "\x08", "\x09", "\x0C", "\x0D", "\x40", "\x30\x78", "\x74\x72\x75\x65", "\x66\x61\x6C\x73\x65", "\x24", "\x73\x74\x72\x69\x6E\x67", "\x72\x75\x6E\x49\x6E\x43\x6F\x6E\x74\x65\x78\x74", "\x4A\x53\x4F\x4E\x33", "\x75\x73\x65\x20\x73\x74\x72\x69\x63\x74", "\x2E\x2F\x69\x73\x41\x72\x67\x75\x6D\x65\x6E\x74\x73", "\x4F\x62\x6A\x65\x63\x74\x2E\x6B\x65\x79\x73\x20\x63\x61\x6C\x6C\x65\x64\x20\x6F\x6E\x20\x61\x20\x6E\x6F\x6E\x2D\x6F\x62\x6A\x65\x63\x74", "\x5B\x6F\x62\x6A\x65\x63\x74\x20\x41\x72\x67\x75\x6D\x65\x6E\x74\x73\x5D", "\x6E\x75\x6D\x62\x65\x72", "\x2E\x2F\x7A\x6C\x69\x62\x2F\x64\x65\x66\x6C\x61\x74\x65", "\x2E\x2F\x75\x74\x69\x6C\x73\x2F\x63\x6F\x6D\x6D\x6F\x6E", "\x2E\x2F\x75\x74\x69\x6C\x73\x2F\x73\x74\x72\x69\x6E\x67\x73", "\x2E\x2F\x7A\x6C\x69\x62\x2F\x6D\x65\x73\x73\x61\x67\x65\x73", "\x2E\x2F\x7A\x6C\x69\x62\x2F\x7A\x73\x74\x72\x65\x61\x6D", "\x5B\x6F\x62\x6A\x65\x63\x74\x20\x41\x72\x72\x61\x79\x42\x75\x66\x66\x65\x72\x5D", "\x6D\x75\x73\x74\x20\x62\x65\x20\x6E\x6F\x6E\x2D\x6F\x62\x6A\x65\x63\x74", "\x2E\x2F\x63\x6F\x6D\x6D\x6F\x6E", "\x2E\x2E\x2F\x75\x74\x69\x6C\x73\x2F\x63\x6F\x6D\x6D\x6F\x6E", "\x2E\x2F\x74\x72\x65\x65\x73", "\x2E\x2F\x61\x64\x6C\x65\x72\x33\x32", "\x2E\x2F\x63\x72\x63\x33\x32", "\x2E\x2F\x6D\x65\x73\x73\x61\x67\x65\x73", "\x70\x61\x6B\x6F\x20\x64\x65\x66\x6C\x61\x74\x65\x20\x28\x66\x72\x6F\x6D\x20\x4E\x6F\x64\x65\x63\x61\x20\x70\x72\x6F\x6A\x65\x63\x74\x29", "\x6E\x65\x65\x64\x20\x64\x69\x63\x74\x69\x6F\x6E\x61\x72\x79", "\x73\x74\x72\x65\x61\x6D\x20\x65\x6E\x64", "\x66\x69\x6C\x65\x20\x65\x72\x72\x6F\x72", "\x73\x74\x72\x65\x61\x6D\x20\x65\x72\x72\x6F\x72", "\x64\x61\x74\x61\x20\x65\x72\x72\x6F\x72", "\x69\x6E\x73\x75\x66\x66\x69\x63\x69\x65\x6E\x74\x20\x6D\x65\x6D\x6F\x72\x79", "\x62\x75\x66\x66\x65\x72\x20\x65\x72\x72\x6F\x72", "\x69\x6E\x63\x6F\x6D\x70\x61\x74\x69\x62\x6C\x65\x20\x76\x65\x72\x73\x69\x6F\x6E", "\x26", "\x3D", "\x25\x32\x30", "\x62\x6F\x6F\x6C\x65\x61\x6E", "\x2E\x2F\x64\x65\x63\x6F\x64\x65", "\x2E\x2F\x65\x6E\x63\x6F\x64\x65", "\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4A\x4B\x4C\x4D\x4E\x4F\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5A\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6A\x6B\x6C\x6D\x6E\x6F\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7A\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x2B\x2F", "\x70\x61\x6B\x6F\x2F\x6C\x69\x62\x2F\x64\x65\x66\x6C\x61\x74\x65", "\x2E\x2F\x62\x74\x6F\x61", "\x71\x75\x65\x72\x79\x73\x74\x72\x69\x6E\x67", "\x2E\x2F\x77\x65\x62\x64\x72\x69\x76\x65\x72", "\x6F\x62\x6A\x65\x63\x74\x2D\x6B\x65\x79\x73", "\x46\x75\x6E\x63\x74\x69\x6F\x6E\x2E\x70\x72\x6F\x74\x6F\x74\x79\x70\x65\x2E\x62\x69\x6E\x64\x20\x2D\x20\x77\x68\x61\x74\x20\x69\x73\x20\x74\x72\x79\x69\x6E\x67\x20\x74\x6F\x20\x62\x65\x20\x62\x6F\x75\x6E\x64\x20\x69\x73\x20\x6E\x6F\x74\x20\x63\x61\x6C\x6C\x61\x62\x6C\x65", "\x6A\x73\x6F\x6E\x33", "\x70\x73", "\x74\x6F\x6B\x65\x6E", "\x5F\x74\x6F\x6B\x65\x6E", "\x31\x2E\x30\x2E\x36", "\x73\x72\x63\x45\x6C\x65\x6D\x65\x6E\x74", "\x6F\x6E", "\x6D\x6F\x75\x73\x65\x6D\x6F\x76\x65", "\x6B\x65\x79\x64\x6F\x77\x6E", "\x63\x6C\x69\x63\x6B", "\x6F\x6E\x74\x6F\x75\x63\x68\x6D\x6F\x76\x65", "\x74\x6F\x75\x63\x68\x6D\x6F\x76\x65", "\x3F", "\x68\x61\x73\x41\x74\x74\x72\x69\x62\x75\x74\x65", "\x77\x65\x62\x64\x72\x69\x76\x65\x72", "\x5F\x5F\x64\x72\x69\x76\x65\x72\x5F\x65\x76\x61\x6C\x75\x61\x74\x65", "\x5F\x5F\x77\x65\x62\x64\x72\x69\x76\x65\x72\x5F\x65\x76\x61\x6C\x75\x61\x74\x65", "\x5F\x5F\x73\x65\x6C\x65\x6E\x69\x75\x6D\x5F\x65\x76\x61\x6C\x75\x61\x74\x65", "\x5F\x5F\x66\x78\x64\x72\x69\x76\x65\x72\x5F\x65\x76\x61\x6C\x75\x61\x74\x65", "\x5F\x5F\x64\x72\x69\x76\x65\x72\x5F\x75\x6E\x77\x72\x61\x70\x70\x65\x64", "\x5F\x5F\x77\x65\x62\x64\x72\x69\x76\x65\x72\x5F\x75\x6E\x77\x72\x61\x70\x70\x65\x64", "\x5F\x5F\x73\x65\x6C\x65\x6E\x69\x75\x6D\x5F\x75\x6E\x77\x72\x61\x70\x70\x65\x64", "\x5F\x5F\x66\x78\x64\x72\x69\x76\x65\x72\x5F\x75\x6E\x77\x72\x61\x70\x70\x65\x64", "\x5F\x5F\x77\x65\x62\x64\x72\x69\x76\x65\x72\x46\x75\x6E\x63", "\x5F\x53\x65\x6C\x65\x6E\x69\x75\x6D\x5F\x49\x44\x45\x5F\x52\x65\x63\x6F\x72\x64\x65\x72", "\x5F\x73\x65\x6C\x65\x6E\x69\x75\x6D", "\x63\x61\x6C\x6C\x65\x64\x53\x65\x6C\x65\x6E\x69\x75\x6D", "\x64\x6F\x6D\x41\x75\x74\x6F\x6D\x61\x74\x69\x6F\x6E", "\x64\x6F\x6D\x41\x75\x74\x6F\x6D\x61\x74\x69\x6F\x6E\x43\x6F\x6E\x74\x72\x6F\x6C\x6C\x65\x72", "\x5F\x5F\x6C\x61\x73\x74\x57\x61\x74\x69\x72\x41\x6C\x65\x72\x74", "\x5F\x5F\x6C\x61\x73\x74\x57\x61\x74\x69\x72\x43\x6F\x6E\x66\x69\x72\x6D", "\x5F\x5F\x6C\x61\x73\x74\x57\x61\x74\x69\x72\x50\x72\x6F\x6D\x70\x74", "\x64\x77", "\x64\x65", "\x64\x69", "\x77\x66", "\x77\x77\x74", "\x77\x77", "\x67\x77", "\x5F\x5F\x77\x65\x62\x64\x72\x69\x76\x65\x72\x5F\x73\x63\x72\x69\x70\x74\x5F\x66\x6E", "\x43\x68\x72\x6F\x6D\x65\x44\x72\x69\x76\x65\x72\x77\x6A\x65\x72\x73\x39\x30\x38\x66\x6C\x6A\x73\x64\x66\x33\x37\x34\x35\x39\x66\x73\x64\x66\x67\x64\x66\x77\x72\x75\x3D", "\x24\x63\x64\x63\x5F\x61\x73\x64\x6A\x66\x6C\x61\x73\x75\x74\x6F\x70\x66\x68\x76\x63\x5A\x4C\x6D\x63\x66\x6C\x5F", "\x24\x63\x68\x72\x6F\x6D\x65\x5F\x61\x73\x79\x6E\x63\x53\x63\x72\x69\x70\x74\x49\x6E\x66\x6F", "\x5F\x57\x45\x42\x44\x52\x49\x56\x45\x52\x5F\x45\x4C\x45\x4D\x5F\x43\x41\x43\x48\x45", "\x5F\x5F\x24\x77\x65\x62\x64\x72\x69\x76\x65\x72\x41\x73\x79\x6E\x63\x45\x78\x65\x63\x75\x74\x6F\x72", "\x63\x64\x5F\x66\x72\x61\x6D\x65\x5F\x69\x64\x5F", "\x69\x66\x72\x61\x6D\x65", "\x66\x72\x61\x6D\x65", "\x64\x72\x69\x76\x65\x72\x2D\x65\x76\x61\x6C\x75\x61\x74\x65", "\x77\x65\x62\x64\x72\x69\x76\x65\x72\x2D\x65\x76\x61\x6C\x75\x61\x74\x65", "\x73\x65\x6C\x65\x6E\x69\x75\x6D\x2D\x65\x76\x61\x6C\x75\x61\x74\x65", "\x77\x65\x62\x64\x72\x69\x76\x65\x72\x43\x6F\x6D\x6D\x61\x6E\x64", "\x77\x65\x62\x64\x72\x69\x76\x65\x72\x2D\x65\x76\x61\x6C\x75\x61\x74\x65\x2D\x72\x65\x73\x70\x6F\x6E\x73\x65", "\x6C\x77\x65", "\x66", "\x76", "\x70", "\x68", "\x6C", "\x53", "\x6C\x77\x63", "\x43\x61\x6E\x6E\x6F\x74\x20\x66\x69\x6E\x64\x20\x6D\x6F\x64\x75\x6C\x65\x20\x27", "\x27", "\x4D\x4F\x44\x55\x4C\x45\x5F\x4E\x4F\x54\x5F\x46\x4F\x55\x4E\x44"]
var iP = {
    rId: Rohr_Opt.Flag,
    ver: _$_543c[138],
    ts: new Date().getTime(),
    cts: new Date().getTime(),
    brVD: (function() {
                    var hR = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
                    var hK = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);
                    return [hR, hK]
                })(),
    brR: (function() {
                    var iZ = [screen.width, screen.height];
                    var iW = [screen.availWidth, screen.availHeight];
                    var iX = screen.colorDepth;
                    var iY = screen.pixelDepth;
                    return [iZ, iW, iX, iY]
                })(),
    bI: (function() {
                    var jb = document.referrer;
                    var ja = window.location.href;
                    return [ja, jb]
                })(),
    mT: [],
    kT: [],
    aT: [],
    tT: [],
    aM: iK()
};
```
(10)   解 aM: iK()有些难度，ik()调用,找到了iK函数，if 内判断是否是phantomjs驱动的，不用管，但是 iQ.getWebdriver()是什么jiba玩意
```
var iK = function() {
                    if (window._phantom || window.phantom || window.callPhantom) {
                        return _$_543c[135]
                    };
                    return iQ.getWebdriver()
                }
```
（11）搜索getWebdriver定位到,b.exports意思是往b这个对象插入属性的意思，但是jC是什么jb？
```
            b.exports = {
                getWebdriver: jC,
                listenWebdriver: jD
            }
```
（12）搜jC，是个函数，函数内调用其他函数进行逻辑判断，看jF比较顺眼，定位jF
```
           var jC = function() {
                if (fx(document)) {
                    return _$_543c[166]
                };
                if (cq(document)) {
                    return _$_543c[167]
                };
                if (jy(document)) {
                    return _$_543c[168]
                };
                if (jF(window)) {
                    return _$_543c[169]
                };
                if (dG(window)) {
                    return _$_543c[60]
                };
                if (fX(window)) {
                    return _$_543c[170]
                };
                if (jG(window)) {
                    return _$_543c[171]
                };
                if (jB(navigator)) {
                    return _$_543c[172]
                };
                return _$_543c[60]
            };
```
（13）这个函数就简单了，判断_$_543c[157]是否在e对象里，_$_543c[157]是“__webdriverFunc”，返回的是布尔值
```
            function jF(e) {
                return _$_543c[157] in e
            }
```
（14）自上而下的推到底端了，我要往回推了，jF返回值必须是false,因为是true说明你是chromedriver等等机器人，后面啥的都没戏；那么jC函数一定要 return _$_543c[60]，index60是''
````
            var jC = function() {
                return _$_543c[60]
            };
````
![return _$_543c[60]是空字符串](https://upload-images.jianshu.io/upload_images/10203810-a6608781b09ae9f2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
（15）那么jC只能是'' ,iK ()的返回值也只能是''
```
var iK = function() {
                    if (window._phantom || window.phantom || window.callPhantom) {
                        return _$_543c[135]
                    };
                    return iQ.getWebdriver()// return ''
                }
```
（16）那么iP就该这么写了，ip初步生成算法全部搞定；
```
var rohrdata = "";
var Rohr_Opt = new Object;
Rohr_Opt.Flag = "100049";
Rohr_Opt.LogVal = "rohrdata";
var _$_543c = ["\x755\x5F\x69\x64\x5F", "\x69\x66\x72\x61\x6D\x65", "\x66\x72\x61\x6D\x65", xxxx省略]
var iP = {
    rId: Rohr_Opt.Flag,
    ver: _$_543c[138],
    ts: new Date().getTime(),
    cts: new Date().getTime(),
    brVD: (function() {
                    var hR = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
                    var hK = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);
                    return [hR, hK]
                })(),
    brR: (function() {
                    var iZ = [screen.width, screen.height];
                    var iW = [screen.availWidth, screen.availHeight];
                    var iX = screen.colorDepth;
                    var iY = screen.pixelDepth;
                    return [iZ, iW, iX, iY]
                })(),
    bI: (function() {
                    var jb = document.referrer;
                    var ja = window.location.href;
                    return [ja, jb]
                })(),
    mT: [],
    kT: [],
    aT: [],
    tT: [],
    aM:_$_543c[60] //或者直接写死成 '',
};
```
（17）还没完，在_token和ip建立连接之前，ip还需要被玩弄几次，接下来看怎么被玩的吧，我找到了iP.reload,意思和Python中dict.update()类似，插入key value，来看看怎么插的！
```
iP.bindUserTrackEvent = function() {
  // xxxxxxxxx  省略，看函数名就是和用户操作这个时间进行绑定，和核心算法没啥关系
                };
iP.reload = function(jv) {
    var jw;
    var jx = {};
    if (typeof jv === _$_543c[91]) {
        jx = iO.parse(jv.split(_$_543c[146])[1])
    } else {
        if (typeof jv === _$_543c[2]) {
            jx = jv
        }
    };
    iP.sign = iJ(jx);
    iP.cts = new Date().getTime();
    jw = iI(iP);
    if (Rohr_Opt.LogVal && typeof(window) !== _$_543c[0]) {
        window[Rohr_Opt.LogVal] = encodeURIComponent(jw)
    };
    return jw
};
```
分析一下：
>新增了sign这个Key,用了iI对ip又算了一遍然后返回出来。cts本来就有而且value就是new Date().getTime();这里脱裤子放屁，不用管。```    iP.sign = iJ(jx); jw = iI(iP);```解决这两个就ok。

（18）根据语义判断jx是个object,iO是什么，是querystring，那么iP.reload就该这么写
```
iP.reload = function(jv) {
    var jw;
    var jx = {};
    if (typeof jv === _$_543c[91]) {
        jx = querystring.parse(jv.split('?')[1])
    } else {
        if (typeof jv === 'object') {
            jx = jv
        }
    };
    iP.sign = iJ(jx);
    iP.cts = new Date().getTime();
    jw = iI(iP);
    if (Rohr_Opt.LogVal && typeof(window) !== _$_543c[0]) {
        window[Rohr_Opt.LogVal] = encodeURIComponent(jw)
    };
    return jw
};
```
（19）但是jx是来源jv这个参数，jv这个参数怎么来的呢，目前找不到线索，直接看sign的生成算法
```
var iJ = function(je) {
    var jd = [];
    var ck = Object.keys(je).sort();
    ck.forEach(function(jf, bx) {
        if (jf !== _$_543c[136] && jf !== _$_543c[137]) {
            jd.push(jf + _$_543c[122] + je[jf])
        }
    });
    jd = jd.join(_$_543c[121]);//_$_543c[121]   &
    return iI(jd)
};
```
(20)优化一下........
```
var iJ = function(je) {
    var jd = [];
    var ck = Object.keys(je).sort();
    ck.forEach(function(jf, bx) {
        if (jf !== 'token' && jf !== '_token') {
            jd.push(jf + '=' + je[jf])
        }
    });
    jd = jd.join('&');
    return iI(jd)
};
```
通过这两行推测，je一定是一个字典```    var ck = Object.keys(je).sort(); jd.push(jf + '=' + je[jf])```,这是我睡一觉头脑清醒后想到的......可能比加班效果好得多（回家其实脑子也一直在考虑这个事情，但是能够更加开阔的去思考）。
(21)假设je是{'name':'dragon','sex':'man','area':'dongjing'}
```
var iJ = function(je) {
    var jd = [];

    //假设 je = {'name':'dragon','sex':'man','area':'dongjing'}

    var ck = Object.keys(je).sort();
    ck.forEach(function(jf, bx) {
        if (jf !== 'token' && jf !== '_token') {
            jd.push(jf + '=' + je[jf])
        }
    });

    //现在jd =  ["area=dongjing", "name=dragon", "sex=man"]

    jd = jd.join('&');    //"area=dongjing&name=dragon&sex=man"
    return iI(jd)
};
var iI = function(jc) {
    jc = cD.deflate(JSON.stringify(jc));//cD pako压缩
    jc = iD(jc);//iD btoa
    return jc
};
```
(22)通过断点调试拿到了sign值，注意此次拦截是拦截的发验证码的click事件，密码登录事件可能不同，但是解决方案一样；
![sign值](https://upload-images.jianshu.io/upload_images/10203810-34417323d92afb5f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
（23）通过，算法逆推，拿到jc这个参数是这个
```js
var iI = function(jc) {
    jc = cD.deflate(JSON.stringify(jc));//cD pako压缩
    jc = iD(jc);//iD btoa
    return jc
};
```
```python
sign = "eJxTKsosznbOSMzLS82xNTIwUistTi2yNTQ3MzK0tLC0NDJWAgDC8wnz"
sign = base64.b64decode(sign.encode())
sign = zlib.decompress(sign)
print(sign)
#  打印内容为： b'"riskChannel=202&user=17621989923"'
```
（24）此时ip生成算法就可以梳理为,sign得到了解决"eJxTKsosznbOSMzLS82xNTIwUistTi2yNTQ3MzK0tLC0NDJWAgDC8wnz"
```
var iI = function(jc) {
    jc = cD.deflate(JSON.stringify(jc));//cD pako压缩
    jc = iD(jc);//iD btoa
    return jc
};
var iJ = function() {
    var je = {'user':'17621989923','riskChannel':'202'}
    var jd = [];
    var ck = Object.keys(je).sort();
    ck.forEach(function(jf, bx) {
        if (jf !== 'token' && jf !== '_token') {
            jd.push(jf + '=' + je[jf])
        }
    });
    jd = jd.join('&');
    return iI(jd)
};

iP.reload = function(jv) {
    var jw;
    var jx = {};
    if (typeof jv === _$_543c[91]) {
        jx = querystring.parse(jv.split('?')[1])
    } else {
        if (typeof jv === 'object') {
            jx = jv
        }
    };
    iP.sign = iJ(jx);//"eJxTKsosznbOSMzLS82xNTIwUistTi2yNTQ3MzK0tLC0NDJWAgDC8wnz"
    iP.cts = new Date().getTime();
    jw = iI(iP);
    if (Rohr_Opt.LogVal && typeof(window) !== _$_543c[0]) {
        window[Rohr_Opt.LogVal] = encodeURIComponent(jw)
    };
    return jw
};
```
（25）进一步梳理........
```
var iI = function(jc) {
    jc = cD.deflate(JSON.stringify(jc));//cD pako压缩
    jc = iD(jc);//iD btoa
    return jc
};
var iJ = function(je) {
    //je = {'user':'17621989923','riskChannel':'202'}
    var jd = [];
    var ck = Object.keys(je).sort();
    ck.forEach(function(jf, bx) {
        if (jf !== 'token' && jf !== '_token') {
            jd.push(jf + '=' + je[jf])
        }
    });
    jd = jd.join('&');
    return iI(jd)
};

iP.reload = function(jv) {
    //jv = {'user':'17621989923','riskChannel':'202'}   object type
    var jw;
    var jx = {};
    if (typeof jv === 'string') {
        jx = querystring.parse(jv.split('?')[1])
    } else {
        if (typeof jv === 'object') {
            jx = jv
        }
    };
    //jx = {'user':'17621989923','riskChannel':'202'}
    iP.sign = iJ(jx);
    iP.cts = new Date().getTime();
    jw = iI(iP);
    if ("rohrdata" && typeof(window) !== "undefined") {
        window['rohrdata'] = encodeURIComponent(jw)  //url编码函数
    };
    return jw
};

```
（26）再次对逆向解码验证 rohrdata得到:
![rohrdata =encodeURIComponent(ip) ](https://upload-images.jianshu.io/upload_images/10203810-51f14228a72199d2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```
{
	"rId": "100049",
	"ver": "1.0.6",
	"ts": 1555554915457,
	"cts": 1555555821946,
	"brVD": [290, 375],
	"brR": [
		[1366, 768],
		[1366, 728], 24, 24
	],
	"bI": ["https://account.dianping.com/account/iframeLogin?callback=EasyLogin_frame_callback0&wide=false&protocol=https:&redir=http%3A%2F%2Fwww.dianping.com", "https://account.dianping.com/login?redir=http://www.dianping.com"],
	"mT": ["220,156", "220,156", "220,157", "219,158", "219,159", "219,161", "219,162", "217,163", "217,165", "215,166", "214,167", "214,169", "213,169", "213,171", "212,172", "211,173", "211,175", "210,177", "210,179", "210,182", "210,184", "210,185", "210,186", "210,188", "210,189", "210,191", "209,193", "208,196", "208,199", "208,200"],
	"kT": ["3,INPUT", "2,INPUT", "9,INPUT", "9,INPUT", "8,INPUT", "9,INPUT", "1,INPUT", "2,INPUT", "6,INPUT", "7,INPUT", "1,INPUT", "\\b,INPUT", "\\b,INPUT", "\\b,INPUT", "\\b,INPUT", "6,INPUT", "3,INPUT", "1,INPUT"],
	"aT": ["220,156,BUTTON", "100,163,INPUT", "99,160,INPUT", "181,113,INPUT", "275,20,DIV"],
	"tT": [],
	"aM": "",
	"sign": "eJxTKsosznbOSMzLS82xNTIwUistTi2yNTQ3MzK0tLC0NDJWAgDC8wnz"
}
```
（27）这和我们得到的ip不一样啊
```
var iP = {
    rId: '100049',
    ver: '1.0.6',
    ts: new Date().getTime(),
    cts: new Date().getTime(),
    brVD: [290, 375],
    brR: [[1366,768],[1366,728],24,24]
    bI: ["https://account.dianping.com/account/iframeLogin?callback=EasyLogin_frame_callback0&wide=false&protocol=https:&redir=http%3A%2F%2Fwww.dianping.com", "https://account.dianping.com/login?redir=http://www.dianping.com"],
    mT: [],
    kT: [],
    aT: [],
    tT: [],
    aM:_$_543c[60] //或者直接写死成 '',
    sign: "eJxTKsosznbOSMzLS82xNTIwUistTi2yNTQ3MzK0tLC0NDJWAgDC8wnz"
};
```
（28）
   mT: [],
   kT: [],
   aT: [], 
这三个本应该是空值，逆向解码得到的却有值，先不管继续往下
```
A 成功校验发送出去的post的token 
eJyNk21vmzAQx7 LpeaVldgGP0WKpq7ZJNqEbi3pXnRVRQjNUAlEwEqbad 9Z9OYbI2mIb/43YP/d cTv1AVrNAYUUKIrxFGT2llzCEZCrCaGo0pN5 vKfe5xCjpfVwxqn2B0bK6maLxLdMEe5LfGccV2LfUEwJLoe7wGzJA5sMxOQGkoB9Ns63Ho1GcJOXPohmusrjYZsV6mJSbvXOUPVTxJp2V66z4kMR5voyTx8mnuH6xrnsbvd8HyKDNVunkIc7rdLCtyqZMynzS1RlU6SqrrHHinZ6wz3Datv2jKoz9z6Zy20YvBHnvJGC8TWTGY4xgys1T/k3SENVAypHek6COmCUJ5DniljiQ1aM kHTUqXiHJDs9BtTpUSDPUacHXUnpSO9JMUe I3dDCUfKkburbV0Cc2hbjSgg4Ui/ESPEPNmjfTIPB GXRWRCjvQRUkd89Mhd4Ugeyfu /H/slbx3StB fLhx/HERRZehySDELK/v1myV9AIKNkAPhpYc3gNPgxuj2RhNoz2HvxKidbYugNLz5 iiLutdsby8nu9m14o9h1HQLrK6iTL2EkZfvfnugjSzMxJOz7 drqdnqi126Pcrj98B0g==

B hordata逆推出来的token   和A的区别是+号换成了空格
"eJyNk21vmzAQx7+LpeaVldgGP0WKpq7ZJNqEbi3pXnRVRQjNUAlEwEqbad+9Z9OYbI2mIb/43YP/d+cTv1AVrNAYUUKIrxFGT2llzCEZCrCaGo0pN5+vKfe5xCjpfVwxqn2B0bK6maLxLdMEe5LfGccV2LfUEwJLoe7wGzJA5sMxOQGkoB9Ns63Ho1GcJOXPohmusrjYZsV6mJSbvXOUPVTxJp2V66z4kMR5voyTx8mnuH6xrnsbvd8HyKDNVunkIc7rdLCtyqZMynzS1RlU6SqrrHHinZ6wz3Datv2jKoz9z6Zy20YvBHnvJGC8TWTGY4xgys1T/k3SENVAypHek6COmCUJ5DniljiQ1aM+kHTUqXiHJDs9BtTpUSDPUacHXUnpSO9JMUe+I3dDCUfKkburbV0Cc2hbjSgg4Ui/ESPEPNmjfTIPB+GXRWRCjvQRUkd89Mhd4Ugeyfu+/H/slbx3StB+fLhx/HERRZehySDELK/v1myV9AIKNkAPhpYc3gNPgxuj2RhNoz2HvxKidbYugNLz5+iiLutdsby8nu9m14o9h1HQLrK6iTL2EkZfvfnugjSzMxJOz7+drqdnqi126Pcrj98B0g=="

C 通过 B 逆向解码得到的json，再编码得到的token，B C本应该相同啊，难道是python代码出错了；
eJyVk29vmzAQxr9K3jS8QYn/YGxXiqa26STahG4r6V60VUUIzawSiICONtO++84mqYkSTSoC6XePj+d8h/njlMHCOe05GCHkScftOb/T0ggDNPB1XFcQYqYvT2LmMQ5i0lGZIFh6Pqjz8m4M8j2RyO1Rzh6N9kNL95j6kMJ9AeIuIDognn5MaqAznV91va5Oh8M4SYrXvB4sVJyvVb4cJMVqJw7Vcxmv0kmxVPmXJM6yeZy8jC7j6t1IT2b1abeA+o1apKPnOKvS/ros6iIpslFbp1+mC1Wa4ISenZCvcDdNs1dVj+G/u8rMPqwT5B146A5XkemQEORiZqZ7gNwgloDCovxAH1skLXJAapG1yABbX+wBcotbM7qHfOtLALe+GJBa3PrCJjm3KD9QEIueRfua8C0Ki9ZBtntA0JtsCyMB6FuUOyQImYm+tBOlbhB+m0Vm1aI8iuKoio86+Bb50dyHh/mng44pPTTVXcV758Q9n0XRTWiSENIfu9OBPgeo4yLgU+HuODiDYbnj4M4418bZ1Jjq31ynVGqZa06v3qLrqqg2+fzmdrqZ3AryFkZBM1NVHSnyHkbf6XRzjerJBQrHVz/PluML0eQb5+8/4mwQUg==
```
(29)这是python代码,我打印了编码后两个json的区别，发现中间少了个空格，这nima........
```
import base64, zlib, time
hordata = {
	"rId":"100049",
	"ver":"1.0.6",
	"ts":1555554915457,
	"cts":1555555821946,
	"brVD":[290, 375],
	"brR":[
		[1366, 768],
		[1366, 728], 24, 24
	],
	"bI":["https://account.dianping.com/account/iframeLogin?callback=EasyLogin_frame_callback0&wide=false&protocol=https:&redir=http%3A%2F%2Fwww.dianping.com", "https://account.dianping.com/login?redir=http://www.dianping.com"],
	"mT":["220,156", "220,156", "220,157", "219,158", "219,159", "219,161", "219,162", "217,163", "217,165", "215,166", "214,167", "214,169", "213,169", "213,171", "212,172", "211,173", "211,175", "210,177", "210,179", "210,182", "210,184", "210,185", "210,186", "210,188", "210,189", "210,191", "209,193", "208,196", "208,199", "208,200"],
	"kT":["3,INPUT", "2,INPUT", "9,INPUT", "9,INPUT", "8,INPUT", "9,INPUT", "1,INPUT", "2,INPUT", "6,INPUT", "7,INPUT", "1,INPUT", "\\b,INPUT", "\\b,INPUT", "\\b,INPUT", "\\b,INPUT", "6,INPUT", "3,INPUT", "1,INPUT"],
	"aT":["220,156,BUTTON", "100,163,INPUT", "99,160,INPUT", "181,113,INPUT", "275,20,DIV"],
	"tT":[],
	"aM":"",
	"sign":"eJxTKsosznbOSMzLS82xNTIwUistTi2yNTQ3MzK0tLC0NDJWAgDC8wnz"
}
import json
info = json.dumps(hordata).encode('utf-8')
print(info)
token = base64.b64encode(zlib.compress(info)).decode('utf-8')
print('根据hordata生成的token',token)
#hordata逆推出来的_token
_token = "eJyNk21vmzAQx7+LpeaVldgGP0WKpq7ZJNqEbi3pXnRVRQjNUAlEwEqbad+9Z9OYbI2mIb/43YP/d+cTv1AVrNAYUUKIrxFGT2llzCEZCrCaGo0pN5+vKfe5xCjpfVwxqn2B0bK6maLxLdMEe5LfGccV2LfUEwJLoe7wGzJA5sMxOQGkoB9Ns63Ho1GcJOXPohmusrjYZsV6mJSbvXOUPVTxJp2V66z4kMR5voyTx8mnuH6xrnsbvd8HyKDNVunkIc7rdLCtyqZMynzS1RlU6SqrrHHinZ6wz3Datv2jKoz9z6Zy20YvBHnvJGC8TWTGY4xgys1T/k3SENVAypHek6COmCUJ5DniljiQ1aM+kHTUqXiHJDs9BtTpUSDPUacHXUnpSO9JMUe+I3dDCUfKkburbV0Cc2hbjSgg4Ui/ESPEPNmjfTIPB+GXRWRCjvQRUkd89Mhd4Ugeyfu+/H/slbx3StB+fLhx/HERRZehySDELK/v1myV9AIKNkAPhpYc3gNPgxuj2RhNoz2HvxKidbYugNLz5+iiLutdsby8nu9m14o9h1HQLrK6iTL2EkZfvfnugjSzMxJOz7+drqdnqi126Pcrj98B0g=="
_token = base64.b64decode(_token.encode())
_token = zlib.decompress(_token)
print(_token)
```
![键值对之间空格](https://upload-images.jianshu.io/upload_images/10203810-e5b752d914539965.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
（30）网上找资料找到了解决方案dumps方法里添加参数separators=(',',':')搞定空格问题（json删除键值对之间的空格）
```
info = json.dumps(hordata,separators=(',',':')).encode('utf-8')
```
（31）这个编码解码不一致的问题解决了，问题还是要回到第28步，全局搜索mT发现，这三个控制在事件绑定的function里面进行了赋值
```
 iP.bindUserTrackEvent = function() {
                    var jj = function(jn) {
                        var jo, jm, jl;
                        jn = jn || window.event;
                        if (jn.pageX == null && jn.clientX !== null) {
                            jo = (jn.target && jn.target.ownerDocument) || document;
                            jm = jo.documentElement;
                            jl = jo.body;
                            jn.pageX = jn.clientX + (jm && jm.scrollLeft || jl && jl.scrollLeft || 0) - (jm && jm.clientLeft || jl && jl.clientLeft || 0);
                            jn.pageY = jn.clientY + (jm && jm.scrollTop || jl && jl.scrollTop || 0) - (jm && jm.clientTop || jl && jl.clientTop || 0)
                        };
                        this.mT.unshift([jn.pageX, jn.pageY].join(_$_543c[73]));
                        if (this.mT.length > 30) {
                            this.mT = this.mT.slice(0, 30)
                        }
                    }.bind(this);
                    var jh = function(jn) {
                        jn = jn || window.event;
                        var bw = typeof jn.which === _$_543c[98] ? jn.which: jn.keyCode;
                        if (bw) {
                            if (!jn[_$_543c[139]]) {
                                jn.srcElement = jn.target
                            };
                            this.kT.unshift([String.fromCharCode(bw), jn.srcElement.nodeName].join(_$_543c[73]))
                        };
                        if (this.kT.length > 30) {
                            this.kT = this.kT.slice(0, 30)
                        }
                    }.bind(this);
                    var jk = function(jn) {
                        var jo, jm, jl, jp, jq;
                        if (jn.touches[0].clientX !== null) {
                            jo = (jn.target && jn.target.ownerDocument) || document;
                            jm = jo.documentElement;
                            jl = jo.body;
                            jp = jn.touches[0].clientX + (jm && jm.scrollLeft || jl && jl.scrollLeft || 0) - (jm && jm.clientLeft || jl && jl.clientLeft || 0);
                            jq = jn.touches[0].clientY + (jm && jm.scrollTop || jl && jl.scrollTop || 0) - (jm && jm.clientTop || jl && jl.clientTop || 0)
                        };
                        this.tT.unshift([jp, jq, jn.touches.length].join(_$_543c[73]));
                        if (this.tT.length > 30) {
                            this.tT = this.tT.slice(0, 30)
                        }
                    }.bind(this);
                    var ji = function(jn) {
                        jn = jn || window.event;
                        if (!jn[_$_543c[139]]) {
                            jn.srcElement = jn.target
                        };
                        this.aT.unshift([jn.clientX, jn.clientY, jn.srcElement.nodeName].join(_$_543c[73]));
                        if (this.aT.length > 30) {
                            this.aT = this.aT.slice(0, 30)
                        }
                    }.bind(this);
                    function jg(jt, js, fm, ju) {
                        if (js.addEventListener) {
                            js.addEventListener(jt, fm, ju || false)
                        } else {
                            if (js.attachEvent) {
                                js.attachEvent(_$_543c[140] + jt, fm)
                            } else {
                                js[jt] = fm
                            }
                        }
                    }
                    jg(_$_543c[141], document, jj, true);
                    jg(_$_543c[142], document, jh, true);
                    jg(_$_543c[143], document, ji, true);
                    if (_$_543c[144] in document) {
                        jg(_$_543c[145], document, jk, true)
                    };
                    if (iP.aM.length === 0) {
                        iQ.listenWebdriver(function(jr) {
                            if (jr && jr.length > 0) {
                                iP.aM = jr
                            }
                        })
                    }
                };
```
（32）问题解决，现在用python代码实现模拟加密和post请求
```
import zlib
import base64
import time
import json
import requests

class GetToken:
    def __init__(self,user,password):
        """
        :param user: 你的电话号
        :param password: 你的密码
        """
        self.password = password
        self.user = user

    def BirthToken(self):
        """
        生成加密的token
        :return:
        """
        userdata = '"riskChannel=202&user={}"'.format(self.user).encode()
        sign = base64.b64encode(zlib.compress(userdata)).decode('utf-8')
        now = int(time.time()*1000)
        ip = {
                "rId":"100049",
                "ver":"1.0.6",
                "ts":now,
                "cts":now+906489,#保证比ts大
                "brVD":[290, 375],
                "brR":[
                    [1366, 768],
                    [1366, 728], 24, 24
                ],
                "bI":["https://account.dianping.com/account/iframeLogin?callback=EasyLogin_frame_callback0&wide=false&protocol=https:&redir=http%3A%2F%2Fwww.dianping.com", "https://account.dianping.com/login?redir=http://www.dianping.com"],
                "mT":["220,156", "220,156", "220,157", "219,158", "219,159", "219,161", "219,162", "217,163", "217,165", "215,166", "214,167", "214,169", "213,169", "213,171", "212,172", "211,173", "211,175", "210,177", "210,179", "210,182", "210,184", "210,185", "210,186", "210,188", "210,189", "210,191", "209,193", "208,196", "208,199", "208,200"],
                "kT":["3,INPUT", "2,INPUT", "9,INPUT", "9,INPUT", "8,INPUT", "9,INPUT", "1,INPUT", "2,INPUT", "6,INPUT", "7,INPUT", "1,INPUT", "\\b,INPUT", "\\b,INPUT", "\\b,INPUT", "\\b,INPUT", "6,INPUT", "3,INPUT", "1,INPUT"],
                "aT":["220,156,BUTTON", "100,163,INPUT", "99,160,INPUT", "181,113,INPUT", "275,20,DIV"],
                "tT":[],
                "aM":"",
                "sign":sign
            }
        info = json.dumps(ip, separators=(',', ':')).encode('utf-8')
        token = base64.b64encode(zlib.compress(info)).decode('utf-8')
        token = token.replace('+',' ')
        print(token)
        return token

    def GetPhonecode(self):
        """
        调用发送手机验证码的接口
        :return:
        """
        # 拿到加密参数
        _token = self.BirthToken()
        url = "https://account.dianping.com/account/ajax/checkRisk"
        headers = {'Referer':"https://account.dianping.com/account/iframeLogin?callback=EasyLogin_frame_callback0&wide=false&protocol=https:&redir=http%3A%2F%2Fwww.dianping.com",
                   'Accept-Encoding':'gzip, deflate, br',
                   'Content-type':'application/x-www-form-urlencoded',
                   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
                   }
        formdata = {
            'riskChannel':'202',
            'user':self.user,
            '_token':_token
        }
        response = requests.post(url,data=formdata,headers=headers)
        # 请求发验证码的接口
        headers.update({'X-Requested-With':'XMLHttpRequest'})
        formdata = {'mobileNo':self.user,
                    'uuid':response.json()['msg']['uuid'],
                    'type':'304',
                    'countrycode':'86'
                    }
        url = 'https://account.dianping.com/account/ajax/mobileVerifySend'
        response = requests.post(url,data=formdata,headers=headers)
        print(response.text)


if __name__ == '__main__':
    gettoken = GetToken('phone','password')
    gettoken.GetPhonecode()



```

