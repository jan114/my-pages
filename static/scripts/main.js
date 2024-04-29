

window.addEventListener("load", event => {
    const element = document.createElement("div");
    element.innerText = "Hello World!";

    element.addEventListener("mouseenter", () => console.log("enter"));
    element.addEventListener("mouseleave", () => console.log("leave"));

    document.body.append(element);
});