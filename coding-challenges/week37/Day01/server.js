const express = require('express');
const fs = require('fs')
const app = express();
const PORT = 3000

app.get('/', (req, res) => {
    let count = Number(fs.readFileSync('VisitedCount.txt','utf-8'))
    count += 1
    fs.writeFileSync('VisitedCount.txt',String(count))
    res.send(`<h1>This page was Visited ${count} times.</h1>`);
});

app.get('/reset', (req, res) => {
    fs.writeFileSync('VisitedCount.txt','0')
    res.sendFile(`${__dirname}/Reset.html`);
});


app.listen(PORT, () => {
    console.log(`Server running at Port : ${PORT}`);
});

