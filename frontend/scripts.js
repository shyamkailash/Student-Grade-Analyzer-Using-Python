function startAnalyzer() {
    document.getElementById("welcomePage").classList.add("hidden");
    document.getElementById("marksPage").classList.remove("hidden");
}
function addSubject() {
    const container = document.getElementById("subjectsContainer");
    const row = document.createElement("div");
    row.className = "subject-row";
    row.innerHTML = `
        <input type="text" placeholder="Subject name">
        <input type="number" placeholder="Marks" min="0" max="100">
    `;
    container.appendChild(row);
}
function submitMarks() {
    alert("Marks entry will be connected to the backend in the next step!");
}