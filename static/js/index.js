console.log("hello world");
let val = "ds";
function getName() {
    let val = "inner ds";
    console.log(val);
}
function hello() {
    alert("欢迎访问我的小站");
}
let count = 0;
getName();
// setInterval(() => {
//     count += 1;
//     console.log(count);
// }, 1000);
console.log(this)

console.log($)

function getData() {
    console.log($);
    $.get('/hello', function(data) {
        console.log(data)
        $('.result').text(data.data);
    });
}

function setJSON() {
    const obj = {
        name: 'sds',
        age: 20
    }
    $.post("/getJSON",JSON.stringify(obj), function(res) {
        console.log(res);
        $('.jsonData').text(JSON.stringify(res));
    })
}