CryptoJS = require('crypto-js');
aes_iv={
    "words": [
        1664431416,
        1198600281,
        1363882577,
        1433161059
    ],
    "sigBytes": 16
}
const decryptData = data => {
    // console.log('secretData', data);
    aes_key = CryptoJS.enc.Utf8.parse("Va5z+yvp7KKEtb1uTtgzwd9nxe=kuXAK");
    const ciphertext = CryptoJS.AES.decrypt(data, aes_key, {
        iv: aes_iv,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });
    let decryptedData = ciphertext.toString(CryptoJS.enc.Utf8);
    // console.log('decryptedData', decryptedData);
    try {
        decryptedData = JSON.parse(decryptedData);
    } catch (error) {
        decryptedData = decryptedData;
    }
    return decryptedData;
};
// 调用
const data = "tMWp5MY9X0FyzY6RYMEFnzJzadcwHzF26005cpcdv8o933msnWvA1nYA19O9yRMGAbcS3Uwe3e7RHJ7wHB+tzAe0wE3zWghl9SSfJEdYNwKB4F4diVY2VUKNo11foX1+8KHl4C+WLJz9BhKAldrQMHUfMqUfvmO2Bjtm4DSpFF/Jwx7NF4hnON4hgT38QsoaSTeT2O1U3x6a9RGv85ZeijTDgqY25JzWMlybRhgRpVQ="
const decryptedData = decryptData(data);
console.log(decryptedData);