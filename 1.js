const pathlist = ["tenzin", "delek"];

// const text = "0 LalaOne: 20003 | ColaTwo. 400 || LalaThree: 1000O | Lolofowr 200000 | || Lalofive 20100 |ry | Loos T2000 |: LalaSeven: 54000 |";
// const numbersOnly = text.match(/\d+/g); // Use 'g' flag to match all occurrences
// let numArray = [];

// if (numbersOnly) {
//   numbersOnly.forEach(number => {
//     numArray.push(Number(number)); // Push each number as a numeric value into the numArray
//   });
//   console.log(numArray); // Output the array of numbers
//   return numArray; // Return the array of numbers
// } else {
//   console.log("No numbers found in the text.");
//   return []; // Return an empty array if no numbers are found
// }
// const dashToCamelCase = (str) =>
//   str
//     .split('-')
//     .map((part, index) => {
//       if (index === 0) {
//         return part;
//       } else {
//         // Convert subsequent parts to camel case only if they exist
//         return part.length > 0 ? part[0].toUpperCase() + part.slice(1) : '';
//       }
//     })
//     .join('');

// const pathname="/about/previous-releases/re-vv"
// const pathList = pathname
//   .split('/')
//   .filter(item => item !== '')
//   .map(part => {
//     if (part.includes('-')) {
//       // If the part contains a hyphen, split it and keep only the first part
//       return part.split('-')[0];
//     } else {
//       return part;
//     }
//   });


// console.log(pathList)



// function formatPathname(pathname) {
//   // Use regex to capitalize letters after hyphens
//   return pathname.replace(/-([a-z])/g, (_, match) => match.toUpperCase());
// }

// const cleanPathname = formatPathname(pathname.replace(/-/g, ''));
const pathname = " /about/get-involved/collab-summit";
const cleanPathname = pathname.replace(/-(.)/g, (match, group1) => group1.toUpperCase());
const finalCleanPathname = cleanPathname.replace(/-/g, ''); 
console.log(finalCleanPathname);

const navigationItems = [["about",{}],["getInvolved"]];


const a=["PreviousRelease"]
const b="release"
const ans= a.includes(b)
console.log(ans)