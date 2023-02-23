# Testing

## Code Validation

The [Towers of Hanoi](https://towers-of-hanoi-game.herokuapp.com/) application was thouroughly tested. Python code was reviewed in the [CI Python Linter](https://pep8ci.herokuapp.com/#). As I was continuously correcting warnings and mistakes using pylint in my GitPod, when I ran the code through the CI Python Linter, there was only one warning about an extra line at the end of the file, which I subsequently deleted. Currently, the run.py file has no errors.

[CI Python Linter No Errors](/readme-images/python_linter_all_clear.png)

Bugs and warnings encountered during the development process will be described below.

## Browser Compatibility

The website was tested on the following browsers: Google Chrome, Safari, Microsoft Edge and Mozilla Firefox. There were no errors discovered in the functionality of the CLI application.

## Responsiveness Test

I did not perform a responsivness test as this CLI application is intended to be used on desktop only. Just for illustration purposes, I am including [Am I Responsive Image](readme-images/amiresponsive.png).

## Fixed Bugs
## Unfixed Bugs

## Input Validation

There are no known bugs in the project.

## Additional Testing
### Lighthouse

The application was also tested using [Google Lighthouse](https://developers.google.com/web/tools/lighthouse) in Chrome Developer Tools. The following aspects were tested:

- Performance - reveals how the site performs during loading
- Accessibility - shows if the site if accessible for all users and suggests ways to improve it
- Best Practices - indicates if the site conforms to industry best practices
- SEO - Search Engine Optimisation - shows if the site is optimised for search engine result rankings

### Results from Lighthouse

[Lighthouse test result](./readme-images/lighthouse_score.png)