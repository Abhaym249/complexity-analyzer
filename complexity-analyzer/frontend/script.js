async function analyze() {
    const code = document.getElementById("code").value;
    const language = document.getElementById("language").value;

    if (!code.trim()) {
        alert("Please paste some code.");
        return;
    }

    const res = await fetch("http://127.0.0.1:5000/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ code, language })
    });

    const data = await res.json();

    document.getElementById("time").innerText = data.time_complexity;
    document.getElementById("space").innerText = data.space_complexity;

    const r = document.getElementById("reasoning");
    r.innerHTML = "";
    data.reasoning.forEach(i => r.innerHTML += `<li>${i}</li>`);

    const s = document.getElementById("suggestions");
    s.innerHTML = "";
    data.suggestions.forEach(i => s.innerHTML += `<li>${i}</li>`);

    document.getElementById("ai").innerText = data.ai_explanation;
    document.getElementById("result").classList.remove("hidden");
}
