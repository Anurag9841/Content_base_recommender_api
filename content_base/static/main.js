//url = http://127.0.0.1:8000/cosine_recommendation/1007

document.addEventListener('DOMContentLoaded', function () {
    const courseIdInput = document.getElementById('courseIdInput');
    const courseListContainer = document.getElementById('courseListContainer');

    function fetchCourseList() {
        const courseId = courseIdInput.value;

        // Check if courseId is not empty
        if (!courseId) {
            alert('Please enter a valid Course ID.');
            return;
        }

        // Fetch data from the API based on the user-entered course ID
        fetch(`http://127.0.0.1:8000/cosine_recommendation/${encodeURIComponent(courseId)}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                displayCourseList(data.recommended_courses);
            })
            .catch(error => {
                console.error('Error fetching courses:', error);
                alert('An error occurred while fetching courses. Please try again.');
            });
    }


    function displayCourseList(courses) {
        // Clear previous content
        courseListContainer.innerHTML = '';

        // Create an unordered list element
        const ul = document.createElement('ul');

        // Iterate through each course in the array
        courses.forEach(course => {
            // Create a list item element
            const li = document.createElement('li');

            // Set the text content of the list item to the course name
            li.textContent = course;

            // Append the list item to the unordered list
            ul.appendChild(li);
        });

        // Append the unordered list to the courseListContainer in the HTML
        courseListContainer.appendChild(ul);
    }
    document.querySelector('button').addEventListener('click', fetchCourseList);
});

