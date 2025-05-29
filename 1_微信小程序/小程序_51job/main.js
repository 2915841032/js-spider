
const crypto = require('crypto');

function hmacSHA256(key, message) {
  return crypto.createHmac('sha256', key)
               .update(message)
               .digest('hex');
}

// const key = 'your-secret-key';
// const message = 'your-message';

// console.log(hmacSHA256(key, h));  // 输出 HMAC-SHA256 值
