
(function() {
    'use strict';

      var client = new SekiroClient("ws://127.0.0.1:5620/business-demo/register?group=test&clientId=" + Math.random());
  client.registerAction("tt", function (request, resolve, reject) {
        var url = request['url'];  // 接收python传的地址
        if (!url){
            reject("url 不能为空")
        }
        resolve({"signature": window.byted_acrawler.sign({url}), "cookie": document.cookie})
  });

})();