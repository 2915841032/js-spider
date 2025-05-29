var demo = new Hlclient("ws://127.0.0.1:12080/ws?group=zzz");
demo.regAction('heallo',function (data) {
    fetch('/static/match/match15/main.wasm').then(response =>
        response.arrayBuffer()
    ).then(bytes => WebAssembly.instantiate(bytes)).then(results => {
        instance = results.instance;
        window.q = instance.exports.encode;
        window.m = function (){
            t1 = parseInt(Date.parse(new Date())/1000/2);
            t2 = parseInt(Date.parse(new Date())/1000/2 - Math.floor(Math.random() * (50) + 1));
            return window.q(t1, t2).toString() + '|' + t1 + '|' + t2;
        };
        window.url = '/api/match/15';
        request = function(){
            //    点击换页后的操作，先得到翻到了几页
            var list = {
                "m": window.m(),
                "page": window.page,
            };
            $.ajax({
                url: window.url,
                dataType: "json",
                async: false,
                data: list,
                type: "GET",
                beforeSend: function(request) {
                },
                success: function(data) {
                    var res=""
                    data = data.data;
                    let html = '';
                    $.each(data, function(index, val) {
                        html += '<td>'+ val.value + '</td>'
                        s+=html
                        res+=val.value;
                    });
                    console.log(res)
                    resolve(res)
                    $('.number').text('').append(html);
                },
                complete: function() {
                },
                error: function() {
                    alert('因未知原因，数据拉取失败。可能是触发了风控系统');
                    alert('生而为虫，我很抱歉');
                    $('.page-message').eq(0).addClass('active');
                    $('.page-message').removeClass('active');
                }
            });
        };
        request()
    }).catch(console.error);
})
