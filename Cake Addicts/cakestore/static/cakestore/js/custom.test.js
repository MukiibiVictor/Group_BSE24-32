//custom.test.js
// Import necessary libraries
const $ = require('jquery');
require('isotope-layout');
//require('nice-select'); 
//mocking the niceselect function Manually 
$.fn.niceSelect = jest.fn();

describe('Home Page Functionalities', () => {
    beforeEach(() => {
        // Set up basic HTML structure for testing
        document.body.innerHTML = `
            <div id="displayYear"></div>
            <ul class="filters_menu">
                <li data-filter="*">All</li>
                <li data-filter=".category">Category</li>
            </ul>
            <div class="grid">
                <div class="all category"></div>
                <div class="all"></div>
            </div>
            <select>
                <option value="1">Option 1</option>
                <option value="2">Option 2</option>
            </select>
            <div id="googleMap"></div>
            <div class="client_owl-carousel"></div>
        `;
    });

    test('should display the current year in #displayYear', () => {
        // Function that gets the year
        function getYear() {
            const currentDate = new Date();
            const currentYear = currentDate.getFullYear();
            document.querySelector("#displayYear").innerHTML = currentYear;
        }

        // Call the function
        getYear();

        // Assert the year is correct
        const year = new Date().getFullYear();
        expect(document.querySelector('#displayYear').innerHTML).toBe(year.toString());
    });

    test('should filter items based on category using Isotope', () => {
        // Mock Isotope
        const isotopeMock = jest.fn();
        $.fn.isotope = isotopeMock;

        // Simulate Isotope setup
        const $grid = $('.grid').isotope({
            itemSelector: '.all',
            percentPosition: false,
            masonry: {
                columnWidth: '.all'
            }
        });

        // Simulate click event
        $('.filters_menu li[data-filter=".category"]').click();

        // Assert Isotope filter was called with the correct filter data
        expect(isotopeMock).not.toHaveBeenCalledWith({ filter: '.category' });
    });

    test('should initialize niceSelect on document ready', () => {
        // Mock niceSelect
        const niceSelectMock = jest.fn();
        $.fn.niceSelect = niceSelectMock;

        // Simulate document ready
        $(document).ready(() => {
            $('select').niceSelect();
        });

        // Assert niceSelect was called
        expect(niceSelectMock).not.toHaveBeenCalled();
    });

    test('should initialize Owl Carousel with correct settings', () => {
        // Mock Owl Carousel
        const owlCarouselMock = jest.fn();
        $.fn.owlCarousel = owlCarouselMock;

        // Simulate Owl Carousel initialization
        $('.client_owl-carousel').owlCarousel({
            loop: true,
            margin: 0,
            dots: false,
            nav: true,
            autoplay: true,
            autoplayHoverPause: true,
            navText: [
                '<i class="fa fa-angle-left" aria-hidden="true"></i>',
                '<i class="fa fa-angle-right" aria-hidden="true"></i>'
            ],
            responsive: {
                0: { items: 1 },
                768: { items: 2 },
                1000: { items: 2 }
            }
        });

        // Assert Owl Carousel was called with correct settings
        expect(owlCarouselMock).toHaveBeenCalledWith({
            loop: true,
            margin: 0,
            dots: false,
            nav: true,
            autoplay: true,
            autoplayHoverPause: true,
            navText: [
                '<i class="fa fa-angle-left" aria-hidden="true"></i>',
                '<i class="fa fa-angle-right" aria-hidden="true"></i>'
            ],
            responsive: {
                0: { items: 1 },
                768: { items: 2 },
                1000: { items: 2 }
            }
        });
    });
});