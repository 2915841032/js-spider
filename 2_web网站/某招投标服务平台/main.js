const path = require('path');
const globalNodeModules = path.join(process.env.APPDATA, 'npm', 'node_modules');
process.env.NODE_PATH = globalNodeModules;
require('module').Module._initPaths();

const fs = require('fs'); //导入需要的库
const parser = require("@babel/parser");
const traverse = require("@babel/traverse").default;
const generator = require("@babel/generator").default;

encodeFile = "req.js";//定义输入以及输出文件
decodeFile = "main_decode3.js";

//将源代码解析成 AST对象
let ast = parser.parse(fs.readFileSync(encodeFile, {encoding: "utf-8"}));

//修改 AST 语法树
let hex_decode = {
    //遍历说中的字符串节点，只需要写一遍，框架会自动遍历所有的节点
    StringLiteral({node}) {
        if (node.value !== node.extra.raw) {
            node.extra.raw = "'" + node.value + "'";
        }
    },
}
//执行实际的修改
traverse(ast, hex_decode);

//将 AST 语法树还原成代码
let {code} = generator(ast, opts = {
    "jsescOption": {"minimal": true},
});
//将生成好的代码写入新的文件
fs.writeFile(decodeFile, code, (err) => {
});