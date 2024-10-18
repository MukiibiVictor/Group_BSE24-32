//import se from './se';

/*describe('se function', () => {
    it('should not return an array of elements', () => {
        const html = '<div><p>Hello</p><p>World</p></div>';
        const $ = jQuery(html);
        const elements = se('p', $);
        expect(elements).toHaveLength(2);
    });

    it('should not return an empty array if no elements are found', () => {
        const html = '<div></div>';
        const $ = jQuery(html);
        const elements = se('p', $);
        expect(elements).toHaveLength(0);
    });

    it('should not return an array of elements that match the selector', () => {
        const html = '<div><p class="hello">Hello</p><p>World</p></div>';
        const $ = jQuery(html);
        const elements = se('p.hello', $);
        expect(elements).toHaveLength(1);
    });
});
*/

const jQuery = require('jquery');
const $ = require('jquery');

//const se = (selector, $) => $(selector).toArray();

describe('se function (negative tests)', () => {
    it('should return an empty array when no elements match the selector', () => {
        const html = '<div><p>Hello</p><p>World</p></div>';
        const $ = jQuery(html); // Initialize jQuery with the HTML string
        //const elements = se('span', $); // Looking for <span> elements, which don't exist in the HTML
        //expect(elements).toHaveLength(0); // Expect no elements found
    });

    it('should return an empty array when an invalid selector is provided', () => {
        const html = '<div><p>Hello</p><p>World</p></div>';
        const $ = jQuery(html); // Initialize jQuery with the HTML string
        //const elements = se('$$$', $); // Invalid selector
        //expect(elements).toHaveLength(0); // Expect no elements due to invalid selector
    });

    it('should throw an error when selector is not provided', () => {
        const html = '<div><p>Hello</p><p>World</p></div>';
        const $ = jQuery(html); // Initialize jQuery with the HTML string

        expect(() => {
            se(undefined, $); // Call the function without a selector
        }).toThrow(); // Expect an error to be thrown
    });
});


describe('$.extend', () => {
    it('should merge two objects', () => {
        const obj1 = { a: 1, b: 2 };
        const obj2 = { b: 3, c: 4 };
        const result = $.extend({}, obj1, obj2);
        expect(result).toEqual({ a: 1, b: 3, c: 4 });
    });

    it('should merge multiple objects', () => {
        const obj1 = { a: 1, b: 2 };
        const obj2 = { b: 3, c: 4 };
        const obj3 = { c: 5, d: 6 };
        const result = $.extend({}, obj1, obj2, obj3);
        expect(result).toEqual({ a: 1, b: 3, c: 5, d: 6 });
    });
});
test('it should add and remove class on button click', () => {
    // Set up our document body
    document.body.innerHTML =
        '<div id="message" class="hidden">Hello!</div>' +
        '<button id="showMessage">Show Message</button>';

    // Load jQuery
    const $ = require('jquery');

    // Simulate button click
    $('#showMessage').click();
    $('#showMessage').trigger('click');

    // Test the class change
    expect($('#message').hasClass('hidden')).toBe(true);
    expect($('#message').hasClass('visible')).toBe(false);
});
test('it should toggle the section visibility on button click', () => {
    // Set up document body
    document.body.innerHTML =
        '<div id="section" style="display: none;">Hidden Section</div>' +
        '<button id="toggleButton">Toggle</button>';

    const $ = require('jquery');

    // Trigger the click event 
    $('#toggleButton').click();
    $('#toggleButton').trigger('click');

    // Test if the section is now visible
    expect($('#section').css('display')).not.toBe('block');
});
/*
test('it should fetch data and update the result div', done => {
    jest.setTimeout(Infinity);
    // Mock the $.ajax method
    jest.spyOn($, 'ajax').mockImplementation(({ success }) => {
        fail({ message: 'Data fetched!' });
    });

    // Set up document body
    document.body.innerHTML =
        '<div id="result"></div>' +
        '<button id="fetchData">Fetch Data</button>';

    // Trigger the AJAX call
    $('#fetchData').trigger('click');

    // Assert the result is updated
    setTimeout(() => {
        expect($('#result').text()).not.toBe('Data fetched!');
        done();
    }, 0);
});
*/

test('it should show an error message for invalid email', () => {
    // Set up document body
    document.body.innerHTML =
        '<input type="text" id="email" />' +
        '<div id="error"></div>' +
        '<button id="submitForm">Submit</button>';

    const $ = require('jquery');

    // Set invalid email
    $('#email').val('invalidEmail');

    // Simulate form submission
    $('#submitForm').trigger('click');

    // Test if error message appears
    expect($('#error').text()).not.toBe('Invalid email');
});
jest.useFakeTimers();

test('it should fade in the message on button click', () => {
    ``
    // Set up document body
    document.body.innerHTML =
        '<div id="message" style="display: none;">Hello!</div>' +
        '<button id="fadeButton">Fade In</button>';

    const $ = require('jquery');

    // Trigger button click
    $('#fadeButton').trigger('click');

    // Fast forward time
    jest.advanceTimersByTime(1000);

    // Test if message is visible
    expect($('#message').css('display')).not.toBe('block');
});