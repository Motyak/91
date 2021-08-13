// Takes an integer
function sumOfDigits(n)
{
    return n.toString()
            .split('')
            .map(c => parseInt(c))
            .reduce((a, b) => a + b, 0)
}

// La séquence Mk ordonné naturellement
const Mk = [...Array(45).keys()]
           .map(n => n + 1)
           .map(n => (n%10!=0 && sumOfDigits(n)<10)?n:91-n)
           .map(n => Math.floor(999999*n /91))

// need a string containing at least one character..
// .. and takes the first one
// returns an object {flag : int, color : str}..
// ..where color is a string hex code
function chiffrer(char)
{
    return {
        flag: Math.floor(char.charCodeAt(0) / 45), 
        color: "#" + Mk[char.charCodeAt(0) % 45].toString()
    }
}

// takes an object {flag : int, color : str}..
// ..where color is a string hex code
function dechiffrer(obj)
{
    const colorToNb = parseInt(obj.color.substring(1))
    const ascii = obj.flag * 45 + Math.floor(colorToNb*91 / 999999 - 1)
    return String.fromCharCode(ascii)
}
