const parse=require('@babel/parser')
const traverse=require('@babel/traverse').default
jscode=`var a = "\u0068\u0065\u006c\u006c\u006f\u002c\u0041\u0053\u0054";`;

var ast =parse.parse(jscode);
console.log(JSON.stringify(ast,null,'\t'));
