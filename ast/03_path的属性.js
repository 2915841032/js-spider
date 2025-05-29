const parse=require('@babel/parser')
const traverse=require('@babel/traverse').default
jscode = `var a = "\u0068\u0065\u006c\u006c\u006f\u002c\u0041\u0053\u0054";
var a = "\u0068\u0065\u006c\u006c\u006f\u002c\u0041\u0053\u0054";
`

var ast =parse.parse(jscode);

// 用来定位/操作节点(ast/树结构, 访问器对象)
traverse(ast, {
    // 定位VariableDeclarator类型, path是定位之后的地址
    VariableDeclarator(path){
        // console.log('当前节点的数据', path.node.init.value)
        // console.log(path.node) // 获取path 下面的node节点
        // console.log(path.toString()); // 获取当前路径的源代码
        // console.log(path.parentPath)  // 获取当前path下面的父节点
        // console.log(path.container);   // 获取兄弟节点   包含自身
        // console.log(path.type);  // 获取节点类型
        // console.log(path.get('init'))
        // path.stop()
        // path.replaceWith('123')
    }
})



// console.log(JSON.stringify(ast,null,'\t'));
