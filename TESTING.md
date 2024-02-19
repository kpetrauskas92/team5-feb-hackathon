# Testing Love Sched
This project was tested continuously during development by the Code Hearted Crew. It has also passed on html, CSS, JS, and accessibility validators.

[return to README.md](README.md)

## Table of Contents
* [**During Development Testing**](#during-development-testing)
  * [*Bugs and Fixes*](#bugs-and-fixes)
* [**Post Development Testing**](#post-development-testing)
  * [*Manual Testing*](#manual-testing)
* [**User Story Testing**](#user-story-testing)
* [**Validators**](#validators)
* [**Accessibility**](#accessibility)



## **During Development Testing**

### Browser Compatibility
- ...
- ...

### Responsiveness

The site has been tested at screen sizes 320px to ###px in width.

## ***Bugs and Fixes:***
1. **ISSUE NAME** -
    * ***Issue Found:***
        * Forms did not behave as expected in development. When data was entered and submitted the CSRF verification failed message was displayed as "CSRF verification failed. Request aborted".
    * ***Solution Used:***
        * This was becasue the host address was not added to settings.py for CSRF_TRUSTED_ORIGINS in the following format:
        `CSRF_TRUSTED_ORIGINS = ['https://...']`

2. **ISSUE NAME** -
    * ***Issue Found:***
        * ...
    * ***Solution Used:***
        * ...

## **Post Development Testing**

### Manual Testing

| FEATURE TESTED            | TEST CASE                                       | PRE-CONDITION                   | EXPECTED RESULT                                                                                              | MESSAGE ALERT                    | ACTUAL RESULT                                                                                                   | PASS  |
|---------------------------|-------------------------------------------------|---------------------------------|--------------------------------------------------------------------------------------------------------------|----------------------------------|---------------------------------------------------------------------------------------------------------------|------------|
| Event Management          | Add a new event                                 | User logged in                  | New event is successfully added to the user's profile page. If the event creator chooses, the event is made public for other users to see. | Event successfully added         | The event is displayed on the user's profile page and on the Valentines Ideas page if chosen to be made public. | PASS  |
| Event Management          | Edit an existing event                          | User logged in and is the creator of the event | Event details are updated successfully and changes are immediately visible.                                 | Event successfully updated       | Changes to the event are visible on the user's profile page, and if the event is set to public, changes are also visible on the Valentines Ideas page. | PASS |
| Event Management          | Delete an existing event                        | User logged in and is the creator of the event | Event is successfully deleted from the user's calendar, profile page, and Valentines Ideas page, if public. | Event successfully deleted       | The event is no longer visible on the user's profile page, calendar, or Valentines Ideas page.                | PASS/  |
| User Interaction          | Likes on an event                               | User logged in                  | Total sum of likes made on an event appear immediately by the event.                                       | None                             | Total sum of likes made on an event appear immediately by the event.                                         | PASS|
| Profile Management        | Add events to personal calendar/date planner    | User logged in and views an event | Selected event is added to the user's personal calendar and visible on their profile page.                 | Event added to your calendar     | The event is displayed on the user's calendar on their profile page.                                        | PASS |
| Navigation and Usability  | Navigate to the Valentines Ideas                | Any user online                 | Clicking the Valentines Ideas link navigates to the page with ideas for Valentine's Day.                    | None                             | The Valentines Ideas page is displayed with a list of romantic ideas.                                       | PASS  |
| Navigation and Usability  | Navigate to the Meet the Team page              | Any user online                 | Clicking the Meet the Team link navigates to the page introducing the team behind the site.                 | None                             | The Meet the Team page is displayed with information about the blog's contributors.                         | PASS|
| Navigation and Usability  | Click on the Terms of Service link              | Any user online                 | Clicking the Terms of Service link navigates to the page with legal information and site usage terms.       | None                             | The Terms of Service page is displayed.                                                                      |            |
| Navigation and Usability  | Navigate to and use the Contact Us form         | Any user online                 | Filling out and submitting the Contact Us form sends a message to the site administrators.                  | Message received! We will respond as soon as possible! | The Contact Us page is displayed. Confirmation that the message has been received is displayed after submission. | PASS  |
| Legal and Compliance      | Review Terms of Service                         | Any user online                 | The Terms of Service page is accessible and displays all necessary legal information.                        | None                             | The Terms of Service page is displayed with all legal information.                                          | PASS |
| Account Management        | Create a new user account                       | User not logged in              | User can successfully create a new account and is redirected to their profile page.                         | Registration successful          | The new user account is created and the user is redirected to their profile page.                            | PASS  |
| Account Management        | Log into an existing account                    | User not logged in              | User can successfully log in with valid credentials and is redirected to their profile page.                | Login successful                 | The user is logged into their account and redirected to their profile page.                                  | PASS |
| Account Management        | Log out of an account                           | User logged in                  | User is successfully logged out and redirected to the blog's homepage.                                      | Logout successful                | The user is logged out and redirected to the homepage.                                                       | PASS |
| Home Page Display         | View home page information and user quotes. Click on Find an idea button to go to Valentines Ideas page | Any user online | Home page loads successfully with short information about the page and user quotes displayed. When the Find an idea button is clicked, the user is directed to the Valentines Ideas page. | None | Home page displays the expected short information, and user quotes are visible. User is directed to the Valentines Ideas page when the button is clicked. | PASS |



[**Back to top**](#testing-love-sched)

## **User Story Testing**
- - screenshots & details

## **Validators**

### HTML - https://validator.w3.org/nu/
- - screenshots & details

### CSS - https://jigsaw.w3.org/css-validator/
- - screenshots & details


### JavaScript - https://jshint.com/
- ...
- ...

## Lighthouse Scores
* All lighthouse tests were run in incognito mode to avoid interference from browser extensions.
* Both mobile and desktop performance are tested.

  - screenshots & details

## **Accessibility**
In addition to the accessibility score on lighthouse, [WAVE - Web accessibility evaluation tool](https://wave.webaim.org/) has been used to check the site for accessibility issues.

  - screenshots & details

[**Back to top**](#testing-love-sched)