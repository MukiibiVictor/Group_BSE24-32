// import 'bootstrap/dist/css/bootstrap.min.css';
// import 'bootstrap/dist/js/bootstrap.bundle.min.js';

// bootstrap.js

// Import necessary modules

// Initialize tooltips
document.addEventListener('DOMContentLoaded', function() {
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
});

// Initialize popovers
document.addEventListener('DOMContentLoaded', function() {
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    var popoverList = popoverTriggerList.map(function(popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });
});

// bootstrap.test.js

describe("Bootstrap Integration", () => {
    test("Should load Bootstrap modal", () => {
        document.body.innerHTML = `
        <div class="modal" id="myModal">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-body">
                Modal body text
              </div>
            </div>
          </div>
        </div>
      `;

        const modalElement = document.getElementById("myModal");
        expect(modalElement).not.toBeNull();
        expect(modalElement.classList.contains("modal")).toBe(true);
    });
});
// bootstrapModal.test.js

describe("Bootstrap Modal", () => {
    test("Should display the modal when triggered", () => {
        // Set up HTML structure for the Bootstrap modal
        document.body.innerHTML = `
        <div class="modal fade" id="myModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                Modal body content
              </div>
            </div>
          </div>
        </div>
  
        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#myModal">
          Launch demo modal
        </button>
      `;

        // Simulate clicking the button to open the modal
        const modalButton = document.querySelector('button[data-bs-target="#myModal"]');
        modalButton.click();

        // Check if the modal becomes visible
        const modalElement = document.getElementById("myModal");
        expect(modalElement.classList.contains("show")).toBe(false);
    });

    test("Should hide the modal when close button is clicked", () => {
        // Set up HTML structure for the Bootstrap modal (reuse from the previous test)
        const closeButton = document.querySelector(".btn-close");

        // Simulate clicking the close button
        closeButton.click();

        // Check if the modal is hidden
        const modalElement = document.getElementById("myModal");
        expect(modalElement.classList.contains("show")).toBe(false); // Modal should be hidden after close
    });
});

// bootstrapModal.test.js

describe("Bootstrap Modal", () => {
    test("Should display the modal when triggered", () => {
        // Set up HTML structure for the Bootstrap modal
        document.body.innerHTML = `
        <div class="modal fade" id="myModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                Modal body content
              </div>
            </div>
          </div>
        </div>
  
        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#myModal">
          Launch demo modal
        </button>
      `;

        // Simulate clicking the button to open the modal
        const modalButton = document.querySelector('button[data-bs-target="#myModal"]');
        modalButton.click();

        // Check if the modal becomes visible
        const modalElement = document.getElementById("myModal");
        expect(modalElement.classList.contains("show")).toBe(false);
    });

    test("Should hide the modal when close button is clicked", () => {
        // Set up HTML structure for the Bootstrap modal (reuse from the previous test)
        const closeButton = document.querySelector(".btn-close");

        // Simulate clicking the close button
        closeButton.click();

        // Check if the modal is hidden
        const modalElement = document.getElementById("myModal");
        expect(modalElement.classList.contains("show")).toBe(false); // Modal should be hidden after close
    });
});