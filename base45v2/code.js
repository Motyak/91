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
// returns an object {flag : int, hex color : str}
function chiffrer(char)
{
    return {
        "flag": Math.floor(char.charCodeAt(0) / 45), 
        "color": "#" + Mk[char.charCodeAt(0) % 45].toString()
    }
}
