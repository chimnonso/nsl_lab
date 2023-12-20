// journals.js

document.addEventListener('DOMContentLoaded', function () {
    const viewButtons = document.querySelectorAll('.view-button');
    const modalBody = document.getElementById('journalModalBody');
  
    viewButtons.forEach(button => {
      button.addEventListener('click', function () {
        const journalId = this.getAttribute('data-journal-id');
        // Fetch journal content using AJAX (replace this with your API endpoint)
        fetch(`http://localhost:8000/publication/journal/${journalId}/`)
          .then(response => response.json())
          .then(data => {
            // Update modal body with the fetched content
            modalBody.innerHTML = `<p>${data.abstract}</p>`;
          })
          .catch(error => console.error('Error fetching journal content:', error));
      });
    });
  });
  