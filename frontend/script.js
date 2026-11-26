
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

async function submitMarks() {

    const studentName = document.getElementById("studentName").value.trim();

    const subjectRows = document.querySelectorAll(".subject-row");

    const marks = {};

    if (!studentName) {
        alert("Please enter your name!");
        return;
    }

    for (let row of subjectRows) {

        const subject = row.children[0].value.trim();
        const markValue = row.children[1].value;

        if (!subject || markValue === "") {
            alert("Please enter all subject names and marks!");
            return;
        }

        const mark = Number(markValue);

        if (!Number.isFinite(mark) || mark < 0 || mark > 100) {
            alert("Marks must be between 0 and 100!");
            return;
        }

        const subjectKey = subject.toLowerCase();

        if (Object.keys(marks).some(
            name => name.toLowerCase() === subjectKey
        )) {
            alert("Duplicate subject names are not allowed!");
            return;
        }

        marks[subject] = mark;
    }

    if (Object.keys(marks).length === 0) {
        alert("Please add at least one subject!");
        return;
    }

    try {

        const response = await fetch("http://127.0.0.1:5000/api/calculate", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                student_name: studentName,
                marks: marks
            })
        });

        const data = await response.json();

        if (!response.ok) {
            alert(data.error || "Something went wrong!");
            return;
        }

        console.log("Backend Result:", data);

        alert("Marks submitted successfully! Check the browser console.");

    } catch (error) {

        console.error("Error:", error);
        alert("Cannot connect to backend. Please check Flask.");

    }
}
