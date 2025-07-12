const fs = require("fs")
const path = require("path")

const chapters = JSON.parse(fs.readFileSync("chapters.json", "utf-8"));
const template = fs.readFileSync("template.html", "utf-8");

const distDir = "dist";
fs.rmSync(distDir, { recursive: true, force: true });
fs.mkdirSync(distDir, { recursive: true });

chapters.forEach(ch => {
    const html = template
        .replace(/{{title}}/g, ch.title)
        .replace(/{{file}}/g, ch.file);
    fs.writeFileSync(path.join(distDir, `${ch.slug}.html`), html);
});

const listItems = chapters.map(ch =>
    `<li><a class = "hover:underline text-blue-600" href="${ch.slug}.html">${ch.title}</a></li>`
).join("\n");

const indexHTML = `
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Memes for Everychapter of {{title}}</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>

<body class="bg-zinc-50 text-slate-50 antialiased p-6">
    <h1 class="text-3xl font-semibold mb-6">Thus Spoke Zarathustra</h1>
    <ul class ="space-y-2 text-lg">
    ${listItems}
    </ul>
</body>
</html>
`;

fs.writeFileSync(path.join(distDir, "index.html"), indexHTML);
console.log(chapters.length + " Pages build in dist/ ");
