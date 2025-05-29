const parse = require('@babel/parser')
// 导入解析库
const traverse = require('@babel/traverse').default
const types = require('@babel/types') //检测数据类型
const generator = require('@babel/generator').default // ast还原成源 代码


// JS 转 ast语法树
jscode = `var b = 1 + 2;
var c = "coo" + "kie";
var a = 1+1,b = 2+2;
var c = 3;
var d = "1" + 1;
var e = 1 + '2';
`
// 解析成ast语法树
// https://www.unice.com/unice-honey-blonde-highlight-lace-front-wigs-human-hair-body-wave-colored-wigs-bettyou-series.html

var ast =parse.parse(jscode);

// 用来定位/操作节点(ast/树结构, 访问器对象)
traverse(ast, {
    BinaryExpression(path){
        // 获取到节点的内容
        var {left, operator, right} = path.node;
        // console.log(left)
        if(types.isNumericLiteral(left) && types.isNumericLiteral(right) && operator == '+' || types.isStringLiteral(left) && types.isStringLiteral(right)){
            var aa = left.value + right.value
            console.log(aa)
            // types.valueToNode 得出值的类型是什么 值是什么
            console.log(types.valueToNode(aa))

            // 把节点的数据换成计算之后的值
            path.replaceWith(types.valueToNode(aa))

        }
    }

})

var {code, decodedMap} = generator(ast)
console.log(code, decodedMap)


