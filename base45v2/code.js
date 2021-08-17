// Takes an integer
const sumOfDigits = n => {
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
// ..where color is a string hex code (without hex char)
function chiffrer(char)
{
    return {
        flag: Math.floor(char.charCodeAt(0) / 45), 
        color: Mk[char.charCodeAt(0) % 45].toString()
    }
}

// takes an object {flag : int, color : str}..
// ..where color is a string hex code (without hex char)
// return a formatted string 
function formater(objs)
{
    return objs.map(obj => `${obj.flag}-${obj.color}`)
}

// pas prog fonctionnelle = degueulasse
function verifierFormat(str)
{
    const regexAll = /^(?:\d-\d{5,6},)*\d-\d{5,6}$/gm
    if(!str.match(regexAll))
        return false
    const regexNb = /\d-(\d{5,6})/g
    let match
    while((match = regexNb.exec(str)) !== null)
        if(!Mk.includes(parseInt(match[1])))
            return false
    return true
}
// takes a formatted string and returns an..
// ..array of objects {flag : int, color : str}
function parser(str)
{
    return str.split(',').map(e => ({
        flag: e[0],
        color: (e.substr(2).length === 5?'0':'') + e.substr(2)
    }))
}

// takes an object {flag : int, color : str}..
// ..where color is a string hex code (without hex char)
function dechiffrer(obj)
{
    const colorToNb = parseInt(obj.color)
    // const ascii = obj.flag * 45 + Math.floor(colorToNb*91 / 999999) - 1
    const ascii = obj.flag * 45 + Mk.findIndex((e) => e === colorToNb)
    console.log(ascii)
    return String.fromCharCode(ascii)
}
