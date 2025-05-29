const CryptoJS = require('crypto-js');

function decryptAES(str) {
    const key = CryptoJS.enc.Base64.parse("SjXbYTJb7zXoUToSicUL3A==");
    const iv = CryptoJS.enc.Base64.parse("OekMLjghRg8vlX/PemLc+Q==");
    const decrypted = CryptoJS.AES.decrypt(str, key, {
            iv: iv,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        }
    );
    return decrypted.toString(CryptoJS.enc.Utf8);
}

data='Cqstxq9qAjYz8qBmSI85JEmNnCU864iW0G2BVCY7skQ4gh/nQEKWq3Z5PyhnWusFKpVm/jGU858GFSR8jwn78J2+rQaTYsyxxWrCOZGVPweFz8kmIDZuoROV286Tez077it1oj3ohcrLBatitzWPRwJfNg2qo3RLBCyjr6Azaf2Y7yaEHbS7nBeeZcL+x66eo9Z5E13wJGBOvfCvb2HV2bHfUi+SR/LVOsobNq1Aw0lKs9vatvgZhSd0J37kLxJ2TF1cANTZEidtXpsYHPj9FoXmU1Rplis41lRvoqzrVCXP1JRRqBOARRK+fIjEJvb8uqF/mHNHBj4ChtRbH5/0aMijCStemA3D6JAvzCEfkzA='
console.log(decryptAES(data))