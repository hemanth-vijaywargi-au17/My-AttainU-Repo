// Question - 1) Check if a Number is Prime or not.
function isPrime(n) {
    m1 = `${n} is not a Prime Number`
    m2 = `${n} is a Prime Number`
    // 1 is neither a Prime nor a Composite Number.
    if (n == 1) {
        return m1
    }
    // 2 is the only Even Prime Number.
    if (n == 2) {
        return m2
    }
    // Any Even Number other than 2 is not a Prime Number.
    if (n > 2 && n % 2 == 0) {
        return m1
    }
    // if n is not divisible by numbers in the range 2 to n-1 then it is called a Prime Number.
    // But we don't need to check until n-1, max Divisor we have to check is upto sqrt(n) (ignoring the decimal places)
    // we can also skip over checking it for 2 and just start from 3
    max_divisor = parseInt(Math.sqrt(n))
    for (var i = 3; i <= max_divisor;) {
        if (n % i == 0) {
            return m1
        }
        i += 2 //Skipping over all Even Divisors, as odd numbers are not divisble by an even number
    }
    return m2
}

console.log(isPrime(prompt("Enter a Number to Check if it's Prime.")))


// Question - 2) Check if String is Palindrome.
// Two Pointers Algorithm, Time Complexity - O(n), Space Complexity - O(1)
function isPalindrome(s) {
    if (typeof s != String) {
        s = String(s)
    }
    var l = 0
    var r = s.length - 1
    while (l < r) {

        if (s[l] != s[r]) {
            return `${s} is not a Palindrome.`
        }
        l++
        r--

    }
    return `${s} is a Palindrome.`
}

console.log(isPalindrome(prompt("Enter a Word to Check if it's a Palindrome.")))



// Question -3) Check if a Number is Armstrong Number.
/* 
An Armstrong number is a positive m-digit number that is equal to the sum of the mth powers of their digits. 
It is also known as pluperfect, or Plus Perfect, or Narcissistic number.
For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers. 153 = (1)^3 + (5)^3 + (3)^3 = 1 + 125 + 27 = 153
*/
function isArmstrong(n) {
    m1 = `${n} is not an Armstrong Number.`
    m2 = `${n} is an Armstrong Number.`

    if (typeof n != String) {
        n = String(n)
    }
    // Checking if the number is a floating number or a negative Number.
    if (n != parseInt(n) || (n[0] == "-")) {
        return m1
    }
    var sum = 0
    var digits = String(n).length
    for (var i in n) {
        sum = sum + Math.pow(n[i], digits)
    }
    if (sum == Number(n)) {
        return m2
    }
    else {
        return m1
    }

}

console.log(isArmstrong(prompt("Enter a Number to check if it's an Armstrong Number")))