const crypto = require('crypto');

function calculateSignature() {
  var u = parseInt((Date.parse((new Date).toString()) + 0).toString(), 10) / 1e3

  const prefix = 'OaxhSsnvFnRCUql53jVDUVVp26pQkYea';
  const input = prefix + u;

  // 使用Node.js内置SHA1算法验证
  const hash = crypto.createHash('sha1');
  hash.update(input, 'utf8');
  return {'hex':hash.digest('hex'),'time':u};
}

// 测试输入
const inputTimestamp = '1742561441';
const expectedOutput = '9149bce5acb4ede35b003bb4530d220a2e9ef3e2';
const actualOutput = calculateSignature(inputTimestamp);

console.log('预期输出:', expectedOutput);
console.log('实际输出:', actualOutput);
console.log('验证结果:', actualOutput === expectedOutput ? '✓ 匹配' : '✗ 不匹配');